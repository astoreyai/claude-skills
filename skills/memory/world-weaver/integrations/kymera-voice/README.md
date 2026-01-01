# Kymera Voice Integration

World Weaver memory integration for Kymera Voice assistant.

## Overview

This integration connects World Weaver's tripartite memory system to Kymera Voice,
enabling the voice assistant to:

- **Remember conversations**: Store voice interactions as episodic memories
- **Context enhancement**: Retrieve relevant memories to inform responses
- **Personal knowledge**: Access user's semantic knowledge graph
- **Learn patterns**: Build procedural memories from repeated interactions

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Kymera Voice (ky.py)                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Wake Word   │  │ GPU STT     │  │ Streaming TTS       │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         │                │                     │            │
│         └────────────────┼─────────────────────┘            │
│                          │                                  │
│                   ┌──────▼──────┐                           │
│                   │ JarvisMemory│◄─── Memory Hook           │
│                   │    Hook     │                           │
│                   └──────┬──────┘                           │
└──────────────────────────┼──────────────────────────────────┘
                           │ HTTP/WS
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                 World Weaver MCP Server                       │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐  │
│  │   Episodic   │ │   Semantic   │ │     Procedural       │  │
│  │   Memory     │ │   Memory     │ │     Memory           │  │
│  └──────────────┘ └──────────────┘ └──────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

## Installation

### 1. Install World Weaver

```bash
cd ~/ww
pip install -e ".[dev]"
```

### 2. Install Kymera Voice

```bash
cd ~/vm/kymera-voice
pip install -e ".[dev]"
```

### 3. Start World Weaver Services

```bash
# Start databases (if using Docker)
docker-compose -f ~/ww/docker-compose.yml up -d

# Or start MCP server directly
WW_URL=http://localhost:8765 python -m ww.mcp.server
```

### 4. Run Kymera Voice with Memory

```bash
# Voice assistant with memory enabled (default)
cd ~/vm/kymera-voice
kymera-voice jarvis

# Or with custom WW URL
WW_URL=http://custom:9999 kymera-voice jarvis

# Disable memory if needed
kymera-voice jarvis --no-memory
```

## API Reference

### JarvisMemoryHook

Main integration class in `ww.integrations.kymera.jarvis_hook`.

```python
from ww.integrations.kymera import JarvisMemoryHook

# Create hook (async)
hook = await JarvisMemoryHook.create_async(
    ww_url="http://localhost:8765",
    session_id="ky-session-123",
)

# Enhance context before LLM call
enhanced = await hook.enhance_context(
    query="What did we discuss about XAI?",
    session_id="ky-session-123",
)
# Returns: EnhancedContext with system_prompt_addition, relevant_memories

# Store interaction after response
await hook.on_response(
    user_text="What is XAI?",
    response_text="XAI stands for Explainable AI...",
    was_action=False,
    was_interrupted=False,
)
```

### VoiceMemoryBridge

Lower-level bridge in `ww.integrations.kymera.bridge`.

```python
from ww.integrations.kymera import VoiceMemoryBridge

bridge = VoiceMemoryBridge(ww_url="http://localhost:8765")
await bridge.connect()

# Store conversation
await bridge.store_conversation(
    user_text="Set a reminder",
    assistant_text="Reminder set for 3pm",
    was_action=True,
    session_id="ky-123",
)

# Get relevant context
context = await bridge.get_context_for_query(
    query="What reminders do I have?",
    session_id="ky-123",
)
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WW_URL` | `http://localhost:8765` | World Weaver server URL |
| `WW_SESSION_PREFIX` | `ky-` | Session ID prefix |
| `WW_MAX_MEMORIES` | `10` | Max memories to retrieve |
| `WW_LOOKBACK_DAYS` | `7` | Days to search back |

### Kymera Voice Config

In `VoiceConfig`:

```python
config = VoiceConfig()
ky = Ky(
    config,
    memory_enabled=True,  # Enable WW integration
    ww_url="http://localhost:8765",
)
```

## Memory Flow

### 1. Conversation Start

When Kymera Voice starts:
1. `JarvisMemoryHook.create_async()` connects to WW server
2. Session ID generated with `ky-{uuid}` format
3. Initial context loaded from recent memories

### 2. User Query

When user speaks:
1. STT transcribes audio to text
2. `hook.enhance_context()` retrieves relevant memories
3. Memories added to LLM system prompt
4. LLM generates response with memory context

### 3. Response Storage

After each interaction:
1. `hook.on_response()` called with user/assistant text
2. Episode created with:
   - Content: "User: X | Assistant: Y"
   - Metadata: session_id, was_action, was_interrupted
   - Importance: Based on interaction type
3. Entities extracted and linked in semantic memory

### 4. System Actions

For system commands (volume, media, etc.):
1. Action executed directly (no LLM)
2. Episode stored with `was_action=True`
3. Lower importance weight applied

## Testing

Run integration tests:

```bash
cd ~/vm/kymera-voice
pytest tests/test_ww_integration.py -v
```

Tests cover:
- WW availability detection
- Graceful fallback when WW unavailable
- Memory hook initialization
- Context enhancement
- Episode storage
- URL configuration

## Troubleshooting

### Memory not connecting

```bash
# Check WW server is running
curl http://localhost:8765/health

# Check logs
tail -f ~/.ww/logs/server.log

# Verify environment
echo $WW_URL
```

### Context not enhanced

```bash
# Verify memories exist
/recall --recent --limit 5

# Check session ID matches
# In Kymera Voice logs, look for "Memory: enabled"
```

### Episodes not stored

```bash
# Check WW server logs for errors
# Verify database connections
curl http://localhost:6333/collections  # Qdrant
curl http://localhost:7474              # Neo4j
```

## Related Files

- `ww/integrations/kymera/jarvis_hook.py` - Main hook class
- `ww/integrations/kymera/bridge.py` - Low-level bridge
- `ww/integrations/kymera/context_injector.py` - Context building
- `vm/kymera-voice/src/kymera_voice/core/ky.py` - Voice interface
- `vm/kymera-voice/tests/test_ww_integration.py` - Integration tests

## Changelog

### v1.0.0 (2025-11-28)
- Initial integration with JarvisMemoryHook
- Context enhancement before LLM calls
- Episode storage after responses
- Graceful fallback when WW unavailable
- 13 integration tests passing
