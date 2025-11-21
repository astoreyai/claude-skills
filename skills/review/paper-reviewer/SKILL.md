# Scientific Paper Reviewer Skill (Multi-Venue)

## Quick Reference Card

**START HERE**: Use the venue detection tree below before proceeding.

```
VENUE DETECTION TREE:
User mentions "NeurIPS" OR has neurips template? 
→ Use Section 3: NeurIPS Review Pathway

User mentions "IEEE" OR has IEEE template/format?
→ Use Section 4: IEEE Review Pathway  

Cannot determine?
→ Ask user: "Is this for NeurIPS, IEEE, or another venue?"
```

---

## 1. Skill Overview

**Purpose**: Systematic, standards-compliant peer review for NeurIPS conferences and IEEE journals/transactions.

**Key Features**:
- Dual-pathway architecture (NeurIPS vs IEEE)
- Intelligent venue routing
- Venue-specific scoring systems
- Shared ethics and classification components

---

## 2. Architecture

```
paper-reviewer-v2/
├── SKILL.md (orchestrator - this file)
├── components/
│   ├── shared/
│   │   ├── venue-detector.md ← START HERE
│   │   ├── paper-classifier.md
│   │   └── ethics-screener.md
│   ├── neurips/ ← NeurIPS-specific evaluation
│   └── ieee/ ← IEEE-specific evaluation
├── templates/
│   ├── neurips/review-synthesis.md
│   └── ieee/review-synthesis.md
└── reference/
    ├── neurips/[NeurIPS guidelines]
    └── ieee/[IEEE guidelines]
```

---

## 3. NeurIPS Review Pathway

### Overview
- **Format**: Conference (double-blind)
- **Scoring**: 1-6 scale with acceptance rate targets
- **Timeline**: 3-4 hours per paper
- **Key requirement**: Mandatory paper checklist

### Review Stages

**Stage 1**: Paper Classification (15 min)
- Use: `components/shared/paper-classifier.md`
- Output: Primary type + secondary characteristics

**Stage 2**: Technical Assessment (45-60 min)  
- Use: `components/neurips/technical-assessment.md`
- Output: Quality score (1-4)

**Stage 3**: Contribution Assessment (30-40 min)
- Use: `components/neurips/contribution-assessment.md`  
- Output: Originality (1-4) + Significance (1-4)

**Stage 4**: Clarity Assessment (20-30 min)
- Use: `components/neurips/clarity-assessment.md`
- Output: Clarity score (1-4)

**Stage 5**: Ethics & Checklist (20-30 min)
- Use: `components/shared/ethics-screener.md`
- Use: `components/neurips/checklist-processor.md`
- Output: Ethics flag + checklist compliance

**Stage 6**: Scoring & Synthesis (30-45 min)
- Use: `templates/neurips/review-synthesis.md`
- Output: Overall score (1-6) + Confidence (1-5)

### NeurIPS Scoring Scale

| Score | Label | Target % | Use When |
|-------|-------|----------|----------|
| 6 | Strong Accept | ~0.5% | Groundbreaking, flawless |
| 5 | Accept | ~20-25% | Clear contribution, sound |
| 4 | Borderline Accept | ~10% | Strengths > weaknesses |
| 3 | Borderline Reject | ~10% | Weaknesses > strengths |
| 2 | Reject | ~50-60% | Insufficient contribution |
| 1 | Strong Reject | ~5% | Fundamental flaws |

### NeurIPS Review Format

```
SUMMARY: [100-200 words - factual overview]

STRENGTHS: [3-7 specific points with line refs]
1. [Strength with evidence]
2. [Strength with evidence]
...

WEAKNESSES: [3-8 specific points with line refs]
1. [Weakness with evidence and severity]
2. [Weakness with evidence and severity]
...

QUESTIONS: [3-5 questions for authors]
1. [Question] - Impact: [How answer affects evaluation]
2. [Question] - Impact: [How answer affects evaluation]
...

LIMITATIONS: [Yes/No + justification]
ETHICAL CONCERNS: [Yes/No + details if flagged]

SCORES:
- Quality: [1-4]
- Clarity: [1-4]  
- Originality: [1-4]
- Significance: [1-4]
- Overall: [1-6] [Detailed justification]
- Confidence: [1-5] [Basis for confidence level]
```

---

## 4. IEEE Review Pathway

### Overview
- **Format**: Journal (single-blind typical)
- **Decision**: 3-tier (Accept/Revise/Reject)
- **Timeline**: Prompt completion (editor has 90-day window)
- **Key focus**: Technical soundness + practical significance

### Review Stages

**Stage 1**: Paper Classification (15 min)
- Use: `components/shared/paper-classifier.md`
- Note: IEEE papers typically longer, more comprehensive

**Stage 2**: Technical Assessment (45-60 min)
- Use: `components/ieee/technical-assessment.md`  
- Output: Technical soundness evaluation

**Stage 3**: Significance Assessment (30-40 min)
- Use: `components/ieee/significance-assessment.md`
- Output: Originality + significance evaluation

**Stage 4**: Clarity Assessment (20-30 min)
- Use: `components/ieee/clarity-assessment.md`
- Output: Communication quality assessment

**Stage 5**: Ethics Screening (15-20 min)
- Use: `components/shared/ethics-screener.md`
- Focus: Plagiarism, duplicate publication, data integrity

**Stage 6**: Decision Recommendation (30-45 min)
- Use: `templates/ieee/review-synthesis.md`
- Output: Accept/Revise/Reject recommendation

### IEEE Decision Framework

```
Decision Tree:
Research technically sound?
├─ NO → REJECT (explain flaws)
└─ YES → Contribution significant?
    ├─ NO → REJECT (insufficient contribution)
    └─ YES → Issues requiring changes?
        ├─ NONE → ACCEPT (rare on first submission)
        ├─ MINOR → MINOR REVISION
        └─ MAJOR → MAJOR REVISION
```

### IEEE Review Format

```
SUMMARY: [Brief restatement of purpose/findings]

MAJOR CONCERNS:
1. [Methodological/analytical issues]
2. [Significant technical problems]
...

MINOR CONCERNS:
1. [Clarity/presentation issues]
2. [Editorial suggestions]
...

STRENGTHS:
- [Notable positive aspects]
- [Well-executed elements]
...

QUESTIONS FOR AUTHORS:
- [Clarifications needed]
- [Additional details required]
...

SUGGESTIONS FOR IMPROVEMENT:
- [Constructive, actionable feedback]
- [Reference additions with justification]
...

OVERALL ASSESSMENT: [Holistic evaluation]

RECOMMENDATION: [Accept / Major Revision / Minor Revision / Reject]
[Detailed justification for recommendation]
```

---

## 5. Best Practices (All Venues)

### Universal Do's
✓ Complete venue detection first
✓ Be thorough and systematic  
✓ Provide specific, actionable feedback
✓ Maintain professional tone
✓ Support criticisms with clear reasoning
✓ Complete reviews promptly
✓ Protect confidentiality

### Universal Don'ts
✗ Skip venue detection
✗ Use AI tools to draft reviews
✗ Be vague or dismissive
✗ Speculate about authors
✗ Suggest excessive irrelevant references
✗ Review with conflicts of interest
✗ Share confidential information

---

## 6. Venue Comparison Matrix

| Aspect | NeurIPS | IEEE |
|--------|---------|------|
| Review Model | Double-blind | Single-blind (typical) |
| Output | 1-6 score | Accept/Revise/Reject |
| Page Limit | 9 pages strict | Flexible by journal |
| Checklist | Mandatory | Not required |
| Timeline | Conference cycle | ~90 days |
| Acceptance Rate | ~25% | Varies by journal |
| Emphasis | Novelty + reproducibility | Technical quality + impact |
| Borderline Papers | Explicit 3-4 scores | Revision categories |

---

## 7. Quick Start Instructions

**New users**:
1. Read this SKILL.md first
2. Run venue detection (Section 2)
3. Follow appropriate pathway (Section 3 or 4)
4. Use components in order

**Experienced reviewers**:
1. Confirm venue
2. Jump to appropriate stage
3. Reference scoring/decision frameworks as needed

---

## 8. Component Dependencies

### Shared (Used by Both Venues)
- `venue-detector.md` - ALWAYS run first
- `paper-classifier.md` - Classification for both venues
- `ethics-screener.md` - Universal ethics check

### NeurIPS-Specific
- `technical-assessment.md` - Conference-focused evaluation
- `contribution-assessment.md` - Novelty emphasis
- `clarity-assessment.md` - Reproducibility focus
- `checklist-processor.md` - NeurIPS mandatory checklist
- `scoring-calibration.md` - 1-6 score determination

### IEEE-Specific  
- `technical-assessment.md` - Journal-depth evaluation
- `significance-assessment.md` - Practical impact focus
- `clarity-assessment.md` - Communication quality
- `decision-recommendation.md` - 3-tier decision logic

---

## 9. Troubleshooting

**Can't determine venue?**
→ Use `components/shared/venue-detector.md` protocol

**Unsure about scoring?**
→ NeurIPS: Check acceptance rate targets in Section 3
→ IEEE: Use decision tree in Section 4

**Ethics concerns?**
→ Flag immediately, consult `ethics-screener.md`

**Paper spans multiple types?**
→ Use `paper-classifier.md` to identify primary + secondary

**Deadline pressure?**
→ Prioritize technical assessment and decision, but complete all stages

---

## 10. Skill Metadata

**Version**: 2.0 (Multi-Venue)
**Supported**: NeurIPS 2025, IEEE Journals/Transactions 2025
**Last Updated**: October 2025
**Maintainer**: Review Standards Committee

**Changelog**:
- v2.0: Added IEEE pathway with decision tree routing
- v2.0: Created venue detection component
- v2.0: Separated shared vs venue-specific components
- v1.0: NeurIPS-only implementation

---

## Appendix: Ethical Principles (Both Venues)

**Confidentiality**: Never share or use unpublished work
**Objectivity**: Review based on merit, not personal bias
**Constructiveness**: Help authors improve their work
**Professionalism**: Maintain respectful, courteous tone
**Integrity**: Report suspected misconduct promptly
**Timeliness**: Complete reviews within expected timeframe
**Independence**: Declare conflicts, decline if present

---

**END OF MAIN SKILL DOCUMENTATION**

For detailed component usage, see individual files in `components/`, `templates/`, and `reference/` directories.
