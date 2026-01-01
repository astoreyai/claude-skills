# Ky Assistant

Personal AI voice assistant with orchestration, memory, and proactive features.

## Description

Ky is a Jarvis-like AI assistant that combines voice interaction, persistent memory, and intelligent task orchestration. It uses local LLMs for fast responses and Claude for complex tasks, with automatic routing based on task complexity.

## Applies When

- User wants a personal voice assistant
- User needs task orchestration and planning
- User wants proactive suggestions and memory
- User needs calendar/email integration
- User wants low-latency voice responses

## Components

### Closure (Brain)
Central orchestrator with lazy-loaded components:
- **Orchestrator**: Task coordination and context management
- **Planner**: LLM-powered task decomposition
- **Router**: Subagent routing (developer, researcher, trader, scribe)
- **Memory**: WW integration for persistent memory
- **Local LLM**: Ollama routing for 29-56ms latency
- **Integrations**: Calendar, Email, Visual wrappers
- **Proactive**: Memory surfacing, skill learning
- **Resilience**: Circuit breakers, health monitoring
- **Dashboard**: TUI status display

### VM (Voice)
Kymera Voice layer for audio I/O:
- Wake word detection (OpenWakeWord)
- GPU-accelerated STT (faster-whisper)
- Streaming TTS (Kokoro)
- Echo cancellation and VAD
- MCP server with 7 voice tools

### WW (Memory)
World Weaver tri-mode memory:
- Episodic (experiences with FSRS decay)
- Semantic (knowledge graph with ACT-R)
- Procedural (skills with Memp algorithm)

## Usage

```bash
# Start Ky with system tray
~/ky/ky-tray

# Interactive mode
~/ky/ky

# One-shot task
~/ky/ky "schedule a meeting with Bob tomorrow"

# Status dashboard
~/ky/ky-status

# Voice mode
~/ky/ky --voice
```

## Configuration

### Environment Variables
```bash
ANTHROPIC_API_KEY     # Required for Claude
OLLAMA_HOST           # Ollama URL (default: localhost:11434)
WW_URL                # WW memory URL (default: localhost:8765)
```

### Service Installation
```bash
# User services (tray, memory)
~/ky/services/install.sh install

# System services (Ollama)
~/ky/services/install.sh install --system
```

## Features

### LLM Routing
- **TRIVIAL** (greetings, yes/no) → tinyllama (~56ms)
- **SIMPLE/MODERATE** (questions, explanations) → mistral (~29ms)
- **COMPLEX** (code, analysis) → Claude (~800ms)

### Resilience
- Circuit breakers for all services
- Health monitoring with auto-recovery
- Graceful degradation through fallback chain

### Proactive Features
- Morning briefings with calendar/email
- Memory surfacing based on context
- Skill learning from successful patterns
- Proactive suggestions

## Requirements

- Python 3.11+
- Ollama (for local LLM)
- Neo4j + Qdrant (for WW memory)
- Docker (for services)
- PyGObject/GTK (for system tray)

## Location

`/home/aaron/ky/`

## Related

- [World Weaver Memory](../memory/world-weaver/SKILL.md)
- [Kymera Voice](../../integrations/kymera-voice/README.md)
