# Venue Detection Component

## Purpose
Route review request to appropriate pathway (NeurIPS vs IEEE).

## Detection Algorithm

### Priority 1: Explicit User Statement
```
User says "NeurIPS" OR "Neural Information Processing Systems"?
→ ROUTE: NeurIPS Pathway ✓

User says "IEEE" OR mentions IEEE publication name?
→ ROUTE: IEEE Pathway ✓

User says other venue?
→ INFORM: This skill supports NeurIPS and IEEE only
```

### Priority 2: Document Markers

**NeurIPS Indicators**:
- `\usepackage{neurips_2025}` or similar
- "NeurIPS 2025 Paper Checklist" section
- Single-column, 9-page limit
- Double-blind formatting

**IEEE Indicators**:
- `\documentclass{IEEEtran}`
- Two-column format
- Numeric citations [1], [2], [3]
- Author names visible (single-blind)

### Priority 3: Ask User
```
If cannot determine from above:
→ "Is this for NeurIPS, IEEE, or another venue?"
→ Wait for response
→ Route based on answer
```

## Output Format
```
VENUE: [NeurIPS / IEEE / Other]
CONFIDENCE: [High / Medium / Low]
BASIS: [Explicit statement / Template markers / User confirmation]
NEXT: [Route to Section 3 / Route to Section 4 / Inform limitations]
```

## Critical Rule
**Never proceed with review until venue confirmed.**
