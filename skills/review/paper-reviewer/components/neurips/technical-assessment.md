# Technical Assessment Component

## Purpose
Evaluate the technical soundness, rigor, and correctness of the submission across appropriate dimensions based on paper type.

## Assessment Protocols by Paper Type

### Protocol A: Theoretical Soundness Assessment

**When to use**: Papers with theoretical contributions (theorems, proofs, formal analysis)

**Checklist Cross-Reference**: Question #3 (Theory assumptions and proofs)

#### Step 1: Assumption Identification

**Extract all assumptions**:
- Read all theorems, lemmas, and propositions
- List explicitly stated assumptions
- Identify implicit assumptions
- Check for hidden assumptions in proofs

**Document assumptions**:
```
Stated Assumptions:
1. [Assumption 1 with reference to paper section]
2. [Assumption 2 with reference to paper section]

Implicit/Potentially Missing Assumptions:
1. [What seems assumed but not explicitly stated]
2. [Boundary conditions not discussed]
```

#### Step 2: Assumption Evaluation

**For each assumption, assess**:
- **Clarity**: Is it clearly stated in theorem statement?
- **Reasonableness**: Is it reasonable for the problem domain?
- **Strength**: Is it too strong (overly restrictive)?
- **Justification**: Is it justified or referenced?
- **Necessity**: Is it actually needed for the result?

**Common issues**:
- Assumptions buried in proof rather than in theorem statement
- Overly strong assumptions that limit applicability
- Unjustified assumptions (why should we believe this?)
- Contradictory assumptions
- Missing regularity conditions

#### Step 3: Proof Structure Verification

**Identify proof methodology**:
- Direct proof
- Proof by contradiction
- Proof by induction (check base case and inductive step)
- Proof by construction
- Probabilistic argument
- Other specialized technique

**Trace logical flow**:
1. Premises (assumptions + givens) → clearly identified?
2. Intermediate steps → each justified?
3. Conclusion → follows from premises?

**Check for referenced results**:
- Are cited lemmas/theorems properly referenced?
- Are they from established literature or proven earlier in paper?
- Are they applied correctly?

#### Step 4: Rigor Assessment

**Look for common proof gaps**:
- "It is easy to see that..." (without justification)
- "Clearly..." or "Obviously..." (hiding complexity)
- Missing cases in case analysis
- Undefined symbols or operations appearing suddenly
- Unjustified inequality steps
- Quantifier issues (switching order without justification)
- Measure-theoretic details glossed over
- Continuity or differentiability assumed without verification
- Limit operations without justification

**Assess mathematical communication**:
- Notation consistent and standard?
- All symbols defined before use?
- Equations numbered and referenced correctly?
- Proof structure clear (lemma → theorem flow)?

#### Step 5: Technical Depth Assessment

**Evaluate**:
- **Novelty of techniques**: New proof techniques or standard approaches?
- **Difficulty**: Straightforward or technically challenging?
- **Completeness**: All cases covered? Edge cases handled?
- **Generality**: Results specific or broadly applicable?

**Quality indicators**:
- *High quality*: Novel techniques, handles edge cases, generalizes well
- *Good quality*: Sound proofs, standard techniques competently applied
- *Adequate*: Correct but straightforward, limited novelty
- *Poor*: Gaps, errors, or trivial extensions of known results

### Scoring Guidance for Theoretical Papers:

**Quality Score 4 (Excellent)**:
- Complete, clearly stated assumptions
- Rigorous proofs with no significant gaps
- Novel or sophisticated techniques
- Handles edge cases and generalizes well
- Exceptionally clear exposition

**Quality Score 3 (Good)**:
- Assumptions mostly complete and clear
- Proofs sound with minor unclear steps
- Standard but competent techniques
- Adequate generality
- Clear enough exposition

**Quality Score 2 (Fair)**:
- Some missing or unclear assumptions
- Proof gaps requiring reader to fill in
- Limited technical novelty or rigor
- Narrow applicability
- Exposition could be clearer

**Quality Score 1 (Poor)**:
- Critical assumptions missing or contradictory
- Fundamental proof errors or major gaps
- Trivial or incorrect results
- Very narrow or unclear applicability
- Poor mathematical exposition

---

### Protocol B: Experimental Soundness Assessment

**When to use**: Papers with empirical contributions (experiments, benchmarks, empirical studies)

**Checklist Cross-References**: 
- Question #4 (Experimental result reproducibility)
- Question #5 (Open access to data and code)
- Question #6 (Experimental setting/details)
- Question #7 (Experiment statistical significance)
- Question #8 (Experiments compute resources)

#### Step 1: Experimental Design Assessment

**Evaluate research questions**:
- Are they clearly stated?
- Do they align with paper's claims?
- Are they answerable with proposed experiments?

**Assess experimental setup**:
```
Dataset Selection:
- [ ] Datasets appropriate for research questions
- [ ] Sufficient variety (or justified focus)
- [ ] Dataset sizes adequate
- [ ] Standard benchmarks used (if applicable)
- [ ] Justification for dataset choices

Baseline Selection:
- [ ] Appropriate baselines selected
- [ ] Recent work included (within 1-2 years)
- [ ] Fair comparison (same data, metrics)
- [ ] Seminal methods included
- [ ] Baselines implemented correctly

Evaluation Protocol:
- [ ] Train/val/test splits clearly defined
- [ ] No data leakage
- [ ] Cross-validation used (if appropriate)
- [ ] Metrics aligned with goals
- [ ] Multiple metrics for comprehensive evaluation
```

**Red flags**:
- Testing only on toy datasets for claimed real-world method
- Missing obvious recent baselines
- Metrics that don't match stated goals
- Comparing to weak or outdated baselines only
- Data leakage between train and test

#### Step 2: Statistical Rigor Assessment

**Error Bars and Variance**:
```
For each main result, check:
- [ ] Error bars reported?
- [ ] What do they represent?
  - Standard deviation
  - Standard error of the mean
  - Confidence interval (what level?)
- [ ] Source of variance?
  - Multiple random seeds (how many?)
  - Cross-validation folds
  - Different train/test splits
  - Ensemble variations
- [ ] Sample size adequate?
```

**Statistical Significance**:
- Are improvements tested for significance?
- Are appropriate statistical tests used?
  - t-tests (paired or unpaired?)
  - Wilcoxon signed-rank test
  - ANOVA for multiple comparisons
  - Bonferroni or similar corrections
- Are p-values reported and interpreted correctly?
- Are effect sizes reported (not just p-values)?

**Common statistical issues**:
- Single-run results for stochastic methods
- Reporting only mean without variance
- Cherry-picking best runs
- Multiple comparisons without correction
- HARKing (Hypothesizing After Results Known)
- P-hacking or fishing for significance
- Overfitting to validation/test set through iteration

#### Step 3: Reproducibility Assessment

**Algorithm/Method Details**:
```
Check for:
- [ ] Pseudocode or detailed algorithmic description
- [ ] All hyperparameters specified
- [ ] Hyperparameter selection method (grid search, random, manual, etc.)
- [ ] Optimization details
  - Learning rate and schedule
  - Batch size
  - Number of epochs/iterations
  - Stopping criteria
  - Optimizer (Adam, SGD, etc.)
- [ ] Initialization strategy
- [ ] Random seed policy
- [ ] Any other implementation details
```

**Data Details**:
```
Check for:
- [ ] Dataset sources cited with versions
- [ ] Data preprocessing described
  - Normalization
  - Augmentation
  - Filtering
  - Feature extraction
- [ ] Data splits specified
  - Split ratios
  - Random seeds for splitting
  - Or standard published splits
- [ ] Class balancing addressed (if applicable)
```

**Computational Details**:
```
Check for:
- [ ] Hardware specified (GPU model, CPU, memory)
- [ ] Software versions (framework, libraries)
- [ ] Training time per run
- [ ] Total compute budget
- [ ] Parallelization details
```

**Code and Data Availability**:
```
Code: [Provided/Promised upon acceptance/Not available]
├─ If provided: Anonymous? Complete? Runnable?
├─ If promised: Clear timeline? Licensing?
└─ If not available: Justified? (proprietary, etc.)

Data: [Provided/Public/Restricted/Not available]
├─ If provided: Complete? Documented?
├─ If public: Properly cited with access info?
├─ If restricted: Access procedure described?
└─ If not available: Justified? (privacy, IP, etc.)
```

#### Step 4: Results Interpretation Assessment

**Claims vs. Evidence**:
For each main claim:
1. What evidence is presented?
2. Does evidence actually support the claim?
3. Are there alternative explanations not considered?
4. Are limitations acknowledged?
5. Are negative results or failures reported?

**Common overstatement patterns**:
- "State-of-the-art" without comprehensive comparison
- "Significant improvement" without statistical testing
- Generalizing from limited experiments
- Confusing correlation with causation
- Ignoring negative results or failure modes
- Overclaiming from in-distribution evaluation
- Extrapolating beyond experimental scope

**Ablation Studies**:
- Are ablation studies included?
- Do they isolate contribution of each component?
- Are they comprehensive enough?
- Do results make sense?

### Scoring Guidance for Empirical Papers:

**Quality Score 4 (Excellent)**:
- Excellent experimental design (appropriate datasets, strong baselines)
- Rigorous statistical evaluation with error bars and significance tests
- Comprehensive ablation studies
- Highly reproducible (complete details, code/data available)
- Claims well-supported by evidence
- Addresses negative results honestly

**Quality Score 3 (Good)**:
- Good experimental design with reasonable baselines
- Adequate statistical rigor (error bars, multiple runs)
- Some ablation studies
- Reproducible with sufficient details
- Claims generally supported
- Acknowledges limitations

**Quality Score 2 (Fair)**:
- Limited experimental evaluation
- Weak statistical rigor (few runs, no error bars)
- Missing important baselines or ablations
- Insufficient reproducibility details
- Some overclaiming or unsupported statements
- Limited scope

**Quality Score 1 (Poor)**:
- Fundamentally flawed experimental design
- No statistical rigor (single runs, cherry-picked results)
- Missing critical baselines
- Not reproducible (too many missing details)
- Serious overclaiming
- Misleading presentation of results

---

### Protocol C: Dataset Quality Assessment

**When to use**: Papers introducing new datasets or benchmarks

**Focus areas**: Documentation, ethics, licensing, utility

#### Step 1: Documentation Completeness

**Dataset Description**:
```
Check for:
- [ ] Clear description of what data contains
- [ ] Data source(s) identified and cited
- [ ] Collection methodology explained
- [ ] Data statistics provided
  - Total size
  - Number of examples
  - Features/attributes
  - Class distribution
  - Train/val/test splits
- [ ] File formats specified
- [ ] Data schema/structure documented
- [ ] Known issues or limitations discussed
```

**Data Quality**:
- How was quality controlled?
- Annotation process described?
- Inter-annotator agreement reported?
- Noise characterization?
- Outliers handled how?

#### Step 2: Ethical Data Practices

**Privacy and Consent**:
- Is PII removed or anonymized?
- Was consent obtained (if identifiable individuals)?
- Are privacy protocols described?
- GDPR/regional law compliance addressed?

**Bias and Representation**:
- Demographics discussed?
- Known biases acknowledged?
- Representative of target population?
- Fairness implications considered?

**Sensitive Content**:
- Does dataset contain sensitive information?
- Are safeguards in place?
- Is access controlled appropriately?

#### Step 3: Licensing and Attribution

**Check for**:
- [ ] Clear license for new dataset
- [ ] Source data licenses respected
- [ ] Attribution provided for derived data
- [ ] Terms of use specified
- [ ] Commercial use addressed
- [ ] Redistribution rights clear

#### Step 4: Use Case Demonstration

**Baseline Experiments**:
- Are baseline results provided?
- Multiple methods tested?
- Appropriate metrics used?
- Results demonstrate dataset utility?

**Dataset Utility**:
- Clear use cases identified?
- Advantages over existing datasets explained?
- Gap in research addressed?
- Sufficient difficulty/challenge?

### Scoring Guidance for Dataset Papers:

**Quality Score 4 (Excellent)**:
- Comprehensive documentation
- Exemplary ethical practices
- Clear licensing
- Strong baseline experiments
- Significant contribution to field

**Quality Score 3 (Good)**:
- Good documentation
- Adequate ethical consideration
- Licensing clear
- Reasonable baselines
- Useful contribution

**Quality Score 2 (Fair)**:
- Incomplete documentation
- Ethical concerns not fully addressed
- Licensing unclear
- Weak baselines
- Limited utility

**Quality Score 1 (Poor)**:
- Poor documentation
- Serious ethical problems
- No clear license
- No or inadequate baselines
- Marginal utility or serious issues

---

## Documentation Template

```
TECHNICAL ASSESSMENT:

Paper Type: [Theoretical/Empirical/Dataset/Other]

Protocol Used: [A/B/C]

Assessment Summary:
[Brief overall technical assessment]

Detailed Findings:

[For Theoretical Papers]:
Assumptions: [Complete/Incomplete/Unclear]
- [List any issues with assumptions]

Proof Rigor: [Rigorous/Minor gaps/Significant gaps/Flawed]
- [List specific proof issues if any]

Notation: [Clear/Adequate/Confusing]
- [Note any notation issues]

Technical Novelty: [High/Moderate/Low]

[For Empirical Papers]:
Experimental Design: [Excellent/Good/Fair/Poor]
- [Key strengths/weaknesses]

Statistical Rigor: [Excellent/Good/Fair/Poor]
- Error bars: [Appropriate/Inadequate/Missing]
- Significance testing: [Appropriate/Inadequate/Missing]

Reproducibility: [High/Moderate/Low]
- Information completeness: [Complete/Adequate/Insufficient]
- Code/data availability: [Available/Promised/Not available]

Results Interpretation: [Sound/Mostly sound/Overstated/Misleading]

[For Dataset Papers]:
Documentation: [Comprehensive/Good/Adequate/Poor]
Ethics: [Exemplary/Adequate/Concerns]
Licensing: [Clear/Adequate/Unclear]
Utility: [High/Moderate/Low]

Quality Score: [1-4]
Justification: [Explanation of score]

Specific Strengths:
1. [Strength 1]
2. [Strength 2]

Specific Weaknesses:
1. [Weakness 1]
2. [Weakness 2]

Questions for Authors:
1. [Technical question 1]
2. [Technical question 2]
```
