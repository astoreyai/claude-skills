# Changelog

All notable changes to the latex-check skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-05

### Added

- **Comprehensive audit system** with 60+ rules across 11 categories:
  - Document structure & encoding detection
  - Package configuration & loading order validation
  - Cross-reference system analysis (hyperref, cleveref)
  - Bibliography setup verification (biblatex + biber)
  - TikZ/PGF graphics & externalization support
  - pgfplots data visualization best practices
  - Beamer presentation analysis (aspect ratio, overlays, contrast)
  - Typography optimization (microtype)
  - Accessibility guidelines (WCAG 2.1 AA)
  - Code quality & linting (ChkTeX, latexindent)
  - Compilation workflow guidance (latexmk)

- **Checklist system** (`checklists/latex_checklist.yml`):
  - Structured rules with IDs, severity levels, and CTAN references
  - Engine-specific recommendations (pdfLaTeX, XeLaTeX, LuaLaTeX)
  - Package compatibility checking
  - Conference template awareness

- **Beamer-specific analysis** (`lexicons/beamer_overlays.yml`):
  - Overlay pattern detection (\pause, <n->, \onslide, etc.)
  - Overlay density heuristics (max 5 per frame recommended)
  - Aspect ratio mappings (43, 169, 1610, etc.)
  - WCAG 2.1 contrast guidelines (AA and AAA compliance)
  - Theme recommendations (professional, modern, minimal)

- **Output schema** (`schema/tex_audit_schema.json`):
  - Complete JSON schema for structured findings
  - Metadata tracking (audit date, skill version, file path)
  - Document analysis (class, engine, packages)
  - TikZ and Beamer-specific sections
  - Compilation guidance (commands, toolchain, time estimates)
  - Summary statistics (findings by severity, overall status)

- **Lint configurations**:
  - `lint/.chktexrc` - ChkTeX semantic checking (150+ lines)
    - Space before references
    - Command spacing
    - Math punctuation
    - Quotation mark style
    - Abbreviation handling
  - `lint/indentconfig.yaml` - latexindent formatting (200+ lines)
    - Environment-specific indentation
    - Beamer and TikZ awareness
    - Alignment rules for tabular/align
    - Trailing whitespace removal
    - Maximum line width enforcement

- **Minimal Working Examples** (4 complete templates):
  - `mwes/tikz_externalization.tex` - Complete externalization setup
    - External library configuration
    - Cache directory management
    - Explicit figure naming with \tikzsetnextfilename
    - Shell-escape compilation guide
    - Makefile integration example
    - Security notes for -shell-escape

  - `mwes/beamer_16_9_overlays.tex` - Modern Beamer presentation
    - 16:9 aspect ratio configuration
    - All overlay commands demonstrated (\pause, \onslide, \only, etc.)
    - Best practices (≤5 overlays per frame)
    - WCAG AA contrast considerations
    - Theme and color customization
    - Handout mode guidance

  - `mwes/modern_bibliography.tex` - biblatex + biber setup
    - Backend configuration (biber not BibTeX)
    - Multiple citation styles (authoryear, numeric, apa, ieee)
    - Citation commands (\textcite, \parencite)
    - Compilation toolchain (pdflatex → biber → pdflatex)
    - UTF-8 support demonstration
    - .bib file template included

  - `mwes/best_practices_article.tex` - Complete modern setup
    - Correct package loading order (with detailed comments)
    - Mathematics (amsmath, amsthm, theorem environments)
    - Graphics (TikZ, graphicx, caption, subcaption)
    - Tables (booktabs professional formatting)
    - Cross-references (cleveref integration)
    - Typography (microtype optimization)
    - 300+ lines of best-practice demonstrations

- **Report templates**:
  - `templates/audit_report_template.md` - Comprehensive findings report
    - Executive summary with status assessment
    - Document analysis section
    - Findings grouped by category
    - Detailed findings with evidence and references
    - TikZ and Beamer specialized sections
    - Compilation guidance
    - Action items prioritized by severity

  - `templates/fix_plan_template.md` - Step-by-step remediation guide
    - Priority-ordered actions (critical, warning, improvement)
    - Package loading order fixes with complete preamble
    - TikZ externalization setup guide
    - Beamer optimization (aspect ratio, overlays, contrast)
    - Bibliography migration guide (BibTeX → biblatex)
    - Compilation checklist
    - Makefile template for reproducible builds
    - Testing and verification procedures

- **Package loading order validation**:
  - Enforces correct sequence (encoding → language → math → graphics → hyperref → cleveref → microtype)
  - Detects common errors (hyperref too early, cleveref before hyperref)
  - Provides reorganized preamble template

- **TikZ externalization support**:
  - Compilation cost estimation (low/medium/high/very_high)
  - Externalization detection and configuration checking
  - Shell-escape requirement validation
  - Security warnings for -shell-escape usage
  - Cache directory setup guidance
  - Figure naming recommendations (\tikzsetnextfilename)

- **Beamer presentation analysis**:
  - Aspect ratio detection and recommendations (169 for modern displays)
  - Overlay density analysis (count per frame, flag >5)
  - Frame content balance checking (>20 lines → overcrowded)
  - Contrast estimation for WCAG 2.1 AA compliance
  - Theme consistency verification
  - Handout mode detection

- **Bibliography system recommendations**:
  - Detection of legacy BibTeX usage
  - Migration path to modern biblatex + biber
  - Backend verification (biber vs. bibtex vs. bibtex8)
  - Toolchain validation (pdflatex → biber → pdflatex sequence)
  - Citation style recommendations

- **Compilation guidance**:
  - latexmk usage recommendations (automated multi-pass)
  - Shell-escape security considerations
  - Engine selection (pdfLaTeX vs. XeLaTeX vs. LuaLaTeX)
  - Continuous preview mode (-pvc flag)
  - Estimated compilation time based on complexity

### Documentation

- Comprehensive SKILL.md (600+ lines):
  - Complete audit process with 5 phases
  - 60+ detection rules with implementation details
  - Example usage patterns (article, Beamer, TikZ, bibliography)
  - False positive mitigation strategies
  - Integration points with other skills

- Detailed README.md (500+ lines):
  - Feature overview with examples
  - 4 use case demonstrations
  - Configuration file explanations
  - MWE descriptions with compilation instructions
  - Package loading order rationale
  - Troubleshooting guide (8 common issues)
  - Complete reference list (14 official sources)

- CHANGELOG.md with semantic versioning guidelines
- LICENSE file (MIT)

### Dependencies

None. This is an instruction-only skill that composes with:
- Optional `tex-runner` skill for compilation testing
- Optional file organization skills for multi-file projects

### Performance

- **Fast checks** (<1 second): Structure, package order, pattern matching
- **Medium checks** (1-5 seconds): Preamble analysis, overlay counting
- **Optional slow checks** (5-30 seconds): Full compilation test

### Scientific Grounding

All recommendations cite official documentation:
- LaTeX Project documentation
- CTAN package manuals (hyperref, cleveref, biblatex, microtype, etc.)
- TikZ & PGF manual (tikz.dev)
- pgfplots manual
- Beamer user guide
- WCAG 2.1 accessibility guidelines
- ChkTeX semantic checking guide
- latexmk automated compilation guide

### Security

- Explicit warnings for shell-escape usage
- Security notes in TikZ externalization MWE
- Explanation of restricted shell escape
- Recommendation to only use with trusted documents

---

## Versioning Guidelines

- **Major (X.0.0)**: Breaking changes to skill interface, output format, or checklist structure
- **Minor (1.X.0)**: New features, additional rules, new MWEs, enhanced analysis
- **Patch (1.0.X)**: Bug fixes, documentation improvements, checklist refinements

## Planned Features (Future Releases)

### 1.1.0 (Planned)
- [ ] Additional conference template profiles (Springer, Elsevier, IEEE extended)
- [ ] Glossary and acronym support (glossaries package)
- [ ] Advanced math checking (mathtools, physics packages)
- [ ] Algorithm environment support (algorithm2e, algorithmicx)
- [ ] Code listing analysis (listings, minted packages)
- [ ] Index and nomenclature checking

### 1.2.0 (Planned)
- [ ] Multi-file project analysis (\input, \include tracking)
- [ ] Figure and table caption consistency checking
- [ ] Citation key naming convention validation
- [ ] Collaboration tools integration (latexdiff support)
- [ ] Git integration recommendations (.gitignore templates)
- [ ] Overleaf compatibility checking

### 1.3.0 (Planned)
- [ ] Language-specific rules (French, German, Spanish babel/polyglossia)
- [ ] Custom package ecosystem support (local .sty files)
- [ ] Performance profiling (identify slow packages/commands)
- [ ] Batch processing for multiple documents
- [ ] Web-based report viewer

### 2.0.0 (Planned)
- [ ] Breaking: New JSON schema with hierarchical findings structure
- [ ] Automated fix application (with user approval)
- [ ] Interactive fix wizard
- [ ] Integration with TeX Studio, VSCode LaTeX Workshop
- [ ] Real-time checking mode (as-you-type)
- [ ] Machine learning-based pattern detection

## Known Limitations

### 1.0.0
- Conference templates may have specific requirements that override general rules
- Custom class files (`.cls`) are analyzed generically
- Multilingual documents beyond babel/polyglossia basics not fully supported
- Very large documents (>10,000 lines) may have slower analysis
- Local style files (`.sty`) analyzed as black boxes
- TikZ externalization assumes standard setup (may need adjustment for exotic configurations)

---

## Migration Guide

### From BibTeX to biblatex (assisted by this skill)

**Before** (legacy):
```latex
\bibliographystyle{plain}
\bibliography{references}
```

**After** (modern):
```latex
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{references.bib}
% ...
\printbibliography
```

Skill provides complete migration guide in fix plan.

### From 4:3 to 16:9 Beamer

**Before**:
```latex
\documentclass{beamer}  % Default 4:3
```

**After**:
```latex
\documentclass[aspectratio=169]{beamer}  % Modern 16:9
```

Skill detects aspect ratio and recommends modern standard.

### Adding TikZ Externalization

**Before** (slow):
```latex
\usepackage{tikz}
\begin{tikzpicture}
  % Complex figure
\end{tikzpicture}
```

**After** (fast):
```latex
\usepackage{tikz}
\usetikzlibrary{external}
\tikzexternalize[prefix=tikz-cache/]
% ...
\tikzsetnextfilename{figure-name}
\begin{tikzpicture}
  % Complex figure (cached)
\end{tikzpicture}
```

Skill provides complete setup in `tikz_externalization.tex` MWE.

---

## Community Contributions

We welcome contributions:
- New checklist rules
- Additional MWEs for specific use cases
- Conference template profiles
- Translation of documentation
- Performance improvements

Submit PRs to: https://github.com/astoreyai/claude-skills

---

## Acknowledgments

This skill is grounded in official documentation from:
- The LaTeX Project Team
- Till Tantau (TikZ & PGF creator)
- Christian Feuersänger (pgfplots maintainer)
- Till Tantau, Joseph Wright, Vedran Miletić (Beamer maintainers)
- Heiko Oberdiek (hyperref maintainer)
- Toby Cubitt (cleveref author)
- Philipp Lehman, Philip Kime (biblatex & biber)
- Robert Schlicht (microtype author)
- Javier Bezos, Johannes Braams (babel maintainers)

And the broader TeX community for maintaining excellent documentation on CTAN and TeX StackExchange.

---

**Note**: This is the initial production release. Report issues at https://github.com/astoreyai/claude-skills/issues
