#!/usr/bin/env python3
"""
Text Metrics: Probability-based text analysis for AI detection.

Provides advanced statistical and model-based metrics:
- Token rank histograms (GLTR-style)
- DetectGPT curvature probes
- Cohesion metrics (Coh-Metrix-inspired)

Designed to compose with ai-check skill for comprehensive AI writing pattern detection.

References:
- GLTR: Gehrmann et al. (2019) "Statistical Detection and Visualization of Generated Text"
- DetectGPT: Mitchell et al. (2023) "Zero-Shot Machine-Generated Text Detection"
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class TokenRankAnalyzer:
    """
    GLTR-style token rank histogram analysis.

    Computes the distribution of token ranks from a language model's predictions.
    LLM-generated text tends to concentrate in top-ranked tokens.
    """

    def __init__(self, model_name: str = "gpt2"):
        """
        Initialize with a language model.

        Args:
            model_name: HuggingFace model identifier (default: gpt2)
        """
        print(f"Loading model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()

        # Set pad token if not exists
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def compute_token_ranks(self, text: str) -> List[int]:
        """
        Compute rank of each token given preceding context.

        Args:
            text: Input text to analyze

        Returns:
            List of ranks (1-indexed, where 1 = most probable token)
        """
        # Tokenize
        tokens = self.tokenizer.encode(text, return_tensors="pt")

        if tokens.shape[1] < 2:
            return []

        ranks = []

        with torch.no_grad():
            for i in range(1, tokens.shape[1]):
                # Context is everything before position i
                context = tokens[:, :i]

                # Get model predictions
                outputs = self.model(context)
                logits = outputs.logits[0, -1, :]  # Last position predictions

                # Get rank of actual next token
                actual_token = tokens[0, i].item()

                # Sort by probability (descending)
                sorted_indices = torch.argsort(logits, descending=True)

                # Find rank of actual token (1-indexed)
                rank = (sorted_indices == actual_token).nonzero(as_tuple=True)[0].item() + 1
                ranks.append(rank)

        return ranks

    def token_rank_histogram(self, text: str) -> Dict[str, float]:
        """
        Compute GLTR-style histogram: percentage in top-10, top-100, top-1000, rest.

        Args:
            text: Input text

        Returns:
            {
                'top10_pct': float,
                'top100_pct': float,
                'top1000_pct': float,
                'rest_pct': float,
                'mean_rank': float,
                'median_rank': float
            }
        """
        ranks = self.compute_token_ranks(text)

        if not ranks:
            return {
                'top10_pct': 0.0,
                'top100_pct': 0.0,
                'top1000_pct': 0.0,
                'rest_pct': 0.0,
                'mean_rank': 0.0,
                'median_rank': 0.0
            }

        total = len(ranks)
        top10 = sum(1 for r in ranks if r <= 10)
        top100 = sum(1 for r in ranks if r <= 100)
        top1000 = sum(1 for r in ranks if r <= 1000)
        rest = total - top1000

        return {
            'top10_pct': (top10 / total) * 100,
            'top100_pct': (top100 / total) * 100,
            'top1000_pct': (top1000 / total) * 100,
            'rest_pct': (rest / total) * 100,
            'mean_rank': np.mean(ranks),
            'median_rank': np.median(ranks)
        }


class DetectGPTProbe:
    """
    DetectGPT curvature-based detection.

    Measures log-probability curvature by perturbing text and comparing
    probabilities. Generated text occupies regions with distinctive curvature.
    """

    def __init__(self, model_name: str = "gpt2"):
        """
        Initialize with a language model.

        Args:
            model_name: HuggingFace model identifier
        """
        print(f"Loading model for DetectGPT: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()

        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def compute_log_probability(self, text: str) -> float:
        """
        Compute average log-probability of text.

        Args:
            text: Input text

        Returns:
            Mean log-probability per token
        """
        tokens = self.tokenizer.encode(text, return_tensors="pt")

        if tokens.shape[1] < 2:
            return 0.0

        with torch.no_grad():
            outputs = self.model(tokens, labels=tokens)
            loss = outputs.loss.item()

        # Loss is negative log-likelihood, so return negative
        return -loss

    def perturb_text(self, text: str, num_perturbations: int = 10) -> List[str]:
        """
        Generate perturbations by randomly replacing tokens.

        Args:
            text: Original text
            num_perturbations: Number of perturbed versions

        Returns:
            List of perturbed texts
        """
        words = text.split()
        perturbations = []

        if len(words) < 3:
            return [text] * num_perturbations

        for _ in range(num_perturbations):
            perturbed = words.copy()

            # Replace 10-20% of words randomly
            num_replacements = max(1, int(len(words) * np.random.uniform(0.1, 0.2)))

            for _ in range(num_replacements):
                idx = np.random.randint(0, len(perturbed))
                # Simple replacement: sample from vocabulary
                # (In production, use mask-filling with another model)
                perturbed[idx] = "[MASK]"

            perturbations.append(" ".join(perturbed))

        return perturbations

    def curvature_score(
        self,
        text: str,
        num_perturbations: int = 10
    ) -> Dict[str, float]:
        """
        Compute DetectGPT curvature criterion.

        Args:
            text: Original text
            num_perturbations: Number of perturbations for estimation

        Returns:
            {
                'original_logprob': float,
                'mean_perturbed_logprob': float,
                'curvature': float  (positive = likely generated)
            }
        """
        original_logprob = self.compute_log_probability(text)

        perturbations = self.perturb_text(text, num_perturbations)
        perturbed_logprobs = [
            self.compute_log_probability(p) for p in perturbations
        ]

        mean_perturbed = np.mean(perturbed_logprobs)

        # Curvature: original log-prob vs mean perturbed log-prob
        # Positive curvature suggests generated text (sits at local maximum)
        curvature = original_logprob - mean_perturbed

        return {
            'original_logprob': original_logprob,
            'mean_perturbed_logprob': mean_perturbed,
            'curvature': curvature
        }


class CohesionAnalyzer:
    """
    Coh-Metrix-inspired cohesion metrics.

    Analyzes discourse connectives, referential cohesion, and lexical diversity.
    """

    # Common discourse connectives
    ADDITIVE = ["also", "and", "furthermore", "moreover", "additionally", "besides"]
    TEMPORAL = ["then", "next", "subsequently", "finally", "meanwhile", "afterwards"]
    CAUSAL = ["because", "since", "therefore", "thus", "consequently", "hence"]
    ADVERSATIVE = ["but", "however", "although", "yet", "nevertheless", "despite"]

    def __init__(self):
        self.all_connectives = (
            self.ADDITIVE + self.TEMPORAL + self.CAUSAL + self.ADVERSATIVE
        )

    def count_connectives(self, text: str) -> Dict[str, float]:
        """
        Count discourse connectives per 1,000 tokens.

        Returns:
            {
                'additive_rate': float,
                'temporal_rate': float,
                'causal_rate': float,
                'adversative_rate': float,
                'total_rate': float
            }
        """
        tokens = text.lower().split()
        n_tokens = len(tokens)

        if n_tokens == 0:
            return {
                'additive_rate': 0.0,
                'temporal_rate': 0.0,
                'causal_rate': 0.0,
                'adversative_rate': 0.0,
                'total_rate': 0.0
            }

        additive_count = sum(1 for t in tokens if t.strip('.,;:!?') in self.ADDITIVE)
        temporal_count = sum(1 for t in tokens if t.strip('.,;:!?') in self.TEMPORAL)
        causal_count = sum(1 for t in tokens if t.strip('.,;:!?') in self.CAUSAL)
        adversative_count = sum(1 for t in tokens if t.strip('.,;:!?') in self.ADVERSATIVE)
        total_count = additive_count + temporal_count + causal_count + adversative_count

        return {
            'additive_rate': (additive_count / n_tokens) * 1000,
            'temporal_rate': (temporal_count / n_tokens) * 1000,
            'causal_rate': (causal_count / n_tokens) * 1000,
            'adversative_rate': (adversative_count / n_tokens) * 1000,
            'total_rate': (total_count / n_tokens) * 1000
        }

    def lexical_diversity(self, text: str) -> Dict[str, float]:
        """
        Compute lexical diversity metrics.

        Returns:
            {
                'type_token_ratio': float,
                'unique_lemmas': int,
                'hapax_legomena': int  (words appearing once)
            }
        """
        tokens = re.findall(r'\b\w+\b', text.lower())

        if not tokens:
            return {
                'type_token_ratio': 0.0,
                'unique_lemmas': 0,
                'hapax_legomena': 0
            }

        unique = set(tokens)
        freq = {}
        for token in tokens:
            freq[token] = freq.get(token, 0) + 1

        hapax = sum(1 for count in freq.values() if count == 1)

        return {
            'type_token_ratio': len(unique) / len(tokens),
            'unique_lemmas': len(unique),
            'hapax_legomena': hapax
        }

    def referential_cohesion(self, text: str) -> Dict[str, float]:
        """
        Compute referential cohesion (pronoun and noun phrase overlap).

        Returns:
            {
                'pronoun_rate': float (per 1,000 tokens),
                'unique_pronoun_types': int
            }
        """
        PRONOUNS = {
            'i', 'me', 'my', 'mine', 'myself',
            'you', 'your', 'yours', 'yourself',
            'he', 'him', 'his', 'himself',
            'she', 'her', 'hers', 'herself',
            'it', 'its', 'itself',
            'we', 'us', 'our', 'ours', 'ourselves',
            'they', 'them', 'their', 'theirs', 'themselves',
            'this', 'that', 'these', 'those'
        }

        tokens = text.lower().split()

        if not tokens:
            return {
                'pronoun_rate': 0.0,
                'unique_pronoun_types': 0
            }

        pronouns_found = [t.strip('.,;:!?') for t in tokens if t.strip('.,;:!?') in PRONOUNS]

        return {
            'pronoun_rate': (len(pronouns_found) / len(tokens)) * 1000,
            'unique_pronoun_types': len(set(pronouns_found))
        }

    def cohesion_bundle(self, text: str) -> Dict:
        """
        Compute all cohesion metrics.

        Returns:
            Combined dictionary of all metrics
        """
        connectives = self.count_connectives(text)
        diversity = self.lexical_diversity(text)
        referential = self.referential_cohesion(text)

        return {
            'connectives': connectives,
            'lexical_diversity': diversity,
            'referential_cohesion': referential
        }


# High-level API functions
def token_rank_hist(
    text: str,
    model_name: str = "gpt2"
) -> Dict:
    """
    Convenience function for GLTR-style token rank analysis.

    Args:
        text: Input text
        model_name: Model to use

    Returns:
        Token rank histogram dict
    """
    analyzer = TokenRankAnalyzer(model_name)
    return analyzer.token_rank_histogram(text)


def detectgpt_score(
    text: str,
    model_name: str = "gpt2",
    num_perturbations: int = 10
) -> Dict:
    """
    Convenience function for DetectGPT curvature analysis.

    Args:
        text: Input text
        model_name: Model to use
        num_perturbations: Number of perturbations

    Returns:
        Curvature score dict
    """
    probe = DetectGPTProbe(model_name)
    return probe.curvature_score(text, num_perturbations)


def cohesion_bundle(text: str) -> Dict:
    """
    Convenience function for cohesion metrics.

    Args:
        text: Input text

    Returns:
        Cohesion metrics dict
    """
    analyzer = CohesionAnalyzer()
    return analyzer.cohesion_bundle(text)


def full_analysis(
    text: str,
    model_name: str = "gpt2",
    num_perturbations: int = 10
) -> Dict:
    """
    Run all analyses on text.

    Args:
        text: Input text
        model_name: Model to use for probability metrics
        num_perturbations: Number of perturbations for DetectGPT

    Returns:
        Combined results dictionary
    """
    print("Running token rank analysis...")
    token_ranks = token_rank_hist(text, model_name)

    print("Running DetectGPT probe...")
    curvature = detectgpt_score(text, model_name, num_perturbations)

    print("Running cohesion analysis...")
    cohesion = cohesion_bundle(text)

    return {
        'token_ranks': token_ranks,
        'curvature': curvature,
        'cohesion': cohesion
    }


if __name__ == "__main__":
    # Example usage
    sample_text = """
    It is worth noting that artificial intelligence has made significant progress.
    Generally, models tend to exhibit certain patterns. Moreover, these patterns
    can often be detected through careful analysis.
    """

    print("=== Text Metrics Analysis ===\n")
    results = full_analysis(sample_text, model_name="gpt2", num_perturbations=5)
    print(json.dumps(results, indent=2, default=str))
