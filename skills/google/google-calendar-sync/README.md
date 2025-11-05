# Google Calendar Sync

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Comprehensive Google Calendar integration enabling event management, calendar organization, availability checking, recurring event handling, and workflow automation through the Google Calendar API v3. Manage your schedule, create events, check availability, and automate calendar workflows programmatically.

## Features

- ✅ Full CRUD operations for calendar events (create, read, update, delete)
- ✅ Multiple calendar management and organization
- ✅ Recurring event support with RRULE syntax
- ✅ Availability checking and free/busy queries
- ✅ Attendee management and meeting invitations
- ✅ Reminders (popup and email) configuration
- ✅ Video conferencing (Google Meet) integration
- ✅ Event colors and categories
- ✅ Calendar sharing and permissions management
- ✅ Import/export (ICS format) support
- ✅ Time zone handling
- ✅ Event search and filtering

## Installation

### Prerequisites

- Claude Code installed
- Google Cloud Console project
- OAuth2 credentials
- Python 3.8+

### Setup

1. Enable Google Calendar API in Google Cloud Console
2. Create OAuth2 credentials and download credentials.json
3. Install dependencies:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dateutil pytz
   ```
4. Authenticate:
   ```bash
   python scripts/authenticate.py
   ```

## Usage

### Basic Usage

Ask Claude to manage your calendar:

```
"List my meetings for today"
"Create a team meeting tomorrow at 2pm"
"Check my availability for Friday afternoon"
"Schedule a recurring weekly standup every Monday at 9am"
```

### Common Operations

| Operation | Example |
|-----------|---------|
| List events | "Show my events for this week" |
| Create event | "Schedule meeting with Alice on Thursday at 3pm" |
| Update event | "Move tomorrow's 2pm meeting to 3pm" |
| Delete event | "Cancel the budget review meeting" |
| Check availability | "When am I free on Friday?" |
| Create recurring | "Create daily standup at 9am for next month" |

## Examples

### Example 1: Schedule Team Meeting

**Input:** "Schedule team meeting next Tuesday 2-3pm with video link"

**Output:** Event created with Google Meet link, calendar invites sent

### Example 2: Find Free Time

**Input:** "When are John and I both free tomorrow afternoon?"

**Output:** List of available time slots based on calendar analysis

## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| default_calendar | Primary calendar to use | 'primary' |
| default_duration | Event length in minutes | 60 |
| timezone | Time zone for events | System timezone |
| send_notifications | Email attendees by default | true |

## Troubleshooting

- **Authentication errors**: Re-run authenticate.py
- **Rate limits**: Implement exponential backoff
- **Invalid timezone**: Use IANA timezone names
- **Permission denied**: Check OAuth scopes

## Dependencies

- google-auth, google-auth-oauthlib, google-auth-httplib2
- google-api-python-client
- python-dateutil, pytz

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)

## Related Skills

- [Google Docs Collaboration](../google-docs-collaboration/)
- [Google Drive Management](../google-drive-management/)
- [Google Gmail Integration](../google-gmail-integration/)
