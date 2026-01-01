# /ww-audit Command

Run comprehensive audit of World Weaver codebase using specialized bug-hunting agents.

## Usage

```
/ww-audit [scope] [options]
```

## Arguments

- `scope`: What to audit (default: all)
  - `all` - Full system audit
  - `learning` - Learning code (neuromodulators, traces, hebbian)
  - `memory` - Memory stores (episodic, semantic, procedural)
  - `concurrency` - Race conditions and threading
  - `performance` - Memory leaks and caching
  - `hinton` - Validate against Hinton's principles

## Options

- `--quick` - Fast audit (single pass)
- `--deep` - Thorough audit (multiple passes)
- `--output PATH` - Custom output location

## Examples

```bash
# Full audit
/ww-audit

# Quick learning audit
/ww-audit learning --quick

# Deep concurrency audit
/ww-audit concurrency --deep

# Custom output
/ww-audit all --output /home/aaron/mem/custom_audit.md
```

## Agents Invoked

| Scope | Agents |
|-------|--------|
| learning | ww-bio-auditor, ww-hinton-validator, ww-trace-debugger |
| memory | ww-bio-auditor, ww-cache-analyzer |
| concurrency | ww-race-hunter, ww-leak-hunter |
| performance | ww-leak-hunter, ww-cache-analyzer |
| hinton | ww-hinton-validator |
| all | All 6 agents |

## Output

Reports are generated to `/home/aaron/mem/`:
- `WW_AUDIT_SUMMARY_{timestamp}.md` - Overall summary
- `WW_AUDIT_{agent}_{timestamp}.md` - Per-agent reports

## Workflow

1. Parse scope and options
2. Select relevant agents
3. Run agents in parallel on target paths
4. Collect and merge results
5. Generate summary report
6. Display critical findings
