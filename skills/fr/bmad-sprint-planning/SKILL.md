---
name: bmad-sprint-planning
description: Planification Sprint BMAD - Générer sprint-status.yaml depuis les fichiers epic pour l'exécution agile
---

# Skill BMAD - Sprint Planning

Ce skill guide la génération du sprint-status.yaml à partir des fichiers epic pour organiser l'exécution agile.

## Objectif

Créer un sprint-status.yaml qui orchestre les sprints, track les epics/stories et maintient l'alignement entre planification et exécution.

## Principes BMAD Sprint Planning

1. **Epics → Sprints** : Un epic = un ou plusieurs sprints
2. **Value-Based Prioritization** : Livre de la valeur business chaque sprint
3. **Story Readiness** : Toutes stories doivent être "developer-ready"
4. **Velocity Tracking** : Mesure et ajuste basé sur vélocité réelle

## Workflow Sprint Planning

### Phase 1 : Review Epics

**Analyse tous les epics** dans `_bmad-output/epics/` :

```
epics/
├── epic-1-user-auth.md      (13 pts, 3 stories)
├── epic-2-dashboard.md       (21 pts, 5 stories)
├── epic-3-notifications.md   (8 pts, 2 stories)
└── ...
```

**Pour chaque epic, extrait** :
- Epic ID et titre
- Nombre de stories
- Story points totaux
- Dépendances
- Business value

### Phase 2 : Définir la Vélocité

**Estime la vélocité d'équipe** :
- **1 dev solo** : 5-8 story points / semaine
- **2 devs** : 10-15 story points / semaine
- **Team (3-5)** : 20-30 story points / semaine

**Ajuste selon** :
- Complexité du projet
- Expérience de l'équipe
- Disponibilité (full-time vs part-time)

### Phase 3 : Créer les Sprints

**Assigne epics aux sprints** basé sur :
1. Business value (Must Have d'abord)
2. Dépendances techniques
3. Vélocité capacity

**Template Sprint** :
```yaml
sprint_1:
  name: "Foundation Sprint"
  duration: "2 weeks"
  capacity: 20 # story points
  goal: "Build authentication and core data models"
  epics:
    - epic-1-user-auth  # 13 pts
  stories:
    - epic-1-story-1-signup     # status: todo
    - epic-1-story-2-login      # status: todo
    - epic-1-story-3-reset-pwd  # status: todo
  status: "planned"  # planned | in_progress | completed
```

### Phase 4 : Générer sprint-status.yaml

**Structure complète** :

```yaml
project:
  name: "[Project Name from PRD]"
  start_date: "2025-01-06"
  current_sprint: 1
  total_sprints: 4
  
team:
  size: 1  # or 2, 3, etc.
  velocity: 8  # story points per sprint
  
sprints:
  sprint_1:
    name: "Foundation Sprint"
    duration: "2 weeks"
    start_date: "2025-01-06"
    end_date: "2025-01-20"
    capacity: 8
    goal: "User authentication and core infrastructure"
    epics:
      - epic-1-user-auth
    stories:
      - id: "epic-1.1"
        title: "Sign Up Form"
        points: 3
        status: "todo"  # todo | in_progress | done
        assignee: null
      - id: "epic-1.2"
        title: "Login Flow"
        points: 5
        status: "todo"
      - id: "epic-1.3"
        title: "Password Reset"
        points: 5
        status: "todo"
    actual_velocity: 0  # updated as stories complete
    status: "planned"
    
  sprint_2:
    name: "Core Features Sprint"
    duration: "2 weeks"
    start_date: "2025-01-21"
    end_date: "2025-02-04"
    capacity: 8
    goal: "Dashboard and user profile"
    epics:
      - epic-2-dashboard
    stories:
      - id: "epic-2.1"
        title: "Dashboard Layout"
        points: 3
        status: "todo"
      - id: "epic-2.2"
        title: "User Profile"
        points: 5
        status: "todo"
    status: "planned"
    
  sprint_3:
    name: "Enhancements Sprint"
    duration: "2 weeks"
    start_date: "2025-02-05"
    end_date: "2025-02-19"
    capacity: 8
    goal: "Notifications and settings"
    epics:
      - epic-3-notifications
    stories:
      - id: "epic-3.1"
        title: "Email Notifications"
        points: 5
        status: "todo"
      - id: "epic-3.2"
        title: "In-App Notifications"
        points: 3
        status: "todo"
    status: "planned"

backlog:
  epics:
    - epic-4-advanced-search  # postponed
    - epic-5-analytics        # postponed
```

### Phase 5 : Validation

**Vérifier** :
- [ ] Tous les epics sont assignés OU dans backlog
- [ ] Capacity de chaque sprint ≈ velocity
- [ ] Dépendances respectées (epic X avant epic Y)
- [ ] Business value décroissante (Must Have → Nice to Have)
- [ ] Sprint goals sont clairs

## Sprint Status Tracking

**Pendant l'exécution**, update le fichier :

```yaml
sprint_1:
  # ... config ...
  stories:
    - id: "epic-1.1"
      title: "Sign Up Form"
      points: 3
      status: "done"  # ✅ Completed!
      completed_date: "2025-01-10"
    - id: "epic-1.2"
      title: "Login Flow"
      points: 5
      status: "in_progress"  # 🔄 Working on it
      started_date: "2025-01-11"
    - id: "epic-1.3"
      title: "Password Reset"
      points: 5
      status: "todo"  # ⏳ Not started
  actual_velocity: 3  # Story 1.1 done = 3 pts
  status: "in_progress"
```

## Sprint Planning Meeting

**Pour chaque sprint**, faire :

1. **Review Sprint Goal**
   - What business value we're delivering

2. **Review Stories**
   - Each story is clear and actionable
   - Acceptance criteria understood
   - Estimates agreed

3. **Identify Risks**
   - Blockers
   - Dependencies
   - Unknowns

4. **Commit to Sprint**
   - Team agrees on capacity
   - Stories selected

## Sprint Retrospective

**Après chaque sprint** :

```yaml
retrospectives:
  sprint_1:
    date: "2025-01-20"
    velocity_planned: 8
    velocity_actual: 7
    notes: |
      - ✅ What went well: Auth implementation smooth
      - ⚠️ What to improve: Underestimated password reset complexity
      - 🔄 Action items: Add 20% buffer to estimates
    adjustments:
      - "Increase velocity estimate to 9 for sprint 2 (team getting faster)"
```

## Output

Génère dans : `_bmad-output/sprint-status.yaml`

## Utilisation Continue

**Update sprint-status.yaml** :
- Quand une story commence → `status: in_progress`
- Quand une story est complète → `status: done`
- À la fin du sprint → Update `actual_velocity`, `status: completed`
- Après retrospective → Ajuste vélocité pour sprint suivant

## Next Steps

Après Sprint Planning :

1. **Create Story** → Utilise `/sm` + skill `bmad-create-story` pour chaque story du sprint
2. **Dev Story** → Utilise `/dev` + skill `bmad-dev-story` pour implémenter
3. **Update Status** → Update `sprint-status.yaml` au fur et à mesure
