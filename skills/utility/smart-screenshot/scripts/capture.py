#!/usr/bin/env python3
"""
Smart Screenshot Tool - PrtSc with OCR and MarkItDown conversion

Press PrtSc to capture screen region, extract text with OCR,
convert to markdown, and save with auto-formatting.
"""
import argparse
import sys
from PIL import Image, ImageGrab, ImageEnhance, ImageFilter
import pytesseract
from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pyautogui
import io

try:
    from markitdown import MarkItDown
    MARKITDOWN_AVAILABLE = True
except ImportError:
    MARKITDOWN_AVAILABLE = False
    print("Warning: markitdown not available. Install with: pip install markitdown")

class ScreenCapture:
    def __init__(self):
        self.root = None
        self.canvas = None
        self.start_x = None
        self.start_y = None
        self.current_rect = None
        self.screenshot = None
        self.mode = None  # 'image' or 'text'
    
    def select_region(self):
        """Interactive region selection"""
        # Take full screenshot
        self.screenshot = ImageGrab.grab()
        
        # Create fullscreen window
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.root.configure(background='grey')
        
        # Create canvas
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.canvas = tk.Canvas(
            self.root,
            width=screen_width,
            height=screen_height,
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Bind events
        self.canvas.bind('<Button-1>', self.on_mouse_down)
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_mouse_up)
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        # Instructions
        instruction = tk.Label(
            self.root,
            text="Click and drag to select region (Press ESC to cancel)",
            bg='black',
            fg='white',
            font=('Arial', 12)
        )
        instruction.place(x=10, y=10)
        
        self.root.mainloop()
        
        return self.selected_region
    
    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y
    
    def on_mouse_drag(self, event):
        if self.current_rect:
            self.canvas.delete(self.current_rect)
        
        self.current_rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline='red', width=2
        )
    
    def on_mouse_up(self, event):
        x1, y1 = min(self.start_x, event.x), min(self.start_y, event.y)
        x2, y2 = max(self.start_x, event.x), max(self.start_y, event.y)
        
        self.selected_region = (x1, y1, x2, y2)
        self.root.quit()
        self.root.destroy()

def choose_mode():
    """Ask user to choose between image or text mode"""
    root = tk.Tk()
    root.withdraw()
    
    result = messagebox.askquestion(
        "Capture Mode",
        "Do you want to capture as IMAGE?\n\n"
        "YES = Image mode (save screenshot)\n"
        "NO = Text mode (OCR + Markdown)",
        icon='question'
    )
    
    root.destroy()
    return 'image' if result == 'yes' else 'text'

def enhance_for_ocr(image):
    """Enhance image for better OCR results"""
    # Convert to grayscale
    image = image.convert('L')
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    
    # Sharpen
    image = image.filter(ImageFilter.SHARPEN)
    
    # Threshold to black and white
    threshold = 128
    image = image.point(lambda p: p > threshold and 255)
    
    return image

def ocr_image(image, language='eng'):
    """Extract text from image using OCR"""
    # Enhance image
    enhanced = enhance_for_ocr(image)
    
    # Perform OCR
    custom_config = r'--oem 3 --psm 6'  # LSTM OCR Engine, uniform text block
    text = pytesseract.image_to_string(
        enhanced,
        lang=language,
        config=custom_config
    )
    
    return text.strip()

def convert_to_markdown(text, source_info=None):
    """Convert extracted text to formatted markdown"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    markdown = f"""# Screenshot Text

**Captured:** {timestamp}
"""
    
    if source_info:
        markdown += f"**Source:** {source_info}\n"
    
    markdown += f"""
## Extracted Text

{text}

---
*Extracted using OCR*
"""
    
    return markdown

def image_to_markdown_with_markitdown(image_path):
    """Use Microsoft's MarkItDown for conversion"""
    if not MARKITDOWN_AVAILABLE:
        return None
    
    try:
        md = MarkItDown()
        result = md.convert(image_path)
        return result.text_content
    except Exception as e:
        print(f"MarkItDown error: {e}")
        return None

def save_file_dialog(default_name, default_ext='.md'):
    """Show save file dialog"""
    root = tk.Tk()
    root.withdraw()
    
    filetypes = []
    if default_ext == '.md':
        filetypes = [
            ('Markdown files', '*.md'),
            ('Text files', '*.txt'),
            ('All files', '*.*')
        ]
    else:
        filetypes = [
            ('PNG files', '*.png'),
            ('JPEG files', '*.jpg'),
            ('All files', '*.*')
        ]
    
    filename = filedialog.asksaveasfilename(
        title="Save As",
        initialfile=default_name,
        defaultextension=default_ext,
        filetypes=filetypes
    )
    
    root.destroy()
    return filename

def capture_and_process(mode=None, output=None):
    """Main capture and processing workflow"""
    # Choose mode if not specified
    if not mode:
        mode = choose_mode()
    
    print(f"📸 Mode: {mode.upper()}")
    
    # Select region
    print("Select region on screen...")
    capturer = ScreenCapture()
    region = capturer.select_region()
    
    if not hasattr(capturer, 'selected_region'):
        print("Capture cancelled")
        return
    
    # Crop screenshot
    cropped = capturer.screenshot.crop(region)
    
    if mode == 'image':
        # Image mode - just save the screenshot
        if not output:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            default_name = f"screenshot-{timestamp}.png"
            output = save_file_dialog(default_name, '.png')
        
        if output:
            cropped.save(output, 'PNG')
            print(f"✓ Screenshot saved: {output}")
            
            # Show success message
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Success", f"Screenshot saved to:\n{output}")
            root.destroy()
        
    elif mode == 'text':
        # Text mode - OCR and convert to markdown
        print("🔍 Extracting text with OCR...")
        text = ocr_image(cropped)
        
        if not text:
            print("❌ No text found in image")
            return
        
        print(f"✓ Extracted {len(text)} characters")
        
        # Try MarkItDown first, fall back to simple conversion
        if MARKITDOWN_AVAILABLE:
            # Save temp image for MarkItDown
            temp_image = Path("temp_screenshot.png")
            cropped.save(temp_image, 'PNG')
            
            print("📝 Converting with MarkItDown...")
            markdown = image_to_markdown_with_markitdown(str(temp_image))
            
            # Clean up temp file
            temp_image.unlink()
            
            if not markdown:
                markdown = convert_to_markdown(text)
        else:
            markdown = convert_to_markdown(text)
        
        # Save markdown
        if not output:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            default_name = f"screenshot-text-{timestamp}.md"
            output = save_file_dialog(default_name, '.md')
        
        if output:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"✓ Markdown saved: {output}")
            
            # Show success with preview
            root = tk.Tk()
            root.withdraw()
            preview = text[:100] + "..." if len(text) > 100 else text
            messagebox.showinfo(
                "Success",
                f"Text extracted and saved to:\n{output}\n\nPreview:\n{preview}"
            )
            root.destroy()

def main():
    parser = argparse.ArgumentParser(
        description='Smart Screenshot with OCR and MarkItDown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive capture (prompts for mode)
  python capture.py
  
  # Capture as image
  python capture.py --mode image
  
  # Capture text with OCR
  python capture.py --mode text
  
  # Specify output file
  python capture.py --mode text --output notes.md
  
  # Full screen capture
  python capture.py --fullscreen --mode image
        """
    )
    
    parser.add_argument(
        '--mode',
        choices=['image', 'text'],
        help='Capture mode (image or text)'
    )
    
    parser.add_argument(
        '--output',
        help='Output file path'
    )
    
    parser.add_argument(
        '--fullscreen',
        action='store_true',
        help='Capture entire screen (skip region selection)'
    )
    
    parser.add_argument(
        '--region',
        help='Region coordinates as x1,y1,x2,y2'
    )
    
    args = parser.parse_args()
    
    if args.fullscreen:
        # Capture full screen
        screenshot = ImageGrab.grab()
        
        if args.mode == 'text' or (not args.mode and choose_mode() == 'text'):
            # OCR full screen
            text = ocr_image(screenshot)
            markdown = convert_to_markdown(text, "Full screen")
            
            if not args.output:
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                args.output = f"fullscreen-{timestamp}.md"
            
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"✓ Saved: {args.output}")
        else:
            # Save full screen image
            if not args.output:
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                args.output = f"fullscreen-{timestamp}.png"
            
            screenshot.save(args.output, 'PNG')
            print(f"✓ Saved: {args.output}")
    
    elif args.region:
        # Capture specific region
        coords = [int(x) for x in args.region.split(',')]
        screenshot = ImageGrab.grab(bbox=tuple(coords))
        
        # Process similar to fullscreen
        if args.mode == 'text':
            text = ocr_image(screenshot)
            markdown = convert_to_markdown(text)
            
            if not args.output:
                args.output = "screenshot.md"
            
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"✓ Saved: {args.output}")
        else:
            if not args.output:
                args.output = "screenshot.png"
            
            screenshot.save(args.output, 'PNG')
            print(f"✓ Saved: {args.output}")
    
    else:
        # Interactive capture
        capture_and_process(mode=args.mode, output=args.output)

if __name__ == '__main__':
    main()
