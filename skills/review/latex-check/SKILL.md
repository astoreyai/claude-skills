---
name: latex-check
description: Comprehensive LaTeX/TikZ/Beamer auditor. Validates document structure, package configuration, cross-references, bibliography setup, TikZ externalization, and Beamer presentations. Produces standards-backed reports with MWEs and compilation guidance.
---

# LaTeX/TikZ/Beamer Auditor

## Overview

A comprehensive auditing skill for LaTeX documents, including article/report/book classes, TikZ/PGF graphics, pgfplots visualizations, and Beamer presentations. All recommendations are grounded in official CTAN documentation and TeX best practices.

## Auto-Invoke Triggers

Use this skill when task mentions:
- "LaTeX check" or "TeX audit"
- "TikZ" or "pgfplots"
- "Beamer" or "slides"
- "compile errors" or "compilation issues"
- "aspectratio" or "16:9"
- "externalize" or "tikzexternalize"
- "latexmk" or "pdflatex"
- "biblatex" or "biber"
- "hyperref" or "cleveref"

## Scientific & Standards Foundation

This skill enforces best practices from:

1. **LaTeX Project Documentation** - Official LaTeX kernel and class documentation
2. **TikZ & PGF Manual** (tikz.dev) - Graphics and externalization library
3. **pgfplots Manual** (CTAN) - Data plotting best practices
4. **Beamer User Guide** (CTAN) - Presentation class guidelines
5. **hyperref Manual** (CTAN) - Package loading order and PDF metadata
6. **cleveref Manual** (CTAN) - Type-aware cross-referencing
7. **biblatex Manual** (CTAN) - Modern bibliography with biber backend
8. **microtype Manual** (CTAN) - Character protrusion and font expansion
9. **csquotes Manual** (CTAN) - Locale-aware quotation handling
10. **WCAG 2.1** - Web Content Accessibility Guidelines (for Beamer contrast)
11. **ChkTeX Documentation** - Semantic LaTeX linting
12. **latexmk Manual** (CTAN) - Automated multi-pass compilation

## Audit Scope

### 1. Document & Engine Configuration
- Document class detection (article, beamer, IEEEtran, etc.)
- Engine compatibility (pdfLaTeX, XeLaTeX, LuaLaTeX)
- Input encoding and font encoding
- Class options validation

### 2. Package Configuration
- Package loading order (critical for hyperref, cleveref)
- Package compatibility checks
- Required vs. optional packages
- Version-specific requirements

### 3. Cross-References & Hyperlinks
- hyperref loading position (near end of preamble)
- PDF metadata configuration
- cleveref integration (load after hyperref)
- Label prefix conventions (fig:, tab:, sec:, eq:)

### 4. Bibliography
- Modern biblatex + biber vs. legacy BibTeX
- Backend configuration verification
- Citation style consistency
- Toolchain completeness (pdflatex → biber → pdflatex)

### 5. TikZ/PGF & pgfplots
- TikZ library loading
- pgfplots compatibility level
- Data file separation for large plots
- Externalization setup and security
- Shell-escape requirements and warnings

### 6. Beamer Presentations
- Aspect ratio configuration (43, 169, 1610)
- Theme and color scheme consistency
- Overlay density analysis (≤5 per frame recommended)
- Frame content balance
- WCAG AA contrast compliance (≥4.5:1 normal, ≥3:1 large text)

### 7. Typography & Formatting
- microtype for improved typography
- Font selection and loading
- Page layout and geometry
- Quotation handling with csquotes

### 8. Linting & Code Quality
- ChkTeX semantic checks
- latexindent formatting
- Code organization and readability

### 9. Compilation Workflow
- latexmk usage and configuration
- Shell-escape security considerations
- Multi-pass compilation requirements
- Estimated compilation time

### 10. Accessibility
- Alternative text for figures (when feasible)
- Color-independent information encoding
- Contrast ratios for Beamer slides
- Logical document structure

## Audit Process

### Phase 1: Document Analysis

1. **Read the LaTeX source file(s)**
   - Main `.tex` file
   - Included files via `\input` or `\include`
   - Class files (`.cls`) if custom
   - Style files (`.sty`) if custom

2. **Extract metadata**:
   ```
   - Document class: \documentclass[options]{class}
   - Class options: aspectratio, fontsize, paper size, etc.
   - Engine hints: fontspec (XeLaTeX/LuaLaTeX), inputenc (pdfLaTeX)
   ```

3. **Parse preamble**:
   - List all `\usepackage{...}` commands in order
   - Extract package options
   - Note custom commands and environments

4. **Detect document type**:
   - Article/report/book → Standard academic document
   - Beamer → Presentation (trigger Beamer-specific checks)
   - IEEEtran/ACM/others → Conference/journal template

### Phase 2: Run Checklist Rules

Load rules from `checklists/latex_checklist.yml` and execute in order:

#### 2.1 Document Structure
- `class_detect`: Identify class and validate options
- `engine_detect`: Determine appropriate LaTeX engine
- `encoding_check`: Verify UTF-8 input and T1 font encoding (pdfLaTeX)

#### 2.2 Package Configuration
Execute in sequence:

1. **hyperref_order**: Verify hyperref loaded near end
   ```
   RULE: hyperref must come after most packages
   EXCEPTION: cleveref, glossaries must come after hyperref
   ```

2. **hyperref_metadata**: Check PDF metadata
   ```
   VERIFY: \hypersetup{pdftitle=..., pdfauthor=..., pdfsubject=..., pdfkeywords=...}
   ```

3. **cleveref_present**: If cross-refs detected, recommend cleveref
   ```
   DETECT: \ref{}, \label{} usage
   RECOMMEND: \usepackage{cleveref} after hyperref
   ```

4. **cleveref_order**: Verify cleveref loaded last
   ```
   RULE: cleveref must be one of the last packages
   EXCEPTION: Only microtype may come after
   ```

5. **bib_backend**: Check bibliography system
   ```
   PREFER: biblatex with backend=biber
   LEGACY: \bibliography{}, \bibliographystyle{} → flag for migration
   ```

6. **microtype_enabled**: Verify microtype for typography
   ```
   CHECK: \usepackage{microtype} present
   NOTE: Works with pdfLaTeX, XeLaTeX, LuaLaTeX
   ```

7. **csquotes_present**: Check quotation handling
   ```
   DETECT: ``, '', \"{}, etc. → recommend csquotes
   VERIFY: \usepackage{csquotes} after babel/polyglossia
   ```

8. **babel_polyglossia**: Language support
   ```
   pdfLaTeX: \usepackage[language]{babel}
   XeLaTeX/LuaLaTeX: \usepackage{polyglossia}
   ```

#### 2.3 TikZ & PGF
Execute if TikZ detected:

1. **tikz_present**: Confirm TikZ package and usage
   ```
   DETECT: \usepackage{tikz}, \begin{tikzpicture}
   ```

2. **tikz_libraries**: Verify library loading
   ```
   COMMON: positioning, arrows.meta, shapes, calc
   CHECK: \usetikzlibrary{...} before first use
   ```

3. **pgfplots_present**: Check pgfplots usage
   ```
   DETECT: \usepackage{pgfplots}, \begin{axis}
   ```

4. **pgfplots_compat**: Verify compatibility level
   ```
   REQUIRE: \pgfplotsset{compat=1.18} or compat=newest
   REASON: Enables modern features and behavior
   ```

5. **tikz_compile_cost**: Estimate compilation time
   ```
   COUNT: Number of tikzpicture environments
   ESTIMATE:
     - 1-5 figures: Low
     - 6-15 figures: Medium
     - 16-30 figures: High
     - 31+ figures: Very High
   RECOMMEND: Externalization if High or Very High
   ```

6. **externalize_detection**: Check externalization setup
   ```
   DETECT: \usetikzlibrary{external}, \tikzexternalize
   VERIFY: prefix=tikz-cache/ or similar
   ```

7. **externalize_shell_escape**: Verify shell-escape awareness
   ```
   IF externalization detected:
     REQUIRE: Compilation with -shell-escape
     WARN: Security implications (only trusted documents)
     RECOMMEND: latexmk -pdf -shell-escape document.tex
   ```

8. **tikz_naming**: Check for explicit figure naming
   ```
   RECOMMEND: \tikzsetnextfilename{descriptive-name}
   REASON: Reproducible cache names, easier debugging
   ```

#### 2.4 Beamer (if applicable)
Execute if `\documentclass{beamer}` detected:

1. **beamer_class**: Confirm Beamer detection
2. **aspect_ratio**: Check aspectratio option
   ```
   DEFAULT: 43 (4:3)
   MODERN: 169 (16:9 widescreen)
   OTHER: 1610 (16:10), 149 (14:9)
   RECOMMEND: 169 for contemporary displays
   ```

3. **frame_title**: Verify all frames have titles
   ```
   CHECK: \begin{frame}{Title} or \frametitle{Title}
   REASON: Structure, navigation, accessibility
   ```

4. **overlay_detection**: Count overlay specifications
   ```
   DETECT: \pause, <n->, \onslide<>, \only<>, etc.
   LOAD: lexicons/beamer_overlays.yml patterns
   ```

5. **overlay_density**: Flag excessive overlays
   ```
   THRESHOLD: 5 overlays per frame
   IF count > 5:
     WARN: Over-complexity
     SUGGEST: Consolidate or split frame
   ```

6. **frame_content_balance**: Check frame content volume
   ```
   HEURISTIC: >20 lines of content → potentially overcrowded
   RECOMMEND: Split across multiple frames
   ```

7. **contrast_check**: Assess WCAG compliance
   ```
   ANALYZE: Theme colors (if standard theme)
   REFERENCE: lexicons/beamer_overlays.yml contrast guidelines
   WARN: Potential contrast failures
   RECOMMEND: Test with contrast checker
   ```

### Phase 3: Optional Compilation Test

If user requests or document is problematic:

1. **Invoke compilation** (if code-capable helper available):
   ```
   COMMAND: latexmk -pdf -interaction=nonstopmode -halt-on-error document.tex
   IF externalization detected:
     ADD: -shell-escape flag
   ```

2. **Parse compilation output**:
   - Errors → severity: error
   - Warnings → severity: warn
   - Overfull/underfull boxes → severity: info

3. **Check auxiliary files**:
   - `.log` file for detailed errors
   - `.bcf` file for biblatex backend
   - `.bbl` file for bibliography compilation

### Phase 4: Generate Outputs

#### 4.1 Create Audit Report
Use `templates/audit_report_template.md`:

1. **Fill executive summary**:
   - Overall status (excellent/good/needs_improvement/critical_issues)
   - Count findings by severity
   - Highlight top 3-5 issues

2. **Document analysis section**:
   - Class, engine, packages
   - TikZ/Beamer specifics

3. **Findings by category**:
   - Group by checklist section
   - Include evidence (line numbers, code snippets)
   - Reference official documentation

4. **Detailed findings**:
   - Each finding with:
     - ID (from checklist)
     - Severity (error/warn/info)
     - Message
     - Evidence
     - Reference (CTAN manual, page number if applicable)
     - Fix recommendation

5. **Compilation guidance**:
   - Recommended command
   - Shell-escape notes
   - Estimated compilation time

6. **MWE references**:
   - Link to generated minimal working examples

#### 4.2 Create Fix Plan
Use `templates/fix_plan_template.md`:

1. **Priority 1 actions** (errors):
   - Step-by-step fix instructions
   - Code snippets for corrections
   - Expected outcome

2. **Priority 2 actions** (warnings):
   - Recommended improvements
   - Impact explanation

3. **Priority 3 actions** (info):
   - Best practices
   - Optional enhancements

4. **Package loading order**:
   - Complete preamble template
   - Organized by category
   - Comments explaining order

5. **Specialized fixes**:
   - TikZ externalization setup (if needed)
   - Beamer aspect ratio and overlay fixes (if applicable)
   - Bibliography migration guide (if needed)

#### 4.3 Generate JSON Output
Conform to `schema/tex_audit_schema.json`:

```json
{
  "metadata": {...},
  "document": {...},
  "packages": {...},
  "tikz": {...},
  "beamer": {...},
  "findings": [...],
  "compilation": {...},
  "mwe_paths": [...],
  "summary": {...}
}
```

#### 4.4 Create Minimal Working Examples

Generate MWEs for relevant fixes:

1. **TikZ Externalization** (if applicable):
   - Copy `mwes/tikz_externalization.tex`
   - Customize for user's specific setup

2. **Beamer 16:9 with Overlays** (if applicable):
   - Copy `mwes/beamer_16_9_overlays.tex`
   - Adapt to user's theme

3. **Modern Bibliography** (if BibTeX detected):
   - Copy `mwes/modern_bibliography.tex`
   - Show migration path

4. **Best Practices Template**:
   - Always provide `mwes/best_practices_article.tex`
   - Demonstrates complete modern setup

#### 4.5 Provide Lint Configurations

1. **ChkTeX configuration**:
   - Copy `lint/.chktexrc` to project
   - Explain usage: `chktex -v0 -l document.tex`

2. **latexindent configuration**:
   - Copy `lint/indentconfig.yaml` to project
   - Explain usage: `latexindent -l=indentconfig.yaml -w document.tex`

### Phase 5: Safeguards & Notes

1. **Shell-escape warning**:
   ```
   IF -shell-escape required:
     EMPHASIZE: Security implications
     NOTE: Only use with trusted documents
     EXPLAIN: Restricted shell escape in modern distributions
   ```

2. **Package conflicts**:
   ```
   IF known conflicts detected:
     WARN: Specific incompatibilities
     SUGGEST: Alternative approaches
   ```

3. **Manual references**:
   ```
   FOR each recommendation:
     CITE: Specific manual section
     PROVIDE: CTAN link or official documentation URL
   ```

4. **Beamer accessibility**:
   ```
   IF Beamer detected:
     NOTE: Contrast recommendations are WCAG 2.1 AA guidelines
     ACKNOWLEDGE: Theme customization may be needed
     PROVIDE: Contrast checking tools
   ```

## Detection Rules Implementation

### Package Loading Order
Correct order (with rationale):

```latex
% 1. ENCODING & FONTS (pdfLaTeX only)
\usepackage[utf8]{inputenc}    % UTF-8 input
\usepackage[T1]{fontenc}        % T1 font encoding

% 2. LANGUAGE
\usepackage[english]{babel}     % Or polyglossia for XeLaTeX/LuaLaTeX
\usepackage{csquotes}           % After babel

% 3. MATHEMATICS (early for other packages to use)
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}

% 4. GRAPHICS & FLOATS
\usepackage{graphicx}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}

% 5. TABLES
\usepackage{booktabs}
\usepackage{array}
\usepackage{multirow}

% 6. TIKZ (if needed)
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta,shapes,calc}
\usepackage{pgfplots}
\pgfplotsset{compat=newest}

% 7. BIBLIOGRAPHY
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{references.bib}

% 8. PAGE LAYOUT
\usepackage{geometry}

% 9. HYPERLINKS (near end!)
\usepackage[colorlinks=true,...]{hyperref}

% 10. CROSS-REFERENCES (after hyperref!)
\usepackage{cleveref}

% 11. TYPOGRAPHY (last!)
\usepackage{microtype}
```

**Rationale**:
- Encoding/fonts first: Affects character processing
- Language early: Affects hyphenation patterns
- Math early: Other packages may need math commands
- Graphics/tables: Independent, can be anywhere in middle
- TikZ: May use math, graphics facilities
- Bibliography: Needs to hook into referencing
- Hyperref late: Redefines many commands, needs others loaded first
- cleveref after hyperref: Needs hyperref's reference system
- microtype last: Fine-tunes final typography

### TikZ Externalization Detection
```
IF \usetikzlibrary{external} present:
  CHECK for \tikzexternalize command
  VERIFY prefix setting
  COUNT tikzpicture environments
  ESTIMATE cache size

  IF count > 10:
    STRONGLY RECOMMEND externalization
  IF count 5-10:
    RECOMMEND externalization
  IF count < 5:
    NOTE: Optional, may not provide significant benefit

  ALWAYS WARN: Requires -shell-escape
```

### Beamer Overlay Analysis
```
FOR each \begin{frame}...\end{frame}:
  COUNT occurrences of:
    - \pause
    - <n-> patterns (extract n)
    - \onslide<...>
    - \only<...>
    - \item<...>

  COMPUTE max overlay number for frame

  IF max > 5:
    WARN: Excessive overlays
    PROVIDE frame title/line number
    SUGGEST: Consolidation strategies

  ACCUMULATE global overlay statistics
```

### Contrast Estimation (Beamer)
```
FOR standard Beamer themes:
  LOAD known color schemes
  ESTIMATE contrast ratios

FOR custom themes:
  WARN: Manual contrast checking required
  PROVIDE: Online contrast checker tools
  REFERENCE: WCAG 2.1 SC 1.4.3

ALWAYS NOTE:
  - Normal text: ≥4.5:1 (AA)
  - Large text (≥18pt): ≥3:1 (AA)
  - Don't rely solely on color
```

## Example Usage Patterns

### Pattern 1: Basic Article Audit
```
User: "Check my LaTeX document for issues"

Process:
1. Read document.tex
2. Detect class: article
3. Run document/packages/crossref/bib checks
4. Generate audit report
5. Provide fix plan
6. Include best_practices_article.tex as reference
```

### Pattern 2: Beamer Presentation Audit
```
User: "Review my presentation slides for LaTeX issues"

Process:
1. Read slides.tex
2. Detect class: beamer
3. Run all standard checks
4. ADDITIONALLY run Beamer-specific checks:
   - Aspect ratio
   - Overlay density
   - Contrast estimation
   - Frame content balance
5. Generate audit report with Beamer section
6. Provide beamer_16_9_overlays.tex as reference
7. Highlight WCAG contrast requirements
```

### Pattern 3: TikZ-Heavy Document Audit
```
User: "My document with lots of TikZ figures compiles very slowly"

Process:
1. Read document.tex
2. Count tikzpicture environments
3. IF count > 15:
   - STRONGLY recommend externalization
   - Generate externalization setup guide
   - Provide tikz_externalization.tex MWE
   - Explain shell-escape security
   - Show Makefile integration
4. Estimate compilation time savings
```

### Pattern 4: Bibliography Migration
```
User: "How do I modernize my bibliography setup?"

Process:
1. Detect legacy BibTeX usage:
   - \bibliographystyle{}
   - \bibliography{}
2. Recommend migration to biblatex + biber
3. Provide modern_bibliography.tex as guide
4. Show step-by-step migration:
   - Remove old commands
   - Add biblatex package
   - Change compilation workflow
5. Explain benefits:
   - UTF-8 support
   - Flexible formatting
   - Better sorting
```

## False Positive Mitigation

### Conference Templates
```
IF document uses conference class (IEEEtran, ACM, etc.):
  SUPPRESS warnings about:
    - Package loading order (template may have specific requirements)
    - Class options (conference-mandated)
    - Bibliography style (often required by venue)

  STILL CHECK:
    - Compilation issues
    - TikZ externalization opportunities
    - Code quality (ChkTeX, indentation)
```

### Legacy Documents
```
IF document appears to be legacy (pre-2010 packages):
  NOTE: Document may be intentionally using older packages
  DISTINGUISH:
    - Critical issues (will cause errors)
    - Modernization opportunities (optional improvements)
  PROVIDE migration path but acknowledge may not be desired
```

### Minimal Documents
```
IF document is very short (<100 lines, simple structure):
  REDUCE recommendations to essentials
  DON'T recommend:
    - microtype (minimal benefit)
    - Complex cross-reference systems
    - Externalization (overhead not worth it)
```

## Integration Points

### With tex-runner Skill (if available)
```
IF tex-runner skill available:
  INVOKE for compilation test:
    tex-runner.compile(
      path=document.tex,
      engine=detected_engine,
      shell_escape=externalization_detected,
      timeout=300
    )

  PARSE results:
    - Errors → add to findings with severity=error
    - Warnings → add to findings with severity=warn
    - Success → note in report
```

### With File Organization Skills
```
IF large project with multiple files:
  ANALYZE structure:
    - Main file
    - \input{} and \include{} files
    - figures/ directory
    - data/ directory for pgfplots

  RECOMMEND:
    - Organized directory structure
    - Separation of content and presentation
    - Version control (.gitignore for auxiliary files)
```

## Output Format Standards

### Audit Report Structure
1. **Executive Summary** (1 page)
2. **Document Analysis** (class, engine, packages)
3. **Findings by Category** (grouped, prioritized)
4. **Detailed Findings** (with evidence and references)
5. **TikZ Analysis** (if applicable)
6. **Beamer Analysis** (if applicable)
7. **Compilation Guidance** (commands, toolchain)
8. **MWE References** (links to examples)
9. **Lint Configuration** (ChkTeX, latexindent setup)
10. **Action Items** (prioritized checklist)

### Fix Plan Structure
1. **Overview** (summary of fixes)
2. **Priority 1** (critical errors)
3. **Priority 2** (warnings)
4. **Priority 3** (improvements)
5. **Package Loading Order** (complete preamble)
6. **Specialized Fixes** (TikZ, Beamer, bibliography)
7. **Compilation Checklist** (verification steps)
8. **Testing** (how to verify fixes)
9. **Makefile** (reproducible builds)
10. **Resources** (documentation links)

## Performance Notes

- **Fast checks** (< 1 second): Document structure, package order, basic pattern matching
- **Medium checks** (1-5 seconds): Detailed preamble analysis, overlay counting
- **Slow checks** (5-30 seconds): Full compilation test (if invoked)

Prioritize fast checks; only invoke compilation test if:
1. User explicitly requests it
2. Static analysis reveals ambiguous issues
3. Document has known compilation problems

---

**Version**: 1.0.0
**License**: MIT
**Maintained by**: Claude Skills Library
