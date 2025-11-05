# Task Creation Patterns

## Task Note Structure

Standard structure for task notes in Obsidian.

### Basic Task Template

```markdown
---
type: task
plan: "[[plans/PLAN-NAME]]"
spec: "[[specs/SPEC-NAME]]"
status: todo
priority: high|medium|low
estimate: 2d
assignee: "[[people/PERSON-NAME]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
due: YYYY-MM-DD
tags:
  - task
  - COMPONENT-NAME
  - PROJECT-NAME
---

# Task: [Task Title]

## Context

Brief description of why this task exists and what problem it solves.

Part of: [[plans/PLAN-NAME]]
Related to: [[specs/SPEC-NAME]]

## Objective

Clear statement of what will be accomplished when this task is complete.

## Acceptance Criteria

- [ ] Criterion 1: Specific, testable condition
- [ ] Criterion 2: Another specific condition
- [ ] Criterion 3: Final verification step

## Technical Approach

### Implementation Steps

1. Step 1: What to do first
2. Step 2: What to do next
3. Step 3: Final implementation step

### Code Changes

**Files to modify:**
- `src/path/to/file1.js` - What changes
- `src/path/to/file2.js` - What changes

**New files:**
- `src/path/to/newfile.js` - Purpose

### Testing Strategy

- Unit tests: [describe]
- Integration tests: [describe]
- Manual testing: [steps]

## Dependencies

**Depends on:**
- [ ] [[tasks/prerequisite-task-1]]
- [ ] External: API key from service X

**Blocks:**
- [[tasks/downstream-task-1]]
- [[tasks/downstream-task-2]]

## Resources

- API Documentation: [link]
- Design mockup: [[designs/feature-design]]
- Similar implementation: [[tasks/reference-task]]

## Progress Log

### YYYY-MM-DD HH:MM
- Started implementation
- Approach: [brief description]

### YYYY-MM-DD HH:MM
- ✅ Completed acceptance criterion 1
- 🔄 Working on acceptance criterion 2
- 📝 Note: [observations or decisions]

### YYYY-MM-DD HH:MM
- 🚧 Blocker: [description]
- 💡 Potential solution: [idea]

### YYYY-MM-DD HH:MM
- ✅ Task complete
- 🔗 Pull Request: [link]
- 📋 Testing results: All tests passing

## Notes

Additional context, decisions made, lessons learned.

```

## Status Values

Use consistent status values in frontmatter:

- `todo`: Not yet started
- `in-progress`: Currently working on it
- `blocked`: Cannot proceed due to dependency
- `review`: Code review or testing
- `done`: Completed and verified

## Priority Levels

- `high`: Critical path, must complete for milestone
- `medium`: Important but not blocking
- `low`: Nice to have, can defer

## Estimate Format

Use consistent time estimates:
- `1h`, `2h`: Hours for small tasks
- `1d`, `2d`: Days for medium tasks
- `1w`, `2w`: Weeks for large tasks (consider breaking down)

## Task Breakdown Patterns

### By Component

**Database Task:**
```yaml
---
type: task
component: database
tags: [task, database, schema]
---
```

**API Task:**
```yaml
---
type: task
component: api
tags: [task, api, backend]
---
```

**Frontend Task:**
```yaml
---
type: task
component: frontend
tags: [task, ui, react]
---
```

### By Type

**Feature Implementation:**
```yaml
---
type: task
task-type: feature
tags: [task, feature, new-functionality]
---
```

**Bug Fix:**
```yaml
---
type: task
task-type: bug
bug-severity: critical|high|medium|low
tags: [task, bug, bugfix]
---
```

**Technical Debt:**
```yaml
---
type: task
task-type: tech-debt
tags: [task, refactoring, tech-debt]
---
```

**Testing:**
```yaml
---
type: task
task-type: testing
test-type: unit|integration|e2e
tags: [task, testing]
---
```

## Subtask Pattern

For complex tasks, create subtasks:

**Parent Task:**
```markdown
## Subtasks
- [ ] [[tasks/subtask-1-setup]]
- [ ] [[tasks/subtask-2-implementation]]
- [ ] [[tasks/subtask-3-testing]]
```

**Child Task:**
```yaml
---
parent-task: "[[tasks/parent-task-name]]"
---
```

## Task Linking Examples

**From Task to Related Tasks:**
```markdown
## Related Tasks
- Depends on: [[tasks/prerequisite]]
- Blocks: [[tasks/downstream]]
- Similar to: [[tasks/reference]]
```

**From Plan to Tasks:**
```markdown
### Phase 1 Tasks
- [ ] [[tasks/task-1-name]]
- [ ] [[tasks/task-2-name]]
```

**From Task to Plan:**
```markdown
## Part of Implementation
This task is part of [[plans/feature-implementation]]
```

## Progress Tracking in Tasks

### Simple Progress
```markdown
## Progress
- [x] Step 1
- [x] Step 2
- [ ] Step 3
```

### Detailed Progress Log
```markdown
## Progress Log

### 2025-10-20 09:00
Status: Started
- Created basic structure
- Set up test framework

### 2025-10-20 14:30
Status: In Progress (50%)
- ✅ Implemented core logic
- ✅ Added error handling
- 🔄 Writing tests
- ⏭️ Next: Integration testing

### 2025-10-21 16:00
Status: Complete
- ✅ All tests passing
- ✅ Code reviewed
- 🔗 PR: #123
```

## Task Size Guidelines

**Small Task** (1-4 hours):
- Single function or component
- Isolated change
- Minimal dependencies

**Medium Task** (1-2 days):
- Multiple related changes
- Some integration work
- Limited dependencies

**Large Task** (3-5 days):
- Multiple components
- Complex integration
- Consider breaking down further

**Too Large** (>5 days):
- Break into multiple tasks
- Create subtasks
- Define clear milestones

## Common Task Templates

### API Endpoint Task
```markdown
---
type: task
component: api
endpoint: /api/v1/resource
method: GET|POST|PUT|DELETE
---

# Implement [METHOD] /api/v1/resource

## Endpoint Specification
- Method: [GET/POST/PUT/DELETE]
- Path: `/api/v1/resource`
- Auth: Required/Optional
- Rate limit: X requests/hour

## Request Schema
[Describe or link to schema]

## Response Schema
[Describe or link to schema]

## Implementation
[Steps]

## Tests
- [ ] Success case
- [ ] Error cases
- [ ] Edge cases
- [ ] Auth validation
```

### UI Component Task
```markdown
---
type: task
component: frontend
ui-type: component
---

# Create [ComponentName] Component

## Component Purpose
What this component does and why.

## Props Interface
[Describe component props]

## Visual Design
Reference: [[designs/component-mockup]]

## Behavior
- User interaction patterns
- State management
- Side effects

## Acceptance Criteria
- [ ] Matches design mockup
- [ ] Responsive on mobile
- [ ] Accessible (WCAG 2.1 AA)
- [ ] Tests passing

## Implementation
[Steps]
```

### Database Migration Task
```markdown
---
type: task
component: database
migration-type: schema|data
---

# Database Migration: [Description]

## Migration Type
Schema change / Data migration

## Changes
- Tables affected
- Columns added/modified/removed
- Indexes added/removed

## Up Migration
```sql
-- SQL for forward migration
```

## Down Migration
```sql
-- SQL for rollback
```

## Data Impact
- Estimated rows affected
- Downtime required: Yes/No
- Backup strategy

## Testing
- [ ] Test on local database
- [ ] Test on staging database
- [ ] Verify rollback works
- [ ] Document any manual steps
```

## Dataview Queries for Tasks

### Tasks by Status
```dataview
TABLE status, priority, estimate, assignee
FROM "tasks"
WHERE type = "task"
GROUP BY status
SORT priority DESC
```

### My Active Tasks
```dataview
TASK
FROM "tasks"
WHERE assignee = [[people/my-name]]
AND status IN ["todo", "in-progress"]
SORT priority DESC, due ASC
```

### Blocked Tasks
```dataview
TABLE plan, priority, updated
FROM "tasks"
WHERE status = "blocked"
SORT updated DESC
```
