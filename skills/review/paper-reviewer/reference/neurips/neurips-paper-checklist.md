# NeurIPS Paper Checklist (16 Questions)

## Purpose
Encourage best practices for reproducibility, transparency, ethics, and societal impact.

## Instructions
- Answer Yes/No/NA for each question
- NA = Not Applicable or Not Available
- Provide brief justification for each answer
- Answering "No" is acceptable with proper justification
- Checklist is visible to reviewers and will be published with paper

## The 16 Questions

### Q1: Claims
Do main claims in abstract/introduction accurately reflect paper's contributions and scope?
- Claims should match results
- Contributions clearly stated with assumptions/limitations
- Aspirational goals ok if clearly marked as not attained

### Q2: Limitations
Does paper discuss limitations of the work?
- Encouraged to have separate "Limitations" section
- Discuss assumptions and robustness
- Reflect on scope and factors affecting performance
- Reviewers instructed not to penalize honesty

### Q3: Theory Assumptions and Proofs
For theoretical results, are full assumptions stated and complete proofs provided?
- All assumptions clearly stated or referenced
- Proofs in paper or supplement (with sketch if in supplement)
- Theorems/lemmas properly referenced

### Q4: Experimental Result Reproducibility
Does paper fully disclose information needed to reproduce main results?
- Algorithm clearly described or architecture fully specified
- Model access provided if applicable
- Reproducibility required regardless of code/data release

### Q5: Open Access to Data and Code
Are code, data, and instructions to reproduce results included?
- Preferred but "No" acceptable (e.g., proprietary)
- Submit anonymized versions
- Include exact commands and environment
- Papers not rejected solely for not releasing code

### Q6: Experimental Setting/Details
Are all training details specified (data splits, hyperparameters, etc.)?
- Important details in main paper
- Full details can be in code/appendix
- Explain hyperparameter selection

### Q7: Experiment Statistical Significance
Are error bars or statistical significance information reported?
- Required for experiments supporting main claims
- Specify what error bars represent
- Explain calculation method
- State assumptions

### Q8: Experiments Compute Resources
Is sufficient compute resource information provided?
- Type of workers (CPU/GPU/cloud)
- Memory and storage
- Time per run and total compute
- Disclose if more compute used than reported

### Q9: Code of Ethics
Does research conform to NeurIPS Code of Ethics?
- Must review and confirm conformance
- Explain special circumstances if any

### Q10: Broader Impacts
Does paper discuss potential positive and negative societal impacts?
- Examples: malicious use, fairness, privacy, security
- Many papers are foundational; not all need discussion
- Discuss if direct path to negative applications
- Consider mitigation strategies

### Q11: Safeguards
Are safeguards described for high-risk models/data?
- Required for models/data with misuse potential
- Describe access controls, usage guidelines
- Address scraped internet data safety

### Q12: Licenses for Existing Assets
Are creators cited and licenses respected for existing code/data/models?
- Cite original papers
- State license names
- Check and respect terms
- Include URLs if possible

### Q13: New Assets Documentation
Are new assets (datasets/code/models) documented?
- Communicate details via structured templates
- Include license and terms of use
- Discuss consent if applicable
- Anonymize for submission

### Q14: Crowdsourcing and Human Subjects
Are full instructions and compensation details provided?
- Full text of instructions (can be in supplement)
- Must pay at least minimum wage in region
- Screenshots if applicable

### Q15: IRB Approvals
Are potential risks described and IRB approval obtained?
- Required for human subjects research
- Clearly state approval
- Don't break anonymity in submission
- Follow institution's procedures

### Q16: LLM Usage Declaration
Is LLM usage described if important/original/non-standard component?
- Describe if LLM is core to methodology
- Not required for writing/editing/formatting
- Using LLM for grammar doesn't need declaration

## Reviewer Use

Reviewers should:
- Use checklist as evaluation factor
- Not penalize honest "No" answers with justification
- Flag inconsistencies between checklist and paper
- Consider completeness and honesty as positive signals
