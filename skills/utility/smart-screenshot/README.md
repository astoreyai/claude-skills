# Smart Screenshot

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Intelligent screen capture with OCR, markdown conversion, and smart formatting. Triggered by PrtSc key, captures screen regions, extracts text with OCR, converts to markdown using MarkItDown, and saves with auto-formatting. Similar to Windows Snipping Tool but with AI enhancements.

## Features

- ✅ Keyboard shortcut activation (PrtSc or custom)
- ✅ Multiple capture modes (region, window, full screen, scrolling)
- ✅ OCR text extraction (Tesseract or EasyOCR)
- ✅ Markdown conversion using Microsoft MarkItDown
- ✅ Image annotation tools (arrows, boxes, text, highlights)
- ✅ PDF to markdown conversion
- ✅ Multi-monitor support
- ✅ Clipboard integration
- ✅ Background service mode
- ✅ Auto-save with templates

## Installation

### Prerequisites

- Python 3.8+
- Tesseract OCR engine
- Screen access permissions

### Setup

1. Install Tesseract OCR:
   - Windows: Download from UB-Mannheim/tesseract
   - macOS: `brew install tesseract`
   - Linux: `sudo apt-get install tesseract-ocr`

2. Install Python dependencies:
   ```bash
   pip install pillow pyautogui mss pytesseract pyscreenshot keyboard pynput markitdown
   ```

3. Run service:
   ```bash
   python scripts/screenshot_service.py
   ```

## Usage

### Quick Capture

1. Press PrtSc
2. Choose "Image" or "Text" mode
3. Select region
4. Auto-process and save

### Command Line

```bash
# Capture with UI
python scripts/capture.py

# Capture and OCR to markdown
python scripts/capture.py --mode text --output notes.md

# Convert PDF to markdown
python scripts/pdf_to_markdown.py --input document.pdf --output document.md
```

## Examples

### Example 1: Code Documentation

Capture code from screen, OCR extracts it, save as markdown code block

### Example 2: Meeting Slides

Capture multiple slides, extract text, combine into formatted notes

### Example 3: Research Papers

Screenshot paper sections, annotate with notes, save annotated version

## Configuration

Edit `config.yaml`:
```yaml
hotkey: "Print"
default_mode: "prompt"
ocr:
  engine: "tesseract"
  enhance: true
output:
  directory: "~/Screenshots"
  clipboard: true
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)
