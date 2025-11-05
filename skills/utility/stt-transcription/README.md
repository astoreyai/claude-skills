# Speech-to-Text Transcription

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![License](https://img.shields.io/badge/license-MIT-green)

## Description

Comprehensive speech-to-text capabilities using multiple STT engines including Whisper (local/free), Google Speech, Azure Speech, and AssemblyAI. Record audio, transcribe files, real-time processing, speaker identification, timestamps, and multi-language support.

## Features

- ✅ Multiple STT engines (Whisper, Google, Azure, AssemblyAI)
- ✅ Audio recording with voice activity detection
- ✅ File transcription (WAV, MP3, M4A, FLAC, OGG)
- ✅ Real-time streaming transcription
- ✅ Speaker diarization (identify who said what)
- ✅ Multi-language support (99+ languages)
- ✅ Timestamp and segment tracking
- ✅ Multiple output formats (text, JSON, SRT, VTT)
- ✅ Batch processing
- ✅ Audio enhancement (denoise, normalize)
- ✅ Video subtitle generation

## Installation

### Prerequisites

- Python 3.8+
- Microphone (for recording)
- API keys (for cloud engines)

### Setup

1. Install Whisper (free, local):
   ```bash
   pip install openai-whisper
   ```

2. For cloud engines (optional):
   ```bash
   pip install google-cloud-speech azure-cognitiveservices-speech assemblyai
   ```

3. Audio dependencies:
   ```bash
   pip install sounddevice soundfile numpy
   ```

## Usage

### Record and Transcribe

```bash
# Record audio
python scripts/record_audio.py --output recording.wav

# Transcribe with Whisper (free)
python scripts/transcribe_whisper.py --file recording.wav

# Real-time transcription
python scripts/stream_whisper.py
```

### Engine Comparison

| Engine | Cost | Speed | Quality | Best For |
|--------|------|-------|---------|----------|
| Whisper | Free | Medium | High | Privacy, offline |
| Google | $1.44/hr | Fast | High | Real-time |
| Azure | $1/hr | Fast | High | Enterprise |
| AssemblyAI | $0.90/hr | Medium | Very High | Analysis |

## Examples

### Example 1: Meeting Transcription

Record meeting, transcribe with speaker labels, export as markdown

### Example 2: Voice Notes

Quick voice note recording and transcription to markdown

### Example 3: Video Subtitles

Extract audio from video, generate SRT subtitles

## Configuration

Choose Whisper model size:
- tiny/base: Fast, good for notes
- small/medium: Balanced
- large: Best accuracy, slower

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Aaron Storey (@astoreyai)
