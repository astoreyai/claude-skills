# LaTeX-Check: Comprehensive LaTeX/TikZ/Beamer Auditor

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Status](https://img.shields.io/badge/status-production-green)
![License](https://img.shields.io/badge/license-MIT-blue)

A best-in-class Claude skill for auditing LaTeX documents, TikZ graphics, pgfplots visualizations, and Beamer presentations. Provides standards-backed analysis grounded in official CTAN documentation.

## Features

- **Comprehensive Auditing**: 60+ rules across 11 categories
  - Document structure & encoding
  - Package configuration & loading order
  - Cross-references & hyperlinks
  - Bibliography setup (biblatex + biber)
  - TikZ/PGF graphics & externalization
  - pgfplots data visualization
  - Beamer presentations (aspect ratio, overlays, contrast)
  - Typography & microtype
  - Accessibility (WCAG 2.1 AA compliance)
  - Code quality & linting
  - Compilation workflow

- **Standards-Grounded**: All recommendations reference official manuals
  - LaTeX Project documentation
  - CTAN package manuals (hyperref, cleveref, biblatex, microtype, etc.)
  - TikZ & PGF manual (tikz.dev)
  - pgfplots manual
  - Beamer user guide
  - WCAG 2.1 accessibility guidelines

- **Actionable Outputs**:
  - Detailed audit report with evidence and references
  - Prioritized fix plan with step-by-step instructions
  - Minimal working examples (MWEs) demonstrating best practices
  - Lint configurations (ChkTeX, latexindent)
  - JSON output conforming to schema

- **Specialized Support**:
  - TikZ externalization setup for faster compilation
  - Beamer overlay density analysis
  - WCAG contrast checking for presentations
  - Modern bibliography migration (BibTeX → biblatex)
  - Package loading order validation

## Quick Start

### Installation

```bash
git clone https://github.com/astoreyai/claude-skills.git
cd claude-skills/skills/review/latex-check
```

### Basic Usage

```
User: "Check my LaTeX document for issues: paper.tex"

Claude will:
1. Analyze document structure and packages
2. Validate cross-references and bibliography setup
3. Check TikZ/Beamer usage (if applicable)
4. Generate comprehensive audit report
5. Provide prioritized fix plan
6. Include relevant MWEs
```

### Example Output

```
Generated files:
- tex_audit_report.md       # Human-readable findings
- tex_fix_plan.md           # Step-by-step fixes
- tex_audit_findings.json   # Structured data
- mwes/                     # Minimal working examples
- lint/                     # Configuration files
```

## Use Cases

### 1. Article/Report Review

**Scenario**: Academic paper with complex cross-references and bibliography

**What it checks**:
- ✅ Package loading order (hyperref, cleveref, microtype)
- ✅ Bibliography setup (biblatex + biber)
- ✅ Cross-reference system (label prefixes, cleveref usage)
- ✅ Typography (microtype, font encoding)
- ✅ Compilation workflow (latexmk)

**MWE provided**: `best_practices_article.tex`

---

### 2. Beamer Presentation Review

**Scenario**: Conference presentation slides

**What it checks**:
- ✅ Aspect ratio (recommends 16:9 for modern displays)
- ✅ Overlay density (flags frames with >5 overlays)
- ✅ Contrast compliance (WCAG 2.1 AA: ≥4.5:1)
- ✅ Theme consistency
- ✅ Frame content balance

**MWE provided**: `beamer_16_9_overlays.tex`

---

### 3. TikZ-Heavy Document Optimization

**Scenario**: Document with 20+ TikZ figures, slow compilation

**What it does**:
- ✅ Counts TikZ figures and estimates compile cost
- ✅ Recommends externalization for faster recompilation
- ✅ Generates externalization setup guide
- ✅ Explains shell-escape security considerations
- ✅ Provides Makefile integration

**MWE provided**: `tikz_externalization.tex`

**Expected improvement**: 10-50x faster recompilation

---

### 4. Bibliography Modernization

**Scenario**: Legacy document using BibTeX

**What it does**:
- ✅ Detects legacy `\bibliography{}` and `\bibliographystyle{}`
- ✅ Recommends migration to biblatex + biber
- ✅ Provides step-by-step migration guide
- ✅ Explains benefits (UTF-8, flexible formatting, better sorting)
- ✅ Shows complete modern setup

**MWE provided**: `modern_bibliography.tex`

## Configuration Files

### ChkTeX Linting

**Generated**: `lint/.chktexrc`

ChkTeX performs semantic LaTeX checking beyond syntax errors:
- Command spacing
- Reference spacing (`~` before `\ref`)
- Dash usage (-, --, ---)
- Quotation marks (`` vs ")
- Math mode punctuation

**Usage**:
```bash
chktex -v0 -l document.tex
```

**Inline suppression**:
```latex
% Suppress warning 24 for this file
% chktex-file 24

% Suppress warning 2 for one line
See Figure~\ref{fig:example}  % chktex 2
```

---

### latexindent Formatting

**Generated**: `lint/indentconfig.yaml`

Consistent code formatting with customizable rules:
- 4-space indentation (configurable)
- Environment-specific indentation
- Beamer and TikZ awareness
- Alignment within tabular/align
- Trailing whitespace removal

**Usage**:
```bash
# Format in place (creates backup)
latexindent -l=indentconfig.yaml -w document.tex

# Write to new file
latexindent -l=indentconfig.yaml -o formatted.tex document.tex
```

## Minimal Working Examples

### 1. TikZ Externalization (`mwes/tikz_externalization.tex`)

**Demonstrates**:
- External library setup
- Cache directory configuration
- Explicit figure naming
- Shell-escape compilation
- Makefile integration

**Compile**:
```bash
latexmk -pdf -shell-escape tikz_externalization.tex
```

**Result**: Figures cached in `tikz-cache/`, 10x+ faster recompilation

---

### 2. Beamer 16:9 with Overlays (`mwes/beamer_16_9_overlays.tex`)

**Demonstrates**:
- Aspect ratio configuration (16:9)
- Overlay specifications (`<n->`, `\pause`, `\onslide`)
- Best practices (≤5 overlays per frame)
- Contrast considerations (WCAG AA)
- Theme selection

**Compile**:
```bash
latexmk -pdf beamer_16_9_overlays.tex
```

---

### 3. Modern Bibliography (`mwes/modern_bibliography.tex`)

**Demonstrates**:
- biblatex + biber setup
- Citation styles (authoryear, numeric, apa, ieee)
- Multiple citation commands (`\textcite`, `\parencite`)
- Compilation toolchain (pdflatex → biber → pdflatex)
- UTF-8 support

**Compile**:
```bash
latexmk -pdf modern_bibliography.tex
```

**Note**: Requires `references.bib` file (template included in MWE)

---

### 4. Best Practices Article (`mwes/best_practices_article.tex`)

**Demonstrates**:
- Complete modern LaTeX setup
- Correct package loading order
- Mathematics (amsmath, amsthm)
- Figures (TikZ, graphicx)
- Tables (booktabs)
- Cross-references (cleveref)
- Typography (microtype)

**Use as template** for new LaTeX projects

## Audit Report Structure

### Executive Summary
- Overall status (excellent/good/needs_improvement/critical_issues)
- Findings count by severity (error/warn/info)
- Top 3-5 issues highlighted

### Document Analysis
- Class and options
- Detected engine
- Package summary
- Recommended additions

### Findings by Category
Organized into 11 categories:
1. Document Structure
2. Package Configuration
3. Cross-References
4. Bibliography
5. TikZ & PGF
6. Beamer (if applicable)
7. Typography
8. Floats & Figures
9. Mathematics
10. Lint & Formatting
11. Accessibility

### Detailed Findings
Each finding includes:
- **ID**: Checklist rule identifier
- **Severity**: error/warn/info
- **Message**: Human-readable description
- **Evidence**: Code snippet or line number
- **Reference**: CTAN manual section
- **Fix**: Recommended correction

### Specialized Sections
- TikZ externalization analysis (if applicable)
- Beamer overlay density analysis (if applicable)
- Contrast assessment (if Beamer)

### Action Items
Prioritized checklist sorted by severity and impact

## Fix Plan Structure

### Priority 1: Critical Issues
Must-fix errors that prevent compilation or cause serious problems

### Priority 2: Warnings
Strongly recommended improvements for best practices

### Priority 3: Improvements
Optional enhancements for code quality

### Specialized Fixes
- **Package Loading Order**: Complete reorganized preamble
- **TikZ Externalization**: Step-by-step setup guide
- **Beamer Optimization**: Aspect ratio, overlay consolidation, contrast fixes
- **Bibliography Migration**: BibTeX → biblatex migration path

### Testing & Verification
- Compilation checklist
- Expected outcomes
- Makefile template for reproducible builds

## Package Loading Order

Correct order is critical, especially for `hyperref` and `cleveref`:

```latex
% 1. Encoding & Fonts (pdfLaTeX)
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

% 2. Language
\usepackage[english]{babel}
\usepackage{csquotes}

% 3. Mathematics (early!)
\usepackage{amsmath}

% 4. Graphics & Floats
\usepackage{graphicx}

% 5. TikZ (if needed)
\usepackage{tikz}

% 6. Bibliography
\usepackage[backend=biber]{biblatex}

% 7. Page Layout
\usepackage{geometry}

% 8. Hyperlinks (NEAR END!)
\usepackage{hyperref}

% 9. Cross-References (AFTER hyperref!)
\usepackage{cleveref}

% 10. Typography (LAST!)
\usepackage{microtype}
```

**Why this order matters**:
- hyperref redefines many commands → load after most packages
- cleveref needs hyperref's reference system → load after hyperref
- microtype fine-tunes final typography → load last

## Compilation Workflow

### Recommended: latexmk

Automates multi-pass compilation:

```bash
# Basic compilation
latexmk -pdf document.tex

# With TikZ externalization
latexmk -pdf -shell-escape document.tex

# Continuous preview mode
latexmk -pdf -pvc document.tex

# Clean auxiliary files
latexmk -c

# Clean all (including PDF)
latexmk -C
```

### Manual Compilation (if needed)

For document with bibliography:
```bash
pdflatex document.tex
biber document
pdflatex document.tex
pdflatex document.tex
```

**Why multiple passes?**
1. First pdflatex: Generate `.aux` and `.bcf` files
2. biber: Process bibliography, generate `.bbl`
3. Second pdflatex: Include citations
4. Third pdflatex: Resolve cross-references

## TikZ Externalization

### Why Externalize?

**Problem**: TikZ figures compile every time, even if unchanged
**Solution**: Cache compiled figures as PDFs, reuse unless modified

**Performance gains**:
- 10-50x faster recompilation
- Reduced memory usage
- Individual figure debugging easier

### Setup

```latex
\usepackage{tikz}
\usetikzlibrary{external}
\tikzexternalize[prefix=tikz-cache/]
```

### Compilation

```bash
# Create cache directory
mkdir -p tikz-cache

# Compile with shell-escape
latexmk -pdf -shell-escape document.tex
```

### Security Note

⚠️ `-shell-escape` allows LaTeX to execute system commands. **Only use with trusted documents.**

Modern TeX distributions use "restricted shell escape" for improved security.

## Beamer Best Practices

### Aspect Ratio

**Modern displays**: Use 16:9

```latex
\documentclass[aspectratio=169]{beamer}
```

**Options**:
- `43` - 4:3 (traditional, default)
- `169` - 16:9 (widescreen)
- `1610` - 16:10
- `149` - 14:9

### Overlay Density

**Recommendation**: ≤5 overlays per frame

**Why?**
- Cognitive load on audience
- Increased PDF file size
- Harder to maintain

**Solution**: Consolidate or split complex frames

### Contrast (WCAG 2.1 AA)

**Requirements**:
- Normal text (<18pt): ≥4.5:1 contrast ratio
- Large text (≥18pt): ≥3:1 contrast ratio

**Testing**: Use online contrast checkers
- https://webaim.org/resources/contrastchecker/
- https://contrast-ratio.com/

### Accessibility

- Don't rely solely on color
- Use descriptive frame titles
- Provide handout mode: `\documentclass[handout]{beamer}`

## Troubleshooting

### Issue: "hyperref loaded too early"
**Solution**: Move `\usepackage{hyperref}` near end of preamble

---

### Issue: "cleveref not working"
**Solution**: Load cleveref **after** hyperref

---

### Issue: "biber not found"
**Solution**: Ensure biber installed. On most systems:
```bash
# TeX Live
sudo tlmgr install biber

# MiKTeX
mpm --install=biber
```

---

### Issue: "TikZ externalization fails"
**Solution**:
1. Ensure `-shell-escape` flag used
2. Create cache directory: `mkdir -p tikz-cache`
3. Check for write permissions

---

### Issue: "Beamer overlays not working"
**Solution**: Check overlay specification syntax:
- `\item<1->` not `\item<1>-`
- `<2-4>` for range
- `<1,3,5>` for specific slides

## JSON Output Schema

Complete structured output available in `tex_audit_findings.json`:

```json
{
  "metadata": {
    "audit_date": "2025-11-05T...",
    "skill_version": "1.0.0",
    "file_path": "document.tex"
  },
  "document": {
    "doc_class": "article",
    "engine": "pdflatex"
  },
  "packages": {
    "loaded": [...],
    "recommended": [...]
  },
  "tikz": {...},
  "beamer": {...},
  "findings": [...],
  "compilation": {...},
  "summary": {
    "total_findings": 12,
    "by_severity": {"info": 5, "warn": 6, "error": 1},
    "overall_status": "good"
  }
}
```

Schema: `schema/tex_audit_schema.json`

## References

All recommendations grounded in official documentation:

1. **LaTeX Project**: https://www.latex-project.org/help/documentation/
2. **CTAN**: https://ctan.org/ (package repository)
3. **TikZ & PGF**: https://tikz.dev/
4. **pgfplots**: https://ctan.org/pkg/pgfplots
5. **Beamer**: https://ctan.org/pkg/beamer
6. **hyperref**: https://ctan.org/pkg/hyperref
7. **cleveref**: https://ctan.org/pkg/cleveref
8. **biblatex**: https://ctan.org/pkg/biblatex
9. **microtype**: https://ctan.org/pkg/microtype
10. **csquotes**: https://ctan.org/pkg/csquotes
11. **ChkTeX**: https://www.nongnu.org/chktex/
12. **latexmk**: https://ctan.org/pkg/latexmk
13. **latexindent**: https://ctan.org/pkg/latexindent
14. **WCAG 2.1**: https://www.w3.org/TR/WCAG21/

## Community Resources

- **TeX StackExchange**: https://tex.stackexchange.com/
- **LaTeX Wikibook**: https://en.wikibooks.org/wiki/LaTeX
- **Overleaf Documentation**: https://www.overleaf.com/learn

## Contributing

Enhancements welcome:
- Additional checklist rules
- More MWEs for specific use cases
- Conference template profiles
- Multilingual support

## License

MIT License - see LICENSE file

## Support

- Issues: https://github.com/astoreyai/claude-skills/issues
- Documentation: See SKILL.md for complete rule definitions
- Examples: See `mwes/` directory

---

**Version**: 1.0.0 | **Status**: Production Ready | **Maintained by**: Claude Skills Library
