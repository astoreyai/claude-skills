#!/usr/bin/env python3
"""
post_to_discord.py - Post daily worklog to Discord #progress channel

Reads today's worklog and posts it to Discord via webhook.
Run manually or via cron at end of day.

Config: ~/.config/worklog/discord-webhook (contains webhook URL)
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError

HOME = Path.home()
WORKLOG_DIR = HOME / "worklog"
CONFIG_DIR = HOME / ".config" / "worklog"
WEBHOOK_FILE = CONFIG_DIR / "discord-webhook"
LOG_FILE = HOME / ".claude" / "logs" / "worklog-discord.log"


def log(message: str):
    """Log message to file."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def get_webhook_url() -> str:
    """Get Discord webhook URL from config file."""
    if not WEBHOOK_FILE.exists():
        return ""
    return WEBHOOK_FILE.read_text().strip()


def get_worklog_content(date: str = None) -> str:
    """Get worklog content for specified date (default: today)."""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    worklog_file = WORKLOG_DIR / f"{date}.md"

    if not worklog_file.exists():
        return ""

    return worklog_file.read_text()


def generate_morning_rollup() -> str:
    """Generate morning rollup by calling checkpoint.py with --morning --slack."""
    import subprocess

    checkpoint_script = HOME / ".claude" / "skills" / "worklog" / "checkpoint.py"

    if not checkpoint_script.exists():
        log(f"checkpoint.py not found at {checkpoint_script}")
        return ""

    try:
        result = subprocess.run(
            ["python3", str(checkpoint_script), "--morning", "--slack", "--no-write"],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            log(f"checkpoint.py --morning failed: {result.stderr}")
            return ""

    except subprocess.TimeoutExpired:
        log("checkpoint.py --morning timed out")
        return ""
    except Exception as e:
        log(f"Error running checkpoint.py: {e}")
        return ""


def format_for_discord(content: str) -> str:
    """Format markdown content for Discord (clean up, truncate if needed)."""
    # Remove the footer
    if "---\n*" in content:
        content = content.split("---\n*")[0].strip()

    # Discord message limit is 2000 chars
    if len(content) > 1900:
        content = content[:1900] + "\n\n*[truncated]*"

    return content


def post_to_discord(webhook_url: str, content: str) -> bool:
    """Post content to Discord webhook."""
    if not webhook_url:
        log("No webhook URL configured")
        return False

    payload = {
        "content": content,
        "username": "Worklog Bot",
    }

    try:
        req = Request(
            webhook_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": "WorklogBot/1.0"
            },
            method="POST"
        )

        with urlopen(req, timeout=30) as response:
            log(f"Posted to Discord successfully (status {response.status})")
            return True

    except URLError as e:
        log(f"Discord post failed: {e}")
        return False
    except Exception as e:
        log(f"Error posting to Discord: {e}")
        return False


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Post worklog to Discord")
    parser.add_argument("--date", type=str, help="Date to post (YYYY-MM-DD, default: today)")
    parser.add_argument("--yesterday", action="store_true", help="Post yesterday's worklog")
    parser.add_argument("--morning", action="store_true", help="Post morning rollup (comprehensive yesterday summary)")
    parser.add_argument("--dry-run", action="store_true", help="Print content without posting")
    parser.add_argument("--setup", action="store_true", help="Show setup instructions")
    args = parser.parse_args()

    if args.setup:
        print("""
Discord Webhook Setup
=====================

1. Open Discord and go to your server
2. Right-click the #progress channel > Edit Channel
3. Go to Integrations > Webhooks
4. Click "New Webhook"
5. Name it "Worklog Bot" (optional: set avatar)
6. Click "Copy Webhook URL"
7. Run: mkdir -p ~/.config/worklog
8. Run: echo "YOUR_WEBHOOK_URL" > ~/.config/worklog/discord-webhook
9. Test: python3 ~/.claude/skills/worklog/post_to_discord.py --dry-run

Cron Setup
==========
Run: crontab -e
Add these lines:
  # End of day worklog post at 5pm
  0 17 * * * python3 ~/.claude/skills/worklog/post_to_discord.py
  # Morning rollup at 9am
  0 9 * * * python3 ~/.claude/skills/worklog/post_to_discord.py --morning
""")
        return

    # Handle morning rollup separately
    if args.morning:
        content = generate_morning_rollup()
        if not content:
            print("No data for morning rollup")
            log("No data for morning rollup")
            sys.exit(1)

        if args.dry_run:
            print("=== Would post morning rollup to Discord ===")
            print(content)
            print("=============================================")
            return

        webhook_url = get_webhook_url()
        if not webhook_url:
            print("Error: No Discord webhook configured")
            print("Run with --setup for instructions")
            sys.exit(1)

        if post_to_discord(webhook_url, content):
            print("Posted morning rollup to Discord")
        else:
            print("Failed to post to Discord")
            sys.exit(1)
        return

    # Determine date
    if args.yesterday:
        date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    elif args.date:
        date = args.date
    else:
        date = datetime.now().strftime("%Y-%m-%d")

    # Get content
    content = get_worklog_content(date)

    if not content:
        print(f"No worklog found for {date}")
        log(f"No worklog found for {date}")
        sys.exit(1)

    # Format for Discord
    formatted = format_for_discord(content)

    if args.dry_run:
        print("=== Would post to Discord ===")
        print(formatted)
        print("=============================")
        return

    # Get webhook
    webhook_url = get_webhook_url()

    if not webhook_url:
        print("Error: No Discord webhook configured")
        print("Run with --setup for instructions")
        sys.exit(1)

    # Post
    if post_to_discord(webhook_url, formatted):
        print(f"Posted {date} worklog to Discord")
    else:
        print("Failed to post to Discord")
        sys.exit(1)


if __name__ == "__main__":
    main()
