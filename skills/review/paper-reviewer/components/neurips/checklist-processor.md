# NeurIPS Checklist Processor

## Purpose
Systematically evaluate author responses to the 16-question NeurIPS paper checklist.

## Processing Protocol

### Step 1: Completeness Check

**Verify all 16 questions answered**:
- Q1 (Claims)
- Q2 (Limitations)
- Q3 (Theory assumptions/proofs)
- Q4 (Reproducibility)
- Q5 (Code/Data access)
- Q6 (Experimental settings)
- Q7 (Statistical significance)
- Q8 (Compute resources)
- Q9 (Code of Ethics)
- Q10 (Broader impacts)
- Q11 (Safeguards)
- Q12 (Licenses for existing assets)
- Q13 (New assets documentation)
- Q14 (Human subjects/crowdsourcing)
- Q15 (IRB approvals)
- Q16 (LLM usage)

**If any missing → Immediate flag to AC (desk reject risk)**

### Step 2: Response Validation

For each question check:
- [ ] Appropriate answer (Yes/No/NA)?
- [ ] Justification provided?
- [ ] Justification quality (substantive/minimal/missing)?

**Invalid responses**:
- "TODO" left in place
- No justification
- Justification contradicts answer
- Evasive non-answer

### Step 3: Answer Adequacy

**Q1 (Claims)**: Should almost always be "Yes"
- Cross-check: Do claims match results?
- Red flag: "No" or "NA" without excellent reason

**Q2 (Limitations)**: Should be "Yes" with substantive discussion
- Cross-check: Is there Limitations section? Are limitations honest?
- Red flag: "No" (has limitations but doesn't discuss)
- Note: "NA" (no limitations) almost never appropriate

**Q3 (Theory assumptions/proofs)**: "Yes" if theoretical, "NA" if not
- Cross-check: Are assumptions stated? Proofs complete?
- Red flag: "Yes" but missing proofs

**Q4 (Reproducibility)**: "Yes" if experimental, "NA" if not
- Cross-check: Could expert reproduce?
- Red flag: "No" without compelling reason

**Q5 (Code/Data)**: "Yes" preferred, "No" acceptable with reason
- Valid "No": Proprietary, privacy, security
- Invalid: "Just didn't do it"

**Q6 (Experimental settings)**: Should be "Yes" if experimental
- Red flag: "No" - should almost never be "No"

**Q7 (Statistical significance)**: "Yes" for empirical work
- Acceptable "No": "Single deterministic algorithm"
- Problematic: Stochastic method without error bars

**Q8 (Compute resources)**: Should be "Yes"
- May be brief but should have essentials

**Q9 (Code of Ethics)**: Should be "Yes"
- Red flag: "No" or "NA" requires explanation

**Q10 (Broader impacts)**: "Yes" if applied, "NA" if foundational
- Acceptable "NA": Pure theory without clear application
- Problematic: "NA" for obviously applicable work

**Q11 (Safeguards)**: "NA" for most, "Yes" if risky
- Red flag: Should be "Yes" but is "NA" or "No"

**Q12 (Licenses)**: "Yes" if using existing assets
- Red flag: Using assets but says "NA"

**Q13 (New assets)**: "Yes" if releasing, "NA" if not

**Q14 (Human subjects)**: "NA" for most
- Red flag: Used humans but says "NA"

**Q15 (IRB)**: "NA" for most
- Red flag: Human subjects without IRB

**Q16 (LLM usage)**: "NA" for most (LLM not core method)
- "Yes" only if LLM central to contribution

### Step 4: Synthesis

**Overall Checklist Assessment**:
```
Completeness: [Complete/Incomplete]
Answer Validity: [All valid/Some invalid]

Adequacy by Question:
- Fully adequate: [List Qs]
- Adequate with concerns: [List Qs]
- Inadequate: [List Qs]

Critical Issues: [Any problematic responses]
Positive Notes: [Particularly thorough responses]

Integration with Review:
[How checklist informs assessment]

Questions for Authors: [Follow-up needed]
```

## Checklist Impact on Review

1. **Desk Reject Risk**: Incomplete → potential desk reject
2. **Transparency Signal**: Honest limitations → positive; evasive → negative
3. **Dimension Assessment**: Q4-8 inform reproducibility; Q9-11 inform ethics
4. **Red Flags**: Contradictions, inappropriate "NA", unsupported "Yes"

## Documentation Template

```
CHECKLIST EVALUATION:

Completeness: [Complete/Incomplete - list missing if any]

Per-Question Assessment:

Q1 (Claims): [Answer] - [Adequate/Inadequate] - [Notes]
Q2 (Limitations): [Answer] - [Adequate/Inadequate] - [Notes]
Q3 (Theory): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q4 (Reproducibility): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q5 (Code/Data): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q6 (Settings): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q7 (Statistics): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q8 (Compute): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q9 (Ethics): [Answer] - [Adequate/Inadequate] - [Notes]
Q10 (Impacts): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q11 (Safeguards): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q12 (Licenses): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q13 (Assets): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q14 (Human Subjects): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q15 (IRB): [Answer] - [Adequate/Inadequate/NA] - [Notes]
Q16 (LLM): [Answer] - [Adequate/Inadequate/NA] - [Notes]

Summary:
Critical Issues: [None/List]
Concerns: [None/List]
Positive Aspects: [Note thorough/honest responses]

Impact on Review:
[How checklist responses inform overall assessment]
```
