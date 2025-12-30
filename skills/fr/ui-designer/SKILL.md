---
name: ui-designer
description: Skill principal UI - Orchestre design system, couleurs, typography, spacing, responsive, a11y, components
---

# Skill UI Designer (Orchestrateur)

Ce skill est le point d'entrée principal pour tout travail de design UI. Il orchestre les skills spécialisés et fournit les principes fondamentaux communs.

> "Le bon design est invisible. L'utilisateur ne remarque pas l'interface, il accomplit simplement ses objectifs avec plaisir."

---

## Architecture des Skills UI

```
ui-designer (ce skill)
├── ui-colors      → Palettes, contraste, dark mode, sémantique
├── ui-typography  → Échelles, hiérarchie, responsive, lisibilité
├── ui-spacing     → Grille 8px, Gestalt, layout, breathing room
├── ui-responsive  → Mobile-first, breakpoints, adaptabilité
├── ui-a11y        → WCAG 2.1, ARIA, accessibilité universelle
└── ui-components  → Atomic Design, patterns, états, composition
```

### Quand Charger Quel Skill

| Tâche | Skill à charger |
|-------|-----------------|
| Créer/réviser une palette de couleurs | `ui-colors` |
| Définir le système typographique | `ui-typography` |
| Travailler sur le layout/espacement | `ui-spacing` |
| Adapter pour mobile/desktop | `ui-responsive` |
| Audit ou amélioration accessibilité | `ui-a11y` |
| Créer/standardiser des composants | `ui-components` |
| Nouveau projet complet | Charger tous les skills |
| Revue design globale | Ce skill + checklist |

---

## Principes Fondamentaux

### Philosophie du Bon Design

Privilégier :
- **L'élégance** sur la complexité
- **L'espace** sur l'encombrement  
- **La subtilité** sur l'exubérance
- **La cohérence** sur la variété
- **La clarté** sur la décoration

### Règle 60-30-10

Distribution harmonieuse des couleurs :
- **60%** : Couleur dominante (fonds, surfaces principales)
- **30%** : Couleur secondaire (composants, cartes, sections)
- **10%** : Couleur d'accent (boutons, liens, focus, CTAs)

### Hiérarchie Visuelle

L'œil doit savoir immédiatement où regarder.

**Techniques :**
- **Taille** : Les éléments importants sont plus grands
- **Poids** : Le texte important est plus gras
- **Couleur** : Les accents attirent l'attention
- **Position** : Le contenu clé est placé en haut/centre
- **Espace** : L'isolation crée de l'importance

### Un Seul Point Focal

**Règle :** Un seul point focal par écran/section. Si tout est important, rien ne l'est.

---

## Design Tokens - Format Standard

### Format DTCG (W3C Design Tokens)

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "colors": {
    "primary": {
      "$value": "#3B82F6",
      "$type": "color",
      "$description": "Couleur primaire pour actions principales"
    },
    "neutral": {
      "50": { "$value": "#F8FAFC", "$type": "color" },
      "100": { "$value": "#F1F5F9", "$type": "color" },
      "200": { "$value": "#E2E8F0", "$type": "color" },
      "300": { "$value": "#CBD5E1", "$type": "color" },
      "400": { "$value": "#94A3B8", "$type": "color" },
      "500": { "$value": "#64748B", "$type": "color" },
      "600": { "$value": "#475569", "$type": "color" },
      "700": { "$value": "#334155", "$type": "color" },
      "800": { "$value": "#1E293B", "$type": "color" },
      "900": { "$value": "#0F172A", "$type": "color" }
    },
    "semantic": {
      "success": { "$value": "#22C55E", "$type": "color" },
      "warning": { "$value": "#F59E0B", "$type": "color" },
      "error": { "$value": "#EF4444", "$type": "color" },
      "info": { "$value": "#3B82F6", "$type": "color" }
    }
  },
  "typography": {
    "fontFamily": {
      "sans": { "$value": "Inter, system-ui, sans-serif", "$type": "fontFamily" },
      "mono": { "$value": "JetBrains Mono, monospace", "$type": "fontFamily" }
    },
    "fontSize": {
      "xs": { "$value": "0.75rem", "$type": "dimension" },
      "sm": { "$value": "0.875rem", "$type": "dimension" },
      "base": { "$value": "1rem", "$type": "dimension" },
      "lg": { "$value": "1.125rem", "$type": "dimension" },
      "xl": { "$value": "1.25rem", "$type": "dimension" },
      "2xl": { "$value": "1.5rem", "$type": "dimension" },
      "3xl": { "$value": "1.875rem", "$type": "dimension" },
      "4xl": { "$value": "2.25rem", "$type": "dimension" }
    },
    "lineHeight": {
      "tight": { "$value": "1.25", "$type": "number" },
      "normal": { "$value": "1.5", "$type": "number" },
      "relaxed": { "$value": "1.75", "$type": "number" }
    }
  },
  "spacing": {
    "0": { "$value": "0", "$type": "dimension" },
    "1": { "$value": "0.25rem", "$type": "dimension" },
    "2": { "$value": "0.5rem", "$type": "dimension" },
    "3": { "$value": "0.75rem", "$type": "dimension" },
    "4": { "$value": "1rem", "$type": "dimension" },
    "6": { "$value": "1.5rem", "$type": "dimension" },
    "8": { "$value": "2rem", "$type": "dimension" },
    "12": { "$value": "3rem", "$type": "dimension" },
    "16": { "$value": "4rem", "$type": "dimension" }
  },
  "borderRadius": {
    "none": { "$value": "0", "$type": "dimension" },
    "sm": { "$value": "0.25rem", "$type": "dimension" },
    "md": { "$value": "0.5rem", "$type": "dimension" },
    "lg": { "$value": "0.75rem", "$type": "dimension" },
    "xl": { "$value": "1rem", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  },
  "shadow": {
    "sm": { 
      "$value": "0 1px 2px 0 rgb(0 0 0 / 0.05)", 
      "$type": "shadow" 
    },
    "md": { 
      "$value": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)", 
      "$type": "shadow" 
    },
    "lg": { 
      "$value": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)", 
      "$type": "shadow" 
    }
  }
}
```

### Variables CSS Équivalentes

```css
:root {
  /* Colors */
  --color-primary: #3B82F6;
  --color-neutral-50: #F8FAFC;
  --color-neutral-100: #F1F5F9;
  --color-neutral-500: #64748B;
  --color-neutral-900: #0F172A;
  --color-success: #22C55E;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  
  /* Typography */
  --font-sans: Inter, system-ui, sans-serif;
  --font-mono: JetBrains Mono, monospace;
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  
  /* Spacing (base 4px) */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  
  /* Border Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
}
```

---

## Processus de Design

### 1. Structure d'abord
- Définir la hiérarchie de l'information
- Placer les éléments principaux
- Établir la grille/layout
- **Skill :** `ui-spacing`

### 2. Spacing ensuite
- Appliquer le système d'espacement
- Créer les groupes visuels (Gestalt)
- S'assurer que ça respire
- **Skill :** `ui-spacing`

### 3. Typographie
- Établir l'échelle typographique
- Définir la hiérarchie des textes
- Vérifier la lisibilité
- **Skill :** `ui-typography`

### 4. Couleurs et style
- Appliquer la palette
- Ajouter les ombres/élévations
- Définir les états visuels
- **Skill :** `ui-colors`

### 5. Composants
- Standardiser les patterns
- Définir tous les états
- Assurer la cohérence
- **Skill :** `ui-components`

### 6. Responsive
- Adapter pour tous les écrans
- Tester les breakpoints
- Optimiser le mobile
- **Skill :** `ui-responsive`

### 7. Accessibilité
- Vérifier les contrastes
- Ajouter les attributs ARIA
- Tester au clavier
- **Skill :** `ui-a11y`

### 8. Polish
- Vérifier les alignements
- Harmoniser les détails
- Tester les états interactifs

---

## Checklist Qualité Globale

### Couleurs
- [ ] Palette limitée et cohérente (5-7 couleurs max)
- [ ] Contraste suffisant (WCAG AA minimum)
- [ ] Pas de couleurs criardes ou sur-saturées
- [ ] Les gris ont une teinte subtile (jamais pur)
- [ ] Règle 60-30-10 respectée
- [ ] Dark mode cohérent (si applicable)

### Espacement
- [ ] Système d'espacement cohérent (base 4px ou 8px)
- [ ] Assez d'espace blanc (breathing room)
- [ ] Padding généreux dans les composants
- [ ] Groupes visuels clairs (Gestalt)
- [ ] Pas de valeurs arbitraires

### Typographie
- [ ] Hiérarchie claire (tailles, poids)
- [ ] Maximum 2 fonts
- [ ] Texte lisible (14px min, contraste, line-height 1.4-1.6)
- [ ] Largeur de ligne optimale (60-80 caractères)
- [ ] Échelle typographique cohérente

### Composants
- [ ] Coins arrondis cohérents
- [ ] Ombres subtiles et appropriées
- [ ] États interactifs définis (hover, focus, active, disabled)
- [ ] Bordures subtiles (1px max, couleur atténuée)
- [ ] Patterns réutilisables

### Accessibilité
- [ ] Ratio de contraste WCAG AA (4.5:1 texte, 3:1 UI)
- [ ] Focus visible sur tous les éléments interactifs
- [ ] Navigation clavier fonctionnelle
- [ ] Attributs ARIA appropriés
- [ ] Textes alternatifs pour les images

### Responsive
- [ ] Mobile-first approach
- [ ] Breakpoints cohérents
- [ ] Touch targets suffisants (44x44px min)
- [ ] Pas de scroll horizontal
- [ ] Contenu priorisé sur mobile

### Harmonie Globale
- [ ] Un seul point focal par vue
- [ ] Alignements respectés
- [ ] Cohérence dans tout le design
- [ ] Design tokens utilisés partout

---

## Anti-Patterns à Éviter

### Visuels
- **Trop de couleurs** : Limite-toi à ta palette
- **Ombres dures** : Toujours diffuses et subtiles
- **Bordures épaisses** : 1px max, couleur atténuée
- **Coins arrondis inconsistants** : Même rayon pour éléments similaires
- **Gris pur** (#808080, #cccccc) : Toujours teinter subtilement
- **Texte sur image sans overlay** : Toujours assurer la lisibilité

### Spacing
- **Éléments collés aux bords** : Toujours du padding
- **Espacement inconsistant** : Utilise ton système
- **Manque d'air** : En cas de doute, ajoute de l'espace
- **Valeurs arbitraires** : Pas de "13px" ou "27px"
- **Groupes visuels flous** : Gestalt clair

### Typography
- **Trop de fonts** : 2 maximum
- **Trop de tailles** : Utilise une échelle définie
- **Texte trop petit** : 14px minimum pour le corps
- **Lignes trop longues** : 80 caractères max
- **Line-height serré** : 1.4 minimum pour le corps

### Interactions
- **Hover invisible** : Doit être perceptible
- **Focus invisible** : Critique pour l'accessibilité
- **États manquants** : Chaque élément interactif a tous ses états
- **Transitions brusques** : 150-300ms ease

---

## Mantras du Designer

- "Quand tu hésites, enlève plutôt qu'ajoute"
- "L'espace blanc est ton ami"
- "La cohérence bat l'originalité"
- "Simple n'est pas ennuyeux, simple est élégant"
- "Chaque pixel doit avoir une raison d'être"
- "Design for the worst case, delight in the best"
- "Accessible design is good design"

---

## Ressources

### Outils de Contraste
- WebAIM Contrast Checker
- Coolors Contrast Checker
- Stark (plugin Figma)

### Systèmes de Design de Référence
- Tailwind CSS (tokens et utilitaires)
- Radix UI (composants accessibles)
- Shadcn/ui (patterns modernes)
- Material Design 3 (guidelines)
- Apple Human Interface Guidelines

### Validation
- axe DevTools (accessibilité)
- Lighthouse (performance + a11y)
- WAVE (Web Accessibility Evaluation)
