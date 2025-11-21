# Changelog

All notable changes to the Text-Metrics skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-05

### Added
- **GLTR Token Rank Analysis**:
  - `TokenRankAnalyzer` class for computing token probability distributions
  - Histogram binning: top-10, top-100, top-1000, rest
  - Mean and median rank statistics
  - Supports any HuggingFace causal language model
  - Grounded in Gehrmann et al. (2019) GLTR paper

- **DetectGPT Curvature Probes**:
  - `DetectGPTProbe` class for log-probability curvature analysis
  - Random text perturbation generation
  - Original vs. perturbed probability comparison
  - Configurable number of perturbations
  - Grounded in Mitchell et al. (2023) DetectGPT paper

- **Coh-Metrix Cohesion Metrics**:
  - `CohesionAnalyzer` class for discourse analysis
  - Connective density (additive, temporal, causal, adversative)
  - Lexical diversity (type-token ratio, hapax legomena)
  - Referential cohesion (pronoun rate, unique types)
  - Grounded in McNamara et al. (2014) Coh-Metrix framework

- **High-Level API Functions**:
  - `token_rank_hist()` - Convenience wrapper for GLTR analysis
  - `detectgpt_score()` - Convenience wrapper for curvature probes
  - `cohesion_bundle()` - Convenience wrapper for cohesion metrics
  - `full_analysis()` - Run all analyses in one call

- **Model Support**:
  - Default: GPT-2 (124M parameters)
  - Support for: gpt2-medium, gpt2-large, facebook/opt-*
  - Any HuggingFace causal LM compatible

- **Performance Features**:
  - GPU acceleration support (CUDA)
  - Model instance caching for batch processing
  - Efficient tokenization with HuggingFace transformers

- **Integration**:
  - Designed to compose with ai-check skill (Dimension 5)
  - Standalone utility for text analysis research
  - JSON-serializable outputs for easy integration

### Documentation
- Comprehensive SKILL.md with scientific foundation and API reference
- Detailed README.md with examples and troubleshooting
- Inline code documentation with type hints
- Usage examples for standalone and integrated modes

### Dependencies
- numpy >= 1.24.0 (numerical operations)
- torch >= 2.0.0 (model inference)
- transformers >= 4.30.0 (language models)

### Performance
- **Token Rank Analysis**:
  - CPU: 3-5 seconds per 500-token document
  - GPU: 0.5-1 second per 500-token document

- **DetectGPT Probe** (10 perturbations):
  - CPU: 5-10 seconds per 500-token document
  - GPU: 1-2 seconds per 500-token document

- **Cohesion Analysis**:
  - <0.1 seconds (no model inference)

### Scientific Grounding
- GLTR methodology from ACL 2019
- DetectGPT from ICML 2023
- Coh-Metrix principles from 2014 textbook
- All methods peer-reviewed and published

---

## Versioning Guidelines

- **Major (X.0.0)**: Breaking changes to API or output format
- **Minor (1.X.0)**: New features, additional metrics, model support
- **Patch (1.0.X)**: Bug fixes, performance optimizations, documentation

## Planned Features (Future Releases)

### 1.1.0 (Planned)
- [ ] Multilingual support (non-English models)
- [ ] Improved perturbation strategies (mask-filling with T5/BERT)
- [ ] Batch processing API for multiple documents
- [ ] Additional cohesion metrics (LSA overlap, argument overlap)
- [ ] Model ensemble for robust detection

### 1.2.0 (Planned)
- [ ] Perplexity-based metrics
- [ ] Burstiness analysis (Guo et al., 2023)
- [ ] Retrieval-based detection (DNA-GPT)
- [ ] Real-time streaming analysis
- [ ] Confidence intervals for all metrics

### 2.0.0 (Planned)
- [ ] Breaking: New output schema with hierarchical structure
- [ ] Support for instruction-tuned models (ChatGPT, Claude)
- [ ] Fine-tuned detection models (RoBERTa-based)
- [ ] Cross-model comparison (analyze with multiple LMs)
- [ ] Explainability features (saliency maps for token ranks)

## Known Issues

### 1.0.0
- Perturbations use simple word replacement; mask-filling models would be more robust
- Short texts (<100 tokens) may show unreliable DetectGPT curvature
- Model mismatch (analyze GPT-4 text with GPT-2) affects accuracy
- English-only; multilingual support requires language-specific models
- GPU memory usage can be high for large models (gpt2-large)

---

**Note**: This is the initial production release. Report issues at https://github.com/astoreyai/claude-skills/issues
