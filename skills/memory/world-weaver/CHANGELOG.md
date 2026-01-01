# Changelog

All notable changes to the World Weaver plugin are documented here.

## [1.1.0] - 2025-11-28

### Added

**Integrations**
- `kymera-voice`: Voice-to-memory integration for Kymera Voice assistant
  - `JarvisMemoryHook`: Main hook class for voice memory
  - `VoiceMemoryBridge`: Low-level bridge for custom integrations
  - Context enhancement before LLM calls
  - Episode storage after responses
  - Graceful fallback when WW unavailable

**Documentation**
- `integrations/kymera-voice/README.md`: Full integration guide
- `integrations/kymera-voice/SKILL.md`: Skill reference

### Changed

- Updated plugin.json to include integrations section
- Added kymera-voice as optional integration

### Integration

- Hooks into `vm/kymera-voice/src/kymera_voice/core/ky.py`
- Hooks into `vm/kymera-voice/src/kymera_voice/core/ky_optimized.py`
- 13 integration tests in `vm/kymera-voice/tests/test_ww_integration.py`

## [1.0.0] - 2025-11-27

### Added

**Skills**
- `ww-store`: Store episodes, entities, and skills in World Weaver
- `ww-recall`: Multi-strategy memory retrieval (semantic, temporal, graph, skill)
- `ww-context`: Build comprehensive context from memories
- `ww-consolidate`: Trigger and manage memory consolidation

**Commands**
- `/remember [content]`: Quick episode storage with auto-context
- `/recall [query]`: Search memories with filters
- `/ww-context`: Show current memory context
- `/consolidate`: Trigger memory consolidation

**Agents**
- `ww-memory`: Direct interface to all memory operations
- `ww-retriever`: Multi-strategy retrieval specialist
- `ww-synthesizer`: Cross-memory synthesis and context building

**Hooks**
- `session_start.py`: Load memory context on session start
- `session_end.py`: Store session summary as episode

**Infrastructure**
- `plugin.json`: Plugin manifest with configuration
- `README.md`: Installation and usage documentation

### Integration

- Works with World Weaver MCP server (`ww-memory`)
- Integrates with existing session-initializer/synthesizer hooks
- Supports Neo4j (graph) and Qdrant (vector) backends

## [0.1.0] - 2025-11-27

### Initial Development

- Plugin architecture planning
- Core skill definitions
- Hook implementation
