---
name: paper-reviewer
description: Comprehensive pre-submission review orchestrator. Coordinates methodology checks, bias detection, AI text detection, statistical validation, and reporting guideline compliance for journal submissions.
version: 1.0.0
author: Aaron Storey
---

# Paper Reviewer

Comprehensive pre-submission review for journal manuscripts. Orchestrates multiple specialized skills from research-assistant to ensure publication readiness.

## When to Use

- Before submitting papers to journals
- After completing systematic reviews
- When preparing dissertation chapters for committee
- For quality assurance on research manuscripts

## Features

1. **AI Text Detection** - Identify LLM-generated patterns
2. **Methodology Assessment** - Verify research design rigor
3. **Bias Detection** - Apply RoB 2, ROBINS-I, QUADAS-2 frameworks
4. **Statistical Validation** - Check assumptions, effect sizes, power analysis
5. **Reporting Compliance** - Validate CONSORT, PRISMA, STROBE guidelines
6. **Citation Integrity** - Verify references, check for retractions
7. **Reproducibility Audit** - Assess code/data availability

## Usage

```
Review the manuscript at ~/Documents/submissions/AffectivePrompting/ for journal submission.
This is a systematic review targeting IEEE Transactions.
```

## Review Pipeline

### Phase 1: Triage
- Classify paper type (RCT, systematic review, observational, etc.)
- Identify target journal requirements
- List available files

### Phase 2: AI Detection
- Run ai-check skill
- Flag sections with AI patterns >30%
- Generate authenticity report

### Phase 3: Methodology
- Assess study design appropriateness
- Verify protocol adherence
- Check randomization/blinding (if applicable)

### Phase 4: Risk of Bias
- Apply appropriate RoB tool
- Document domain-by-domain assessment
- Generate traffic light visualization

### Phase 5: Statistical Validation
- Verify assumption testing
- Check effect size reporting
- Validate power analysis

### Phase 6: Reporting Compliance
- Apply appropriate checklist (CONSORT/PRISMA/STROBE)
- Calculate compliance percentage
- List missing items

### Phase 7: Citation Audit
- Verify all references
- Check for retractions
- Validate DOIs

### Phase 8: Reproducibility
- Check code availability
- Verify data accessibility
- Assess documentation completeness

## Output

Generates comprehensive review report:
- Executive summary with overall assessment
- Section-by-section findings
- Priority-ranked revision checklist
- Detailed appendices

## Paper Type-Specific Workflows

### Systematic Reviews
- PRISMA 2020 compliance
- AMSTAR 2 quality assessment
- Meta-analysis validation

### RCTs
- CONSORT compliance
- RoB 2 bias assessment
- ITT/per-protocol analysis check

### Observational Studies
- STROBE compliance
- ROBINS-I bias assessment
- Confounding control verification

## Integration

Uses research-assistant skills:
- ai-check
- risk-of-bias
- hypothesis-test
- effect-size
- power-analysis
- publication-prep
- citation-format
- prisma-diagram

## Configuration

Default thresholds (can override):
- AI detection: 30% (flag if higher)
- Reporting compliance: 85% minimum
- All 8 phases enabled by default

---

*Part of ai_scientist research workflow automation*
