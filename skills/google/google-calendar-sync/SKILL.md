---
name: google-calendar-sync
description: Manages Google Calendar through the Calendar API. Create, read, update, and delete events, manage multiple calendars, set reminders, handle recurring events, and sync with local schedules. Use when working with Google Calendar, scheduling events, checking availability, managing meetings, or automating calendar workflows.
---

# Google Calendar Sync

Comprehensive Google Calendar integration enabling event management, calendar organization, availability checking, recurring event handling, and workflow automation through the Google Calendar API v3.

## Quick Start

When asked to work with Google Calendar:

1. **Authenticate**: Set up OAuth2 credentials (one-time setup)
2. **List events**: View upcoming events and meetings
3. **Create events**: Schedule new meetings and appointments
4. **Update events**: Modify existing events
5. **Check availability**: Find free time slots
6. **Manage calendars**: Work with multiple calendars

## Prerequisites

### One-Time Setup

**1. Enable Calendar API:**
```bash
# Visit Google Cloud Console
# https://console.cloud.google.com/

# Enable Calendar API for your project
# APIs & Services > Enable APIs and Services > Google Calendar API
```

**2. Create OAuth2 Credentials:**
```bash
# In Google Cloud Console:
# APIs & Services > Credentials > Create Credentials > OAuth client ID
# Application type: Desktop app
# Download credentials as credentials.json
```

**3. Install Dependencies:**
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dateutil pytz --break-system-packages
```

**4. Initial Authentication:**
```bash
python scripts/authenticate.py
# Opens browser for Google sign-in
# Saves token.json for future use
```

See [reference/setup-guide.md](reference/setup-guide.md) for detailed setup.

## Core Operations

### List Events

**View upcoming events:**
```bash
# Today's events
python scripts/list_events.py --today

# This week
python scripts/list_events.py --days 7

# Specific date range
python scripts/list_events.py \
  --start 2025-01-01 \
  --end 2025-01-31

# Next N events
python scripts/list_events.py --limit 10
```

**Filter events:**
```bash
# By search term
python scripts/list_events.py --query "team meeting"

# By calendar
python scripts/list_events.py --calendar "Work"

# Only free/busy
python scripts/list_events.py --show-deleted false
```

**Get event details:**
```bash
# Get specific event
python scripts/get_event.py --event-id EVENT_ID

# Export to file
python scripts/get_event.py --event-id EVENT_ID --output event.json
```

### Create Events

**Simple event:**
```bash
# Basic event
python scripts/create_event.py \
  --summary "Team Meeting" \
  --start "2025-01-20 14:00" \
  --end "2025-01-20 15:00"

# With description
python scripts/create_event.py \
  --summary "Project Review" \
  --start "2025-01-21 10:00" \
  --end "2025-01-21 11:00" \
  --description "Q4 project review meeting"

# With location
python scripts/create_event.py \
  --summary "Client Meeting" \
  --start "2025-01-22 14:00" \
  --end "2025-01-22 15:00" \
  --location "Conference Room A"
```

**All-day event:**
```bash
python scripts/create_event.py \
  --summary "Conference" \
  --start "2025-02-15" \
  --end "2025-02-17" \
  --all-day
```

**With attendees:**
```bash
python scripts/create_event.py \
  --summary "Team Standup" \
  --start "2025-01-20 09:00" \
  --duration 30 \
  --attendees "alice@company.com,bob@company.com" \
  --send-notifications
```

**With reminders:**
```bash
python scripts/create_event.py \
  --summary "Important Meeting" \
  --start "2025-01-20 14:00" \
  --duration 60 \
  --reminders "popup:10,email:60"  # 10 min popup, 60 min email
```

**Video conference:**
```bash
# Add Google Meet link
python scripts/create_event.py \
  --summary "Virtual Meeting" \
  --start "2025-01-20 14:00" \
  --duration 60 \
  --add-meet-link
```

### Recurring Events

**Create recurring:**
```bash
# Daily standup
python scripts/create_recurring.py \
  --summary "Daily Standup" \
  --start "2025-01-20 09:00" \
  --duration 15 \
  --rule "FREQ=DAILY;COUNT=30"

# Weekly meeting
python scripts/create_recurring.py \
  --summary "Team Meeting" \
  --start "2025-01-20 14:00" \
  --duration 60 \
  --rule "FREQ=WEEKLY;BYDAY=MO,WE,FR;UNTIL=20251231"

# Monthly review
python scripts/create_recurring.py \
  --summary "Monthly Review" \
  --start "2025-01-15 10:00" \
  --duration 120 \
  --rule "FREQ=MONTHLY;BYMONTHDAY=15"
```

**Recurrence rule examples:**
```python
# Every weekday
"FREQ=DAILY;BYDAY=MO,TU,WE,TH,FR"

# Every Monday and Wednesday
"FREQ=WEEKLY;BYDAY=MO,WE"

# First Monday of every month
"FREQ=MONTHLY;BYDAY=1MO"

# Every 2 weeks
"FREQ=WEEKLY;INTERVAL=2"

# Until specific date
"FREQ=DAILY;UNTIL=20251231T235959Z"

# Specific number of occurrences
"FREQ=WEEKLY;COUNT=10"
```

See [reference/recurrence-rules.md](reference/recurrence-rules.md) for complete RRULE syntax.

### Update Events

**Modify event:**
```bash
# Update time
python scripts/update_event.py \
  --event-id EVENT_ID \
  --start "2025-01-20 15:00" \
  --end "2025-01-20 16:00"

# Update summary and description
python scripts/update_event.py \
  --event-id EVENT_ID \
  --summary "Updated Meeting Title" \
  --description "New description"

# Add attendees
python scripts/update_event.py \
  --event-id EVENT_ID \
  --add-attendees "new@company.com"

# Move to different calendar
python scripts/move_event.py \
  --event-id EVENT_ID \
  --destination-calendar "Personal"
```

**Update recurring instance:**
```bash
# Update single instance
python scripts/update_event.py \
  --event-id EVENT_ID \
  --instance-date "2025-01-20" \
  --start "2025-01-20 16:00"

# Update all future instances
python scripts/update_event.py \
  --event-id EVENT_ID \
  --start "2025-01-20 16:00" \
  --update-following
```

### Delete Events

**Delete event:**
```bash
# Delete single event
python scripts/delete_event.py --event-id EVENT_ID

# Delete recurring instance
python scripts/delete_event.py \
  --event-id EVENT_ID \
  --instance-date "2025-01-20"

# Delete all future instances
python scripts/delete_event.py \
  --event-id EVENT_ID \
  --delete-following
```

### Check Availability

**Find free time:**
```bash
# Check availability
python scripts/check_availability.py \
  --start "2025-01-20 09:00" \
  --end "2025-01-20 17:00" \
  --duration 60

# Check multiple calendars
python scripts/check_availability.py \
  --calendars "Work,Personal" \
  --date "2025-01-20" \
  --duration 30

# Find next available slot
python scripts/find_next_slot.py \
  --duration 60 \
  --business-hours-only
```

**FreeBusy query:**
```bash
# Check if people are free
python scripts/check_freebusy.py \
  --emails "alice@company.com,bob@company.com" \
  --start "2025-01-20 14:00" \
  --end "2025-01-20 15:00"
```

### Calendar Management

**List calendars:**
```bash
# Get all calendars
python scripts/list_calendars.py

# Get calendar details
python scripts/get_calendar.py --calendar-id "primary"
```

**Create calendar:**
```bash
# Create new calendar
python scripts/create_calendar.py \
  --summary "Project Alpha" \
  --description "Project Alpha team calendar" \
  --timezone "America/New_York"
```

**Share calendar:**
```bash
# Share with user
python scripts/share_calendar.py \
  --calendar-id CALENDAR_ID \
  --email "user@company.com" \
  --role writer

# Make public
python scripts/share_calendar.py \
  --calendar-id CALENDAR_ID \
  --public \
  --role reader
```

**Calendar roles:**
- `owner` - Full control
- `writer` - Create/modify events
- `reader` - View only
- `freeBusyReader` - See free/busy only

## Common Workflows

### Workflow 1: Schedule Meeting with Attendees

**Scenario:** Find time and schedule meeting

```bash
# 1. Check availability
python scripts/check_freebusy.py \
  --emails "alice@company.com,bob@company.com" \
  --date "2025-01-20" \
  --duration 60

# 2. Create meeting
python scripts/create_event.py \
  --summary "Project Discussion" \
  --start "2025-01-20 14:00" \
  --duration 60 \
  --attendees "alice@company.com,bob@company.com" \
  --add-meet-link \
  --send-notifications
```

### Workflow 2: Sync with Local Calendar

**Scenario:** Export/import events

```bash
# Export to ICS
python scripts/export_calendar.py \
  --calendar-id "primary" \
  --output calendar.ics \
  --start "2025-01-01" \
  --end "2025-12-31"

# Import from ICS
python scripts/import_calendar.py \
  --file events.ics \
  --calendar-id "primary"
```

### Workflow 3: Daily Schedule Summary

**Scenario:** Get morning email with day's schedule

```bash
# Generate daily summary
python scripts/daily_summary.py \
  --send-email \
  --to "me@company.com"
```

### Workflow 4: Recurring Task Events

**Scenario:** Create recurring reminders

```bash
# Create recurring task
python scripts/create_recurring.py \
  --summary "Submit Weekly Report" \
  --start "2025-01-20 16:00" \
  --duration 30 \
  --rule "FREQ=WEEKLY;BYDAY=FR" \
  --reminders "popup:0"
```

### Workflow 5: Event Analytics

**Scenario:** Analyze calendar usage

```bash
# Generate statistics
python scripts/calendar_stats.py \
  --start "2025-01-01" \
  --end "2025-01-31" \
  --output stats.json

# Meeting time analysis
python scripts/meeting_analysis.py --days 30
```

## Event Colors

**Color IDs:**
```python
COLORS = {
    '1': 'Lavender',
    '2': 'Sage',
    '3': 'Grape',
    '4': 'Flamingo',
    '5': 'Banana',
    '6': 'Tangerine',
    '7': 'Peacock',
    '8': 'Graphite',
    '9': 'Blueberry',
    '10': 'Basil',
    '11': 'Tomato'
}
```

**Set event color:**
```bash
python scripts/update_event.py \
  --event-id EVENT_ID \
  --color-id 9  # Blueberry
```

## Reminder Options

**Reminder methods:**
- `popup` - In-app notification
- `email` - Email reminder

**Reminder timing:**
```python
# Minutes before event
reminders = [
    {'method': 'popup', 'minutes': 10},
    {'method': 'email', 'minutes': 60},
    {'method': 'popup', 'minutes': 1440}  # 1 day
]
```

**Use default reminders:**
```python
# Use calendar's default reminders
'useDefault': True
```

## Time Zones

**Specify timezone:**
```bash
# Event in specific timezone
python scripts/create_event.py \
  --summary "Meeting" \
  --start "2025-01-20 14:00" \
  --timezone "America/Los_Angeles" \
  --duration 60
```

**Common timezones:**
```python
'America/New_York'
'America/Chicago'
'America/Denver'
'America/Los_Angeles'
'Europe/London'
'Europe/Paris'
'Asia/Tokyo'
'Australia/Sydney'
'UTC'
```

## Event Status

**Status values:**
- `confirmed` - Event is confirmed (default)
- `tentative` - Event is tentative
- `cancelled` - Event is cancelled

**Set status:**
```bash
python scripts/update_event.py \
  --event-id EVENT_ID \
  --status tentative
```

## Visibility Settings

**Visibility options:**
- `default` - Default visibility
- `public` - Public event
- `private` - Private event
- `confidential` - Only time shown, details hidden

**Set visibility:**
```bash
python scripts/update_event.py \
  --event-id EVENT_ID \
  --visibility private
```

## API Rate Limits

**Calendar API quotas:**
- **Queries per day:** 1,000,000
- **Queries per 100 seconds per user:** 500

**Best practices:**
- Batch operations when possible
- Cache calendar data
- Use incremental sync for updates
- Implement exponential backoff

## OAuth Scopes

```python
# Full access
'https://www.googleapis.com/auth/calendar'

# Read-only
'https://www.googleapis.com/auth/calendar.readonly'

# Events only
'https://www.googleapis.com/auth/calendar.events'

# Events read-only
'https://www.googleapis.com/auth/calendar.events.readonly'

# Settings only
'https://www.googleapis.com/auth/calendar.settings.readonly'
```

## Scripts Reference

**Authentication:**
- `authenticate.py` - OAuth setup
- `refresh_token.py` - Refresh token

**Events:**
- `list_events.py` - List events
- `get_event.py` - Get event details
- `create_event.py` - Create event
- `create_recurring.py` - Create recurring event
- `update_event.py` - Update event
- `delete_event.py` - Delete event
- `move_event.py` - Move to different calendar

**Availability:**
- `check_availability.py` - Check free time
- `find_next_slot.py` - Find next available
- `check_freebusy.py` - FreeBusy query

**Calendars:**
- `list_calendars.py` - List all calendars
- `get_calendar.py` - Get calendar details
- `create_calendar.py` - Create calendar
- `share_calendar.py` - Share calendar

**Import/Export:**
- `export_calendar.py` - Export to ICS
- `import_calendar.py` - Import from ICS

**Automation:**
- `daily_summary.py` - Daily schedule email
- `weekly_report.py` - Weekly calendar report
- `sync_calendar.py` - Sync with external source

**Analytics:**
- `calendar_stats.py` - Usage statistics
- `meeting_analysis.py` - Meeting patterns
- `time_tracking.py` - Track time allocation

## Best Practices

1. **Use RFC3339 format:** For dates/times (2025-01-20T14:00:00-08:00)
2. **Specify timezones:** Avoid ambiguity
3. **Send notifications:** When adding/updating attendees
4. **Use batch requests:** For multiple operations
5. **Handle recurring events carefully:** Understand instance vs series
6. **Cache calendar lists:** Reduce API calls
7. **Implement sync tokens:** For incremental updates
8. **Respect quotas:** Monitor usage

## Integration Examples

See [examples/](examples/) for complete workflows:
- [examples/meeting-scheduler.md](examples/meeting-scheduler.md) - Automated meeting scheduling
- [examples/calendar-sync.md](examples/calendar-sync.md) - Multi-calendar synchronization
- [examples/reminder-system.md](examples/reminder-system.md) - Custom reminder workflows
- [examples/analytics.md](examples/analytics.md) - Calendar analytics and insights

## Troubleshooting

**"Invalid time zone"**
- Use IANA timezone names
- Check spelling
- Reference: https://www.iana.org/time-zones

**"Invalid recurrence rule"**
- Verify RRULE syntax
- Use FREQ, COUNT/UNTIL, and optional parameters
- See [reference/recurrence-rules.md](reference/recurrence-rules.md)

**"Event not found"**
- Event may be deleted
- Check calendar ID
- Verify event ID

**"Insufficient permissions"**
- Check OAuth scopes
- Re-authenticate with needed scopes

## Reference Documentation

- [reference/setup-guide.md](reference/setup-guide.md) - Setup instructions
- [reference/recurrence-rules.md](reference/recurrence-rules.md) - RRULE reference
- [reference/api-reference.md](reference/api-reference.md) - API documentation
- [reference/timezone-reference.md](reference/timezone-reference.md) - Timezone list
