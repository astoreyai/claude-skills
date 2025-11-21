# Kymera Brand Skill - Quick Start Guide

## 📦 Package Contents

Your kymera-brand skill package includes:

```
kymera-brand-skill/
├── SKILL.md              Core skill definition with design system
├── README.md             Comprehensive documentation and usage guide
├── install.sh            Automated installation script
└── demo-component.jsx    React example showcasing the aesthetic
```

## ⚡ Quick Installation

### Method 1: Automated Installation (Recommended)
```bash
# Navigate to the directory containing the skill files
cd /path/to/kymera-brand-skill

# Run the installation script
./install.sh
```

The script will:
- Detect your Claude skills directory
- Create the skill folder structure
- Copy all necessary files
- Verify installation success

### Method 2: Manual Installation
```bash
# Create the skill directory
mkdir -p /mnt/skills/user/kymera-brand

# Copy the skill file
cp SKILL.md /mnt/skills/user/kymera-brand/

# Copy supporting documentation
cp README.md demo-component.jsx /mnt/skills/user/kymera-brand/
```

### Method 3: Project-Based Installation
If you're working within a Claude Project:
1. Upload `SKILL.md` to your project's knowledge base
2. Claude will automatically detect and use it
3. No file system access required

## 🎯 First Use

Once installed, try these example prompts:

### Example 1: Trading Dashboard
```
Create a React trading dashboard showing real-time momentum scores 
across multiple timeframes using kymera-brand design system.
```

### Example 2: Academic Presentation
```
Make a PowerPoint presentation about explainable AI in facial 
recognition with kymera-brand aesthetic for Clarkson University.
```

### Example 3: Technical Report
```
Generate a Word document template for AI research papers using 
kymera-brand styling with proper heading hierarchy and code blocks.
```

## 🎨 Design System Overview

### Core Aesthetic Principles

**Jarvis-Inspired Interface Design**
- Dark foundations with atmospheric depth
- Cyan luminescence as signature accent
- Geometric precision and technical sophistication
- Holographic HUD elements
- Real-time data visualization emphasis

### Color Palette Quick Reference

```css
/* Primary Colors */
--kymera-cyan-primary: #00D9FF    /* Main brand accent */
--kymera-cyan-glow: #00FFFF       /* Highlights & active states */
--kymera-dark-deep: #0A0E1A       /* Background foundation */
--kymera-dark-surface: #121826    /* Card/surface backgrounds */

/* Market Colors (Trading Context) */
--kymera-market-green: #00FF88    /* Bullish/gains */
--kymera-market-red: #FF3366      /* Bearish/losses */
--kymera-market-neutral: #FFB800  /* Neutral signals */
```

### Typography Hierarchy

```
Display Headers:    Orbitron, Exo 2, Rajdhani (700-900 weight)
Technical/Code:     JetBrains Mono, Fira Code, Space Mono
Body Text:          Inter Tight, IBM Plex Sans, Space Grotesk
```

## 📋 Supported Artifact Types

The kymera-brand skill works across all Claude artifact types:

- ✅ **HTML/React** - Interactive dashboards, landing pages, web apps
- ✅ **PowerPoint** - Technical presentations with dark themes
- ✅ **Word Documents** - Reports, papers, technical documentation
- ✅ **PDF** - Professional documents with brand styling
- ✅ **Excel Spreadsheets** - Data tables with conditional formatting
- ✅ **Markdown** - Technical documentation and README files

## 🔧 Customization Options

### Context-Specific Adaptations

The skill automatically adapts to context:

**Academic Context (Clarkson University)**
- Professional credibility maintained
- Cleaner typography choices
- Appropriate formality for academic settings
- Emphasis on clarity and reproducibility

**Trading Context (Kymera Systems LLC)**
- High data density layouts
- Monospace typography dominates
- Real-time dashboard aesthetics
- Market color conventions integrated

### Explicit Overrides

You can override specific elements while maintaining the brand:

```
Create a landing page with kymera-brand but use a light theme 
for maximum readability.
```

```
Generate a presentation with kymera aesthetic but use warmer 
orange accents instead of cyan.
```

## 🎓 Usage Patterns

### Automatic Activation
Claude automatically applies kymera-brand when detecting:
- "Kymera Systems" or "Kymera brand" mentions
- Jarvis/holographic/technical aesthetic requests
- Trading or financial systems contexts
- Aaron's research or business work

### Explicit Invocation
For guaranteed application, reference directly:
```
Use kymera-brand skill to create [artifact type]
```

### Combining with Other Skills
The skill works alongside other specialized skills:
```
Create a PowerPoint using both pptx skill and kymera-brand 
for optimal presentation quality.
```

## 🚨 Troubleshooting

### Skill Not Applying Automatically
**Solution:** Explicitly mention "kymera-brand" or "Jarvis aesthetic" in your prompt

### Academic Work Feels Too Casual
**Solution:** Specify "academic context" or mention Clarkson University

### Colors Appear Washed Out
**Solution:** Verify dark theme is being used; light themes reduce brand impact

### Similar Outputs Across Artifacts
**Solution:** Specify unique requirements for each use case; skill encourages variation

## 📊 Example Gallery

### Trading Dashboard
Demonstrates: Real-time data visualization, monospace typography, atmospheric effects, multi-timeframe analysis

### Research Presentation
Demonstrates: Academic professionalism, technical diagrams, clean hierarchy, geometric patterns

### Investment Report
Demonstrates: Professional document formatting, data tables, chart integration, executive summary style

### Technical Documentation
Demonstrates: Code block styling, clear heading hierarchy, technical precision, developer-friendly layout

## 🔄 Version History

**v1.0.0** (November 2025)
- Initial release
- Support for all major artifact types
- Dual-context adaptation (academic/trading)
- Comprehensive design system documentation
- Example components and templates

## 📚 Additional Resources

**Skill File:** `/mnt/skills/user/kymera-brand/SKILL.md`  
Full design system specification with implementation guidelines

**Documentation:** `/mnt/skills/user/kymera-brand/README.md`  
Comprehensive usage guide with examples and troubleshooting

**Demo Component:** `/mnt/skills/user/kymera-brand/demo-component.jsx`  
Reference implementation showing aesthetic in practice

## 💡 Pro Tips

1. **Start with explicit invocation** until you understand activation patterns
2. **Combine contexts** when appropriate: "trading presentation for academic conference"
3. **Reference the demo component** to see implementation patterns in action
4. **Specify artifact type** early in prompt for optimal results
5. **Use technical terminology** to trigger appropriate aesthetic choices
6. **Request variations** to avoid convergence on similar outputs

## 🤝 Getting Help

**For skill-specific questions:**
- Review the comprehensive README.md
- Examine the demo-component.jsx for implementation patterns
- Reference the SKILL.md for design system details

**For general Claude skills questions:**
- Visit https://docs.claude.com
- Check Claude support documentation
- Explore other example skills at https://github.com/anthropics/skills

## 🎯 Next Steps

1. ✅ Complete installation using preferred method
2. ✅ Try the example prompts above
3. ✅ Examine the demo component code
4. ✅ Create your first branded artifact
5. ✅ Experiment with context-specific adaptations
6. ✅ Explore combining with other skills

---

**Remember:** This skill transforms generic AI outputs into intentional, technically sophisticated designs that reflect systematic thinking and engineering precision. The Jarvis aesthetic isn't just about cyan colors—it's about creating interfaces that feel purposefully engineered rather than accidentally generated.

**Version:** 1.0.0  
**Created:** November 2025  
**Maintained by:** Aaron Wright, Kymera Systems LLC
