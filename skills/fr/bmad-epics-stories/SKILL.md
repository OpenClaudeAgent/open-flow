---
name: bmad-epics-stories
description: Epics & User Stories BMAD - Créer epics et user stories à partir du PRD et de l'Architecture
---

# Skill BMAD - Epics & User Stories

Ce skill guide la création d'Epics et User Stories à partir du PRD et de l'Architecture.

## Objectif

Décomposer le PRD et l'Architecture en Epics et User Stories implémentables, en respectant l'alignement parfait entre vision produit et exécution technique.

## Principes BMAD

1. **Epics = Groupes de valeur business** : Chaque epic livre une valeur business complète
2. **Stories = Incréments verticaux** : Chaque story traverse toutes les couches (UI → Backend → DB)
3. **Alignement PRD-Arch-Stories** : Traçabilité complète du besoin à l'implémentation
4. **Independent, Negotiable, Valuable, Estimable, Small, Testable** (INVEST)

## Workflow

### Phase 1 : Review PRD & Architecture

**Analyser** :
- User stories du PRD
- Composants de l'Architecture
- User journeys principales
- Critères de succès

### Phase 2 : Identifier les Epics

**Créer des Epics** basés sur :
- User journeys principales
- Modules fonctionnels
- Value streams business

**Template Epic** :
```markdown
# Epic [N]: [Epic Name]

## Business Value
[Quelle valeur business cet epic livre-t-il ?]

## User Journeys
- [User journey 1]
- [User journey 2]

## Scope
### IN Scope
- [Feature 1]
- [Feature 2]

### OUT Scope
- [Feature postponée]

## Success Criteria
1. [Critère mesurable 1]
2. [Critère mesurable 2]

## User Stories
- Story 1: [Titre]
- Story 2: [Titre]
- ...

## Technical Notes
[Notes architecture, dépendances techniques]

## Estimated Effort
[Story points ou temps]
```

### Phase 3 : Créer les User Stories

**Pour chaque Epic**, créer des stories INVEST :

**Template User Story** :
```markdown
# Story [Epic-N.M]: [Story Title]

## User Story
As a [user persona]
I want to [action]
So that [benefit/value]

## Acceptance Criteria
1. [ ] Given [context], when [action], then [result]
2. [ ] Given [context], when [action], then [result]
3. [ ] ...

## Technical Notes
- Component(s): [Frontend/Backend/DB components concerned]
- API endpoints: [If applicable]
- Data model changes: [If applicable]

## Dependencies
- Depends on: [Story X, Story Y]
- Blocks: [Story Z]

## Estimated Effort
[Story points: 1, 2, 3, 5, 8, 13]

## Definition of Done
- [ ] Code implemented and reviewed
- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Acceptance criteria validated by PO
```

### Phase 4 : Prioriser & Séquencer

**Créer la séquence** :
1. Stories fondation (auth, data models)
2. Stories core features (user journeys principales)
3. Stories edge cases et optimisations

**Matrice de priorisation** :
- **Must Have** : Critique MVP
- **Should Have** : Important mais peut attendre
- **Could Have** : Nice to have
- **Won't Have** : Hors scope

### Phase 5 : Validation

**Vérifier** :
- ✅ Chaque user story du PRD est couverte
- ✅ Chaque composant d'architecture est utilisé
- ✅ Stories sont INVEST
- ✅ Dépendances sont claires
- ✅ Priorisation alignée avec critères de succès PRD

## Output

Génère les epics dans : `_bmad-output/epics/`

```
_bmad-output/epics/
├── epic-1-user-auth.md
├── epic-2-dashboard.md
├── epic-3-notifications.md
└── ...
```

## Exemple Complet

### Epic Example
```markdown
# Epic 1: User Authentication

## Business Value
Permettre aux utilisateurs de créer un compte et se connecter de manière sécurisée.

## User Journeys
- Nouvel utilisateur s'inscrit
- Utilisateur existant se connecte
- Utilisateur réinitialise son mot de passe

## Scope
### IN Scope
- Email/password authentication
- JWT tokens
- Password reset flow

### OUT Scope
- OAuth (Google, Facebook) - Epic 5
- 2FA - Epic 6

## Success Criteria
1. 95% des utilisateurs peuvent créer un compte en < 2min
2. 0 fuite de données utilisateur

## User Stories
- Story 1.1: Sign Up Form
- Story 1.2: Login Flow
- Story 1.3: Password Reset

## Technical Notes
- Backend: Node.js + Express
- Auth: JWT + bcrypt
- DB: PostgreSQL users table

## Estimated Effort
13 story points (3 stories @ 3,5,5)
```

### Story Example
```markdown
# Story 1.1: Sign Up Form

## User Story
As a new user
I want to create an account with email and password
So that I can access the platform

## Acceptance Criteria
1. [ ] Given I'm on signup page, when I enter valid email/password, then account is created
2. [ ] Given I enter invalid email, when I submit, then I see error "Invalid email format"
3. [ ] Given I enter weak password (<8 chars), when I submit, then I see error "Password must be 8+ characters"
4. [ ] Given email already exists, when I submit, then I see error "Email already registered"
5. [ ] Given signup successful, when I complete, then I'm redirected to dashboard

## Technical Notes
- Component: Frontend SignUp form + Backend /api/auth/signup endpoint
- API: POST /api/auth/signup (email, password) → {user, token}
- DB: Create users table (id, email, password_hash, created_at)
- Validation: Email format + password strength (min 8 chars)
- Security: bcrypt for password hashing

## Dependencies
- Depends on: None (foundation story)
- Blocks: Story 1.2 (Login)

## Estimated Effort
3 story points

## Definition of Done
- [ ] SignUp form UI implemented (React)
- [ ] Backend endpoint /api/auth/signup created
- [ ] Password hashing with bcrypt
- [ ] Email validation
- [ ] Unit tests for validation logic
- [ ] Integration test for signup flow
- [ ] Error handling for all edge cases
- [ ] Documentation updated (API docs)
```

## Next Steps

Après Epics & Stories :

1. **Sprint Planning** → Utilise `/sm` + skill `bmad-sprint-planning`
2. **Create Story** → Utilise `/sm` + skill `bmad-create-story`
3. **Implementation** → Utilise `/dev` + skill `bmad-dev-story`
