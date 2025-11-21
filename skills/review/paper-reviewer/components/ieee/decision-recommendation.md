# IEEE Decision Recommendation Component

## Purpose
Synthesize assessment components into final Accept/Revise/Reject recommendation using IEEE decision framework.

## IEEE Three-Tier Decision System

### Decision Categories

**ACCEPT**
- Article meets IEEE standards for publication
- No significant changes required
- May have minor corrections (typos, formatting)
- **Rare on first submission**

**REVISE**
- Article has merit but requires changes
- Subdivided into Major and Minor Revision
- **Most common decision**

**REJECT**
- Fundamental flaws or insufficient contribution
- Cannot be salvaged with revision
- Out of scope or inappropriate for venue

## Decision Tree Framework

### Primary Decision Tree

```
STEP 1: Evaluate Technical Soundness
Is the research technically sound without major flaws?
│
├─ NO → RECOMMEND REJECT
│       └─ Justification: Fundamental technical problems
│
└─ YES → Proceed to STEP 2

STEP 2: Evaluate Contribution
Is the contribution significant and original enough for this venue?
│
├─ NO → RECOMMEND REJECT
│       └─ Justification: Insufficient contribution
│
└─ YES → Proceed to STEP 3

STEP 3: Evaluate Required Changes
What level of changes are needed?
│
├─ NO ISSUES → RECOMMEND ACCEPT (rare)
│
├─ MINOR ISSUES ONLY → RECOMMEND MINOR REVISION
│   └─ Examples:
│       - Clarity improvements needed
│       - Additional references to add
│       - Minor experimental gaps
│       - Presentation enhancements
│       - Editorial corrections
│
└─ MAJOR ISSUES → RECOMMEND MAJOR REVISION or REJECT
    └─ Decision depends on:
        - Can issues be resolved with revision?
        - Is core contribution preserved after fixes?
        - Is additional work reasonable?
```

### Secondary Considerations

**Ethical Issues**:
```
Ethics concerns flagged?
├─ YES → RECOMMEND REJECT
│       └─ Flag to editor immediately
└─ NO → Continue with primary tree
```

**Scope Appropriateness**:
```
Within IEEE publication scope?
├─ NO → RECOMMEND REJECT (out of scope)
└─ YES → Continue with primary tree
```

**Too Poorly Written**:
```
Language prevents evaluation?
├─ YES → NOTIFY EDITOR (desk reject candidate)
└─ NO → Continue with primary tree
```

## Major vs Minor Revision Decision Logic

### When to Recommend MAJOR REVISION

**Use when**:
- Significant methodological issues requiring new experiments
- Major gaps in validation requiring substantial work
- Serious clarity issues requiring extensive rewriting
- Important missing comparisons requiring new experiments
- Theoretical work needs significant additional analysis
- Multiple moderate issues combine to major scope

**Characteristics**:
- Changes require substantial time/effort (weeks to months)
- May require new data collection or experiments
- Core technical approach may need modification
- Original reviewers should re-review

**Example issues**:
- "Missing comparison to state-of-the-art methods X, Y, Z"
- "Methodology section unclear; needs major restructuring"
- "Insufficient experimental validation on realistic datasets"
- "Theoretical claims lack rigorous proofs"
- "Significant technical errors in Section 3 analysis"

### When to Recommend MINOR REVISION

**Use when**:
- Issues are fixable without new experiments
- Clarifications and elaborations sufficient
- Additional discussion or analysis needed
- Minor methodological adjustments required
- Presentation improvements needed
- Additional references to incorporate

**Characteristics**:
- Changes require modest time/effort (days to weeks)
- No new data collection needed
- Core technical approach sound
- May not require full re-review

**Example issues**:
- "Add discussion of computational complexity"
- "Include recent work [refs] in related work"
- "Clarify notation in Section 3.2"
- "Improve figure quality and captions"
- "Address grammatical issues throughout"
- "Add brief ablation study on parameter X"

### Borderline Cases

When uncertain between Major and Minor:
- **Lean toward Major** if multiple minor issues compound
- **Lean toward Minor** if issues are localized and clear
- Consider: "Would I be satisfied with authors' response addressing these issues without seeing revised experiments?"
  - YES → Minor Revision
  - NO → Major Revision

## Decision Matrix

### Technical Soundness × Significance

|                    | High Significance | Medium Significance | Low Significance |
|--------------------|-------------------|---------------------|------------------|
| **Excellent Tech** | Accept or Minor Rev | Minor Revision | Reject (scope) |
| **Good Tech**      | Minor Revision | Minor/Major Revision | Major Rev or Reject |
| **Adequate Tech**  | Major Revision | Major Revision | Reject |
| **Poor Tech**      | Reject | Reject | Reject |

## Assembling Justification

### Structure of Recommendation

```
RECOMMENDATION: [Accept / Minor Revision / Major Revision / Reject]

JUSTIFICATION:
[2-3 paragraph summary explaining recommendation]

Paragraph 1: Overall assessment
- State recommendation clearly
- Summarize key strengths
- Summarize key weaknesses

Paragraph 2: Technical evaluation summary
- Core technical soundness
- Significance and originality
- Contribution quality

Paragraph 3: Required changes (if revision)
- What must be addressed
- What changes would strengthen paper
- Timeline expectations

For Reject: Explain why paper cannot meet standards even with revision
```

### Example Justifications

**Accept Example**:
```
RECOMMENDATION: Accept

This paper presents a novel and significant contribution to [area]. 
The methodology is sound, the experiments are comprehensive, and the 
results clearly demonstrate the value of the proposed approach. The 
writing is clear and the presentation is professional. Minor corrections 
noted in the review should be addressed during production.

The technical quality is excellent with rigorous experimental validation 
across multiple datasets. The contribution advances the state-of-the-art 
in [specific area] and will be of broad interest to the IEEE community. 
The originality is evident in [specific novel aspects].

I recommend acceptance with minor editorial corrections as noted in the 
detailed review.
```

**Minor Revision Example**:
```
RECOMMENDATION: Minor Revision

This paper makes a solid contribution to [area] with sound methodology 
and good experimental validation. However, several clarifications and 
minor additions would strengthen the paper before publication.

The technical approach is sound and the results are convincing. The 
significance is moderate but appropriate for [journal name]. The main 
concerns are presentation-related and can be addressed without new 
experiments.

Required changes:
1. Clarify the methodology in Section 3.2 as detailed in review
2. Add comparison to recent work [specific refs]
3. Improve figure quality and add missing details to captions
4. Expand discussion of limitations

These changes should be straightforward and do not require extensive 
revision. I expect to support acceptance after these minor revisions.
```

**Major Revision Example**:
```
RECOMMENDATION: Major Revision

This paper addresses an important problem and shows promise, but significant 
issues must be resolved before it can be accepted for publication.

The core technical approach appears sound, but the experimental validation 
is insufficient. The paper lacks comparison to key state-of-the-art methods 
and the evaluation is limited to toy datasets. Additionally, several 
methodological details are unclear and require clarification.

Required changes:
1. Add comprehensive comparison to methods X, Y, and Z
2. Evaluate on realistic, standard benchmark datasets
3. Provide complete methodological details (Sections 3.1-3.3)
4. Add ablation study analyzing key design choices
5. Substantially expand related work section

If these issues are adequately addressed, the paper has potential for 
publication. However, the revisions are substantial and will require 
re-review by the original reviewers.
```

**Reject Example**:
```
RECOMMENDATION: Reject

While this paper tackles an interesting problem, it has fundamental issues 
that cannot be adequately addressed through revision.

The primary concern is that the contribution is too incremental for [journal 
name]. The proposed method is essentially [prior work] with minor modifications, 
and the improvements shown are marginal and not statistically significant. 
Additionally, the experimental evaluation is limited and does not convincingly 
demonstrate advantages over existing approaches.

Specific issues:
1. Novelty over [prior work] is insufficient
2. Experimental improvements are marginal (2-3% with no significance testing)
3. Missing comparison to several key related methods
4. Theoretical analysis is incomplete and contains errors
5. Problem scope is too narrow for broad interest

I recommend the authors substantially extend this work before resubmission, 
either to this or another venue. Suggestions for strengthening future 
submission are provided in the detailed review.
```

## Review Assembly Workflow

### Step 1: Gather Assessments

Compile from prior components:
- [ ] Technical soundness evaluation
- [ ] Significance and originality assessment
- [ ] Clarity and presentation evaluation
- [ ] Ethics screening results
- [ ] Major concerns list
- [ ] Minor concerns list

### Step 2: Apply Decision Tree

Work through primary decision tree systematically:
1. Technical soundness acceptable? (If no → Reject)
2. Contribution sufficient? (If no → Reject)
3. Level of issues? (None → Accept, Minor → Minor Rev, Major → Major Rev or Reject)

### Step 3: Draft Recommendation

Write clear, justified recommendation with:
- Decision statement
- Supporting reasoning
- Specific required changes (if revision)
- Timeline expectations

### Step 4: Verify Consistency

Check that:
- [ ] Recommendation aligns with major concerns severity
- [ ] Required revisions match recommendation level
- [ ] Tone is professional and constructive
- [ ] Specific actionable guidance provided
- [ ] No contradictions between sections

## Common Mistakes to Avoid

**Don't**:
- Recommend Accept for papers with major flaws
- Recommend Reject for papers with fixable issues
- Use Minor Revision for major rewrites
- Provide vague or unhelpful justifications
- Make recommendation inconsistent with review body
- Demand unrealistic changes for revision

**Do**:
- Be honest about paper quality
- Provide clear, specific justification
- Calibrate to IEEE standards for target venue
- Give actionable guidance for revisions
- Be constructive even when recommending rejection
- Consider whether issues are truly fixable

## Integration with Review Template

This component produces the final sections:
- Overall Assessment paragraph
- Recommendation statement
- Justification paragraphs

Which complete the IEEE review format:
```
[Earlier sections: Summary, Major Concerns, Minor Concerns, Strengths, 
Questions, Suggestions]

OVERALL ASSESSMENT:
[From this component]

RECOMMENDATION:
[From this component]

[Detailed justification from this component]
```

## Special Considerations

### For Conference vs Journal
- Conferences: Slightly lower bar acceptable
- Journals: Higher standard for technical depth
- Transactions: Highest bar for novelty and rigor

### For Resubmissions
- Check if prior concerns adequately addressed
- Give credit for improvements made
- Don't demand perfection if prior issues resolved

### For Interdisciplinary Papers
- Consider value to both communities
- Don't penalize for targeting multiple audiences
- Evaluate appropriateness for specific IEEE venue

## Final Checklist

Before finalizing recommendation:
- [ ] Decision follows logically from review
- [ ] Justification is clear and specific
- [ ] Required changes are reasonable and actionable
- [ ] Tone is professional and constructive
- [ ] Timeline expectations communicated
- [ ] Recommendation serves authors and field

---

**Key Principle**: The recommendation should help both the editor make an informed decision AND help authors improve their work, whether for this venue or another.
