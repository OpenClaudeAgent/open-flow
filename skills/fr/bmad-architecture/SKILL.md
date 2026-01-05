---
name: bmad-architecture
description: Design d'Architecture BMAD - Créer une architecture scalable guidée par les parcours utilisateurs et la valeur business
---

# Skill BMAD - Architecture Design

Ce skill guide la création d'un document d'architecture selon la méthodologie BMAD.

## Objectif

Concevoir une architecture simple qui scale quand nécessaire, dirigée par les parcours utilisateurs et la valeur business.

## Principes BMAD pour l'Architecture

1. **User journeys drive decisions** : Parcours utilisateurs dirigent les choix techniques
2. **Embrace boring technology** : Technologie éprouvée pour la stabilité
3. **Simple solutions that scale** : Commence simple, scale quand nécessaire
4. **Developer productivity is architecture** : La productivité dev est de l'architecture
5. **Connect to business value** : Chaque décision liée à la valeur business

## Workflow Architecture BMAD

### Phase 1 : Review PRD & User Journeys

**Analyser** :
- Les user journeys principales du PRD
- Les exigences non-fonctionnelles (performance, scale, security)
- Les contraintes techniques existantes

### Phase 2 : System Context & Boundaries

**Définir** :
- Les limites du système
- Les systèmes externes avec lesquels interagir
- Les interfaces principales

### Phase 3 : Architecture Patterns

**Choisir** :
- Pattern architectural principal (monolithique, microservices, serverless, etc.)
- Justification basée sur les besoins réels, pas les tendances
- Compromis clairement documentés

### Phase 4 : Component Design

**Détailler** :
- Composants principaux et leurs responsabilités
- Interactions entre composants
- Data flow
- API boundaries

### Phase 5 : Technology Stack

**Sélectionner** :
- Backend : Langages, frameworks, bases de données
- Frontend : Frameworks, state management
- Infrastructure : Cloud provider, CI/CD, monitoring
- **Justification** : Pourquoi chaque choix ? Quels compromis ?

### Phase 6 : Quality Attributes

**Adresser** :
- Performance : Targets et stratégies
- Scalability : Horizontal vs vertical, limites
- Security : Authentification, autorisation, encryption
- Reliability : SLA, fault tolerance
- Maintainability : Code quality, testing strategy

## Template Architecture BMAD

```markdown
# Architecture Document

## System Overview
[Vue d'ensemble en 2-3 paragraphes]

## User Journeys & Technical Mapping
1. **Journey 1** : [User journey] → [Technical flow]
2. **Journey 2** : [User journey] → [Technical flow]
3. ...

## Architecture Pattern
**Pattern** : [Monolithic / Microservices / Serverless / etc.]

**Justification** :
- [Raison 1]
- [Raison 2]

**Compromis** :
- ✅ Avantages : [...]
- ⚠️ Inconvénients : [...]

## System Context Diagram
[Mermaid ou Excalidraw diagram]

## Component Architecture

### Component 1: [Name]
- **Responsibility** : [...]
- **Technology** : [...]
- **Interfaces** : [APIs, Events, etc.]

### Component 2: [Name]
- **Responsibility** : [...]
- **Technology** : [...]
- **Interfaces** : [APIs, Events, etc.]

## Technology Stack

### Backend
- Language : [...]
- Framework : [...]
- Database : [...]
- **Justification** : [Boring technology that works]

### Frontend
- Framework : [...]
- State Management : [...]
- **Justification** : [Developer productivity]

### Infrastructure
- Cloud : [AWS / GCP / Azure / On-prem]
- CI/CD : [...]
- Monitoring : [...]

## Data Architecture
- Data models
- Data flow
- Storage strategy

## Quality Attributes

### Performance
- Target : [e.g., < 200ms response time]
- Strategy : [Caching, CDN, etc.]

### Scalability
- Approach : [Horizontal / Vertical]
- Limits : [Expected load]

### Security
- Authentication : [...]
- Authorization : [...]
- Data protection : [...]

### Reliability
- SLA : [99.9% uptime]
- Fault tolerance : [...]
- Backup strategy : [...]

## Deployment Architecture
[Diagram + explanation]

## Development Guidelines
- Code organization
- Testing strategy
- CI/CD workflow

## Open Questions & Future Considerations
- [Question 1]
- [Question 2]
- ...
```

## Output

Génère l'architecture dans : `_bmad-output/architecture/architecture.md`

## Diagrammes

Utilise l'agent `/tech-writer` pour créer des diagrammes :
- Mermaid (MG)
- Excalidraw (ED, DF)

## Next Steps

Après l'Architecture :

1. **Epics & Stories** → Utilise `/pm` + skill `bmad-epics-stories`
2. **Sprint Planning** → Utilise `/sm` + skill `bmad-sprint-planning`
3. **Implementation** → Utilise `/dev` + skill `bmad-dev-story`
