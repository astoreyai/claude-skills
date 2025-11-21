# Kymera Brand Skill

A comprehensive design system skill for generating Jarvis-inspired, technically sophisticated artifacts across all formats—from React dashboards to academic presentations.

## Overview

The kymera-brand skill transforms Claude's default aesthetic outputs into cohesive, technically precise interfaces that embody holographic command center aesthetics. Inspired by advanced HUD systems and sophisticated trading terminals, this skill provides guidance for creating artifacts that feel engineered rather than generic.

**Aesthetic Philosophy:** Dark foundations, cyan luminescence, geometric precision, atmospheric depth, and technical sophistication.

**Coverage:** All artifact types including HTML/React, PowerPoint, Word documents, PDFs, spreadsheets, and Markdown.

## Installation

### Option 1: User Skill (Recommended)
1. Navigate to your Claude skills directory (typically `/mnt/skills/user/`)
2. Create a new directory: `mkdir kymera-brand`
3. Place the `SKILL.md` file in this directory
4. The skill will be automatically available in your Claude sessions

### Option 2: Project Skill
If working within a specific Claude Project:
1. Upload the `SKILL.md` file to your project's knowledge base
2. Claude will automatically detect and use it when relevant

### Option 3: Direct Reference
For one-time use or testing, you can reference the skill file directly in your prompt.

## Usage

### Automatic Activation
Once installed, Claude will automatically detect when to apply kymera-brand styling based on:
- Mentions of "Kymera Systems" or "Kymera brand"
- Requests for Jarvis-style, holographic, or technical aesthetics
- Trading dashboard or financial systems contexts
- When you explicitly request branded outputs

### Explicit Invocation
For guaranteed activation, reference the skill directly:

```
Create a React dashboard for momentum trading signals using kymera-brand aesthetic.
```

```
Make a PowerPoint presentation about XAI research with kymera-brand styling.
```

```
Generate an Excel template for trading journal with kymera-brand formatting.
```

## Example Prompts

### HTML/React Artifacts

**Trading Dashboard:**
```
Build a React trading dashboard displaying SABR20 momentum scores across 
15m, 1h, and 4h timeframes. Apply kymera-brand design system with real-time 
data visualization, cyan glow effects, and technical precision.
```

**Academic Portfolio:**
```
Create a personal research website for my AI dissertation work using 
kymera-brand aesthetic. Include sections for publications, current research, 
and contact information.
```

**Landing Page:**
```
Design a landing page for Kymera Systems LLC describing our algorithmic 
trading approach. Use the kymera-brand system with emphasis on technical 
sophistication and data-driven methodology.
```

### PowerPoint Presentations

**Research Presentation:**
```
Create a PowerPoint presentation on "Explainable Facial Recognition with 
Vision Transformers" for Clarkson University. Apply kymera-brand aesthetic 
with dark backgrounds, cyan accents, and geometric technical diagrams.
```

**Trading Strategy Overview:**
```
Generate a presentation deck explaining multi-timeframe momentum reversal 
strategies using kymera-brand design. Include technical charts and 
systematic approach visualization.
```

### Word Documents

**Technical Report:**
```
Draft a technical report template for AI research papers using kymera-brand 
styling. Include proper heading hierarchy, code block formatting, and 
citation sections.
```

**Standard Operating Procedure:**
```
Create an SOP document for trading system execution with kymera-brand 
formatting. Use monospace fonts for protocols and cyan highlights for 
critical steps.
```

### Spreadsheets

**Trading Journal:**
```
Design an Excel trading journal template with kymera-brand styling. Include 
conditional formatting for P&L, trade scoring metrics, and performance analytics.
```

**Research Data Tracker:**
```
Create a spreadsheet for tracking dissertation research progress with 
kymera-brand design—task lists, timeline visualization, and resource allocation.
```

### PDFs

**Investment Thesis:**
```
Generate a PDF investment thesis document for Kymera Systems using 
kymera-brand aesthetic. Professional formatting with technical precision 
and data visualization.
```

## Color Reference Quick Guide

```css
/* Primary Colors */
Cyan Primary:   #00D9FF  /* Main accent */
Cyan Glow:      #00FFFF  /* Highlights */
Dark Deep:      #0A0E1A  /* Main background */
Dark Surface:   #121826  /* Cards */

/* Context-Specific */
Market Green:   #00FF88  /* Bullish/gains */
Market Red:     #FF3366  /* Bearish/losses */
Warning:        #FF8C00  /* Alerts */
```

## Typography Stack

```
Display:    'Orbitron', 'Exo 2', 'Rajdhani'
Technical:  'JetBrains Mono', 'Fira Code', 'Space Mono'
Body:       'Inter Tight', 'IBM Plex Sans', 'Space Grotesk'
```

## Key Design Principles

1. **Dark Foundations:** Always anchor with dark backgrounds unless explicitly academic/formal context requires otherwise
2. **Cyan Signature:** Use cyan as the distinctive brand identifier—sparingly for maximum impact
3. **Technical Precision:** Monospace fonts for all data, code, and numeric values
4. **Atmospheric Depth:** Layer gradients, patterns, and subtle effects; avoid flat surfaces
5. **Geometric Structure:** Use grids, hexagons, and connecting lines to suggest systematic thinking
6. **Intentional Motion:** Animations should feel responsive and technical, not decorative
7. **Data Primacy:** Make information the hero; design serves clarity

## Context Adaptation

### Academic (Clarkson University)
- Professional credibility with subtle brand integration
- Cleaner typography (IBM Plex Sans, Inter Tight)
- Emphasis on reproducibility and clarity
- Appropriate formality for academic contexts

### Trading Systems (Kymera Systems LLC)
- High data density, dashboard-focused layouts
- Dominant monospace typography
- Real-time aesthetic with atmospheric effects
- Technical indicators and market conventions

## Troubleshooting

**Issue:** Claude isn't applying kymera-brand automatically
- **Solution:** Explicitly mention "kymera-brand" or "Jarvis aesthetic" in your prompt

**Issue:** Output seems too similar across different artifacts
- **Solution:** The skill encourages variation—specify unique requirements for each use case

**Issue:** Academic artifacts feel too informal/technical
- **Solution:** Specify "academic context" or "Clarkson University presentation" to trigger appropriate adaptations

**Issue:** Colors seem washed out or unclear
- **Solution:** Verify you're requesting dark theme; light themes reduce brand impact

## Customization

This skill is designed to be flexible. You can:

1. **Override specific elements:** Request different color palettes while maintaining structure
2. **Blend with other skills:** Combine with document-specific skills (pptx, xlsx, etc.)
3. **Specify constraints:** Request reduced motion, increased contrast, or specific accessibility requirements

## Examples Gallery

See the skill in action across different artifact types:

**React Dashboard:** Momentum trading terminal with real-time SABR20 scoring
**PowerPoint:** XAI research presentation with technical diagrams
**Excel:** Trading journal with conditional formatting and analytics
**Word Doc:** Technical specification with code blocks and diagrams
**PDF:** Investment thesis with data visualization

## Contributing

As you use this skill, note which patterns work exceptionally well and which need refinement. The skill can evolve based on actual usage patterns and emerging aesthetic preferences.

## Version

Current Version: 1.0.0  
Created: November 2025  
Context: Dual-purpose design system for academic AI research and algorithmic trading applications

---

**Remember:** This skill doesn't just change colors—it transforms the entire aesthetic philosophy from generic AI outputs to intentional, technically sophisticated designs that reflect systematic thinking and engineering precision.
