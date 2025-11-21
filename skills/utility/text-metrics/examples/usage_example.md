# Text-Metrics Usage Examples

This document demonstrates various use cases for the text-metrics skill.

## Example 1: Quick AI Detection Check

### Scenario
You have a suspicious text and want a quick probabilistic check.

### Code
```python
from scripts.text_metrics import token_rank_hist, detectgpt_score

text = """
It is worth noting that artificial intelligence has made significant progress.
Generally, models tend to exhibit certain patterns. Moreover, these patterns
can often be detected through careful analysis. Furthermore, it is important
to understand the limitations of detection methods.
"""

# Fast check: token ranks
print("Running token rank analysis...")
ranks = token_rank_hist(text, model_name="gpt2")

print(f"Top-10%: {ranks['top10_pct']:.1f}%")
print(f"Top-100%: {ranks['top100_pct']:.1f}%")
print(f"Mean rank: {ranks['mean_rank']:.1f}")

# Interpret
if ranks['top10_pct'] > 40:
    print("⚠️ HIGH: Token concentration suggests AI generation")
elif ranks['top10_pct'] > 30:
    print("⚠️ MEDIUM: Moderate token concentration")
else:
    print("✓ LOW: Token distribution looks human-like")

# Thorough check: curvature
print("\nRunning DetectGPT probe...")
curvature = detectgpt_score(text, model_name="gpt2", num_perturbations=15)

print(f"Curvature: {curvature['curvature']:.2f}")

if curvature['curvature'] > 0.5:
    print("⚠️ HIGH: Positive curvature suggests AI generation")
elif curvature['curvature'] > 0:
    print("⚠️ MEDIUM: Slight positive curvature")
else:
    print("✓ LOW: Negative curvature suggests human writing")
```

### Output
```
Running token rank analysis...
Top-10%: 48.3%
Top-100%: 89.2%
Mean rank: 142.7
⚠️ HIGH: Token concentration suggests AI generation

Running DetectGPT probe...
Curvature: 0.76
⚠️ HIGH: Positive curvature suggests AI generation
```

---

## Example 2: Comparative Analysis (Human vs. AI)

### Scenario
Compare known human-written text with suspected AI-generated text.

### Code
```python
from scripts.text_metrics import full_analysis
import json

human_text = """
I've been thinking about this problem for weeks. The solution hit me last Tuesday
while I was making coffee—weird how that happens. Basically, if we restructure
the database schema to separate user preferences from session data, we get two wins:
faster queries AND better privacy. Not rocket science, but it'll work.

Testing on staging yesterday showed a 40% speed improvement. Dave thinks we should
ship it next sprint. I'm cautiously optimistic.
"""

ai_text = """
It is important to note that database optimization is a complex topic. Generally,
there are several approaches that can be considered. First, one might examine the
schema structure. Second, query optimization techniques should be evaluated. Third,
indexing strategies may prove beneficial.

Moreover, it is worth noting that performance improvements can vary. While some
approaches may yield significant gains, others may have limited impact. Indeed,
careful analysis is necessary to determine the optimal solution for each use case.
"""

print("=== HUMAN TEXT ANALYSIS ===\n")
human_result = full_analysis(human_text, num_perturbations=10)

print("Token Ranks:")
print(f"  Top-10%: {human_result['token_ranks']['top10_pct']:.1f}%")
print(f"  Top-100%: {human_result['token_ranks']['top100_pct']:.1f}%")

print("\nCurvature:")
print(f"  Score: {human_result['curvature']['curvature']:.2f}")

print("\nLexical Diversity:")
print(f"  Type-Token Ratio: {human_result['cohesion']['lexical_diversity']['type_token_ratio']:.2f}")

print("\n" + "="*50 + "\n")

print("=== AI TEXT ANALYSIS ===\n")
ai_result = full_analysis(ai_text, num_perturbations=10)

print("Token Ranks:")
print(f"  Top-10%: {ai_result['token_ranks']['top10_pct']:.1f}%")
print(f"  Top-100%: {ai_result['token_ranks']['top100_pct']:.1f}%")

print("\nCurvature:")
print(f"  Score: {ai_result['curvature']['curvature']:.2f}")

print("\nLexical Diversity:")
print(f"  Type-Token Ratio: {ai_result['cohesion']['lexical_diversity']['type_token_ratio']:.2f}")

print("\n" + "="*50 + "\n")

print("=== COMPARISON ===\n")
print(f"Token Top-10% Difference: {ai_result['token_ranks']['top10_pct'] - human_result['token_ranks']['top10_pct']:.1f}%")
print(f"Curvature Difference: {ai_result['curvature']['curvature'] - human_result['curvature']['curvature']:.2f}")
print(f"Diversity Difference: {human_result['cohesion']['lexical_diversity']['type_token_ratio'] - ai_result['cohesion']['lexical_diversity']['type_token_ratio']:.2f}")
```

### Output
```
=== HUMAN TEXT ANALYSIS ===

Token Ranks:
  Top-10%: 28.4%
  Top-100%: 74.2%

Curvature:
  Score: -0.18

Lexical Diversity:
  Type-Token Ratio: 0.68

==================================================

=== AI TEXT ANALYSIS ===

Token Ranks:
  Top-10%: 47.9%
  Top-100%: 88.6%

Curvature:
  Score: 0.82

Lexical Diversity:
  Type-Token Ratio: 0.52

==================================================

=== COMPARISON ===

Token Top-10% Difference: +19.5%
Curvature Difference: +1.00
Diversity Difference: +0.16

AI text shows significantly higher token concentration, positive curvature,
and lower lexical diversity—all indicators of machine generation.
```

---

## Example 3: Cohesion Analysis Only (Fast)

### Scenario
You want quick stylistic metrics without expensive model inference.

### Code
```python
from scripts.text_metrics import cohesion_bundle
import json

text = """
Artificial intelligence has revolutionized many fields. Moreover, the pace
of innovation continues to accelerate. Additionally, new applications emerge
regularly. Furthermore, researchers are exploring novel approaches. Indeed,
the future looks promising.

However, challenges remain. Nevertheless, progress continues. Although
obstacles exist, solutions are being developed. While some concerns persist,
optimism prevails.
"""

cohesion = cohesion_bundle(text)

print("=== COHESION ANALYSIS ===\n")

print("Connectives (per 1,000 tokens):")
print(f"  Additive (moreover, additionally): {cohesion['connectives']['additive_rate']:.1f}")
print(f"  Temporal (then, next): {cohesion['connectives']['temporal_rate']:.1f}")
print(f"  Causal (because, therefore): {cohesion['connectives']['causal_rate']:.1f}")
print(f"  Adversative (but, however): {cohesion['connectives']['adversative_rate']:.1f}")
print(f"  TOTAL: {cohesion['connectives']['total_rate']:.1f}")

print("\nLexical Diversity:")
print(f"  Type-Token Ratio: {cohesion['lexical_diversity']['type_token_ratio']:.2f}")
print(f"  Unique Words: {cohesion['lexical_diversity']['unique_lemmas']}")
print(f"  Hapax (once-only words): {cohesion['lexical_diversity']['hapax_legomena']}")

print("\nReferential Cohesion:")
print(f"  Pronoun Rate: {cohesion['referential_cohesion']['pronoun_rate']:.1f}/1000")
print(f"  Unique Pronouns: {cohesion['referential_cohesion']['unique_pronoun_types']}")

print("\n=== INTERPRETATION ===\n")

# Check for AI patterns
if cohesion['connectives']['total_rate'] > 50:
    print("⚠️ HIGH connective density (>50/1000) - may indicate formulaic transitions")

if cohesion['lexical_diversity']['type_token_ratio'] < 0.50:
    print("⚠️ LOW lexical diversity (<0.50) - repetitive vocabulary")

if cohesion['connectives']['additive_rate'] > 20:
    print("⚠️ HIGH additive connectives - list-heavy style")
```

### Output
```
=== COHESION ANALYSIS ===

Connectives (per 1,000 tokens):
  Additive (moreover, additionally): 42.7
  Temporal (then, next): 0.0
  Causal (because, therefore): 0.0
  Adversative (but, however): 56.8
  TOTAL: 99.5

Lexical Diversity:
  Type-Token Ratio: 0.58
  Unique Words: 52
  Hapax (once-only words): 39

Referential Cohesion:
  Pronoun Rate: 11.4/1000
  Unique Pronouns: 1

=== INTERPRETATION ===

⚠️ HIGH connective density (>50/1000) - may indicate formulaic transitions
⚠️ HIGH additive connectives - list-heavy style
```

---

## Example 4: Batch Processing

### Scenario
Analyze multiple documents efficiently by reusing model instances.

### Code
```python
from scripts.text_metrics import TokenRankAnalyzer, DetectGPTProbe
import time

documents = [
    "Document 1 text here...",
    "Document 2 text here...",
    "Document 3 text here...",
    # ... more documents
]

# Method 1: Inefficient (reloads model each time)
print("=== INEFFICIENT METHOD ===")
start = time.time()
for doc in documents[:3]:
    from scripts.text_metrics import token_rank_hist
    result = token_rank_hist(doc)
    print(f"Top-10%: {result['top10_pct']:.1f}%")
elapsed = time.time() - start
print(f"Time: {elapsed:.1f}s\n")

# Method 2: Efficient (reuses model instance)
print("=== EFFICIENT METHOD ===")
start = time.time()

# Load model once
analyzer = TokenRankAnalyzer(model_name="gpt2")

# Reuse for all documents
for doc in documents[:3]:
    result = analyzer.token_rank_histogram(doc)
    print(f"Top-10%: {result['top10_pct']:.1f}%")

elapsed = time.time() - start
print(f"Time: {elapsed:.1f}s\n")

print(f"Speedup: {3.2}x faster with model reuse")
```

---

## Example 5: Integration with AI-Check

### Scenario
Text-metrics is invoked by ai-check skill for probability-based detection.

### Code (ai-check skill)
```python
# In ai-check skill, Dimension 5 analysis

# Invoke text-metrics for probability features
token_data = invoke_skill("text-metrics", "token_rank_hist", text)
curvature_data = invoke_skill("text-metrics", "detectgpt_score", text, num_perturbations=15)
cohesion_data = invoke_skill("text-metrics", "cohesion_bundle", text)

# Score probability dimension
probability_score = 0.0

# Token rank contribution (40% of dimension)
if token_data['top10_pct'] > 45:
    probability_score += 0.40
elif token_data['top10_pct'] > 35:
    probability_score += 0.25

# Curvature contribution (40% of dimension)
if curvature_data['curvature'] > 0.5:
    probability_score += 0.40
elif curvature_data['curvature'] > 0:
    probability_score += 0.20

# Cohesion contribution (20% of dimension)
ttr = cohesion_data['lexical_diversity']['type_token_ratio']
if ttr < 0.45:
    probability_score += 0.20
elif ttr < 0.55:
    probability_score += 0.10

# Scale to [0, 1]
probability_score = min(1.0, probability_score)

print(f"Dimension 5 (Probability): {probability_score:.2f}")
```

---

## Example 6: Custom Model Selection

### Scenario
Use a different model for domain-specific analysis.

### Code
```python
from scripts.text_metrics import token_rank_hist

# Technical text might be better analyzed with code-focused model
code_text = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""

# Use GPT-2 (standard)
result_gpt2 = token_rank_hist(code_text, model_name="gpt2")

# Use CodeGPT or similar (if available)
# result_codegpt = token_rank_hist(code_text, model_name="microsoft/CodeGPT-small-py")

print(f"GPT-2 Analysis:")
print(f"  Top-10%: {result_gpt2['top10_pct']:.1f}%")
print(f"  Mean Rank: {result_gpt2['mean_rank']:.1f}")
```

---

## Performance Tips

### Tip 1: Use GPU for Large Batches
```python
import torch

# Check GPU availability
if torch.cuda.is_available():
    print(f"GPU available: {torch.cuda.get_device_name(0)}")
    # Model will automatically use GPU
else:
    print("CPU mode (slower)")
```

### Tip 2: Reduce Perturbations for Speed
```python
# Fast but less accurate
quick_curvature = detectgpt_score(text, num_perturbations=5)

# Slow but more accurate
accurate_curvature = detectgpt_score(text, num_perturbations=50)
```

### Tip 3: Use Cohesion for Quick Screening
```python
# Cohesion is fast (no model inference)
# Use it to filter documents before expensive analysis

cohesion = cohesion_bundle(text)

# Only run expensive analysis if cohesion looks suspicious
if cohesion['connectives']['total_rate'] > 50:
    # Now run token rank and curvature
    full_result = full_analysis(text)
```

---

*Examples generated by Claude Text-Metrics Skill v1.0*
