# Claude Code Service

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Transform Claude Code from a command-line tool into a persistent background service with web UI, API access, and automated workflows. Run Claude as always-on assistance with multiple service modes including daemon, web server, API endpoint, and IDE integration.

## Features

- ✅ Background service (daemon) mode for always-on assistance
- ✅ Web server with browser-based chat interface
- ✅ RESTful API endpoint for programmatic access
- ✅ IDE integration (VS Code, JetBrains, Sublime Text)
- ✅ System service installation (Windows, macOS, Linux)
- ✅ Scheduled tasks and automation
- ✅ Webhook integration (GitHub, Slack, etc.)
- ✅ Authentication and security (Basic, Token, OAuth)
- ✅ SSL/TLS support
- ✅ Rate limiting and monitoring
- ✅ Docker deployment ready
- ✅ Health monitoring and metrics

## Installation

### Prerequisites

- Claude Code installed
- Python 3.8+
- Administrator/root access (for system service installation)
- Optional: Docker for containerized deployment

### Setup

1. Copy skill to Claude Code skills directory
2. Install web server dependencies:
   ```bash
   pip install flask flask-cors fastapi uvicorn
   ```
3. Choose deployment mode (see Usage)

## Usage

### Web Server Mode

```bash
claude-code serve --port 8080
# Access at http://localhost:8080
```

### Background Service

```bash
# Start daemon
claude-code daemon start

# Check status
claude-code daemon status
```

### System Service Installation

**Windows:**
```bash
python scripts/install_windows_service.py
```

**macOS:**
```bash
python scripts/install_macos_service.py
```

**Linux:**
```bash
python scripts/install_linux_service.py
```

## Examples

### Example 1: Web UI Access

Start service, access browser interface, chat with Claude

### Example 2: API Integration

Call RESTful endpoints from other applications

### Example 3: Scheduled Automation

Configure daily tasks (morning summary, email checks)

## Security

- Always use authentication for public-facing services
- Enable SSL/TLS for production
- Implement rate limiting
- Never commit credentials

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)
