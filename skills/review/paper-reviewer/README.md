# Scientific Paper Reviewer Skill v2.0

## Multi-Venue Peer Review System

A comprehensive skill for conducting systematic, standards-compliant peer reviews for NeurIPS conferences and IEEE journals/transactions.

---

## Quick Start

### 1. Determine Venue
**Always start here**: Use the venue detection tree in `SKILL.md` Section 2

```
User mentions NeurIPS → Section 3
User mentions IEEE → Section 4  
Cannot determine → Ask user
```

### 2. Follow Appropriate Pathway
- **NeurIPS**: Double-blind, 1-6 scoring, checklist required
- **IEEE**: Single-blind (typical), Accept/Revise/Reject, decision tree

### 3. Use Components in Order
Each pathway has stage-by-stage components to guide systematic review

---

## What's New in v2.0

### Major Updates
✨ **Dual-venue support**: NeurIPS and IEEE pathways
✨ **Intelligent routing**: Automatic venue detection
✨ **Decision trees**: Clear logic for IEEE recommendations
✨ **Shared components**: Universal ethics and classification
✨ **Complete IEEE workflow**: From assessment to decision

### Architecture Improvements
- Separated venue-specific vs universal components
- Clear decision frameworks for both venues
- Comprehensive reference materials
- Streamlined templates

---

## Directory Structure

```
paper-reviewer-v2/
│
├── SKILL.md                    ★ START HERE - Main orchestrator
├── README.md                   ← You are here
│
├── components/                 Component library
│   ├── shared/                 Universal components
│   │   ├── venue-detector.md  ← Always run first
│   │   ├── paper-classifier.md
│   │   └── ethics-screener.md
│   │
│   ├── neurips/               NeurIPS-specific evaluation
│   │   ├── technical-assessment.md
│   │   ├── contribution-assessment.md
│   │   ├── clarity-assessment.md
│   │   └── checklist-processor.md
│   │
│   └── ieee/                  IEEE-specific evaluation
│       ├── technical-assessment.md
│       ├── significance-assessment.md
│       ├── clarity-assessment.md
│       └── decision-recommendation.md
│
├── templates/                 Review assembly templates
│   ├── neurips/
│   │   └── review-synthesis.md
│   └── ieee/
│       └── review-synthesis.md
│
└── reference/                 Guidelines and standards
    ├── neurips/
    │   ├── guidelines-2025.md
    │   └── paper-checklist.md
    └── ieee/
        ├── reviewer-guidelines.md
        └── decision-process.md
```

---

## How to Use

### For NeurIPS Review

1. **Confirm venue**: Check for NeurIPS template/checklist
2. **Classify paper**: Use shared/paper-classifier.md
3. **Technical assessment**: neurips/technical-assessment.md (45-60 min)
4. **Contribution**: neurips/contribution-assessment.md (30-40 min)
5. **Clarity**: neurips/clarity-assessment.md (20-30 min)
6. **Ethics & checklist**: shared/ethics + neurips/checklist (20-30 min)
7. **Score & synthesize**: neurips/review-synthesis.md (30-45 min)
8. **QA check**: Verify completeness and consistency (10-15 min)

**Total time**: 3-4 hours

**Output**: 1-6 score with confidence + detailed review

### For IEEE Review

1. **Confirm venue**: Check for IEEE template/format
2. **Classify paper**: Use shared/paper-classifier.md
3. **Technical assessment**: ieee/technical-assessment.md (45-60 min)
4. **Significance**: ieee/significance-assessment.md (30-40 min)
5. **Clarity**: ieee/clarity-assessment.md (20-30 min)
6. **Ethics**: shared/ethics-screener.md (15-20 min)
7. **Decision**: ieee/decision-recommendation.md (30-45 min)
8. **QA check**: Verify consistency and tone (10-15 min)

**Total time**: 3-3.5 hours

**Output**: Accept/Revise/Reject with justification

---

## Key Differences: NeurIPS vs IEEE

| Aspect | NeurIPS | IEEE |
|--------|---------|------|
| **Model** | Double-blind | Single-blind (typical) |
| **Output** | 1-6 numerical score | 3-tier decision |
| **Format** | Conference paper (9 pages) | Journal article (varies) |
| **Checklist** | Mandatory | Not required |
| **Timeline** | Conference deadlines | ~90-day cycle |
| **Emphasis** | Novelty + reproducibility | Soundness + significance |
| **Borderlines** | Explicit 3-4 scores | Major/Minor revision |

---

## Decision Trees

### NeurIPS Scoring
```
Technical quality + Contribution significance → Score
6: Groundbreaking (~0.5%)
5: Clear significant contribution (~25%)
4: Strengths > weaknesses (~10%)
3: Weaknesses > strengths (~10%)
2: Insufficient or flawed (~55%)
1: Fundamental problems (~5%)
```

### IEEE Recommendation
```
Technical sound? 
├─ No → REJECT
└─ Yes → Significant contribution?
    ├─ No → REJECT
    └─ Yes → Level of issues?
        ├─ None → ACCEPT
        ├─ Minor → MINOR REVISION
        └─ Major → MAJOR REVISION or REJECT
```

---

## Best Practices

### Universal Guidelines

**Always**:
✓ Run venue detection first
✓ Be specific and constructive
✓ Support claims with evidence
✓ Maintain professional tone
✓ Complete promptly
✓ Protect confidentiality

**Never**:
✗ Skip venue detection
✗ Use AI to draft reviews
✗ Be vague or harsh
✗ Review with conflicts
✗ Share unpublished work

### Quality Checklist

Before submitting any review:
- [ ] Venue correctly identified
- [ ] All stages completed
- [ ] Specific examples/line numbers provided
- [ ] Constructive feedback given
- [ ] Scoring/decision justified
- [ ] Tone professional throughout
- [ ] No identifying information
- [ ] Consistent across sections

---

## Troubleshooting

**Q: Can't determine venue from paper?**
A: Use venue-detector.md protocol → Ask user explicitly

**Q: Paper fits multiple types?**
A: Use paper-classifier.md → Pick primary + note secondary

**Q: Borderline between scores/decisions?**
A: Consult scoring-calibration.md (NeurIPS) or decision-recommendation.md (IEEE)

**Q: Ethical concerns?**
A: Flag immediately, follow ethics-screener.md

**Q: Too poorly written to evaluate?**
A: IEEE: Notify editor. NeurIPS: Note in review, may impact score.

---

## Version History

**v2.0 (October 2025)**
- Added complete IEEE pathway
- Created venue detection system
- Implemented decision tree frameworks
- Separated shared vs venue-specific components
- Enhanced reference materials

**v1.0**
- Initial NeurIPS-only implementation

---

## Support and Feedback

For questions about using this skill:
- Consult SKILL.md for detailed workflows
- Check reference/ materials for official guidelines
- Review component files for specific protocols

For official peer review policies:
- NeurIPS: See neurips.cc/Conferences/2025
- IEEE: See journals.ieeeauthorcenter.ieee.org

---

## Contributing

To extend this skill for other venues:
1. Create venue-specific components
2. Add decision tree to SKILL.md
3. Create appropriate templates
4. Add reference materials
5. Update README

---

## License and Attribution

This skill compiles best practices from:
- NeurIPS reviewer guidelines and checklists
- IEEE peer review policies and procedures
- Academic peer review standards
- Community feedback and iteration

Use responsibly to improve peer review quality and author support.

---

**Remember**: Good reviews are thorough, fair, constructive, and timely. They help authors improve their work and editors make informed decisions.
