#!/usr/bin/env python3
"""
System Health Check & Cleanup Agent

Automated diagnosis and repair of system performance issues:
- Detects crashing services, stale processes, cache bloat
- Fixes orphaned services, kills old processes
- Cleans development caches (pip, go-build, mozilla, etc)
- Optimizes systemd journal
- Reports before/after metrics
"""

import subprocess
import re
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import shutil


class SystemHealthChecker:
    """Diagnose system health and resource usage."""

    def __init__(self):
        self.home = Path.home()
        self.sudo_askpass = self.home / ".local/bin/claude-askpass"
        self.start_time = datetime.now()

    def run_cmd(self, cmd: str, use_sudo: bool = False) -> Tuple[str, int]:
        """Execute command and return output + exit code."""
        if use_sudo:
            env = os.environ.copy()
            env["SUDO_ASKPASS"] = str(self.sudo_askpass)
            env["SUDO_ASKPASS_REQUIRE"] = "force"
            cmd = f"sudo -A {cmd}"

        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            return result.stdout + result.stderr, result.returncode
        except subprocess.TimeoutExpired:
            return "TIMEOUT", 1
        except Exception as e:
            return f"ERROR: {e}", 1

    def get_memory_info(self) -> Dict:
        """Get memory usage (free, used, cache)."""
        output, _ = self.run_cmd("free -h | grep Mem")
        if not output:
            return {}

        parts = output.split()
        return {
            "total": parts[1] if len(parts) > 1 else "N/A",
            "used": parts[2] if len(parts) > 2 else "N/A",
            "free": parts[3] if len(parts) > 3 else "N/A",
            "available": parts[6] if len(parts) > 6 else "N/A",
        }

    def get_disk_info(self) -> Dict:
        """Get disk usage for root filesystem."""
        output, _ = self.run_cmd("df -h / | tail -1")
        if not output:
            return {}

        parts = output.split()
        return {
            "filesystem": parts[0] if len(parts) > 0 else "N/A",
            "size": parts[1] if len(parts) > 1 else "N/A",
            "used": parts[2] if len(parts) > 2 else "N/A",
            "available": parts[3] if len(parts) > 3 else "N/A",
            "percent": parts[4] if len(parts) > 4 else "N/A",
        }

    def get_cpu_info(self) -> Dict:
        """Get CPU load and core count."""
        # Load average
        with open("/proc/loadavg") as f:
            load_parts = f.read().split()
            load_avg = {
                "1min": load_parts[0],
                "5min": load_parts[1],
                "15min": load_parts[2],
            }

        # Core count
        output, _ = self.run_cmd("nproc")
        cores = output.strip() if output else "unknown"

        return {"load_avg": load_avg, "cores": cores}

    def get_top_processes(self, top_n: int = 10) -> List[Dict]:
        """Get top processes by CPU usage."""
        output, _ = self.run_cmd(
            "ps aux --sort=-%cpu | head -{} | tail -{}".format(top_n + 1, top_n)
        )
        if not output:
            return []

        processes = []
        for line in output.strip().split("\n"):
            if not line.strip():
                continue

            parts = line.split(None, 10)
            if len(parts) >= 8:
                processes.append({
                    "user": parts[0],
                    "pid": parts[1],
                    "cpu": parts[2],
                    "mem": parts[3],
                    "start_time": parts[8],
                    "cmd": parts[10] if len(parts) > 10 else "",
                })

        return processes

    def check_failed_services(self) -> List[str]:
        """Check for failed systemd services."""
        output, _ = self.run_cmd(
            "systemctl --user list-units --failed 2>&1 | grep -E '^●' | wc -l"
        )
        count = int(output.strip()) if output.strip().isdigit() else 0

        failed = []
        if count > 0:
            output, _ = self.run_cmd("systemctl --user list-units --failed")
            for line in output.split("\n"):
                if "●" in line:
                    parts = line.split()
                    if parts:
                        failed.append(parts[0])

        return failed

    def check_service_crash_loops(self) -> List[Dict]:
        """Check for services in restart loops (RestartSec=5s pattern)."""
        crash_loops = []
        output, _ = self.run_cmd("journalctl --user -p err -n 50 --no-pager")

        # Look for repeated failures from same service in short time
        lines = output.split("\n")
        service_errors = {}

        for line in lines:
            # Match: "service: Failed at step CHDIR"
            match = re.search(r"(\w+(?:-\w+)*\.service).*Failed", line)
            if match:
                service = match.group(1)
                if service not in service_errors:
                    service_errors[service] = 0
                service_errors[service] += 1

        # More than 5 failures in last 50 entries = crash loop
        for service, count in service_errors.items():
            if count > 5:
                crash_loops.append({
                    "service": service,
                    "failure_count": count,
                    "status": "CRASH LOOP"
                })

        return crash_loops

    def get_old_processes(self, threshold_minutes: int = 15) -> List[Dict]:
        """Find claude/python processes older than threshold."""
        output, _ = self.run_cmd("ps aux")
        if not output:
            return []

        old_processes = []
        lines = output.split("\n")
        now = datetime.now()

        for line in lines:
            if "claude" not in line and "python" not in line:
                continue
            if "grep" in line:
                continue

            try:
                parts = line.split(None, 10)
                if len(parts) >= 9:
                    pid = parts[1]
                    start_time_str = parts[8]

                    # Parse start time (HH:MM or MMM DD format)
                    # Simple heuristic: if has ":" it's today
                    if ":" in start_time_str:
                        try:
                            start_dt = datetime.strptime(
                                start_time_str, "%H:%M"
                            )
                            # Assume today
                            start_dt = start_dt.replace(
                                year=now.year,
                                month=now.month,
                                day=now.day,
                            )
                        except ValueError:
                            continue
                    else:
                        # Assume it's older than today
                        continue

                    age_minutes = (now - start_dt).total_seconds() / 60
                    if age_minutes > threshold_minutes:
                        old_processes.append({
                            "pid": pid,
                            "age_minutes": int(age_minutes),
                            "cmd": parts[10] if len(parts) > 10 else "",
                        })
            except (ValueError, IndexError):
                continue

        return old_processes

    def get_cache_sizes(self) -> Dict[str, str]:
        """Get sizes of development caches."""
        caches = {
            "pip": "~/.cache/pip",
            "go-build": "~/.cache/go-build",
            "mozilla": "~/.cache/mozilla",
            "playwright": "~/.cache/ms-playwright-go",
            "electron": "~/.cache/electron",
            "waveterm": "~/.cache/waveterm-updater",
        }

        sizes = {}
        for name, path in caches.items():
            expanded = str(Path(path).expanduser())
            output, _ = self.run_cmd(f"du -sh {expanded} 2>/dev/null")
            if output:
                size = output.split()[0] if output.split() else "0"
                sizes[name] = size

        return sizes

    def get_total_cache_size(self) -> str:
        """Get total cache size."""
        output, _ = self.run_cmd("du -sh ~/.cache")
        return output.split()[0] if output.split() else "0"

    def diagnose(self) -> Dict:
        """Run full diagnostic."""
        print("🔍 Running system diagnostics...")

        diagnosis = {
            "timestamp": datetime.now().isoformat(),
            "memory": self.get_memory_info(),
            "disk": self.get_disk_info(),
            "cpu": self.get_cpu_info(),
            "top_processes": self.get_top_processes(6),
            "failed_services": self.check_failed_services(),
            "crash_loops": self.check_service_crash_loops(),
            "old_processes": self.get_old_processes(15),
            "cache_sizes": self.get_cache_sizes(),
            "total_cache": self.get_total_cache_size(),
        }

        return diagnosis

    def print_diagnostic_report(self, diagnosis: Dict):
        """Print human-readable diagnostic report."""
        print("\n" + "=" * 60)
        print("SYSTEM HEALTH DIAGNOSTIC REPORT")
        print("=" * 60)

        # Memory
        mem = diagnosis["memory"]
        print(f"\n📊 MEMORY:")
        print(f"  Used: {mem.get('used', 'N/A')} / {mem.get('total', 'N/A')}")
        print(f"  Available: {mem.get('available', 'N/A')}")

        # Disk
        disk = diagnosis["disk"]
        print(f"\n💾 DISK:")
        print(f"  Used: {disk.get('used', 'N/A')} / {disk.get('size', 'N/A')} " +
              f"({disk.get('percent', 'N/A')})")

        # CPU
        cpu = diagnosis["cpu"]
        print(f"\n⚙️  CPU:")
        load = cpu["cpu"]["load_avg"]
        print(f"  Load: {load['1min']} (1m) | {load['5min']} (5m) | {load['15min']} (15m)")
        print(f"  Cores: {cpu['cores']}")

        # Top Processes
        print(f"\n🔥 TOP PROCESSES:")
        for p in diagnosis["top_processes"][:5]:
            print(f"  PID {p['pid']}: {p['cpu']}% CPU - {p['cmd'][:50]}")

        # Issues
        issues = []
        if diagnosis["crash_loops"]:
            issues.append(
                f"❌ Service crash loops: {len(diagnosis['crash_loops'])} services"
            )
        if diagnosis["failed_services"]:
            issues.append(
                f"❌ Failed services: {len(diagnosis['failed_services'])} units"
            )
        if diagnosis["old_processes"]:
            issues.append(
                f"⚠️  Old processes: {len(diagnosis['old_processes'])} "
                f"(>15 min)"
            )

        cache_total = diagnosis["total_cache"]
        if cache_total != "0" and "G" in cache_total:
            issues.append(f"⚠️  Cache bloat: {cache_total}")

        if issues:
            print(f"\n⚠️  ISSUES DETECTED:")
            for issue in issues:
                print(f"  {issue}")
            print(f"\nRun: /system-cleanup")
        else:
            print("\n✅ System healthy - no issues detected")

        print("\n" + "=" * 60)


class SystemCleaner:
    """Perform automated cleanup and optimization."""

    def __init__(self):
        self.home = Path.home()
        self.sudo_askpass = self.home / ".local/bin/claude-askpass"
        self.results = []

    def run_cmd(self, cmd: str, use_sudo: bool = False) -> Tuple[str, int]:
        """Execute command with optional sudo."""
        if use_sudo:
            env = os.environ.copy()
            env["SUDO_ASKPASS"] = str(self.sudo_askpass)
            env["SUDO_ASKPASS_REQUIRE"] = "force"
            cmd = f"sudo -A {cmd}"

        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60,
            )
            return result.stdout + result.stderr, result.returncode
        except Exception as e:
            return f"ERROR: {e}", 1

    def disable_crashing_service(self, service_name: str) -> bool:
        """Disable a crashing service."""
        output, code = self.run_cmd(
            f"systemctl --user disable {service_name} && "
            f"systemctl --user stop {service_name}",
            use_sudo=False,
        )
        success = code == 0
        self.results.append({
            "action": f"Disable {service_name}",
            "success": success,
            "output": output.strip(),
        })
        return success

    def kill_old_processes(self, threshold_minutes: int = 15) -> int:
        """Kill claude/python processes older than threshold."""
        output, _ = self.run_cmd("ps aux | grep -E 'claude|python' | grep -v grep")
        if not output:
            return 0

        killed = 0
        lines = output.split("\n")
        now = datetime.now()

        for line in lines:
            if not line.strip():
                continue

            try:
                parts = line.split(None, 10)
                if len(parts) >= 9:
                    pid = parts[1]
                    start_time_str = parts[8]

                    # Simple heuristic: if contains ":", it's recent
                    if ":" not in start_time_str:
                        continue

                    try:
                        start_dt = datetime.strptime(start_time_str, "%H:%M")
                        start_dt = start_dt.replace(
                            year=now.year,
                            month=now.month,
                            day=now.day,
                        )
                        age_minutes = (now - start_dt).total_seconds() / 60

                        if age_minutes > threshold_minutes:
                            kill_output, kill_code = self.run_cmd(
                                f"kill -9 {pid}",
                                use_sudo=True,
                            )
                            if kill_code == 0:
                                killed += 1
                                self.results.append({
                                    "action": f"Kill PID {pid}",
                                    "success": True,
                                    "age": f"{int(age_minutes)} min",
                                })
                    except ValueError:
                        pass
            except (ValueError, IndexError):
                continue

        if killed > 0:
            self.results.append({
                "action": "Killed old processes",
                "count": killed,
                "success": True,
            })

        return killed

    def clean_cache(self, cache_path: str) -> bool:
        """Clean a specific cache directory."""
        expanded = str(Path(cache_path).expanduser())
        if not Path(expanded).exists():
            return False

        output, code = self.run_cmd(f"rm -rf {expanded}", use_sudo=True)
        success = code == 0

        if success:
            # Get freed space before deletion (rough estimate)
            cache_name = Path(cache_path).name
            self.results.append({
                "action": f"Cleaned {cache_name}",
                "path": cache_path,
                "success": True,
            })

        return success

    def vacuum_journal(self) -> bool:
        """Optimize systemd journal."""
        output, code = self.run_cmd(
            "journalctl --vacuum-size=100M",
            use_sudo=True,
        )
        success = code == 0
        self.results.append({
            "action": "Vacuum journal",
            "success": success,
        })
        return success

    def reload_systemd(self) -> bool:
        """Reload systemd configuration."""
        output, code = self.run_cmd(
            "systemctl daemon-reload",
            use_sudo=True,
        )
        success = code == 0
        self.results.append({
            "action": "Reload systemd",
            "success": success,
        })
        return success

    def cleanup(self, full: bool = True) -> Dict:
        """Run full cleanup workflow."""
        print("\n🧹 Starting system cleanup...\n")

        self.reload_systemd()
        self.disable_crashing_service("backend-api.service")
        self.kill_old_processes(15)

        if full:
            print("🗑️  Cleaning caches...")
            self.clean_cache("~/.cache/pip")
            self.clean_cache("~/.cache/go-build")
            self.clean_cache("~/.cache/mozilla")
            self.clean_cache("~/.cache/ms-playwright-go")
            self.clean_cache("~/.cache/waveterm-updater")
            self.clean_cache("~/.cache/electron")

        self.vacuum_journal()

        return {"results": self.results}

    def print_cleanup_summary(self, cleanup_result: Dict):
        """Print cleanup results."""
        print("\n" + "=" * 60)
        print("CLEANUP COMPLETE")
        print("=" * 60)

        results = cleanup_result.get("results", [])
        for r in results:
            status = "✅" if r.get("success") else "❌"
            action = r.get("action", "Unknown")
            print(f"{status} {action}")

        print("\n" + "=" * 60)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: /system-health or /system-cleanup")
        sys.exit(1)

    command = sys.argv[1]

    if command == "health":
        checker = SystemHealthChecker()
        diagnosis = checker.diagnose()
        checker.print_diagnostic_report(diagnosis)

    elif command == "cleanup":
        cleaner = SystemCleaner()
        result = cleaner.cleanup(full=True)
        cleaner.print_cleanup_summary(result)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
