# Kymera Brand System

**When to use this skill:** Apply when generating any branded artifacts for Kymera Systems LLC or when user requests Jarvis-inspired, technical, or futuristic design aesthetics.

## Core Design Philosophy

The Kymera brand draws from holographic interface paradigms—think technical command centers, heads-up displays, and sophisticated trading terminals. This is not generic corporate design; it's engineered precision with atmospheric depth.

Avoid: Flat, minimalist aesthetics. Corporate blues and grays. Generic SaaS layouts. Safe, "on-distribution" design that lacks character.

Embrace: Layered depth. Luminescent elements. Geometric precision. Technical sophistication. Atmospheric effects that suggest advanced systems operating beneath the surface.

## Color System

### Primary Palette
```
--kymera-cyan-primary: #00D9FF     /* Holographic accent, interactive elements */
--kymera-cyan-glow: #00FFFF        /* Bright highlights, active states */
--kymera-cyan-dim: #0099AA          /* Secondary elements, borders */

--kymera-dark-deep: #0A0E1A         /* Background foundation */
--kymera-dark-surface: #121826      /* Card backgrounds, surfaces */
--kymera-dark-elevated: #1A2332     /* Elevated UI elements */

--kymera-accent-electric: #00FF88   /* Success states, positive metrics */
--kymera-accent-warning: #FF8C00    /* Alerts, important data */
--kymera-accent-critical: #FF0066   /* Critical alerts, negative metrics */
```

### Extended Palette (context-specific)
```
/* Academic/Research Context */
--kymera-academic-blue: #0066CC     /* Professional presentations */
--kymera-academic-silver: #C0C8D0   /* Text on dark backgrounds */

/* Trading Systems Context */
--kymera-market-green: #00FF88      /* Buy signals, gains */
--kymera-market-red: #FF3366        /* Sell signals, losses */
--kymera-market-neutral: #FFB800    /* Neutral/hold signals */
```

### Usage Principles
- **Dominant dark**: Always anchor with dark foundations (--kymera-dark-deep or --kymera-dark-surface)
- **Cyan as signature**: Use cyan variants as the primary brand identifier—sparingly for maximum impact
- **High contrast**: Text should achieve WCAG AAA when possible. Use --kymera-cyan-glow at 0.8+ opacity on dark backgrounds
- **Glow effects**: Apply subtle box-shadow or text-shadow with cyan to create holographic luminescence
- **Atmospheric gradients**: Layer multiple gradients rather than solid fills

## Typography

### Font Families
```
/* Primary: Technical precision */
font-family: 'JetBrains Mono', 'Fira Code', 'Space Mono', monospace;

/* Display: Bold statements, headers */
font-family: 'Orbitron', 'Exo 2', 'Rajdhani', sans-serif;

/* Body (when monospace inappropriate): Clean readability */
font-family: 'Inter Tight', 'IBM Plex Sans', 'Space Grotesk', sans-serif;
```

### Hierarchy Guidelines
- **Hero/Display**: 700-900 weight, large tracking (0.05-0.1em), uppercase transforms for impact
- **Headings**: 600-700 weight, moderate tracking, sentence case or title case
- **Body**: 400-500 weight, comfortable line height (1.6-1.8), slightly increased letter-spacing on dark backgrounds
- **Code/Data**: Monospace exclusively, 400 weight, tabular figures when available

### Context-Specific Typography
- **Academic artifacts** (presentations, papers): Use cleaner sans-serif hierarchies (IBM Plex Sans, Inter Tight) with monospace for code blocks
- **Trading dashboards**: Monospace for all numeric data, display fonts for titles
- **Technical documentation**: Monospace primary, with clear heading hierarchy

## Motion & Interaction

### Animation Principles
Interfaces should feel responsive and alive, not static. Motion suggests sophisticated systems processing data in real-time.

```css
/* Smooth, technical precision */
transition: all 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);

/* Quick, snappy responses */
transition: all 0.15s ease-out;

/* Cinematic, important transitions */
transition: all 0.6s cubic-bezier(0.65, 0.0, 0.35, 1);
```

### Key Patterns
- **Glow on hover**: Intensify box-shadow cyan glow on interactive elements
- **Subtle scan lines**: Animated horizontal gradients suggesting data processing
- **Particle effects**: For significant actions, brief particle bursts (CSS or canvas)
- **Staggered reveals**: Page load animations with 50-100ms delays between elements
- **Data transitions**: Smooth number counting, chart animations that build progressively

## Background Treatments

Never use flat solid colors. Create atmospheric depth:

### Layered Gradients
```css
background: 
  radial-gradient(circle at 20% 50%, rgba(0, 217, 255, 0.1) 0%, transparent 50%),
  radial-gradient(circle at 80% 20%, rgba(0, 255, 136, 0.08) 0%, transparent 50%),
  linear-gradient(180deg, #0A0E1A 0%, #121826 100%);
```

### Geometric Patterns
- **Grid overlays**: Subtle 1px grids suggesting technical schematics
- **Hexagonal patterns**: For academic/research contexts
- **Circuit-like pathways**: Connecting elements visually

### Dynamic Elements
- **Subtle noise textures**: Add grain to prevent flat appearance
- **Animated scan lines**: Horizontal gradients moving slowly across background
- **Glow spots**: Soft radial gradients that pulse slowly (2-4s animations)

## Artifact-Specific Guidance

### HTML/React Artifacts
- Use CSS custom properties for all color values
- Implement dark theme exclusively unless specifically requested otherwise
- Add subtle animations to all interactive elements
- Create depth with layered cards, shadows, and overlays
- For dashboards: prioritize data density without sacrificing readability

### PowerPoint Presentations
- **Dark backgrounds** with geometric accents
- **Cyan highlighting** for emphasis, not decoration
- **Monospace fonts** for data, display fonts for titles
- **Minimal text per slide**: Let visuals communicate
- **Technical diagrams**: Use geometric shapes, connecting lines, glow effects
- Include subtle grid or circuit patterns in slide backgrounds

### Word Documents & Reports
- **Custom header/footer** with thin cyan accent lines
- **Monospace for code blocks** and technical specifications
- **Dark theme when appropriate** (technical reports), professional light theme for formal academic submissions
- **Generous margins** with technical margin notes capability
- **Data tables**: Alternating row shading with subtle cyan highlights

### PDF Documents
- Maintain high contrast for readability
- Use vector graphics and geometric elements
- Apply cyan accents to section dividers and callouts
- Include technical footer with document metadata in monospace

### Spreadsheets (XLSX)
- **Conditional formatting** using kymera color palette
- **Monospace fonts** for all numeric data
- **Dark header rows** with cyan text
- **Subtle gridlines** or remove entirely for cleaner appearance
- **Data visualization**: Charts using brand colors with glow effects where possible

### Markdown Documents
- Use code blocks liberally for technical precision
- Headers with subtle emoji/symbols that suggest technical systems (⚡ 🔷 ⚙️ 📊)
- Tables with alignment for data presentation
- Links styled distinctively in cyan

## Context Adaptation

### Academic Research (Clarkson University)
When generating academic content:
- Maintain professional credibility while incorporating brand elements subtly
- Use cleaner typography (IBM Plex Sans, Inter Tight)
- Cyan accents for university color integration (Clarkson green can be secondary)
- Emphasize clarity and reproducibility in data visualization
- Technical diagrams with geometric precision

### Trading Systems (Kymera Systems LLC)
When generating trading-related content:
- Prioritize data density and real-time dashboard aesthetics
- Monospace fonts dominate for numeric precision
- Market color conventions (green=bullish, red=bearish) alongside brand cyan
- Time-series charts with atmospheric backgrounds
- Technical indicators prominently displayed with clear visual hierarchy

## Implementation Checklist

Before finalizing any artifact, verify:
- [ ] Color variables defined and consistently applied
- [ ] Typography hierarchy clear and intentional
- [ ] Dark theme implemented (unless explicitly inappropriate)
- [ ] Cyan used as signature accent, not overwhelmingly
- [ ] Backgrounds have depth (gradients, patterns, or effects)
- [ ] Interactive elements have hover states with glow
- [ ] Motion feels intentional and technical, not gratuitous
- [ ] Contrast ratios meet accessibility standards
- [ ] Monospace used for all data, code, and numeric values

## Anti-Patterns to Avoid

**Never:**
- Use generic blue gradients on white backgrounds
- Default to system fonts (Arial, Times New Roman, Calibri)
- Create flat, lifeless interfaces
- Overuse cyan to the point of visual fatigue
- Sacrifice readability for aesthetic effect
- Implement animations that distract from content
- Use inconsistent spacing or alignment
- Mix too many unrelated typefaces

**Always:**
- Think like a systems engineer designing a command interface
- Create depth through layering and subtle effects
- Make data the hero, not decoration
- Ensure every design choice serves functional clarity
- Maintain technical precision in all visual elements

## Creative Variation

While this skill provides strong direction, avoid convergence to identical outputs. Vary:
- Exact gradient compositions and angles
- Geometric pattern implementations
- Animation timing and easing functions
- Relative proportions of cyan vs. other accent colors
- Background complexity based on content density

Each artifact should feel part of the Kymera brand family while having its own identity appropriate to its specific purpose and context.
