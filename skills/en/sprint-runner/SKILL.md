# Skill: Sprint Runner

Sprint execution for the Coordinator. This skill enables understanding the roadmap structure and executing sprints on user request.

---

## Roadmap Structure

When a project uses swarm orchestration, the roadmap follows this structure:

```
roadmap/
├── README.md           # Global plan tracking
├── SPRINTS.md          # Sprint index (optional)
├── plans/              # Individual plans
│   └── plan-XX-*.md
└── sprints/            # Sprint details (optional)
    └── sprint-XX-*.md
```

---

## User Commands

| Request | Action |
|---------|--------|
| "Run sprint N" | "Run sprint" workflow |
| "Do plan N" | Read `plans/plan-0N-*.md`, execute |
| "Sprint status" | Read `SPRINTS.md`, summarize |
| "Create a sprint" | "Sprint creation" workflow |
| "Plans in sprint N" | Read sprint, list plans |
| "Next step" | Analyze progress, propose |

---

## Workflow "Run sprint N"

1. **Read the sprint**
   ```
   Read sprints/sprint-0N-*.md
   Extract the list of referenced plans
   ```

2. **Ask the user**
   ```
   ask_user(
     title: "Sprint N - Plan Selection"
     question: "Which plans do you want to execute?"
     options: [list of plans from sprint]
   )
   ```

3. **Execute selected plans**
   - Follow standard Coordinator workflow
   - Invoke Executor for each plan
   - Consolidate reports

4. **Update after each merge**
   - Check off the plan in sprint checklist
   - Update status in README.md

5. **Check sprint completion**
   - If all plans done → propose moving to next sprint
   - If final sprint done → propose new cycle

---

## Workflow "Sprint creation"

If user asks to create a sprint:

```
ask_user(
  title: "Sprint Creation"
  question: "Do you want me to invoke Roadmapper to create this sprint?"
  options: ["Yes, invoke Roadmapper", "No, I'll do it myself"]
)
```

If yes:
1. Invoke `/roadmap` with the request context
2. Roadmapper creates `sprints/sprint-XX-*.md` file
3. Roadmapper updates `SPRINTS.md`

---

## Workflow "Sprint status"

1. Read `SPRINTS.md` for overview
2. Identify active sprint (first not completed)
3. Read the active sprint file
4. Calculate progress (X/Y plans done)
5. Present summary:

```
## Sprint Status

**Active sprint**: Sprint N - [Name]
**Progress**: X/Y plans done (Z%)

### Completed plans
- [x] Plan XX - [description]

### Remaining plans
- [ ] Plan YY - [description]

### Suggested next action
[Next plan to execute]
```

---

## After Execution

After each successful merge:

1. **Check off in sprint**
   - Open `sprints/sprint-XX-*.md`
   - Check `- [x] Plan YY` in checklist

2. **Update README.md**
   - Change plan status: "Pending" → "Done"
   - Add version if applicable

3. **Check the sprint**
   - If all plans checked → sprint complete
   - Update status in `SPRINTS.md`

4. **Propose next steps**
   ```
   ask_user(
     title: "Sprint N completed"
     question: "Move to Sprint N+1?"
     options: ["Yes", "No, take a break"]
   )
   ```

---

## Error Handling

### Plan not found

```
Plan XX doesn't exist in plans/.
Check the number or create the plan with /roadmap.
```

### Sprint not found

```
Sprint N doesn't exist in sprints/.
Available sprints: [list]
```

### Sprint without plans

```
Sprint N contains no plans.
Add plans with /roadmap.
```

---

## Best Practices

1. **One sprint at a time**: Complete current sprint before moving to next
2. **Plans in order**: Respect priorities P0 > P1 > P2
3. **Validation after each plan**: Don't chain without user validation
4. **Immediate updates**: Check off plans as soon as they're merged
5. **Clear communication**: Always inform user of sprint state
