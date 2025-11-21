# Text-Metrics: Probability-Based Text Analysis

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-production-green)
![License](https://img.shields.io/badge/license-MIT-blue)

Advanced statistical and model-based text analysis for AI detection. Provides GLTR token rank histograms, DetectGPT curvature probes, and Coh-Metrix-inspired cohesion metrics.

## Features

- **GLTR Token Rank Analysis**: Histogram of token probabilities (top-10, top-100, top-1000 bins)
- **DetectGPT Curvature Probes**: Log-probability curvature through text perturbations
- **Cohesion Metrics**: Discourse connectives, lexical diversity, referential cohesion
- **Composable Design**: Integrates seamlessly with ai-check skill
- **Model Agnostic**: Works with any HuggingFace causal language model
- **GPU Accelerated**: Optional CUDA support for 5-10x speedup

## Quick Start

### Installation

```bash
cd skills/utility/text-metrics/scripts
pip install -r requirements.txt
```

First run will download the model (~500MB for gpt2).

### Basic Usage

```python
from scripts.text_metrics import full_analysis

text = """
Your text here. Should be at least 100 tokens for
reliable DetectGPT results. Token rank analysis
works with shorter texts (50+ tokens).
"""

results = full_analysis(text)

# Check token rank concentration
print(f"Top-10%: {results['token_ranks']['top10_pct']:.1f}%")
print(f"Top-100%: {results['token_ranks']['top100_pct']:.1f}%")

# Check curvature
curvature = results['curvature']['curvature']
if curvature > 0.5:
    print("High probability of AI generation")

# Check lexical diversity
ttr = results['cohesion']['lexical_diversity']['type_token_ratio']
print(f"Type-Token Ratio: {ttr:.2f}")
```

### Individual Functions

```python
from scripts.text_metrics import token_rank_hist, detectgpt_score, cohesion_bundle

# Token rank histogram only
ranks = token_rank_hist(text, model_name="gpt2")

# DetectGPT only
curvature = detectgpt_score(text, model_name="gpt2", num_perturbations=20)

# Cohesion only (no model needed, fast)
cohesion = cohesion_bundle(text)
```

## API Reference

### `token_rank_hist(text, model_name="gpt2")`

Compute GLTR-style token rank histogram.

**Parameters**:
- `text` (str): Text to analyze (recommended: 50+ tokens)
- `model_name` (str): HuggingFace model ID (default: "gpt2")

**Returns**:
```python
{
    'top10_pct': float,      # % tokens in top-10 ranks
    'top100_pct': float,     # % tokens in top-100 ranks
    'top1000_pct': float,    # % tokens in top-1000 ranks
    'rest_pct': float,       # % tokens beyond top-1000
    'mean_rank': float,      # Mean token rank
    'median_rank': float     # Median token rank
}
```

**Interpretation**:
- **AI-generated**: top10_pct > 40%, top100_pct > 85%
- **Human-written**: top10_pct ~ 20-30%, top100_pct ~ 70-80%

---

### `detectgpt_score(text, model_name="gpt2", num_perturbations=10)`

Compute DetectGPT curvature criterion.

**Parameters**:
- `text` (str): Text to analyze (recommended: 100+ tokens)
- `model_name` (str): HuggingFace model ID (default: "gpt2")
- `num_perturbations` (int): Number of random perturbations (default: 10)

**Returns**:
```python
{
    'original_logprob': float,          # Log-prob of original text
    'mean_perturbed_logprob': float,    # Mean log-prob of perturbations
    'curvature': float                  # Difference (positive = likely AI)
}
```

**Interpretation**:
- **curvature > 0.5**: Likely AI-generated
- **curvature ~ 0**: Ambiguous
- **curvature < -0.5**: Likely human-written

---

### `cohesion_bundle(text)`

Compute Coh-Metrix-inspired cohesion metrics.

**Parameters**:
- `text` (str): Text to analyze

**Returns**:
```python
{
    'connectives': {
        'additive_rate': float,      # Per 1,000 tokens
        'temporal_rate': float,
        'causal_rate': float,
        'adversative_rate': float,
        'total_rate': float
    },
    'lexical_diversity': {
        'type_token_ratio': float,   # Unique/total words
        'unique_lemmas': int,
        'hapax_legomena': int        # Words appearing once
    },
    'referential_cohesion': {
        'pronoun_rate': float,       # Per 1,000 tokens
        'unique_pronoun_types': int
    }
}
```

**Interpretation**:
- **High connective_rate** (>50/1000): May indicate formulaic transitions
- **Low type_token_ratio** (<0.5): Low lexical diversity
- **High pronoun_rate** (>60/1000): High referential cohesion

---

### `full_analysis(text, model_name="gpt2", num_perturbations=10)`

Run all analyses in one call.

**Returns**: Combined dictionary with `token_ranks`, `curvature`, and `cohesion` keys.

## Model Selection

| Model | Size | Speed (CPU) | Accuracy | Recommendation |
|-------|------|-------------|----------|----------------|
| gpt2 | 124M | Fast (3-5s) | Good | **Default** - balanced |
| gpt2-medium | 355M | Medium (8-12s) | Better | Higher accuracy needed |
| gpt2-large | 774M | Slow (20-30s) | Best | GPU + research use |
| facebook/opt-125m | 125M | Fast | Good | Alternative to gpt2 |

Times for 500-token documents on CPU.

## Integration with AI-Check

Text-metrics is designed to provide Dimension 5 (Probability-Based) features for ai-check:

```python
# ai-check invokes text-metrics
token_data = invoke_skill("text-metrics", "token_rank_hist", text)
curvature_data = invoke_skill("text-metrics", "detectgpt_score", text)
cohesion_data = invoke_skill("text-metrics", "cohesion_bundle", text)

# ai-check uses results for probability dimension scoring
if token_data['top10_pct'] > 40 and curvature_data['curvature'] > 0.5:
    probability_score = 0.85  # High AI likelihood
```

## Performance Optimization

### GPU Acceleration

Install PyTorch with CUDA support for 5-10x speedup:

```bash
# Check CUDA version
nvidia-smi

# Install PyTorch with CUDA (example for CUDA 11.8)
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

**Performance comparison (500 tokens, gpt2)**:
- CPU: ~5 seconds
- GPU: ~0.8 seconds

### Caching

For repeated analysis of the same documents:

```python
# Cache model instances
rank_analyzer = TokenRankAnalyzer(model_name="gpt2")
detectgpt_probe = DetectGPTProbe(model_name="gpt2")

# Reuse for multiple texts
for text in documents:
    ranks = rank_analyzer.token_rank_histogram(text)
    curvature = detectgpt_probe.curvature_score(text)
```

### Batch Processing

Process multiple documents efficiently:

```python
from scripts.text_metrics import TokenRankAnalyzer

analyzer = TokenRankAnalyzer("gpt2")

results = []
for doc in documents:
    result = analyzer.token_rank_histogram(doc)
    results.append(result)
```

## Examples

### Example 1: Quick AI Detection

```python
from scripts.text_metrics import token_rank_hist, detectgpt_score

text = "Your text here..."

# Fast check: token ranks only
ranks = token_rank_hist(text)
if ranks['top10_pct'] > 45:
    print("⚠️ High AI likelihood (token concentration)")

# Thorough check: add curvature
curvature = detectgpt_score(text, num_perturbations=20)
if curvature['curvature'] > 0.5:
    print("⚠️ High AI likelihood (curvature anomaly)")
```

### Example 2: Comparative Analysis

```python
human_text = "..."  # Known human sample
ai_text = "..."     # Suspected AI sample

human_result = full_analysis(human_text)
ai_result = full_analysis(ai_text)

print("Token Rank Top-10%:")
print(f"  Human: {human_result['token_ranks']['top10_pct']:.1f}%")
print(f"  AI: {ai_result['token_ranks']['top10_pct']:.1f}%")

print("Curvature:")
print(f"  Human: {human_result['curvature']['curvature']:.2f}")
print(f"  AI: {ai_result['curvature']['curvature']:.2f}")
```

### Example 3: Cohesion Analysis Only

```python
from scripts.text_metrics import cohesion_bundle

text = "..."
cohesion = cohesion_bundle(text)

# Check discourse structure
conn_rate = cohesion['connectives']['total_rate']
if conn_rate > 50:
    print("⚠️ High connective density (formulaic)")

# Check lexical diversity
ttr = cohesion['lexical_diversity']['type_token_ratio']
if ttr < 0.45:
    print("⚠️ Low lexical diversity (repetitive)")
```

## Troubleshooting

### Issue: Out of Memory
**Symptoms**: `RuntimeError: CUDA out of memory` or system freezes
**Solutions**:
1. Use smaller model: `model_name="gpt2"` (not gpt2-large)
2. Reduce perturbations: `num_perturbations=5`
3. Process shorter texts (<1000 tokens)
4. Close other GPU applications

---

### Issue: Slow Inference
**Symptoms**: Each analysis takes >10 seconds
**Solutions**:
1. Install GPU-enabled PyTorch (see Performance Optimization)
2. Use smaller model (gpt2 vs gpt2-medium)
3. Cache model instances (see examples above)
4. Reduce `num_perturbations` to 5-10

---

### Issue: Model Download Fails
**Symptoms**: `ConnectionError` during first run
**Solutions**:
1. Check internet connection
2. Set HuggingFace cache: `export HF_HOME=/path/to/cache`
3. Manually download: `huggingface-cli download gpt2`
4. Use offline mode with pre-downloaded models

---

### Issue: Different Results from GLTR Demo
**Symptoms**: Token ranks don't match GLTR web interface
**Solutions**:
1. GLTR uses GPT-2 117M; ensure `model_name="gpt2"`
2. Tokenization differences may cause slight variations
3. Results should be within ~5% for same model

## Limitations

1. **Model Mismatch**: Detection accuracy depends on similarity between evaluation model and generation model. GPT-4 text analyzed with GPT-2 may show artifacts.

2. **Short Texts**: DetectGPT requires 100+ tokens for reliability. Token ranks work with 50+ tokens.

3. **Post-Editing**: Heavily edited AI text flattens probability curvature, reducing detection accuracy.

4. **Computational Cost**: Model inference is expensive. Single analysis: ~5s CPU, ~1s GPU.

5. **Language**: Currently English-only. Multilingual models needed for other languages.

6. **Perturbation Quality**: Uses simple word replacement. Production systems should use mask-filling models.

## Dependencies

### Core
- Python 3.9+
- numpy >= 1.24.0
- torch >= 2.0.0
- transformers >= 4.30.0

### Optional
- CUDA-enabled PyTorch (GPU acceleration)
- spacy >= 3.5.0 (enhanced NLP)
- nltk >= 3.8.0 (alternative tokenization)

## Scientific References

1. **GLTR**: Gehrmann, S., et al. (2019). "GLTR: Statistical Detection and Visualization of Generated Text." *ACL 2019*.
   - Original paper: https://arxiv.org/abs/1906.04043
   - Demo: http://gltr.io/

2. **DetectGPT**: Mitchell, E., et al. (2023). "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature." *ICML 2023*.
   - Paper: https://arxiv.org/abs/2301.11305

3. **Coh-Metrix**: McNamara, D. S., et al. (2014). "Automated Evaluation of Text and Discourse with Coh-Metrix." *Cambridge University Press*.

## Contributing

Enhancements welcome:
- Additional language models
- Improved perturbation strategies
- Multilingual support
- Batch processing optimizations

## License

MIT License - see LICENSE file

## Support

- Issues: https://github.com/astoreyai/claude-skills/issues
- Documentation: See SKILL.md for complete API
- Examples: See `examples/usage_example.md`

---

**Version**: 1.0.0 | **Status**: Production Ready | **Maintained by**: Claude Skills Library
