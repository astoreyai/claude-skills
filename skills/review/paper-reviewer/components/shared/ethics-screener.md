# Ethics and Responsibility Assessment Component

## Purpose
Identify ethical concerns and ensure responsible research practices.

## Three-Tier Assessment

### Tier 1: Mandatory Quick Screen (All Papers)

**Immediate Red Flags** (require ethics review):
- [ ] Primary goal increases weapon lethality
- [ ] Creates clear path to illegal activity
- [ ] Egregious privacy violations (doxxing tool)
- [ ] Obviously harmful content generation without mitigation
- [ ] Human subjects research without IRB/equivalent
- [ ] Dataset of minors without explicit safeguards
- [ ] Explicit discrimination/surveillance tool without justification

**If ANY checked → Flag for ethics review immediately**

### Tier 2: Domain-Specific Protocols

#### Protocol A: Human Subjects Research

**When to apply**: Direct human participants involved

**Checklist**:
- [ ] IRB approval mentioned
- [ ] Informed consent procedure described
- [ ] Privacy protection explained
- [ ] Fair compensation (≥ minimum wage in region)
- [ ] Risk mitigation described

**Risk Categories**:
- **Low**: Anonymous surveys, public data
- **Medium**: Personal info, sensitive topics
- **High**: Vulnerable populations, psychological stress, medical

**Checklist Reference**: Questions #14, #15

#### Protocol B: Dataset Ethics

**When to apply**: New dataset or data use

**Assessment**:
- [ ] Ethical collection method
- [ ] Privacy: PII minimized
- [ ] Consent obtained (if identifiable)
- [ ] Bias/representation discussed
- [ ] Licensing clear and respected
- [ ] Potential misuses discussed

**Special Concerns** (require extra scrutiny):
- Images/data of children
- Medical/health information
- Biometric data (faces, voices)
- Financial or criminal justice data
- Social media of identifiable individuals

**Checklist Reference**: Questions #12, #13

#### Protocol C: Societal Impact Assessment

**Apply to**: All papers, especially those with applications

**Impact Dimensions** (assess concern level for each):

1. **Safety**: Could cause physical harm? [None/Low/Medium/High]
2. **Security**: Creates vulnerabilities? [None/Low/Medium/High]
3. **Fairness**: Could discriminate? [None/Low/Medium/High]
4. **Privacy**: Threatens privacy? [None/Low/Medium/High]
5. **Misinformation**: Could spread false info? [None/Low/Medium/High]
6. **Environment**: Negative environmental impact? [None/Low/Medium/High]
7. **Dual-Use**: Weaponization potential? [None/Low/Medium/High]

**Discussion Requirement**:
- **Foundational research** (no clear path): Discussion optional
- **Application-oriented**: Discussion required
- **Dual-use obvious**: Discussion + mitigation required

**Checklist Reference**: Question #10 (Broader Impacts)

### Tier 3: Research Integrity

**Integrity Checklist**:
- [ ] No conflicts of interest (or declared)
- [ ] No suspected data fabrication
- [ ] Prior work properly cited
- [ ] No suspected plagiarism
- [ ] Methods sufficiently detailed
- [ ] Limitations honestly discussed

## When to Flag for Ethics Review

**Flag if ANY of**:
- Tier 1 red flags present
- High risk in multiple impact dimensions
- Inadequate discussion of obvious harms
- Human subjects without IRB
- Vulnerable populations without safeguards
- Clear dual-use without mitigation
- Research integrity concerns

**Note**: Flagging ≠ rejection. Ethics reviewers provide guidance.

## Documentation Template

```
ETHICS ASSESSMENT:

Ethics Review Required: [Yes/No]
└─ If Yes, reason: [Specific concern]

Tier 1 Screen: [Pass/Flag]
└─ Red flags: [None/List]

Tier 2 Detailed Assessment:
├─ Human Subjects: [NA/Adequate/Inadequate]
├─ Dataset Ethics: [NA/Adequate/Inadequate]
└─ Societal Impact: [Well-discussed/Adequately-discussed/Poorly-discussed/Not-discussed]

Impact Concern Levels:
├─ Safety: [None/Low/Medium/High]
├─ Security: [None/Low/Medium/High]
├─ Fairness: [None/Low/Medium/High]
├─ Privacy: [None/Low/Medium/High]
├─ Misinformation: [None/Low/Medium/High]
├─ Environment: [None/Low/Medium/High]
└─ Dual-Use: [None/Low/Medium/High]

Tier 3 Integrity: [No concerns/Minor concerns/Significant concerns]

Overall Assessment:
[No concerns / Concerns adequately addressed / Concerns inadequately addressed / Major concerns]

Specific Issues:
- [Issue 1]
- [Issue 2]

Recommendations:
- [Suggestion for addressing concern]

Checklist Evaluation:
- Q9 (Code of Ethics): [Yes/No]
- Q10 (Broader Impacts): [Yes/No/NA]
- Q14 (Human Subjects): [Yes/No/NA]
- Q15 (IRB): [Yes/No/NA]
```
