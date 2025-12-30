---
name: ui-components
description: Composants UI - Atomic Design, patterns d'interaction, etats, design systems
---

# Skill UI Components

Ce skill contient les principes de conception de composants UI, de l'Atomic Design aux patterns d'interaction avances.

---

## Atomic Design (Brad Frost)

L'Atomic Design est une methodologie pour creer des systemes de design modulaires et coherents.

```
Atoms → Molecules → Organisms → Templates → Pages
```

### Niveaux

| Niveau | Definition | Exemples |
|--------|-----------|----------|
| **Atoms** | Elements UI de base, indivisibles | Button, Icon, Label, Input, Badge |
| **Molecules** | Groupes d'atomes fonctionnant ensemble | Search bar (input + button), Form field (label + input + error) |
| **Organisms** | Groupes de molecules formant une section | Header, Card, Form, Navigation |
| **Templates** | Structures de page sans contenu reel | Layout avec placeholders, grille de page |
| **Pages** | Templates avec contenu reel | Page d'accueil, Dashboard |

### Principes Cles

- **Bottom-up** : Construis les petits elements avant les grands
- **Reutilisabilite** : Chaque niveau peut etre reutilise partout
- **Coherence** : Modifier un atome impacte tout le systeme
- **Documentation** : Chaque composant est documente isolement

---

## Composants Essentiels par Categorie

### General

| Composant | Usage | Variants |
|-----------|-------|----------|
| **Button** | Actions principales et secondaires | Primary, Secondary, Ghost, Link, Icon |
| **Icon** | Representation visuelle d'une action/concept | Sizes (sm, md, lg), Filled, Outlined |
| **Typography** | Texte structure | Heading 1-6, Body, Caption, Label |

### Layout

| Composant | Usage | Proprietes cles |
|-----------|-------|-----------------|
| **Grid** | Disposition en colonnes | columns, gap, responsive breakpoints |
| **Flex** | Disposition flexible | direction, justify, align, wrap |
| **Divider** | Separation visuelle | orientation (horizontal/vertical), variant |
| **Space** | Espacement entre elements | size (xs, sm, md, lg, xl) |
| **Container** | Conteneur centre avec max-width | size, padding |

### Navigation

| Composant | Usage | Considerations |
|-----------|-------|----------------|
| **Tabs** | Basculer entre vues | Active state, disabled, icons |
| **Breadcrumb** | Montrer la hierarchie de navigation | Separator, collapsible |
| **Menu** | Liste d'actions/liens | Nested, icons, keyboard nav |
| **Pagination** | Naviguer entre pages de donnees | Simple/complex, page size |
| **Sidebar** | Navigation laterale | Collapsible, nested items |

### Data Entry

| Composant | Usage | Etats |
|-----------|-------|-------|
| **Input** | Saisie de texte | Text, Password, Number, Search |
| **Select** | Selection dans une liste | Single, Multiple, Searchable |
| **Checkbox** | Selection multiple | Checked, Indeterminate, Group |
| **Radio** | Selection unique | Group, Horizontal/Vertical |
| **Switch** | Toggle on/off | With label, Sizes |
| **DatePicker** | Selection de date | Range, Time, Presets |
| **Slider** | Selection de valeur sur une plage | Range, Steps, Marks |
| **TextArea** | Saisie multiligne | Auto-resize, Max length |

### Data Display

| Composant | Usage | Variants |
|-----------|-------|----------|
| **Card** | Conteneur d'information | Clickable, Hoverable, Bordered |
| **Table** | Donnees tabulaires | Sortable, Selectable, Expandable |
| **List** | Liste d'elements | Simple, With actions, Virtualized |
| **Avatar** | Representation d'utilisateur | Image, Initials, Icon, Group |
| **Badge** | Indicateur numerique/status | Dot, Count, Colors |
| **Tag** | Categorisation/labels | Closable, With icon, Colors |
| **Tooltip** | Info contextuelle au hover | Positions, Arrow |

### Feedback

| Composant | Usage | Variants |
|-----------|-------|----------|
| **Alert** | Message important inline | Info, Success, Warning, Error |
| **Modal** | Dialogue bloquant | Sizes, Closable, Centered |
| **Toast** | Notification temporaire | Positions, Auto-dismiss, Actions |
| **Progress** | Indication d'avancement | Bar, Circle, Steps |
| **Skeleton** | Placeholder de chargement | Text, Avatar, Card, Custom |
| **Spinner** | Chargement en cours | Sizes, Colors, Overlay |

---

## Etats de Composants

Chaque composant interactif doit definir tous ses etats visuels.

### Etats Standards

| Etat | Description | Traitement visuel |
|------|-------------|-------------------|
| **Default** | Etat de base au repos | Style standard |
| **Hover** | Curseur au-dessus | Legere modification (brightness, shadow) |
| **Active/Pressed** | En cours de clic | Effet d'enfoncement (scale, shadow reduit) |
| **Focus** | Selectionne au clavier | Ring/outline visible (accessibilite) |
| **Disabled** | Non interactif | Opacite reduite (50-60%), cursor: not-allowed |
| **Loading** | Action en cours | Spinner, texte "Loading...", disabled |
| **Error** | Erreur de validation | Bordure rouge, message d'erreur |
| **Success** | Action reussie | Bordure verte, feedback visuel |

### Exemple : Button States

```
Default   → Background: primary, cursor: pointer
Hover     → Background: primary-dark (+10% darker)
Active    → Background: primary-darker, transform: scale(0.98)
Focus     → Box-shadow: 0 0 0 3px primary-alpha
Disabled  → Opacity: 0.5, cursor: not-allowed
Loading   → Spinner + text, pointer-events: none
```

### Transitions

- **Duree** : 150-200ms pour les micro-interactions
- **Easing** : ease-out pour les entrees, ease-in pour les sorties
- **Proprietes** : background-color, border-color, box-shadow, transform

---

## Patterns d'Interaction

### Forms

| Pattern | Description | Implementation |
|---------|-------------|----------------|
| **Inline Validation** | Validation en temps reel | onBlur ou onChange avec debounce |
| **Multi-step Form** | Formulaire en etapes | Progress indicator, validation par etape |
| **Autosave** | Sauvegarde automatique | Debounce, indicateur de statut |
| **Field Dependencies** | Champs conditionnels | Show/hide selon valeurs |
| **Smart Defaults** | Pre-remplissage intelligent | Historique, geoloc, preferences |

### Navigation

| Pattern | Description | Quand l'utiliser |
|---------|-------------|------------------|
| **Tabs** | Contenu mutuellement exclusif | 2-7 items, contenu lie |
| **Accordion** | Contenu expandable | FAQ, details optionnels |
| **Dropdown Menu** | Actions/options cachees | Actions secondaires |
| **Command Palette** | Recherche d'actions | Power users, raccourcis |
| **Breadcrumb** | Chemin de navigation | Hierarchies profondes |

### Data Patterns

| Pattern | Description | UX |
|---------|-------------|-----|
| **Filter** | Reduire les resultats | Filtres visibles ou en panel |
| **Sort** | Reordonner les resultats | Indicateur de direction |
| **Search** | Recherche textuelle | Autocomplete, highlights |
| **Pagination** | Navigation par pages | Ou infinite scroll |
| **Bulk Actions** | Actions sur selection multiple | Checkbox + action bar |

### Feedback Patterns

| Pattern | Description | Duree |
|---------|-------------|-------|
| **Toast** | Notification non-bloquante | 3-5 secondes |
| **Inline Message** | Feedback contextuel | Jusqu'a resolution |
| **Modal Confirmation** | Action destructive | Require action explicite |
| **Progress Indicator** | Operation longue | Jusqu'a completion |
| **Optimistic Update** | UI mise a jour avant serveur | Rollback si erreur |

### Onboarding Patterns

| Pattern | Description | Usage |
|---------|-------------|-------|
| **Coachmarks** | Points lumineux sur l'UI | Features cles, 3-5 max |
| **Walkthrough** | Visite guidee etape par etape | Premiere utilisation |
| **Empty State CTA** | Guide dans les etats vides | Premiere action |
| **Tooltips contextuels** | Aide au hover | Features complexes |
| **Checklist** | Progression d'onboarding | Setup multi-etapes |

---

## Empty States

Les etats vides sont des opportunites de guider l'utilisateur.

### Anatomie d'un Empty State

```
+----------------------------------+
|                                  |
|       [Illustration/Icon]        |
|                                  |
|         Titre explicatif         |
|    Message secondaire optionnel  |
|                                  |
|      [ Call-to-Action ]          |
|                                  |
|      Lien d'aide (optionnel)     |
+----------------------------------+
```

### Types d'Empty States

| Type | Message | CTA |
|------|---------|-----|
| **First use** | "Bienvenue ! Creez votre premier projet" | "Creer un projet" |
| **No results** | "Aucun resultat pour 'xyz'" | "Modifier les filtres" |
| **Cleared** | "Tous les elements sont traites" | "Voir l'historique" |
| **Error** | "Impossible de charger les donnees" | "Reessayer" |
| **No permission** | "Vous n'avez pas acces a cette section" | "Demander l'acces" |

### Bonnes Pratiques

- **Illustration** : Legere, coherente avec le brand
- **Ton** : Amical, pas culpabilisant
- **Action claire** : Un seul CTA principal
- **Aide** : Lien vers documentation si pertinent

---

## Loading States

Communiquer clairement que quelque chose se passe.

### Quand utiliser quoi

| Pattern | Duree inconnue | Duree connue | Structure previsible |
|---------|---------------|--------------|---------------------|
| **Spinner** | Oui | - | - |
| **Progress Bar** | - | Oui | - |
| **Skeleton** | - | - | Oui |

### Spinner

```
Usage : Chargement de duree inconnue
Placement : Centre du conteneur concerne
Taille : Proportionnelle a la zone
Accompagnement : Texte optionnel ("Chargement...")
```

### Progress Bar

```
Usage : Upload, download, traitement par etapes
Information : Pourcentage, temps restant (si calculable)
Types : Determinate (% connu), Indeterminate (% inconnu)
```

### Skeleton

```
Usage : Contenu avec structure previsible
Avantage : Reduit le Cumulative Layout Shift (CLS)
Implementation : Formes grises animees mimant le contenu
Animation : Pulse ou shimmer (gauche vers droite)
```

### Bonnes Pratiques

- **Instantane (< 100ms)** : Pas d'indicateur
- **Court (100ms - 1s)** : Indicateur subtil (opacity change)
- **Moyen (1s - 10s)** : Spinner ou skeleton
- **Long (> 10s)** : Progress bar avec estimation

---

## Design Tokens pour Composants

Les tokens standardisent les proprietes des composants.

### Spacing Tokens

```css
/* Component spacing */
--button-padding-x: var(--space-4);      /* 16px */
--button-padding-y: var(--space-2);      /* 8px */
--card-padding: var(--space-4);          /* 16px */
--input-padding-x: var(--space-3);       /* 12px */
--input-padding-y: var(--space-2);       /* 8px */
--modal-padding: var(--space-6);         /* 24px */
```

### Size Tokens

```css
/* Component heights */
--input-height-sm: 32px;
--input-height-md: 40px;
--input-height-lg: 48px;
--button-height-sm: 32px;
--button-height-md: 40px;
--button-height-lg: 48px;

/* Touch targets (minimum 44px pour mobile) */
--touch-target-min: 44px;
```

### Border Radius Tokens

```css
--button-radius: var(--radius-md);       /* 8px */
--card-radius: var(--radius-lg);         /* 12px */
--input-radius: var(--radius-md);        /* 8px */
--badge-radius: var(--radius-full);      /* 9999px */
--modal-radius: var(--radius-xl);        /* 16px */
```

### Shadow Tokens

```css
--card-shadow: var(--shadow-sm);
--dropdown-shadow: var(--shadow-md);
--modal-shadow: var(--shadow-lg);
--button-shadow: none;
--button-shadow-hover: var(--shadow-sm);
```

---

## Best Practices

### Composition over Inheritance

```
Bon :  <Card><CardHeader/><CardBody/><CardFooter/></Card>
Mauvais : <Card header="..." body="..." footer="..." />
```

- Composants composes plutot que monolithiques
- Slots/children pour le contenu
- Props pour la configuration

### Single Responsibility

Chaque composant fait UNE chose bien :
- `Button` : Declenche une action
- `Input` : Saisie de texte
- `Card` : Conteneur visuel

Pas de composants "god" qui font tout.

### Props Consistency

Utiliser les memes noms de props partout :

| Prop | Usage | Valeurs |
|------|-------|---------|
| `size` | Taille du composant | 'sm', 'md', 'lg' |
| `variant` | Style visuel | 'primary', 'secondary', 'ghost' |
| `disabled` | Etat desactive | boolean |
| `loading` | Etat de chargement | boolean |
| `fullWidth` | Prend toute la largeur | boolean |

### Theming via Tokens

```
Bon :  background: var(--color-primary);
Mauvais : background: #3B82F6;
```

- Toutes les valeurs via tokens
- Permet le theming (dark mode, white label)
- Facilite les modifications globales

### Accessibilite

Chaque composant interactif doit :
- Avoir un focus state visible
- Etre navigable au clavier
- Avoir les attributs ARIA appropries
- Respecter les contrastes de couleur

---

## Checklist Composant

Avant de finaliser un composant :

### Structure
- [ ] Responsabilite unique claire
- [ ] Props coherentes avec le systeme
- [ ] Composition privilegiee

### Etats
- [ ] Tous les etats visuels definis
- [ ] Transitions fluides (150-200ms)
- [ ] Loading state si pertinent

### Accessibilite
- [ ] Focus state visible
- [ ] Navigation clavier
- [ ] Attributs ARIA
- [ ] Contraste suffisant

### Tokens
- [ ] Spacing via tokens
- [ ] Colors via tokens
- [ ] Pas de valeurs hardcodees

### Documentation
- [ ] Props documentees
- [ ] Variants illustres
- [ ] Exemples d'usage
