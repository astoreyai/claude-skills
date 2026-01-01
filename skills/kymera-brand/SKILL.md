---
name: kymera-brand
description: Kymera Systems brand design - Jarvis-inspired HUD aesthetic with dark and light modes. Use for branded UI, dashboards, presentations, and technical artifacts.
---

# Kymera Brand System

You are a systems designer creating interfaces for **Kymera Systems LLC** - a quantitative trading and AI research platform. Every artifact should feel like a sophisticated command interface from a near-future trading terminal.

## Design Philosophy

**Jarvis meets Bloomberg Terminal**: Clean, technical precision with atmospheric depth. Not generic corporate design—engineered excellence with character.

**Core Principles**:
1. **Data is the hero** - UI exists to present information clearly
2. **Layered depth** - Never flat; always atmospheric
3. **Technical sophistication** - Monospace for precision, display fonts for impact
4. **Intentional motion** - Every animation serves a purpose

## Color System

### Dark Mode (Primary)
```css
:root {
  /* Foundation */
  --ky-dark-deep: #0A0E1A;
  --ky-dark-surface: #121826;
  --ky-dark-elevated: #1A2332;
  --ky-dark-border: rgba(0, 217, 255, 0.15);

  /* Signature Cyan (Jarvis Blue) */
  --ky-cyan-primary: #00D9FF;
  --ky-cyan-glow: #00FFFF;
  --ky-cyan-dim: #0099AA;

  /* Status Colors */
  --ky-success: #00FF88;
  --ky-warning: #FFB800;
  --ky-critical: #FF3366;

  /* Text */
  --ky-text-primary: #FFFFFF;
  --ky-text-secondary: rgba(255, 255, 255, 0.7);
  --ky-text-muted: rgba(255, 255, 255, 0.4);

  /* Glow Effects */
  --ky-glow-cyan: 0 0 20px rgba(0, 217, 255, 0.3), 0 0 40px rgba(0, 217, 255, 0.15);
  --ky-glow-intense: 0 0 10px var(--ky-cyan-glow), 0 0 30px var(--ky-cyan-primary), 0 0 50px rgba(0, 217, 255, 0.5);
}
```

### Light Mode (Professional/Print)
```css
:root.light {
  /* Foundation */
  --ky-light-bg: #F8FAFC;
  --ky-light-surface: #FFFFFF;
  --ky-light-elevated: #F1F5F9;
  --ky-light-border: rgba(10, 14, 26, 0.1);

  /* Signature Blue (Deeper for contrast) */
  --ky-blue-primary: #0066CC;
  --ky-blue-dark: #004499;
  --ky-blue-light: #E6F2FF;

  /* Status Colors (Adjusted for light bg) */
  --ky-success: #059669;
  --ky-warning: #D97706;
  --ky-critical: #DC2626;

  /* Text */
  --ky-text-primary: #0A0E1A;
  --ky-text-secondary: rgba(10, 14, 26, 0.7);
  --ky-text-muted: rgba(10, 14, 26, 0.5);

  /* Subtle Accents (no glow on light) */
  --ky-accent-border: 2px solid var(--ky-blue-primary);
  --ky-accent-bg: var(--ky-blue-light);
}
```

## Typography

### Font Stack
```css
/* Technical/Data - Primary */
--ky-font-mono: 'JetBrains Mono', 'Fira Code', 'SF Mono', monospace;

/* Display/Headers */
--ky-font-display: 'Orbitron', 'Exo 2', 'Rajdhani', sans-serif;

/* Body (when mono inappropriate) */
--ky-font-body: 'Inter Tight', 'IBM Plex Sans', sans-serif;
```

### Usage Rules
| Context | Font | Weight | Style |
|---------|------|--------|-------|
| Hero titles | Display | 700-900 | Uppercase, wide tracking |
| Section headers | Display | 600-700 | Title case |
| Body text | Body/Mono | 400-500 | Normal |
| Data/numbers | Mono | 400-600 | Tabular figures |
| Code/technical | Mono | 400 | Normal |

## Component Patterns

### Dark Mode Card
```css
.ky-card {
  background: var(--ky-dark-surface);
  border: 1px solid var(--ky-dark-border);
  border-radius: 8px;
  box-shadow: var(--ky-glow-cyan);
  backdrop-filter: blur(10px);
}

.ky-card:hover {
  box-shadow: var(--ky-glow-intense);
  border-color: var(--ky-cyan-primary);
}
```

### Light Mode Card
```css
.ky-card-light {
  background: var(--ky-light-surface);
  border: 1px solid var(--ky-light-border);
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.ky-card-light:hover {
  border-color: var(--ky-blue-primary);
  box-shadow: 0 4px 12px rgba(0, 102, 204, 0.15);
}
```

### Navigation
```css
.ky-nav {
  background: rgba(10, 14, 26, 0.9);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--ky-dark-border);
}

.ky-nav-link {
  font-family: var(--ky-font-mono);
  font-size: 0.8125rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--ky-text-muted);
  transition: color 0.2s, text-shadow 0.2s;
}

.ky-nav-link:hover {
  color: var(--ky-cyan-primary);
  text-shadow: 0 0 10px var(--ky-cyan-glow);
}
```

### Buttons
```css
/* Primary - Glowing */
.ky-btn-primary {
  background: var(--ky-cyan-primary);
  color: var(--ky-dark-deep);
  font-family: var(--ky-font-mono);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.75rem 1.5rem;
  border: none;
  box-shadow: var(--ky-glow-cyan);
  transition: all 0.3s ease;
}

.ky-btn-primary:hover {
  box-shadow: var(--ky-glow-intense);
  transform: translateY(-2px);
}

/* Ghost */
.ky-btn-ghost {
  background: transparent;
  color: var(--ky-cyan-primary);
  border: 1px solid var(--ky-cyan-dim);
}

.ky-btn-ghost:hover {
  background: rgba(0, 217, 255, 0.1);
  border-color: var(--ky-cyan-primary);
}
```

## Background Treatments

### Dark Mode - Layered Atmosphere
```css
.ky-bg-dark {
  background:
    radial-gradient(circle at 20% 30%, rgba(0, 217, 255, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(0, 255, 136, 0.05) 0%, transparent 50%),
    linear-gradient(180deg, var(--ky-dark-deep) 0%, var(--ky-dark-surface) 100%);
}

/* Grid overlay */
.ky-grid-overlay {
  background-image:
    linear-gradient(rgba(0, 217, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 217, 255, 0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

### Light Mode - Clean Professional
```css
.ky-bg-light {
  background:
    linear-gradient(180deg, var(--ky-light-bg) 0%, var(--ky-light-elevated) 100%);
}

/* Subtle pattern */
.ky-pattern-light {
  background-image:
    radial-gradient(circle at 50% 50%, rgba(0, 102, 204, 0.03) 1px, transparent 1px);
  background-size: 24px 24px;
}
```

## Animation

### Core Timing Functions
```css
/* Smooth technical */
--ky-ease-smooth: cubic-bezier(0.4, 0.0, 0.2, 1);
/* Quick snap */
--ky-ease-snap: cubic-bezier(0.0, 0.0, 0.2, 1);
/* Cinematic */
--ky-ease-cinematic: cubic-bezier(0.65, 0.0, 0.35, 1);
```

### Signature Animations
```css
/* Scan line effect */
@keyframes ky-scan {
  0% { transform: translateY(-100%); opacity: 0.5; }
  100% { transform: translateY(100vh); opacity: 0; }
}

/* Glow pulse */
@keyframes ky-glow-pulse {
  0%, 100% { box-shadow: var(--ky-glow-cyan); }
  50% { box-shadow: var(--ky-glow-intense); }
}

/* Data fade in */
@keyframes ky-fade-in {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

## Context Guidelines

### Trading Dashboards
- Monospace for ALL numeric data
- High data density, clear hierarchy
- Real-time indicators with pulse animations
- Market colors: green=bullish, red=bearish (alongside brand cyan)
- Status indicators prominent

### Academic/Research
- Cleaner typography (IBM Plex Sans for body)
- Light mode acceptable for papers/print
- Cyan accents subtly integrated
- Diagrams with geometric precision
- Professional but distinctive

### Presentations
- Dark backgrounds with geometric accents
- Minimal text per slide
- Display fonts for titles
- Cyan highlighting for emphasis
- Grid/circuit patterns in backgrounds

## Implementation Checklist

**Every artifact must have:**
- [ ] CSS custom properties for colors
- [ ] Proper font imports (Google Fonts)
- [ ] Dark mode as default (light mode as option)
- [ ] Cyan used as signature accent
- [ ] Background depth (gradients/patterns)
- [ ] Hover states with glow effects
- [ ] Responsive design
- [ ] WCAG AA contrast minimum
- [ ] Monospace for data/code
- [ ] Smooth transitions (0.2-0.3s)

## Anti-Patterns

**NEVER:**
- Generic blue gradients on white
- System fonts (Arial, Times, Calibri)
- Flat, lifeless backgrounds
- Overuse cyan to visual fatigue
- Animations that distract from data
- Inconsistent spacing/alignment

**ALWAYS:**
- Think like designing a command interface
- Create depth through layering
- Make data the hero
- Ensure technical precision
- Respect accessibility standards
