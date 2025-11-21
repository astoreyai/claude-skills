# Google Gmail Integration

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Comprehensive Gmail integration enabling email search, message management, sending, label organization, attachment handling, and workflow automation through the Gmail API v1. Manage your inbox programmatically with powerful search and automation capabilities.

## Features

- ✅ Advanced email search with Gmail query syntax
- ✅ Read and parse email messages
- ✅ Send emails with attachments
- ✅ Reply and forward messages
- ✅ Label management and organization
- ✅ Mark as read/unread, archive, trash
- ✅ Attachment download and handling
- ✅ Batch operations
- ✅ Email filtering and automation
- ✅ Analytics and reporting

## Installation

### Prerequisites

- Google Cloud Console project
- OAuth2 credentials
- Gmail API enabled
- Python 3.8+

### Setup

1. Enable Gmail API
2. Download OAuth2 credentials
3. Install dependencies:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
4. Authenticate:
   ```bash
   python scripts/authenticate.py
   ```

## Usage

```
"Search for unread emails from boss"
"Send email to team with project update"
"Download attachments from invoice emails"
"Archive all read emails older than 30 days"
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)
