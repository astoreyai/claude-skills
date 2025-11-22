# System Health Check & Cleanup Skill

**Version**: 1.0.0
**Category**: System Administration / Performance Optimization
**Author**: Claude Code
**Last Updated**: November 22, 2025

## Overview

Automated system health monitoring and cleanup workflow. Diagnoses performance issues, identifies resource bottlenecks, fixes orphaned services, kills stale processes, and cleans cache bloat. Designed for archimedes (32c/125GB) but works on any Linux system.

## Features

### 1. **System Diagnostics**
- Memory usage (free, used, buffers, cache)
- Disk usage (mounted filesystems)
- CPU load average and core count
- Process analysis (top CPU/memory consumers)
- Service health (running, failed, crashed)
- Systemd journal errors

### 2. **Issue Detection**
- **Crash loops**: Services repeatedly failing to start
- **Orphaned services**: Missing directories/executables
- **Process age**: Long-running claude/python processes (>15 min)
- **Cache bloat**: Large development caches (pip, go-build, npm)
- **Failed services**: Systemd units in failed state
- **Log spam**: Error entries in journal (potential I/O bottlenecks)

### 3. **Automated Cleanup**
- Disable crashing services
- Kill old claude/python processes
- Clean development caches:
  - pip cache (18GB typical)
  - go-build cache (3.3GB typical)
  - Mozilla/Firefox (1.5GB typical)
  - Playwright browsers (126MB typical)
  - Electron cache (442MB typical)
  - Wave Terminal updater (150MB typical)
- Vacuum systemd journal
- Reload systemd configuration

### 4. **Performance Metrics**
- Before/after disk space comparison
- Memory efficiency improvements
- Load average reduction
- Process count normalization

## Usage

### Quick Health Check (No Changes)
```bash
/system-health
```

**Output**: Comprehensive diagnosis showing:
- Memory/disk/CPU status
- Top resource consumers
- Failed services
- Cache sizes
- Recommendations

### Full Cleanup (Automated Fix)
```bash
/system-cleanup
```

**Output**:
- Disables crashing services
- Kills processes >15 min old
- Cleans all caches
- Optimizes journal
- Shows before/after metrics
- Confirms all fixes applied

## Real-World Example

### Scenario: System Glitching After Extended Uptime

**Before Cleanup**:
```
Load: 1.41 (with crash loop)
Memory: 6.4GB / 125GB used
Disk: 275GB / 915GB (32%)
Cache: 25GB
Processes: 80+ including stale claude instances
Failed Services: backend-api looping every 5 seconds
Journal Size: 1.2GB with error spam
```

**Issues Detected**:
- ❌ backend-api.service fails every 5 seconds (directory missing)
- ❌ 2 claude processes: 50% CPU, 21% CPU (14+ min old)
- ❌ 23GB cache bloat (pip, go-build, mozilla)
- ❌ Log spam from repeated service restarts

**After Cleanup**:
```
Load: 0.96 (smooth operation)
Memory: 6.4GB / 125GB used
Disk: 250GB / 915GB (29%) — 25GB freed
Cache: 2GB
Processes: 45 (lean system)
Failed Services: None
Journal Size: 100MB (optimized)
```

**Results**: ✅ Glitching eliminated, system responsive, 25GB freed

## Skill Parameters

### Scope
- **diagnosis-only**: Check health without changes
- **safe-cleanup**: Disable services + kill old processes
- **full-cleanup**: Includes cache purging (default)

### Output Format
- **summary**: Table format (concise)
- **detailed**: Full command output
- **json**: Machine-readable metrics

### Process Age Threshold
- Default: 15 minutes
- Configurable per run
- Only kills claude/python processes (safe)

## Technical Details

### Service Crash Detection
Monitors for:
- `Restart=on-failure` loops (5 second intervals)
- Missing WorkingDirectory or ExecStart paths
- `systemctl list-units --failed` status
- journalctl error spam from same PID

### Cache Cleanup Strategy
**Safe to clean (zero impact)**:
- pip cache (regenerated on first pip command)
- go-build cache (rebuilt on compilation)
- Mozilla/Firefox cache (recreated automatically)
- Playwright browsers (downloaded on first use)
- Electron updates (downloaded if needed)

**Not touched**:
- project dependencies (venv/)
- user data (Documents, Downloads, Projects)
- git repositories
- configuration files

### Process Cleanup
**Kills only**:
- claude processes >15 min old
- Not in use by active terminal
- Confirmed via STAT field (Sl+ = active, Sl = background)

**Preserves**:
- System services (systemd, kernel)
- Active shells (pts, tty)
- Essential daemons (nginx, mysql, etc.)

## Integration with Other Skills

### With memory-keeper
```
System Health Check → Detects issues
                   → Reports to /update-memory
                   → Triggers cleanup
                   → Saves results to CLAUDE.md
```

### With development workflows
```
Before running long jobs:
  /system-health          (check capacity)
    ↓
After long jobs:
  /system-cleanup         (reclaim resources)
    ↓
Continue development
```

## Output Examples

### Diagnostic Output
```
=== SYSTEM HEALTH REPORT ===

Memory:     6.4GB / 125GB (5% used) ✓
Disk:       250GB / 915GB (29%) ✓
CPU Cores:  32 (load avg: 0.96) ✓

TOP PROCESSES:
1. claude (pts/1)      46.7% CPU  - 10 min old  ⚠ OLD
2. claude (pts/3)      33.6% CPU  - 1 min old   ✓
3. firefox             12.7% CPU
4. syncthing           6.5% CPU
5. kitty               3.2% CPU

ISSUES DETECTED:
❌ backend-api.service crash loop (5s restart interval)
❌ claude process PID 3663 is 10+ minutes old
⚠ Cache at 25GB (pip: 18GB, go-build: 3.3GB)
✓ No failed systemd services

RECOMMENDATIONS:
1. Run /system-cleanup to fix all issues
2. Consider increasing cache cleanup frequency
3. Monitor CPU usage if claude processes >50%
```

### Cleanup Summary
```
=== CLEANUP COMPLETE ===

✅ Disabled backend-api.service
✅ Killed 1 old claude process (PID 3663, age 15+ min)
✅ Cleaned pip cache (18GB freed)
✅ Cleaned go-build (3.3GB freed)
✅ Cleaned firefox cache (1.5GB freed)
✅ Cleaned playwright (126MB freed)
✅ Cleaned electron (442MB freed)
✅ Vacuumed journal to 100MB

BEFORE:
  Disk: 275GB (32%)
  Cache: 25GB
  Load: 1.41

AFTER:
  Disk: 250GB (29%) — 25GB freed ✅
  Cache: 2GB — 23GB freed ✅
  Load: 0.96 — smoother ✅

System responsive and optimized!
```

## Troubleshooting

### Issue: Permission Denied on Cache Cleanup
**Solution**: Skill uses askpass helper for sudo auth
- Automatically configured via SUDO_ASKPASS
- Falls back to interactive prompt if helper fails

### Issue: Can't Kill Processes (EPERM)
**Solution**: Process is owned by root or system
- Skill only targets user-owned processes
- System services skipped for safety

### Issue: Service Disabled But Still Running
**Solution**: Service may have been started manually
```bash
systemctl --user stop backend-api.service
systemctl --user disable backend-api.service
```

## Performance Impact

### Runtime
- **Diagnostic only**: ~5 seconds
- **Process cleanup**: ~10 seconds
- **Full cleanup with caches**: ~30-60 seconds

### System Impact
- Non-blocking (spawns background processes)
- I/O intensive during cache deletion (expected)
- Safe to run during active development

## Parameters & Customization

### Command: `/system-health`
- `--verbose`: Show all processes and services
- `--format json`: Output JSON metrics
- `--threshold 30`: Change process age to 30 minutes

### Command: `/system-cleanup`
- `--keep-caches`: Skip cache cleanup
- `--keep-processes`: Skip process cleanup
- `--dry-run`: Show what would be deleted (no changes)

## Known Limitations

1. **Single machine**: Works on archimedes; euclid requires euclid-specific cleanup
2. **Development-focused**: Assumes standard development environment layout
3. **No backup verification**: Deleted caches cannot be recovered (but regenerate automatically)
4. **Sudo required**: Needs passwordless sudo or askpass configured

## Future Enhancements

- [ ] Real-time performance monitoring dashboard
- [ ] Automatic cleanup scheduling (systemd timer)
- [ ] Remote monitoring (euclid + vegetius)
- [ ] Custom cleanup rules (YAML config)
- [ ] Docker/container support
- [ ] Trend analysis (track cleanup frequency)

## References

### System Administration
- [systemd.service](https://man7.org/linux/man-pages/man5/systemd.service.5.html) (service configuration)
- [free(1)](https://man7.org/linux/man-pages/man1/free.1.html) (memory info)
- [df(1)](https://man7.org/linux/man-pages/man1/df.1.html) (disk space)
- [ps(1)](https://man7.org/linux/man-pages/man1/ps.1.html) (process info)

### Archive Tools
- rm(1) - Delete files/directories
- journalctl - Query systemd journal
- systemctl - Manage systemd units

## Support

For issues:
1. Run `/system-health --verbose` to diagnose
2. Check `~/.local/log/system-health.log` for full output
3. Verify sudo configuration: `sudo -v`
4. Consult system logs: `journalctl -n 50 --no-pager`

---

**License**: MIT (Part of astoreyai/claude-skills distribution)
**Repository**: https://github.com/astoreyai/claude-skills/
**Plugin**: system-health-check
