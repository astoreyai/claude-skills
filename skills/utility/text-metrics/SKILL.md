---
name: text-metrics
description: Probability-based text analysis providing GLTR token rank histograms, DetectGPT curvature probes, and Coh-Metrix-inspired cohesion metrics. Designed to compose with ai-check for comprehensive AI writing pattern detection.
---

# Text-Metrics: Probability-Based Text Analysis

## Overview

A utility skill providing advanced statistical and model-based text analysis for AI detection. Implements three core capabilities grounded in peer-reviewed research:

1. **Token Rank Histograms** (GLTR-style): Analyzes token probability distributions
2. **DetectGPT Curvature Probes**: Measures log-probability curvature through perturbations
3. **Cohesion Metrics** (Coh-Metrix-inspired): Evaluates discourse connectives, lexical diversity, and referential cohesion

## Primary Use Case

This skill is designed to **compose with the ai-check skill** to provide Dimension 5 (Probability-Based) detection features. It can also be used standalone for text analysis research.

## Auto-Invoke Conditions

This skill is typically invoked **by other skills** (particularly ai-check) rather than directly by users. It may be invoked when:
- AI-check requests probability-based metrics
- User explicitly requests "token rank analysis" or "GLTR"
- User mentions "DetectGPT" or "curvature probe"
- User asks for "lexical diversity" or "cohesion metrics"

## Scientific Foundation

### 1. GLTR Token Rank Histograms

**Reference**: Gehrmann, S., Strobelt, H., & Rush, A. M. (2019). "GLTR: Statistical Detection and Visualization of Generated Text." ACL 2019.

**Principle**: LLM-generated text tends to select higher-probability tokens (lower ranks) more consistently than human writing, which exhibits more variability and surprisal.

**Method**:
1. For each token in text, compute its rank given preceding context using a language model
2. Bin tokens into: top-10, top-100, top-1000, rest
3. LLM text shows higher concentration in top bins

**Typical Patterns**:
- **AI-generated**: Top-10 > 40%, Top-100 > 85%
- **Human-written**: Top-10 ~ 20-30%, Top-100 ~ 70-80%

### 2. DetectGPT Curvature Probes

**Reference**: Mitchell, E., et al. (2023). "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature." ICML 2023.

**Principle**: Generated text sits at local maxima in the model's probability distribution, while human text does not. Random perturbations of generated text tend to have lower probability.

**Method**:
1. Compute log-probability of original text: `log P(x)`
2. Generate random perturbations: `x'₁, x'₂, ..., x'ₙ`
3. Compute mean perturbed log-probability: `mean(log P(x'ᵢ))`
4. Curvature = `log P(x) - mean(log P(x'ᵢ))`
5. Positive curvature suggests generation

**Interpretation**:
- **Curvature > 0.5**: Likely generated
- **Curvature ~ 0**: Ambiguous
- **Curvature < -0.5**: Likely human

### 3. Coh-Metrix Cohesion Metrics

**Reference**: McNamara, D. S., et al. (2014). "Automated Evaluation of Text and Discourse with Coh-Metrix." Cambridge University Press.

**Principle**: Discourse cohesion patterns (connectives, referential overlap, lexical diversity) differ between human and AI writing.

**Metrics**:
- **Connective Density**: Additive, temporal, causal, adversative connectives per 1,000 tokens
- **Lexical Diversity**: Type-token ratio, unique lemmas, hapax legomena
- **Referential Cohesion**: Pronoun rate, unique pronoun types

## Functions

### 1. `token_rank_hist(text, model_name="gpt2")`

Compute GLTR-style token rank histogram.

**Input**:
- `text`: String to analyze
- `model_name`: HuggingFace model identifier (default: "gpt2")

**Output**:
```json
{
  "top10_pct": 45.2,
  "top100_pct": 87.3,
  "top1000_pct": 96.1,
  "rest_pct": 3.9,
  "mean_rank": 182.4,
  "median_rank": 34.0
}
```

**Usage**:
```python
from scripts.text_metrics import token_rank_hist

result = token_rank_hist("Your text here", model_name="gpt2")
print(f"Top-10 concentration: {result['top10_pct']:.1f}%")
```

### 2. `detectgpt_score(text, model_name="gpt2", num_perturbations=10)`

Compute DetectGPT curvature criterion.

**Input**:
- `text`: String to analyze
- `model_name`: HuggingFace model (default: "gpt2")
- `num_perturbations`: Number of random perturbations (default: 10)

**Output**:
```json
{
  "original_logprob": -2.34,
  "mean_perturbed_logprob": -3.12,
  "curvature": 0.78
}
```

**Usage**:
```python
from scripts.text_metrics import detectgpt_score

result = detectgpt_score("Your text here", num_perturbations=20)
if result['curvature'] > 0.5:
    print("Likely AI-generated")
```

### 3. `cohesion_bundle(text)`

Compute Coh-Metrix-inspired cohesion metrics.

**Input**:
- `text`: String to analyze

**Output**:
```json
{
  "connectives": {
    "additive_rate": 12.5,
    "temporal_rate": 8.3,
    "causal_rate": 6.2,
    "adversative_rate": 9.1,
    "total_rate": 36.1
  },
  "lexical_diversity": {
    "type_token_ratio": 0.62,
    "unique_lemmas": 142,
    "hapax_legomena": 78
  },
  "referential_cohesion": {
    "pronoun_rate": 45.2,
    "unique_pronoun_types": 12
  }
}
```

**Usage**:
```python
from scripts.text_metrics import cohesion_bundle

result = cohesion_bundle("Your text here")
diversity = result['lexical_diversity']['type_token_ratio']
print(f"Lexical diversity: {diversity:.2f}")
```

### 4. `full_analysis(text, model_name="gpt2", num_perturbations=10)`

Run all three analyses in one call.

**Output**: Combined dictionary with all metrics.

## Integration with AI-Check

When ai-check skill invokes text-metrics:

```python
# ai-check calls text-metrics for Dimension 5
token_data = invoke_skill("text-metrics", "token_rank_hist", text)
curvature = invoke_skill("text-metrics", "detectgpt_score", text)
cohesion = invoke_skill("text-metrics", "cohesion_bundle", text)

# Use results in probability dimension scoring
if token_data['top10_pct'] > 40:
    flag_high_probability_concentration()

if curvature['curvature'] > 0.5:
    flag_curvature_anomaly()
```

## Model Selection

### Supported Models (HuggingFace)
- **gpt2** (default): Fast, lightweight, good baseline
- **gpt2-medium**: Better accuracy, slower
- **gpt2-large**: Best accuracy, requires GPU
- **facebook/opt-125m**: Alternative small model
- **facebook/opt-1.3b**: Alternative medium model

**Recommendation**: Use `gpt2` for speed, `gpt2-medium` for accuracy.

### GPU Acceleration

Text-metrics benefits significantly from GPU:
- **CPU**: ~2-5 seconds per 500-token document
- **GPU**: ~0.3-0.8 seconds per 500-token document

Install PyTorch with CUDA support for GPU acceleration.

## Performance Characteristics

| Function | Time (CPU) | Time (GPU) | Memory |
|----------|-----------|-----------|---------|
| `token_rank_hist` | 3-5s | 0.5-1s | ~1GB |
| `detectgpt_score` | 5-10s | 1-2s | ~1GB |
| `cohesion_bundle` | <0.1s | <0.1s | <100MB |
| `full_analysis` | 8-15s | 1.5-3s | ~1GB |

Times for ~500 token documents, gpt2 model.

## Limitations

1. **Model Dependency**: Results depend on choice of language model. Mismatch between evaluation model and generation model affects accuracy.

2. **Short Text**: DetectGPT requires ~100+ tokens for reliable results. Token rank histograms need ~50+ tokens.

3. **Computational Cost**: Model inference is expensive. Cache results when possible.

4. **Perturbation Quality**: Simple word replacement perturbations used here. Production systems should use mask-filling with dedicated models.

5. **Language**: Currently English-only. Multilingual models needed for other languages.

6. **Post-Editing**: Heavily edited AI text may evade detection as curvature flattens.

## Example Usage

### Standalone Analysis
```python
from scripts.text_metrics import full_analysis

text = """
Your sample text here. Should be at least 100 tokens
for reliable DetectGPT results.
"""

results = full_analysis(text, model_name="gpt2", num_perturbations=20)

print("Token Rank Histogram:")
print(f"  Top-10: {results['token_ranks']['top10_pct']:.1f}%")
print(f"  Top-100: {results['token_ranks']['top100_pct']:.1f}%")

print("\nDetectGPT Curvature:")
print(f"  Curvature: {results['curvature']['curvature']:.2f}")

print("\nCohesion Metrics:")
print(f"  Type-Token Ratio: {results['cohesion']['lexical_diversity']['type_token_ratio']:.2f}")
print(f"  Connective Rate: {results['cohesion']['connectives']['total_rate']:.1f}/1000")
```

### Integration with AI-Check
```python
# In ai-check skill, invoke text-metrics for probability dimension
token_metrics = invoke_text_metrics("token_rank_hist", test_text)
curvature_metrics = invoke_text_metrics("detectgpt_score", test_text)
cohesion_metrics = invoke_text_metrics("cohesion_bundle", test_text)

# Score probability dimension
probability_score = compute_probability_dimension(
    token_metrics,
    curvature_metrics,
    cohesion_metrics
)
```

## Files & Resources

- **Implementation**: `scripts/text_metrics.py`
- **Dependencies**: `scripts/requirements.txt`
- **Examples**: `examples/usage_example.md`

## Installation

```bash
cd skills/utility/text-metrics/scripts
pip install -r requirements.txt

# First run will download model (~500MB for gpt2)
python text_metrics.py
```

## Troubleshooting

### Issue: "Model download failed"
**Solution**: Ensure internet connection. Model cached in `~/.cache/huggingface/`.

### Issue: "Out of memory"
**Solution**: Use smaller model (gpt2 instead of gpt2-large) or reduce num_perturbations.

### Issue: "Slow inference"
**Solution**: Install PyTorch with CUDA for GPU acceleration, or use CPU-optimized build.

### Issue: "Results differ from GLTR web demo"
**Solution**: Different models produce different ranks. Ensure same model as reference.

## References

1. Gehrmann, S., Strobelt, H., & Rush, A. M. (2019). "GLTR: Statistical Detection and Visualization of Generated Text." *Proceedings of ACL 2019*.

2. Mitchell, E., Lee, Y., Khazatsky, A., Manning, C. D., & Finn, C. (2023). "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature." *Proceedings of ICML 2023*.

3. McNamara, D. S., Graesser, A. C., McCarthy, P. M., & Cai, Z. (2014). "Automated Evaluation of Text and Discourse with Coh-Metrix." *Cambridge University Press*.

---

**Version**: 1.0.0
**License**: MIT
**Maintained by**: Claude Skills Library
