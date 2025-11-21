# Implementation Plan Template

## Standard Implementation Plan Structure

Use this template when creating implementation plan notes in Obsidian.

```markdown
---
type: implementation-plan
spec: "[[specs/SPEC-NAME]]"
status: planning
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: "[[people/OWNER-NAME]]"
priority: high|medium|low
estimated-duration: Xw
tags:
  - plan
  - implementation
  - PROJECT-NAME
---

# Implementation Plan: [Feature Name]

## Overview

Brief description of what will be implemented and why.

## Related Specification

- Spec: [[specs/SPEC-NAME]]
- Created: YYYY-MM-DD
- Last Updated: YYYY-MM-DD

## Requirements Summary

### Functional Requirements
- User story or feature 1
- User story or feature 2
- Integration requirements

### Non-Functional Requirements
- Performance: [targets]
- Security: [requirements]
- Scalability: [needs]

### Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Technical Approach

### Architecture
High-level architecture description or diagram reference.

### Technology Stack
- Frontend: [technologies]
- Backend: [technologies]
- Database: [technologies]
- Infrastructure: [technologies]

### Design Decisions
Key technical decisions and their rationale.

## Implementation Phases

### Phase 1: Foundation (Week 1)
**Goal**: Set up infrastructure and core architecture

**Tasks**:
- [ ] [[tasks/setup-database-schema]]
- [ ] [[tasks/create-base-api-structure]]
- [ ] [[tasks/setup-authentication]]

**Estimated Effort**: 3-5 days
**Status**: 🔵 Not Started

### Phase 2: Core Features (Weeks 2-3)
**Goal**: Implement primary functionality

**Tasks**:
- [ ] [[tasks/implement-api-endpoints]]
- [ ] [[tasks/create-frontend-components]]
- [ ] [[tasks/integrate-external-api]]

**Estimated Effort**: 7-10 days
**Status**: 🔵 Not Started

### Phase 3: Enhancement & Testing (Week 4)
**Goal**: Polish features and ensure quality

**Tasks**:
- [ ] [[tasks/add-validation-logic]]
- [ ] [[tasks/write-unit-tests]]
- [ ] [[tasks/write-integration-tests]]
- [ ] [[tasks/perform-security-review]]

**Estimated Effort**: 5-7 days
**Status**: 🔵 Not Started

### Phase 4: Deployment & Documentation (Week 5)
**Goal**: Deploy to production and document

**Tasks**:
- [ ] [[tasks/create-deployment-script]]
- [ ] [[tasks/write-user-documentation]]
- [ ] [[tasks/write-technical-documentation]]
- [ ] [[tasks/deploy-to-production]]

**Estimated Effort**: 3-5 days
**Status**: 🔵 Not Started

## Dependencies

### External Dependencies
- **Service Name**: What it provides, why needed
- **API Access**: Credentials needed by [date]

### Internal Dependencies
- **Feature/Component**: What it provides, current status
- **Team/Person**: What they're delivering, timeline

### Blockers
- [ ] No active blockers
- [ ] Blocker: Description and mitigation plan

## Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| External API changes | High | Medium | Version locking, monitoring |
| Database migration complexity | Medium | High | Staging tests, rollback plan |
| Performance issues at scale | High | Low | Load testing, caching strategy |

## Timeline

**Start Date**: YYYY-MM-DD
**Target Completion**: YYYY-MM-DD
**Current Status**: On Track | At Risk | Delayed

### Milestones
- [ ] **M1**: Foundation Complete (Week 1) - YYYY-MM-DD
- [ ] **M2**: Core Features Complete (Week 3) - YYYY-MM-DD
- [ ] **M3**: Testing Complete (Week 4) - YYYY-MM-DD
- [ ] **M4**: Production Deployment (Week 5) - YYYY-MM-DD

## Success Criteria

- [ ] All acceptance criteria met
- [ ] Performance benchmarks achieved
- [ ] Security review passed
- [ ] Documentation complete
- [ ] Production deployment successful
- [ ] No critical bugs in first week

## Progress Updates

### YYYY-MM-DD - Week 1
- **Completed**: 
- **In Progress**: 
- **Blockers**: 
- **Next Week**: 

### YYYY-MM-DD - Week 2
[Updates continue...]

## Related Notes

- Project: [[projects/PROJECT-NAME]]
- Epic: [[epics/EPIC-NAME]]
- Architecture: [[architecture/ARCHITECTURE-DOC]]
- Decision Log: [[decisions/DECISION-NAME]]

## Backlinks

This section will automatically populate with Obsidian backlinks.
```

## Status Indicators

Use consistent status indicators in Phase headings:

- 🔵 Not Started
- 🟡 In Progress (with %)
- 🟢 Complete
- 🔴 Blocked
- ⚠️ At Risk

## Progress Percentage Format

Update phase progress as work progresses:

```markdown
### Phase 2: Core Features (Weeks 2-3) - 🟡 In Progress (60%)
```

## Quick Implementation Plan

For smaller features or rapid prototyping, use abbreviated version:

```markdown
---
type: implementation-plan
spec: "[[specs/SPEC-NAME]]"
status: planning
priority: high
tags: [plan, quick-implementation]
---

# Quick Implementation: [Feature Name]

## Goal
What we're building and why.

## Approach
How we'll build it.

## Tasks
- [ ] [[tasks/task-1]]
- [ ] [[tasks/task-2]]
- [ ] [[tasks/task-3]]

## Timeline
Start: YYYY-MM-DD | Complete: YYYY-MM-DD

## Success
- Done when: [criteria]
```

## Linking Best Practices

**From Spec to Plan:**
```markdown
## Implementation
See [[plans/feature-name-implementation]] for detailed plan.
```

**From Plan to Spec:**
```markdown
## Related Specification
Implementing [[specs/feature-name]]
```

**From Plan to Tasks:**
```markdown
- [ ] [[tasks/implement-api-endpoint]]
```

**From Tasks to Plan:**
```markdown
## Part Of
[[plans/feature-name-implementation]]
```
