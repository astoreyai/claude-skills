# kymera-voice-memory

Voice-to-memory integration skill for Kymera Voice assistant.

## Description

Enables World Weaver memory integration in Kymera Voice, allowing the
voice assistant to remember conversations, retrieve relevant context,
and learn from interactions.

## When to Use

- When configuring Kymera Voice with memory features
- When debugging voice-memory integration issues
- When customizing memory behavior for voice interactions

## Integration Points

### In Kymera Voice (ky.py)

```python
# Import (optional - graceful fallback)
try:
    from ww.integrations.kymera import JarvisMemoryHook
    WW_AVAILABLE = True
except ImportError:
    WW_AVAILABLE = False

# Initialize in __init__
self.memory_enabled = memory_enabled and WW_AVAILABLE
self.ww_url = ww_url or os.environ.get("WW_URL", "http://localhost:8765")
self.memory_hook: JarvisMemoryHook | None = None

# Connect in run()
if self.memory_enabled:
    try:
        self.memory_hook = await JarvisMemoryHook.create_async(
            ww_url=self.ww_url,
            session_id=f"ky-{self.conversation.session_id}",
        )
    except Exception as e:
        logger.warning(f"World Weaver unavailable: {e}")
        self.memory_hook = None

# Enhance context before LLM call
if self.memory_hook:
    enhanced = await self.memory_hook.enhance_context(
        user_text, session_id=self.conversation.session_id
    )
    if enhanced and enhanced.system_prompt_addition:
        context["memory_context"] = enhanced.system_prompt_addition

# Store after response
if self.memory_hook:
    await self.memory_hook.on_response(
        user_text, response_text,
        was_action=False,
        was_interrupted=was_interrupted,
    )
```

## Key Classes

### JarvisMemoryHook

Primary integration class for voice assistants.

**Methods:**
- `create_async(ww_url, session_id)` - Factory for async initialization
- `enhance_context(query, session_id)` - Get relevant memories for query
- `on_response(user, assistant, was_action, was_interrupted)` - Store episode

### EnhancedContext

Returned by `enhance_context()`:
- `system_prompt_addition: str` - Text to add to system prompt
- `relevant_memories: list[dict]` - Raw memory data

### VoiceMemoryBridge

Lower-level bridge for custom integrations:
- `connect()` - Establish connection to WW
- `store_conversation()` - Store interaction episode
- `get_context_for_query()` - Retrieve relevant context

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WW_URL` | `http://localhost:8765` | WW server URL |

### Kymera Voice Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `memory_enabled` | `True` | Enable WW integration |
| `ww_url` | From env | Override WW server URL |

## Requirements

- World Weaver (`ww`) package installed
- WW MCP server running
- Neo4j database (graph storage)
- Qdrant database (vector storage)

## Testing

```bash
cd ~/vm/kymera-voice
pytest tests/test_ww_integration.py -v
```

## Graceful Degradation

The integration is designed for graceful fallback:
1. If `ww` package not installed: `WW_AVAILABLE = False`
2. If WW server not running: `memory_hook = None`
3. If memory operations fail: Logged, but doesn't crash

Voice assistant continues working without memory when WW unavailable.
