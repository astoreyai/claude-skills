#!/bin/bash

# Kymera Brand Skill Installation Script
# This script sets up the kymera-brand skill in your Claude skills directory

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  KYMERA BRAND SKILL INSTALLER"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Determine the skills directory
SKILLS_BASE="/mnt/skills"
USER_SKILLS_DIR="${SKILLS_BASE}/user"
SKILL_NAME="kymera-brand"
SKILL_DIR="${USER_SKILLS_DIR}/${SKILL_NAME}"

echo "📋 Installation Configuration:"
echo "   Skills base directory: ${SKILLS_BASE}"
echo "   User skills directory: ${USER_SKILLS_DIR}"
echo "   Target skill directory: ${SKILL_DIR}"
echo ""

# Check if we're in a Claude environment
if [ ! -d "$SKILLS_BASE" ]; then
    echo "⚠️  Warning: Skills directory not found at ${SKILLS_BASE}"
    echo "   This script should be run in a Claude environment with skills support."
    echo ""
    echo "   Alternative installation methods:"
    echo "   1. Manually copy SKILL.md to ${USER_SKILLS_DIR}/${SKILL_NAME}/"
    echo "   2. Upload SKILL.md to a Claude Project knowledge base"
    echo "   3. Reference the skill file directly in prompts"
    echo ""
    exit 1
fi

# Check if user skills directory exists
if [ ! -d "$USER_SKILLS_DIR" ]; then
    echo "❌ Error: User skills directory not found: ${USER_SKILLS_DIR}"
    echo "   Please ensure your Claude environment has user skills support enabled."
    exit 1
fi

# Check if skill already exists
if [ -d "$SKILL_DIR" ]; then
    echo "⚠️  Skill directory already exists: ${SKILL_DIR}"
    read -p "   Do you want to overwrite it? (y/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Installation cancelled."
        exit 1
    fi
    echo "🗑️  Removing existing skill directory..."
    rm -rf "$SKILL_DIR"
fi

# Create skill directory
echo "📁 Creating skill directory..."
mkdir -p "$SKILL_DIR"

# Check if SKILL.md exists in current directory
if [ ! -f "SKILL.md" ]; then
    echo "❌ Error: SKILL.md not found in current directory"
    echo "   Please ensure SKILL.md is in the same directory as this script."
    exit 1
fi

# Copy SKILL.md to skill directory
echo "📝 Installing skill file..."
cp SKILL.md "$SKILL_DIR/"

# Copy README if it exists
if [ -f "README.md" ]; then
    echo "📄 Installing documentation..."
    cp README.md "$SKILL_DIR/"
fi

# Copy demo component if it exists
if [ -f "demo-component.jsx" ]; then
    echo "🎨 Installing demo component..."
    cp demo-component.jsx "$SKILL_DIR/"
fi

# Verify installation
if [ -f "${SKILL_DIR}/SKILL.md" ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ INSTALLATION SUCCESSFUL"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "📦 Skill installed at: ${SKILL_DIR}"
    echo ""
    echo "📚 Directory structure:"
    echo "   ${SKILL_DIR}/"
    echo "   ├── SKILL.md           (Core skill definition)"
    [ -f "${SKILL_DIR}/README.md" ] && echo "   ├── README.md          (Documentation)"
    [ -f "${SKILL_DIR}/demo-component.jsx" ] && echo "   └── demo-component.jsx (Example artifact)"
    echo ""
    echo "🚀 Usage:"
    echo "   The kymera-brand skill is now available in your Claude sessions."
    echo "   Claude will automatically apply it when relevant, or you can"
    echo "   explicitly request it:"
    echo ""
    echo "   Example prompts:"
    echo "   • 'Create a trading dashboard with kymera-brand aesthetic'"
    echo "   • 'Make a presentation using kymera-brand styling'"
    echo "   • 'Generate a report with the kymera design system'"
    echo ""
    echo "📖 For detailed usage instructions, see:"
    echo "   ${SKILL_DIR}/README.md"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
else
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "❌ INSTALLATION FAILED"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "The skill file was not successfully copied."
    echo "Please check file permissions and try again."
    exit 1
fi
