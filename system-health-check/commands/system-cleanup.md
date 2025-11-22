# /system-cleanup

Full automated system cleanup and optimization

Performs:
- Disables crashing services (backend-api, orphaned services)
- Kills claude/python processes >15 minutes old
- Cleans development caches (pip, go-build, mozilla, playwright, electron)
- Optimizes systemd journal
- Shows before/after metrics

Usage:
```
/system-cleanup             # Full cleanup with all fixes
/system-cleanup --dry-run   # Show what would be deleted (no changes)
/system-cleanup --keep-caches  # Skip cache cleanup, only fix services
```

Example output:
```
✅ Disabled backend-api.service
✅ Killed old processes
✅ Cleaned pip cache (18GB freed)
✅ Cleaned go-build cache (3.3GB freed)
...
RESULT: 25GB freed, load average improved
```

**WARNING**: Caches are regenerated automatically on next use. This is safe.
