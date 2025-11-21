# Scoring Calibration Guide

## NeurIPS Score Distribution

**Target Distribution** (approximate):
- Score 6 (Strong Accept): ~0.5% 
- Score 5 (Accept): ~20-25%
- Score 4 (Borderline Accept): ~10%
- Score 3 (Borderline Reject): ~10%
- Score 2 (Reject): ~50-60%
- Score 1 (Strong Reject): ~5%

## Scoring Decision Tree

### Overall Score Determination

**Score 6 (Strong Accept)** - Exceptional, groundbreaking
- **Requirements**:
  - ALL dimension scores are 4
  - No critical weaknesses
  - Groundbreaking impact potential
  - Exceptional execution
  - No ethical concerns
- **Threshold**: Exceptionally rare (<1% of submissions)
- **Examples**: Paradigm-shifting methods, fundamental theoretical breakthroughs

**Score 5 (Accept)** - Clear contribution, well-executed
- **Requirements**:
  - Most dimensions score 3-4
  - No major weaknesses
  - Clear, significant contribution
  - Sound execution
  - High or moderate impact
- **Threshold**: Top ~20-25% of submissions
- **Examples**: Solid methods papers with good empirical work, good theoretical results

**Score 4 (Borderline Accept)** - Strengths outweigh weaknesses
- **Requirements**:
  - Mixed scores (2-4 range)
  - Strengths outweigh weaknesses
  - Contribution identifiable
  - Weaknesses addressable
- **Threshold**: Use sparingly (~10%)
- **Examples**: Good idea with limited evaluation, narrow but solid contribution

**Score 3 (Borderline Reject)** - Weaknesses outweigh strengths
- **Requirements**:
  - Mixed scores (1-3 range)
  - Weaknesses outweigh strengths
  - Contribution unclear or weak
  - Significant issues present
- **Threshold**: Use sparingly (~10%)
- **Examples**: Interesting idea with major flaws, incremental work with poor execution

**Score 2 (Reject)** - Below publication bar
- **Requirements**:
  - Most dimensions score 1-2
  - Major technical or contribution flaws
  - Insufficient novelty or rigor
  - Poor execution
- **Threshold**: ~50-60% of submissions
- **Examples**: Incremental work, flawed experiments, unclear contribution

**Score 1 (Strong Reject)** - Fundamental problems
- **Requirements**:
  - Fundamental flaws
  - Ethical violations
  - Plagiarism/duplication
  - Well-known results
  - Serious integrity issues
- **Threshold**: Reserved for severe cases (~5%)
- **Examples**: Copied work, fabricated data, dangerous applications

## Dimension Score Integration

**How dimension scores inform overall score**:

```
All 4s → Strong candidate for Score 6
Most 3-4s → Strong candidate for Score 5
Mixed 2-4s, more high → Score 4
Mixed 1-3s, more low → Score 3
Most 1-2s → Score 2
Critical flaws → Score 1
```

**Note**: A single weak dimension doesn't automatically lower overall score if other dimensions are exceptional. Consider the holistic contribution.

## Calibration Examples

### Example 1: Strong Accept (Score 5)
```
Quality: 4 (rigorous proofs, comprehensive experiments)
Clarity: 3 (clear but could be better organized)
Significance: 4 (addresses important problem with strong results)
Originality: 4 (novel theoretical insights)

Overall: 5 (Accept)
Justification: "This paper makes significant theoretical and empirical
contributions to [area]. The proofs are rigorous, experiments comprehensive,
and insights novel. Minor clarity issues don't detract from strong contribution."
```

### Example 2: Borderline Accept (Score 4)
```
Quality: 3 (sound but limited evaluation)
Clarity: 3 (generally clear)
Significance: 3 (moderate impact)
Originality: 2 (incremental novelty)

Overall: 4 (Borderline Accept)
Justification: "The paper presents solid work with adequate execution. The
contribution is moderate and novelty limited, but the problem is relevant and
execution sound. I lean toward acceptance given [specific strength]."
```

### Example 3: Reject (Score 2)
```
Quality: 2 (flawed experimental design)
Clarity: 2 (unclear exposition)
Significance: 2 (limited impact)
Originality: 2 (incremental)

Overall: 2 (Reject)
Justification: "While the paper addresses a relevant problem, the execution
has significant flaws including [specific issues]. The contribution is too
limited and presentation too unclear for acceptance."
```

## Calibration Guidelines

**Be Honest**: Don't inflate scores to be "nice"

**Be Fair**: Don't deflate scores due to minor issues

**Be Calibrated**: Compare to typical NeurIPS papers, not perfect ideal

**Be Consistent**: Scores should match textual assessment

**Be Specific**: Justify scores with concrete evidence

## Common Calibration Errors

**Error 1: Grade Inflation**
- Giving Score 5 to papers that are merely "good enough"
- Reality: Score 5 should be clearly above bar

**Error 2: Perfectionism**
- Rejecting papers for minor flaws
- Reality: Most accepted papers have some weaknesses

**Error 3: Overuse of Borderline**
- Using Score 4/3 for papers that are clearly accept/reject
- Reality: Borderline should be ~20% combined, not majority

**Error 4: Score-Text Mismatch**
- Text describes significant problems, score is 5
- Text praises paper highly, score is 3
- Reality: Scores must align with narrative

## Confidence Score Guidelines

**Score 5 (Absolutely Certain)**:
- Paper directly in expertise
- Checked math/proofs carefully
- Familiar with all related work
- No uncertainty

**Score 4 (Confident)**:
- Paper mostly in expertise
- Understood technical content
- May have missed some related work
- Small possibility of misunderstanding

**Score 3 (Fairly Confident)**:
- Paper partially outside expertise
- Understood main ideas not all details
- Some related work unfamiliar
- Possible gaps

**Score 2 (Willing to Defend)**:
- Paper significantly outside expertise
- Struggled with technical content
- Significant related work unfamiliar

**Score 1 (Educated Guess)**:
- Paper largely outside expertise
- Difficult to understand
- Should not have been assigned this

**Important**: Lower confidence doesn't excuse weak review. Still provide thorough assessment.
