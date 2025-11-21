#!/usr/bin/env python3
"""
Quick audio recording and transcription using Whisper
"""
import argparse
import sounddevice as sd
import soundfile as sf
import numpy as np
import whisper
import sys
from datetime import datetime
from pathlib import Path

def record_audio(duration=None, sample_rate=16000, channels=1, output_file=None):
    """
    Record audio from microphone
    
    Args:
        duration: Recording duration in seconds (None = until Ctrl+C)
        sample_rate: Sample rate in Hz
        channels: Number of audio channels
        output_file: Output WAV file path
    """
    print(f"🎤 Recording... (Press Ctrl+C to stop)")
    
    try:
        if duration:
            print(f"Recording for {duration} seconds...")
            audio = sd.rec(
                int(duration * sample_rate),
                samplerate=sample_rate,
                channels=channels,
                dtype='float32'
            )
            sd.wait()
        else:
            print("Recording until you press Ctrl+C...")
            recording = []
            
            def callback(indata, frames, time, status):
                recording.append(indata.copy())
            
            with sd.InputStream(
                samplerate=sample_rate,
                channels=channels,
                callback=callback
            ):
                input()  # Wait for Enter or Ctrl+C
            
            audio = np.concatenate(recording, axis=0)
    
    except KeyboardInterrupt:
        print("\n✓ Recording stopped")
        if 'audio' in locals():
            pass
        else:
            print("No audio recorded")
            return None
    
    # Generate filename if not provided
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = f"recording-{timestamp}.wav"
    
    # Save audio
    sf.write(output_file, audio, sample_rate)
    print(f"✓ Audio saved to: {output_file}")
    
    return output_file

def transcribe_audio(audio_file, model_size="base", language=None):
    """
    Transcribe audio using Whisper
    
    Args:
        audio_file: Path to audio file
        model_size: Whisper model size (tiny, base, small, medium, large)
        language: Language code (e.g., 'en', 'es', 'fr')
    """
    print(f"🤖 Loading Whisper model '{model_size}'...")
    model = whisper.load_model(model_size)
    
    print(f"📝 Transcribing {audio_file}...")
    result = model.transcribe(
        audio_file,
        language=language,
        task='transcribe',
        verbose=False
    )
    
    return result

def format_transcript(result, format='text'):
    """
    Format transcription result
    
    Args:
        result: Whisper transcription result
        format: Output format ('text', 'json', 'srt', 'vtt')
    """
    if format == 'text':
        return result['text'].strip()
    
    elif format == 'json':
        import json
        return json.dumps(result, indent=2)
    
    elif format == 'srt':
        # SRT subtitle format
        srt = []
        for i, segment in enumerate(result['segments'], 1):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()
            srt.append(f"{i}\n{start} --> {end}\n{text}\n")
        return '\n'.join(srt)
    
    elif format == 'vtt':
        # WebVTT subtitle format
        vtt = ['WEBVTT\n']
        for segment in result['segments']:
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()
            vtt.append(f"{start} --> {end}\n{text}\n")
        return '\n'.join(vtt)

def format_timestamp(seconds):
    """Convert seconds to SRT/VTT timestamp format"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def main():
    parser = argparse.ArgumentParser(
        description='Record audio and transcribe with Whisper',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Quick voice note
  python quick_note.py
  
  # Record 30 seconds
  python quick_note.py --duration 30
  
  # Use larger model for better accuracy
  python quick_note.py --model medium
  
  # Transcribe existing file
  python quick_note.py --file recording.wav
  
  # Save as markdown
  python quick_note.py --output note.md
        """
    )
    
    parser.add_argument(
        '--file',
        help='Audio file to transcribe (skip recording)'
    )
    
    parser.add_argument(
        '--duration',
        type=int,
        help='Recording duration in seconds (default: until stopped)'
    )
    
    parser.add_argument(
        '--model',
        default='base',
        choices=['tiny', 'base', 'small', 'medium', 'large'],
        help='Whisper model size (default: base)'
    )
    
    parser.add_argument(
        '--language',
        help='Language code (e.g., en, es, fr)'
    )
    
    parser.add_argument(
        '--format',
        default='text',
        choices=['text', 'json', 'srt', 'vtt', 'markdown'],
        help='Output format (default: text)'
    )
    
    parser.add_argument(
        '--output',
        help='Output file path (default: auto-generated)'
    )
    
    parser.add_argument(
        '--no-save',
        action='store_true',
        help='Print to stdout instead of saving to file'
    )
    
    args = parser.parse_args()
    
    # Record or load audio
    if args.file:
        audio_file = args.file
        if not Path(audio_file).exists():
            print(f"Error: File not found: {audio_file}")
            sys.exit(1)
    else:
        audio_file = record_audio(duration=args.duration)
        if not audio_file:
            sys.exit(1)
    
    # Transcribe
    result = transcribe_audio(
        audio_file,
        model_size=args.model,
        language=args.language
    )
    
    # Format output
    if args.format == 'markdown':
        # Create markdown note
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transcript = result['text'].strip()
        
        output = f"""# Voice Note

**Date:** {timestamp}
**Audio:** {audio_file}
**Language:** {result.get('language', 'auto-detected')}

## Transcript

{transcript}

## Segments

"""
        for i, segment in enumerate(result['segments'], 1):
            start = format_timestamp(segment['start'])
            text = segment['text'].strip()
            output += f"**[{start}]** {text}\n\n"
    else:
        output = format_transcript(result, format=args.format)
    
    # Save or print
    if args.no_save:
        print("\n" + "="*60)
        print(output)
        print("="*60)
    else:
        # Generate output filename
        if args.output:
            output_file = args.output
        else:
            base = Path(audio_file).stem
            ext = '.md' if args.format == 'markdown' else f'.{args.format}'
            output_file = f"{base}-transcript{ext}"
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        
        print(f"\n✓ Transcript saved to: {output_file}")
        
        # Show preview
        preview = output[:200] + "..." if len(output) > 200 else output
        print(f"\nPreview:\n{preview}")

if __name__ == '__main__':
    main()
