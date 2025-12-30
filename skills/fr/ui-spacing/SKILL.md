---
name: ui-spacing
description: Spacing UI - Système 8px, Gestalt, whitespace, layout, z-index
---

# UI Spacing

## Principes du Whitespace

Le whitespace est un **élément actif**, pas passif. Il joue un rôle fondamental dans le design.

### Fonctions du Whitespace

| Fonction | Description |
|----------|-------------|
| **Compréhension** | Facilite la lecture et le parsing visuel |
| **Relations** | Crée des groupes logiques d'éléments |
| **Attention** | Guide le regard vers les éléments importants |
| **Esthétique** | Apporte élégance et respiration |

### Micro vs Macro Whitespace

- **Micro whitespace** : Espacement entre éléments proches (lettres, lignes, icône et texte)
- **Macro whitespace** : Espacement entre sections, marges de page, zones majeures

---

## Système 8px

Base cohérente pour tous les espacements :

```
space-1:  4px   (half-step, cas spéciaux)
space-2:  8px   (minimum standard)
space-3:  12px
space-4:  16px  (base, espacement par défaut)
space-6:  24px
space-8:  32px
space-12: 48px
space-16: 64px
```

### Pourquoi 8px ?

- Divisible par 2 et 4 (flexibilité)
- S'aligne avec les grilles standard
- Fonctionne bien sur tous les écrans (densité pixel)
- Facilite le calcul mental

---

## Concepts de Spacing (EightShapes)

### Inset (Padding interne)

Espacement à l'intérieur d'un conteneur :

```
┌─────────────────┐
│     INSET       │
│  ┌───────────┐  │
│  │  Content  │  │
│  └───────────┘  │
│                 │
└─────────────────┘
```

| Type | Description | Exemple |
|------|-------------|---------|
| **Square** | Même valeur partout | `padding: 16px` |
| **Squish** | Vertical < Horizontal | `padding: 8px 16px` (boutons) |
| **Stretch** | Vertical > Horizontal | `padding: 16px 8px` (listes) |

### Stack (Vertical)

Espacement vertical entre éléments empilés :

```
┌─────────────┐
│  Element 1  │
└─────────────┘
      ↕ stack
┌─────────────┐
│  Element 2  │
└─────────────┘
      ↕ stack
┌─────────────┐
│  Element 3  │
└─────────────┘
```

Usage : `gap: var(--stack-elements)` ou `margin-bottom`

### Inline (Horizontal)

Espacement horizontal entre éléments adjacents :

```
┌───────┐     ┌───────┐     ┌───────┐
│ Item  │←───→│ Item  │←───→│ Item  │
└───────┘inline└───────┘inline└───────┘
```

Usage : `gap: var(--inline-elements)` ou `margin-right`

### Grid

Espacement dans une grille 2D :

```
┌─────┐  ┌─────┐  ┌─────┐
│     │  │     │  │     │
└─────┘  └─────┘  └─────┘
   ↕ row-gap
┌─────┐  ┌─────┐  ┌─────┐
│     │  │     │  │     │
└─────┘  └─────┘  └─────┘
   ←column-gap→
```

---

## Principes Gestalt

### Proximité

> Les éléments proches sont perçus comme appartenant au même groupe.

```
✅ Bon                    ❌ Mauvais
┌─────────────┐          ┌─────────────┐
│ Label       │          │ Label       │
│ Input ────  │          │             │
│             │          │             │
│ Label       │          │ Input ────  │
│ Input ────  │          │ Label       │
└─────────────┘          │ Input ────  │
                         └─────────────┘
```

### Région Commune

> Les éléments dans une même zone délimitée sont perçus comme un groupe.

```css
/* Carte comme région commune */
.card {
  padding: var(--inset-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
```

### Connectivité Uniforme

> Les éléments connectés visuellement sont perçus comme liés.

- Lignes de connexion
- Fond partagé
- Bordures communes

---

## Layout Patterns

### Grid 12 Colonnes

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-4);
}

/* Colonnes responsives */
.col-6 { grid-column: span 6; }  /* 50% */
.col-4 { grid-column: span 4; }  /* 33% */
.col-3 { grid-column: span 3; }  /* 25% */
```

### Flexbox vs Grid

| Flexbox | Grid |
|---------|------|
| Layout 1D (ligne OU colonne) | Layout 2D (lignes ET colonnes) |
| Contenu définit la taille | Conteneur définit la taille |
| Navigation, toolbars | Layouts de page, grilles |

```css
/* Flexbox : alignement simple */
.toolbar {
  display: flex;
  gap: var(--inline-elements);
  align-items: center;
}

/* Grid : layout complexe */
.page {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  gap: var(--space-6);
}
```

### Stratégies Responsive

```css
/* Mobile-first breakpoints */
--breakpoint-sm: 640px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1280px;

/* Spacing responsive */
.section {
  padding: var(--space-4);
}

@media (min-width: 768px) {
  .section {
    padding: var(--space-8);
  }
}
```

---

## Z-Index Management

### Échelle Standard

```css
:root {
  --z-base: 0;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-fixed: 300;
  --z-modal-backdrop: 400;
  --z-modal: 500;
  --z-popover: 600;
  --z-tooltip: 700;
}
```

### Stacking Contexts

Un nouveau contexte d'empilement est créé par :
- `position: fixed/sticky`
- `opacity < 1`
- `transform`, `filter`, `perspective`
- `isolation: isolate`

### Isolation Pattern

```css
/* Créer un contexte isolé */
.component {
  isolation: isolate;
}

/* Les z-index internes n'affectent pas l'extérieur */
.component .internal {
  position: relative;
  z-index: 10; /* Seulement relatif à .component */
}
```

---

## Density Modes

Adapter l'interface selon le contexte d'utilisation :

| Mode | Multiplicateur | Usage |
|------|---------------|-------|
| **Compact** | 0.75x | Données denses, desktop power users |
| **Comfortable** | 1x | Usage standard, défaut |
| **Spacious** | 1.5x | Mobile, accessibilité, lecture |

```css
:root {
  --density: 1;
}

.compact { --density: 0.75; }
.spacious { --density: 1.5; }

.element {
  padding: calc(var(--space-4) * var(--density));
  gap: calc(var(--space-2) * var(--density));
}
```

---

## Tokens CSS

### Définition des Tokens

```css
:root {
  /* Base spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;

  /* Inset patterns */
  --inset-button: 8px 16px;       /* squish */
  --inset-card: 16px;             /* square */
  --inset-input: 12px 16px;       /* squish */
  --inset-list-item: 12px 8px;    /* stretch */

  /* Stack spacing */
  --stack-xs: 4px;
  --stack-sm: 8px;
  --stack-md: 16px;
  --stack-lg: 24px;
  --stack-xl: 32px;
  --stack-elements: 16px;
  --stack-sections: 48px;

  /* Inline spacing */
  --inline-xs: 4px;
  --inline-sm: 8px;
  --inline-md: 16px;
  --inline-elements: 8px;
  --inline-actions: 12px;

  /* Grid */
  --grid-gap: 16px;
  --grid-columns: 12;
}
```

### Usage

```css
.button {
  padding: var(--inset-button);
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--stack-sm);
}

.card {
  padding: var(--inset-card);
}

.card-content > * + * {
  margin-top: var(--stack-elements);
}

.button-group {
  display: flex;
  gap: var(--inline-actions);
}
```

---

## Checklist Spacing

- [ ] Utiliser le système 8px (éviter valeurs arbitraires)
- [ ] Appliquer la proximité Gestalt (éléments liés = proches)
- [ ] Différencier micro/macro whitespace
- [ ] Tokens pour toutes les valeurs de spacing
- [ ] Z-index dans l'échelle définie
- [ ] Tester les 3 modes de densité
- [ ] Layout responsive avec breakpoints standards
