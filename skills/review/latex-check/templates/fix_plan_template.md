# LaTeX Fix Plan

**Document**: {file_path}
**Generated**: {generation_date}
**Total Actions**: {total_actions}

---

## Overview

This document provides step-by-step instructions to address all findings from the LaTeX audit. Actions are prioritized by severity and impact.

---

## Priority 1: Critical Issues (Must Fix)

{priority_1_actions}

---

## Priority 2: Warnings (Strongly Recommended)

{priority_2_actions}

---

## Priority 3: Improvements (Best Practices)

{priority_3_actions}

---

## Package Loading Order Fix

### Current Order Issues
{current_package_issues}

### Recommended Preamble Structure

```latex
% ====================================================================
% ENCODING & FONTS
% ====================================================================
{encoding_section}

% ====================================================================
% LANGUAGE & LOCALIZATION
% ====================================================================
{language_section}

% ====================================================================
% MATHEMATICS
% ====================================================================
{math_section}

% ====================================================================
% GRAPHICS & FIGURES
% ====================================================================
{graphics_section}

% ====================================================================
% TABLES
% ====================================================================
{tables_section}

% ====================================================================
% TIKZ & PGFPLOTS (if needed)
% ====================================================================
{tikz_section}

% ====================================================================
% BIBLIOGRAPHY
% ====================================================================
{bibliography_section}

% ====================================================================
% PAGE LAYOUT
% ====================================================================
{layout_section}

% ====================================================================
% HYPERLINKS (Load near end)
% ====================================================================
{hyperref_section}

% ====================================================================
% CROSS-REFERENCES (Load after hyperref)
% ====================================================================
{cleveref_section}

% ====================================================================
% TYPOGRAPHY (Load last)
% ====================================================================
{microtype_section}
```

---

## TikZ Externalization Setup (if applicable)

### Step 1: Add Externalization Library

```latex
\usepackage{tikz}
\usetikzlibrary{external}
\tikzexternalize[prefix=tikz-cache/]
```

### Step 2: Name Figures

Before each `\begin{tikzpicture}`, add:

```latex
\tikzsetnextfilename{descriptive-name}
```

### Step 3: Create Cache Directory

```bash
mkdir -p tikz-cache
```

### Step 4: Update Compilation Command

```bash
latexmk -pdf -shell-escape {document_file}
```

### Security Note
⚠️ `-shell-escape` allows LaTeX to execute system commands. Only use with trusted documents.

**Reference**: See `mwes/tikz_externalization.tex` for complete example.

---

## Beamer Fixes (if applicable)

### Fix 1: Set Aspect Ratio

**Current**: {current_aspect_ratio}
**Recommended**: 16:9 for modern displays

```latex
\documentclass[aspectratio=169]{beamer}
```

Available ratios:
- `43` - 4:3 (traditional, default)
- `169` - 16:9 (widescreen)
- `1610` - 16:10
- `149` - 14:9

### Fix 2: Reduce Overlay Complexity

**Frames exceeding threshold** (>5 overlays):

{complex_frames_list}

**Solution**: Consolidate or split frames. Example:

```latex
% Before: 8 overlays
\begin{frame}{Complex Frame}
    \item<1-> Point 1
    \item<2-> Point 2
    ...
    \item<8-> Point 8
\end{frame}

% After: Split into two frames
\begin{frame}{Key Points (Part 1)}
    \item<1-> Point 1
    \item<2-> Point 2
    \item<3-> Point 3
    \item<4-> Point 4
\end{frame}

\begin{frame}{Key Points (Part 2)}
    \item<1-> Point 5
    \item<2-> Point 6
    \item<3-> Point 7
    \item<4-> Point 8
\end{frame}
```

### Fix 3: Improve Contrast

**Potential contrast issues identified**:

{contrast_issues_list}

**WCAG 2.1 Requirements**:
- Normal text (<18pt): ≥4.5:1 (AA), ≥7:1 (AAA)
- Large text (≥18pt): ≥3:1 (AA), ≥4.5:1 (AAA)

**Test contrast**: Use online tools like https://webaim.org/resources/contrastchecker/

**Reference**: See `mwes/beamer_16_9_overlays.tex` for complete example.

---

## Bibliography Migration (if needed)

### Migrate from BibTeX to biblatex + biber

**Step 1**: Replace in preamble:

```latex
% OLD (remove):
% \bibliographystyle{plain}
% \bibliography{references}

% NEW (add):
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{references.bib}
```

**Step 2**: Replace at end of document:

```latex
% OLD (remove):
% \bibliography{references}

% NEW (add):
\printbibliography
```

**Step 3**: Update compilation:

```bash
latexmk -pdf {document_file}
```

latexmk automatically runs: pdflatex → biber → pdflatex → pdflatex

**Reference**: See `mwes/modern_bibliography.tex` for complete example.

---

## Cross-Reference Improvements

### Replace \ref with \cref

**Benefits**:
- Automatic type detection ("Figure 1" vs "Table 2")
- Consistent formatting
- Handles multiple references

**Migration**:

```latex
% OLD
See Figure~\ref{fig:example} and Table~\ref{tab:data}.

% NEW
See \cref{fig:example,tab:data}.
```

**Setup**:

```latex
\usepackage{hyperref}  % Load first
\usepackage{cleveref}  % Load after hyperref
```

---

## Linting and Formatting

### Step 1: Run ChkTeX

```bash
# Copy provided configuration
cp lint/.chktexrc .

# Run check
chktex -v0 -l {document_file}
```

**Common warnings**:
- Warning 1: Command terminated with space
- Warning 2: Use ~ before citations/references
- Warning 8: Dash length (-, --, ---)
- Warning 24: Space before references

**Suppress specific warnings**:
```latex
% At top of file:
% chktex-file 24

% For one line:
See Figure~\ref{fig:example}  % chktex 2
```

### Step 2: Format with latexindent

```bash
# Copy provided configuration
cp lint/indentconfig.yaml .

# Format (creates backup)
latexindent -l=indentconfig.yaml -w {document_file}
```

---

## Compilation Checklist

After applying fixes:

- [ ] Packages loaded in correct order
- [ ] hyperref loaded near end (before cleveref)
- [ ] cleveref loaded last (or before microtype)
- [ ] Bibliography backend set to biber
- [ ] TikZ externalization configured (if needed)
- [ ] Cache directory created (tikz-cache/)
- [ ] Beamer aspect ratio set (if applicable)
- [ ] All labels have consistent prefixes (fig:, tab:, sec:, eq:)
- [ ] Compilation command includes -shell-escape (if externalizing)
- [ ] Test compile successful: `latexmk -pdf {document_file}`

---

## Testing

### Full Compilation Test

```bash
# Clean build
latexmk -C

# Full rebuild
latexmk -pdf {shell_escape_flag} {document_file}

# Check for errors
echo $?  # Should be 0
```

### Verify Output

- [ ] All figures rendered correctly
- [ ] All references resolved (no ??)
- [ ] Bibliography appears
- [ ] Hyperlinks work in PDF
- [ ] TikZ figures cached (if externalizing)
- [ ] Beamer overlays function correctly (if applicable)

---

## Makefile Template

Create `Makefile` for reproducible builds:

```makefile
# Makefile for LaTeX project
MAIN = {document_basename}
SHELL_ESCAPE = {shell_escape_makefile}

.PHONY: all clean distclean view

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	latexmk -pdf $(SHELL_ESCAPE) $(MAIN).tex

clean:
	latexmk -c

distclean: clean
	latexmk -C
	rm -rf tikz-cache/

view: $(MAIN).pdf
	@open $(MAIN).pdf || xdg-open $(MAIN).pdf

# Continuous preview mode
watch:
	latexmk -pdf -pvc $(SHELL_ESCAPE) $(MAIN).tex
```

Usage:
```bash
make          # Build PDF
make clean    # Remove auxiliary files
make distclean # Remove all generated files including PDF
make view     # Open PDF
make watch    # Continuous preview mode
```

---

## Expected Outcomes

After implementing this fix plan:

✅ **Compilation**:
- Clean build with no errors
- Faster recompilation (with externalization if applicable)
- Automated bibliography processing

✅ **Structure**:
- Proper package loading order
- No package conflicts
- Modern LaTeX setup

✅ **Quality**:
- Improved typography (microtype)
- Working hyperlinks and cross-references
- Professional appearance

✅ **Maintainability**:
- Lint-clean code
- Consistent formatting
- Reproducible builds

---

## Additional Resources

### Templates
- Best practices article: `mwes/best_practices_article.tex`
- TikZ externalization: `mwes/tikz_externalization.tex`
- Beamer 16:9: `mwes/beamer_16_9_overlays.tex`
- Modern bibliography: `mwes/modern_bibliography.tex`

### Documentation
- LaTeX Wikibook: https://en.wikibooks.org/wiki/LaTeX
- TeX StackExchange: https://tex.stackexchange.com/
- CTAN Package Search: https://ctan.org/

---

## Support

If issues persist after implementing fixes:

1. Check log file: `{document_basename}.log`
2. Verify package versions: `\listfiles` in preamble
3. Test with minimal working example
4. Consult package documentation on CTAN
5. Search TeX StackExchange for specific errors

---

*Generated by latex-check skill v{skill_version}*
*All recommendations grounded in official CTAN documentation*
