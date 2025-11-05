# Google Docs Collaboration

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Comprehensive Google Workspace document integration enabling programmatic creation, editing, and management of Docs, Sheets, and Slides through their respective APIs. Automate document workflows, extract data, format content, and manage collaboration.

## Features

- ✅ Create, read, and edit Google Docs programmatically
- ✅ Spreadsheet operations (create, read, update, formulas, formatting)
- ✅ Presentation management (create, read, edit slides)
- ✅ Text and paragraph formatting (bold, italic, fonts, styles)
- ✅ Insert elements (images, tables, page breaks)
- ✅ Find and replace operations
- ✅ Export to multiple formats (PDF, DOCX, XLSX, PPTX)
- ✅ Template-based document generation
- ✅ Batch operations for efficiency
- ✅ Sharing and permissions management

## Installation

### Prerequisites

- Google Cloud Console project
- OAuth2 credentials
- APIs enabled: Docs, Sheets, Slides, Drive
- Python 3.8+

### Setup

1. Enable Google Docs, Sheets, and Slides APIs
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

### Basic Usage

```
"Create a Google Doc with meeting notes"
"Update the budget spreadsheet with Q4 numbers"
"Generate a presentation from the project data"
"Export the report as PDF"
```

## Examples

### Example 1: Generate Report

Create document from template, populate with data, export as PDF

### Example 2: Update Spreadsheet

Append rows to tracking sheet, apply formatting, add formulas

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)
