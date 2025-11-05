#!/usr/bin/env python3
"""
Google API Authentication Script

This script handles OAuth2 authentication for Google APIs.
Run once to authenticate and save credentials for future use.

Usage:
    python authenticate.py [--scopes SCOPES]

Example:
    python authenticate.py --scopes drive,gmail,calendar,docs,sheets,slides
"""

import os
import sys
import argparse
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Default scopes for different services
SCOPE_MAPPINGS = {
    'drive': 'https://www.googleapis.com/auth/drive',
    'drive-readonly': 'https://www.googleapis.com/auth/drive.readonly',
    'gmail': 'https://www.googleapis.com/auth/gmail.modify',
    'gmail-readonly': 'https://www.googleapis.com/auth/gmail.readonly',
    'gmail-send': 'https://www.googleapis.com/auth/gmail.send',
    'calendar': 'https://www.googleapis.com/auth/calendar',
    'calendar-readonly': 'https://www.googleapis.com/auth/calendar.readonly',
    'docs': 'https://www.googleapis.com/auth/documents',
    'docs-readonly': 'https://www.googleapis.com/auth/documents.readonly',
    'sheets': 'https://www.googleapis.com/auth/spreadsheets',
    'sheets-readonly': 'https://www.googleapis.com/auth/spreadsheets.readonly',
    'slides': 'https://www.googleapis.com/auth/presentations',
    'slides-readonly': 'https://www.googleapis.com/auth/presentations.readonly',
}

# Default credentials path
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'


def get_scopes(scope_names):
    """Convert scope names to full scope URLs."""
    scopes = []
    for name in scope_names.split(','):
        name = name.strip().lower()
        if name in SCOPE_MAPPINGS:
            scopes.append(SCOPE_MAPPINGS[name])
        elif name.startswith('https://'):
            # Allow full scope URLs
            scopes.append(name)
        else:
            print(f"Warning: Unknown scope '{name}', skipping...")
    return scopes


def authenticate(scopes=None, credentials_file=CREDENTIALS_FILE, token_file=TOKEN_FILE):
    """
    Authenticate with Google APIs using OAuth2.
    
    Args:
        scopes: List of OAuth scopes or comma-separated string
        credentials_file: Path to credentials.json
        token_file: Path to save token.json
    
    Returns:
        Credentials object
    """
    # Default to common scopes if none provided
    if scopes is None:
        scopes = [
            SCOPE_MAPPINGS['drive'],
            SCOPE_MAPPINGS['gmail'],
            SCOPE_MAPPINGS['calendar'],
            SCOPE_MAPPINGS['docs'],
            SCOPE_MAPPINGS['sheets'],
            SCOPE_MAPPINGS['slides'],
        ]
    elif isinstance(scopes, str):
        scopes = get_scopes(scopes)
    
    creds = None
    
    # Load existing token if available
    if os.path.exists(token_file):
        try:
            creds = Credentials.from_authorized_user_file(token_file, scopes)
            print(f"✓ Loaded existing credentials from {token_file}")
        except Exception as e:
            print(f"Warning: Could not load existing token: {e}")
            creds = None
    
    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Refreshing expired credentials...")
                creds.refresh(Request())
                print("✓ Credentials refreshed successfully")
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
                print("Starting new authentication flow...")
                creds = None
        
        if not creds:
            # Check credentials file exists
            if not os.path.exists(credentials_file):
                print(f"Error: Credentials file '{credentials_file}' not found!")
                print("\nTo create credentials:")
                print("1. Visit https://console.cloud.google.com/")
                print("2. Enable the necessary APIs (Drive, Gmail, Calendar, etc.)")
                print("3. Go to 'APIs & Services' > 'Credentials'")
                print("4. Create 'OAuth client ID' (Desktop app)")
                print("5. Download as 'credentials.json'")
                sys.exit(1)
            
            print(f"\nStarting OAuth2 authentication flow...")
            print(f"A browser window will open for you to sign in to Google.")
            print(f"\nRequested scopes:")
            for scope in scopes:
                scope_name = [k for k, v in SCOPE_MAPPINGS.items() if v == scope]
                print(f"  - {scope_name[0] if scope_name else scope}")
            
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, scopes)
            creds = flow.run_local_server(port=0)
            print("✓ Authentication successful!")
        
        # Save credentials
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
        print(f"✓ Credentials saved to {token_file}")
    
    return creds


def main():
    parser = argparse.ArgumentParser(
        description='Authenticate with Google APIs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available scopes:
  drive              - Full Google Drive access
  drive-readonly     - Read-only Drive access
  gmail              - Full Gmail access
  gmail-readonly     - Read-only Gmail access
  gmail-send         - Send emails only
  calendar           - Full Calendar access
  calendar-readonly  - Read-only Calendar access
  docs               - Full Docs access
  docs-readonly      - Read-only Docs access
  sheets             - Full Sheets access
  sheets-readonly    - Read-only Sheets access
  slides             - Full Slides access
  slides-readonly    - Read-only Slides access

Examples:
  python authenticate.py
  python authenticate.py --scopes drive,gmail
  python authenticate.py --scopes drive-readonly,gmail-readonly
  python authenticate.py --credentials-file my-credentials.json
        """
    )
    
    parser.add_argument(
        '--scopes',
        type=str,
        help='Comma-separated list of scopes (default: all services with full access)'
    )
    
    parser.add_argument(
        '--credentials-file',
        type=str,
        default=CREDENTIALS_FILE,
        help=f'Path to credentials.json (default: {CREDENTIALS_FILE})'
    )
    
    parser.add_argument(
        '--token-file',
        type=str,
        default=TOKEN_FILE,
        help=f'Path to save token.json (default: {TOKEN_FILE})'
    )
    
    parser.add_argument(
        '--list-scopes',
        action='store_true',
        help='List all available scope shortcuts'
    )
    
    args = parser.parse_args()
    
    if args.list_scopes:
        print("Available scope shortcuts:")
        for name, url in sorted(SCOPE_MAPPINGS.items()):
            print(f"  {name:20s} - {url}")
        sys.exit(0)
    
    try:
        creds = authenticate(
            scopes=args.scopes,
            credentials_file=args.credentials_file,
            token_file=args.token_file
        )
        
        print("\n" + "="*70)
        print("AUTHENTICATION COMPLETE")
        print("="*70)
        print(f"\nYou can now use the Google API scripts.")
        print(f"Token saved to: {args.token_file}")
        print(f"\nTo re-authenticate, delete {args.token_file} and run this script again.")
        print("\nSecurity note: Keep credentials.json and token.json secure!")
        print("Add them to .gitignore to prevent accidental commits.")
        
    except Exception as e:
        print(f"\nError during authentication: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
