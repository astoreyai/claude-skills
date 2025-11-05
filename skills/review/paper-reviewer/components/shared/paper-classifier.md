# Paper Intake and Classification Component

## Purpose
Classify papers by type and characteristics to select appropriate evaluation pathways.

## Classification Schema

### Primary Paper Types

**1. Theoretical Paper**
- **Characteristics**: Proposes new theorems, proofs, mathematical frameworks, or theoretical analysis
- **Key indicators**: Mathematical notation, theorems/lemmas, proofs, formal analysis
- **Examples**: Convergence proofs, complexity bounds, theoretical guarantees, mathematical frameworks
- **Evaluation emphasis**: Assumption completeness, proof correctness, mathematical rigor

**2. Empirical Paper**
- **Characteristics**: Experimental validation, benchmarking, empirical studies
- **Key indicators**: Datasets, experiments, baselines, performance metrics, tables/figures of results
- **Examples**: New methods tested empirically, comparative studies, ablation studies
- **Evaluation emphasis**: Experimental design, statistical rigor, reproducibility, baseline comparisons

**3. Dataset/Benchmark Paper**
- **Characteristics**: Introduces new datasets or evaluation frameworks
- **Key indicators**: Data collection methodology, dataset statistics, license information, baseline results
- **Examples**: New image dataset, benchmark suite, evaluation protocol
- **Evaluation emphasis**: Documentation, ethics, licensing, use case demonstration, baseline quality

**4. Methods Paper**
- **Characteristics**: New algorithms, architectures, or techniques
- **Key indicators**: Algorithm description, architectural diagrams, novel components
- **Examples**: New neural architecture, optimization algorithm, training procedure
- **Evaluation emphasis**: Novelty, generalizability, comparison to prior methods, ablation studies

**5. Application Paper**
- **Characteristics**: Applying techniques to real-world problems or specific domains
- **Key indicators**: Domain-specific problem, practical deployment, real-world datasets
- **Examples**: Medical diagnosis system, robotics application, industry use case
- **Evaluation emphasis**: Practical impact, domain appropriateness, real-world evaluation, ethics

**6. Position Paper**
- **Characteristics**: Arguing for new perspectives, methodologies, or research directions
- **Key indicators**: Argumentative structure, critique of current approaches, vision for future
- **Examples**: Calls to action, critiques of paradigms, vision papers
- **Evaluation emphasis**: Argument clarity, evidence quality, impact on discourse

### Secondary Characteristics

Mark applicable characteristics:
- **Has theoretical component**: Contains proofs or formal analysis
- **Has empirical component**: Contains experiments or empirical validation
- **Introduces new resource**: Dataset, model, tool, or benchmark
- **Methodological contribution**: Novel technique or approach
- **Survey/analysis component**: Reviews or analyzes existing work
- **Interdisciplinary**: Spans multiple fields or domains

## Classification Protocol

### Step 1: Read Abstract and Introduction

Extract key information:
1. **Problem statement**: What problem does paper address?
2. **Proposed solution**: What is the approach?
3. **Main contribution type**: Theory? Empirical? Dataset? Method? Application?
4. **Evaluation type**: Proofs? Experiments? Case studies? Arguments?

### Step 2: Quick Scan of Methods and Results

Look for:
- **Theorems/proofs** → Theoretical component
- **Experimental setup** → Empirical component
- **Dataset description** → Dataset component
- **Algorithm/architecture** → Methods component
- **Domain application** → Application component
- **Critical analysis** → Position/survey component

### Step 3: Assign Primary Type

Decision tree:
```
Does paper contain theorems/proofs as MAIN contribution?
├─ Yes → Theoretical Paper
└─ No → Does paper introduce NEW dataset/benchmark as MAIN contribution?
    ├─ Yes → Dataset/Benchmark Paper
    └─ No → Does paper propose NEW method/algorithm/architecture?
        ├─ Yes → Methods Paper (if general) OR Application Paper (if domain-specific)
        └─ No → Does paper argue for perspective/direction?
            ├─ Yes → Position Paper
            └─ No → Empirical Paper (comparative/analysis study)
```

### Step 4: Note Secondary Characteristics

Check all that apply:
- [ ] Has theoretical component
- [ ] Has empirical validation
- [ ] Introduces dataset or benchmark
- [ ] Proposes new method or technique
- [ ] Domain-specific application
- [ ] Survey or comparative analysis
- [ ] Interdisciplinary work

### Step 5: Select Evaluation Pathway

Based on primary type, emphasize:

**Theoretical Papers**:
- Assumption completeness (critical)
- Proof correctness and rigor (critical)
- Novelty of theoretical results (critical)
- Clarity of mathematical exposition (important)
- Practical implications (secondary)

**Empirical Papers**:
- Experimental design quality (critical)
- Baseline selection and fairness (critical)
- Statistical significance (critical)
- Reproducibility (important)
- Insights from experiments (important)

**Dataset Papers**:
- Documentation completeness (critical)
- Ethical data practices (critical)
- Licensing clarity (critical)
- Use case demonstration (important)
- Baseline quality (important)

**Methods Papers**:
- Novelty and differentiation (critical)
- Generalizability (critical)
- Comparison to prior methods (critical)
- Ablation studies (important)
- Computational efficiency (secondary)

**Application Papers**:
- Real-world applicability (critical)
- Domain appropriateness (critical)
- Practical evaluation (critical)
- Ethical considerations (critical)
- Scalability (important)

**Position Papers**:
- Argument clarity and logic (critical)
- Evidence quality (critical)
- Novelty of perspective (important)
- Impact on field discourse (important)
- Actionability (secondary)

## Initial Red Flag Screening

### Format Violations

**Critical (potential desk reject)**:
- [ ] Exceeds 9 content pages significantly (>0.5 pages over)
- [ ] Missing NeurIPS checklist entirely
- [ ] Wrong template or style file
- [ ] Major anonymization failures

**Major (flag to AC)**:
- [ ] Exceeds 9 pages by small amount
- [ ] Checklist present but incomplete
- [ ] Minor anonymization issues

**Minor (mention in review)**:
- [ ] Small formatting inconsistencies
- [ ] Minor style issues
- [ ] Typos in checklist

### Anonymity Violations

**Check for**:
- [ ] Author names or affiliations in paper
- [ ] Self-citations that break anonymity ("In our previous work [X]...")
- [ ] URLs or links that reveal identity
- [ ] Acknowledgments section (should be removed for submission)
- [ ] Non-anonymized code/data repositories

**If found**: Document specifically and notify AC

### Ethical Red Flags

**Immediate concerns requiring ethics review**:
- [ ] Research aimed at increasing weapon lethality
- [ ] Tools explicitly designed for illegal activity
- [ ] Privacy violations (doxxing, surveillance without safeguards)
- [ ] Human subjects research without IRB mention
- [ ] Dataset of minors without safeguards
- [ ] Harmful content generation without mitigation

**If found**: Flag immediately for ethics review

### Integrity Concerns

**Check for**:
- [ ] Suspected plagiarism (similar text to known papers)
- [ ] Duplicate submission (same or very similar to other submissions)
- [ ] Data fabrication indicators (too-perfect results, implausible numbers)
- [ ] Missing critical citations (claiming prior work as own)

**If suspected**: Document concerns and notify AC

## Classification Output Template

```
PAPER CLASSIFICATION:

Primary Type: [Theoretical/Empirical/Dataset/Methods/Application/Position]

Secondary Characteristics:
- [List applicable characteristics]

Evaluation Pathway: [Type]-focused evaluation
Priority Assessment Areas:
1. [Highest priority area]
2. [Second priority area]
3. [Third priority area]

Initial Flags:
- Format: [None/List issues]
- Anonymity: [None/List violations]
- Ethics: [None/List concerns]
- Integrity: [None/List concerns]

Recommended Next Steps:
[If no flags]: Proceed with standard review using [Type] protocols
[If flags]: [Specify what needs AC attention or ethics review]

Special Considerations:
[Note any unusual characteristics or considerations for this paper]
```

## Examples

**Example 1: Theoretical Paper**
```
Abstract mentions: "We prove convergence guarantees for..."
Methods section: Contains theorems, lemmas, proofs
Results section: Theorem statements and proof sketches

Classification:
Primary Type: Theoretical Paper
Secondary: Has small empirical validation section
Pathway: Theory-focused (proofs, assumptions, rigor)
Flags: None
```

**Example 2: Methods Paper with Empirical Validation**
```
Abstract mentions: "We propose a new attention mechanism..."
Methods section: Algorithm description, architectural details
Results section: Extensive experiments on multiple benchmarks

Classification:
Primary Type: Methods Paper
Secondary: Strong empirical component
Pathway: Methods-focused but with thorough experimental evaluation
Flags: None
```

**Example 3: Dataset Paper**
```
Abstract mentions: "We introduce ImageNet-X, a new dataset..."
Methods section: Data collection, annotation, statistics
Results section: Baseline results, dataset analysis

Classification:
Primary Type: Dataset/Benchmark Paper
Secondary: Includes baseline experiments
Pathway: Dataset-focused (documentation, ethics, licensing)
Flags: Need to check licensing and ethics carefully
```

## Notes

- Some papers span multiple types; select PRIMARY type and note secondary characteristics
- Classification affects which evaluation protocols to emphasize
- Different types have different acceptance criteria
- Be flexible; unusual papers may not fit categories perfectly
- Document classification reasoning for AC and co-reviewers
