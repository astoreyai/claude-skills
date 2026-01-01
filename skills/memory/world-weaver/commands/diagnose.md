# /ww-diagnose Command

Diagnose problems with World Weaver memory systems.

## Usage

```
/ww-diagnose [symptom] [options]
```

## Arguments

- `symptom`: Problem description
  - `learning` - Learning not improving
  - `memory` - Can't find memories
  - `slow` - Performance issues
  - `errors` - Getting errors
  - `corruption` - Data seems wrong
  - Or describe the issue in quotes: `"memories are disappearing"`

## Options

- `--verbose` - Show detailed diagnostic output
- `--quick` - Fast diagnosis (skip slow checks)
- `--output PATH` - Save diagnostic report

## Examples

```bash
# Diagnose learning issues
/ww-diagnose learning

# Diagnose performance
/ww-diagnose slow

# Custom symptom
/ww-diagnose "episodes not being stored"

# Verbose output
/ww-diagnose memory --verbose
```

## Diagnostic Flow

```
1. Quick health check (services, connections)
2. Symptom-specific checks
3. Run relevant agents if needed
4. Identify root cause
5. Provide fix recommendation
```

## Agents That May Be Invoked

| Symptom | Agents |
|---------|--------|
| learning | ww-bio-auditor, ww-trace-debugger |
| memory | (direct MCP queries) |
| slow | ww-leak-hunter, ww-cache-analyzer |
| errors | ww-race-hunter |
| corruption | ww-race-hunter, ww-cache-analyzer |

## Output

Diagnostic report with:
- Quick check results (service status)
- Root cause identification
- Evidence (logs, queries)
- Recommended fix (code or config)
- Verification steps
