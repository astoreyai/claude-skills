# Changelog - Scientific Paper Reviewer Skill

## [2.0.0] - October 2025

### Major Features Added
- **IEEE Review Pathway**: Complete workflow for IEEE journal/conference submissions
  - IEEE-specific technical assessment component
  - IEEE significance and originality evaluation
  - IEEE clarity and presentation assessment
  - IEEE decision recommendation with decision tree logic
  - IEEE review synthesis template
  
- **Intelligent Venue Detection**: Automatic routing system
  - Priority-based detection algorithm
  - Template marker identification
  - User confirmation protocols
  - High-confidence routing without delays

- **Decision Tree Frameworks**: Clear logic for both venues
  - NeurIPS 1-6 scoring with calibration guidance
  - IEEE 3-tier decision system (Accept/Revise/Reject)
  - Major vs Minor revision distinction
  - Comprehensive decision justification templates

- **Shared Components Library**: Universal evaluation tools
  - Venue detector for intelligent routing
  - Paper classifier for all submission types
  - Ethics screener with universal principles

### Architecture Improvements
- **Modular Design**: Separated venue-specific from universal components
- **Clear Hierarchy**: Orchestrator SKILL.md routes to appropriate pathways
- **Component Isolation**: Each evaluation stage is self-contained
- **Template Standardization**: Consistent review assembly process

### Documentation Enhancements
- **Comprehensive README**: Quick start guide, troubleshooting, best practices
- **Decision Matrices**: Visual comparison of venue requirements
- **Detailed Components**: Each component has complete evaluation protocols
- **Reference Materials**: Official guidelines for both venues

### IEEE-Specific Additions
- **Reviewer Guidelines**: Based on IEEE Author Center documentation
- **Decision Process Guide**: Understanding IEEE accept/revise/reject decisions
- **Ethics Framework**: IEEE-specific misconduct identification
- **Major vs Minor Revision Logic**: Clear criteria for revision levels

### NeurIPS Enhancements
- **Preserved Components**: All v1.0 NeurIPS components retained
- **Updated References**: 2025 guidelines incorporated
- **Enhanced Integration**: Better connection to shared components

### New Files
```
components/shared/venue-detector.md
components/ieee/technical-assessment.md
components/ieee/significance-assessment.md
components/ieee/clarity-assessment.md
components/ieee/decision-recommendation.md
templates/ieee/review-synthesis.md
reference/ieee/reviewer-guidelines.md
reference/ieee/decision-process.md
reference/ieee/ethics-framework.md
```

### Breaking Changes
- **Directory Structure**: Reorganized to accommodate multiple venues
- **SKILL.md**: Complete rewrite with venue routing
- **Component Paths**: All components moved to venue-specific folders

### Migration Guide (v1.0 → v2.0)
1. **For NeurIPS reviews**: Update component paths from `components/` to `components/neurips/`
2. **Venue detection**: Now required first step before review
3. **Shared components**: Ethics and classification moved to `components/shared/`

## [1.0.0] - Initial Release

### Initial Features
- NeurIPS-specific review workflow
- Technical assessment component
- Contribution assessment component
- Clarity assessment component
- Ethics screening component
- Checklist processing component
- Review synthesis templates
- Scoring calibration guidance
- NeurIPS reference materials

### Initial Documentation
- SKILL.md orchestrator
- Component documentation
- NeurIPS 2025 guidelines
- Code of ethics
- Review best practices

---

## Upcoming Features (Planned)

### Potential v2.1 Features
- Additional venue support (ICML, CVPR, AAAI)
- Resubmission detection and handling
- Meta-review synthesis tools
- Area chair decision support
- Workshop paper adaptations

### Potential v3.0 Features
- ACL/EMNLP pathway (NLP venues)
- Computer vision venue support (CVPR, ICCV, ECCV)
- Robotics venue support (ICRA, IROS)
- Cross-venue comparison tools
- Historical review quality analysis

---

## Version Numbering

Format: MAJOR.MINOR.PATCH

- **MAJOR**: New venue support, breaking changes
- **MINOR**: New features, non-breaking enhancements
- **PATCH**: Bug fixes, documentation updates

---

## Contribution Guidelines

To suggest new venues or features:
1. Identify venue guidelines and requirements
2. Map to existing component structure
3. Define venue-specific decision criteria
4. Create templates following established patterns
5. Document clearly with examples

---

## Maintenance Notes

### Review Frequency
- **Annual**: Update for new NeurIPS/IEEE guidelines
- **As needed**: Bug fixes, clarifications
- **Quarterly**: Documentation improvements

### Deprecation Policy
- Old venue guidelines kept for reference
- Major version indicates breaking changes
- Migration guides provided for significant changes

---

## Credits

**Development**: Synthesized from official guidelines and best practices
**Sources**: 
- NeurIPS Conference review guidelines
- IEEE Author Center reviewer resources  
- Academic peer review standards
- Community feedback

**Maintainers**: Peer Review Standards Committee
**Last Updated**: October 2025
**Next Review**: After NeurIPS 2026 / IEEE 2026 guideline updates
