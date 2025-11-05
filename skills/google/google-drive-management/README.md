# Google Drive Management

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Comprehensive Google Drive integration enabling search, file operations, folder management, permissions control, and content synchronization through the Google Drive API v3. Manage your Drive files programmatically with advanced search and organization capabilities.

## Features

- ✅ Advanced file search with query syntax
- ✅ Upload and download files
- ✅ Create and manage folders
- ✅ Move and organize files
- ✅ Sharing and permissions management
- ✅ Export Google Workspace files to multiple formats
- ✅ Batch operations
- ✅ Folder synchronization
- ✅ File metadata management
- ✅ Version history access

## Installation

### Prerequisites

- Google Cloud Console project
- OAuth2 credentials
- Google Drive API enabled
- Python 3.8+

### Setup

1. Enable Google Drive API
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
"Search Drive for budget spreadsheets"
"Upload this file to my Documents folder"
"Share the project folder with the team"
"Sync local folder with Drive"
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)
