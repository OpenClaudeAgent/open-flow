---
name: ui-responsive
description: Responsive Design - Mobile-first, breakpoints, fluid design, container queries
---

# Skill UI Responsive

Ce skill contient les principes et techniques du responsive design pour creer des interfaces qui s'adaptent a tous les ecrans.

---

## Philosophie

> "Le contenu est comme l'eau. Il prend la forme de son conteneur."

Privilegier :
- **Mobile-first** sur desktop-down
- **Progressive enhancement** sur graceful degradation
- **Fluid design** sur breakpoints rigides
- **Content-first** sur device-first
- **Performance** sur decoration

---

## Principes Fondamentaux

### 1. Mobile-First

Toujours designer et coder pour mobile d'abord, puis enrichir pour les grands ecrans.

**Pourquoi:**
- Force a prioriser le contenu essentiel
- Performance optimale sur mobile (moins de CSS a charger)
- Plus facile d'ajouter que de retirer

**En pratique:**
```css
/* Base: Mobile */
.component {
  flex-direction: column;
  padding: 16px;
}

/* Enrichissement: Tablet+ */
@media (min-width: 768px) {
  .component {
    flex-direction: row;
    padding: 24px;
  }
}
```

**Regle:** Jamais de `max-width` dans les media queries. Toujours `min-width`.

---

### 2. Progressive Enhancement

Construire une base solide, puis ajouter des ameliorations pour les navigateurs/devices modernes.

**Niveaux:**
1. **HTML** : Contenu accessible sans CSS/JS
2. **CSS** : Mise en forme et layout
3. **JS** : Interactions enrichies

**Exemple:**
```css
/* Base: Fonctionne partout */
.grid {
  display: block;
}

/* Enhancement: CSS Grid si supporte */
@supports (display: grid) {
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
}
```

---

### 3. Fluid Design

Privilegier les unites relatives et les fonctions CSS modernes pour un design qui s'adapte naturellement.

**Eviter:**
- Largeurs fixes en pixels
- Breakpoints multiples pour la meme propriete
- Media queries inutiles

**Privilegier:**
- Pourcentages et viewport units
- `clamp()`, `min()`, `max()`
- `auto-fit` et `auto-fill`

---

## Breakpoints Standards

```
sm:  640px   - Mobile landscape
md:  768px   - Tablet
lg:  1024px  - Desktop
xl:  1280px  - Large desktop
2xl: 1536px  - Extra large
```

**Usage recommande:**
- 0-639px : Mobile portrait (base, pas de media query)
- 640-767px : Mobile landscape
- 768-1023px : Tablet
- 1024-1279px : Desktop standard
- 1280px+ : Large screens

**Conseil:** La plupart des designs n'ont besoin que de 2-3 breakpoints. Ne pas en ajouter sans raison.

---

## Techniques CSS

### Media Queries (min-width)

```css
/* Mobile base */
.container {
  padding: 16px;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: 24px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
  }
}
```

---

### Container Queries

Pour des composants vraiment modulaires qui reagissent a leur conteneur, pas au viewport.

```css
/* Definir le conteneur */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Styles bases sur la taille du conteneur */
@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}

@container card (min-width: 600px) {
  .card {
    grid-template-columns: 1fr 2fr;
  }
}
```

**Quand utiliser:**
- Composants reutilisables dans differents contextes
- Sidebars/colonnes de tailles variables
- Grilles de cartes adaptatives

---

### Fonctions CSS Modernes

#### clamp()

Valeur fluide avec min et max.

```css
/* font-size: minimum 16px, prefere 4vw, maximum 24px */
.title {
  font-size: clamp(1rem, 4vw, 1.5rem);
}

/* Padding fluide */
.section {
  padding: clamp(16px, 5vw, 64px);
}
```

#### min() et max()

```css
/* Largeur: minimum entre 90% et 1200px */
.container {
  width: min(90%, 1200px);
}

/* Espacement: au moins 20px, ou 5% */
.gap {
  gap: max(20px, 5%);
}
```

---

## Images Responsives

### srcset et sizes

```html
<img 
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w,
    image-1600.jpg 1600w
  "
  sizes="
    (max-width: 640px) 100vw,
    (max-width: 1024px) 50vw,
    33vw
  "
  alt="Description"
/>
```

**Explication:**
- `srcset` : Liste des images disponibles avec leur largeur
- `sizes` : Largeur de l'image selon le viewport
- Le navigateur choisit la meilleure image automatiquement

---

### Picture Element

Pour art direction (images differentes selon le contexte).

```html
<picture>
  <!-- Format moderne si supporte -->
  <source 
    type="image/avif" 
    srcset="image.avif"
  />
  <source 
    type="image/webp" 
    srcset="image.webp"
  />
  
  <!-- Image differente sur mobile -->
  <source 
    media="(max-width: 640px)" 
    srcset="image-mobile.jpg"
  />
  
  <!-- Fallback -->
  <img src="image.jpg" alt="Description" />
</picture>
```

---

### Formats Modernes

**Priorite (du plus au moins efficace):**
1. **AVIF** : Meilleure compression, support croissant
2. **WebP** : Bon compromis, support large
3. **JPEG/PNG** : Fallback universel

**Lazy Loading:**
```html
<img src="image.jpg" loading="lazy" alt="Description" />
```

**CSS pour images responsives:**
```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

---

## Navigation Responsive

### Hamburger Menu

Pattern classique mobile → navigation complete desktop.

```css
/* Mobile: Menu cache */
.nav-menu {
  position: fixed;
  inset: 0;
  transform: translateX(-100%);
  transition: transform 0.3s ease;
}

.nav-menu.open {
  transform: translateX(0);
}

.hamburger {
  display: block;
}

/* Desktop: Menu visible */
@media (min-width: 768px) {
  .nav-menu {
    position: static;
    transform: none;
    display: flex;
  }
  
  .hamburger {
    display: none;
  }
}
```

---

### Bottom Navigation

Pattern mobile populaire (apps natives).

```css
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-around;
  padding: 8px 0;
  padding-bottom: env(safe-area-inset-bottom);
}

/* Desktop: masque ou deplace */
@media (min-width: 768px) {
  .bottom-nav {
    display: none;
  }
}
```

---

### Patterns Adaptatifs

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| Hamburger | Hamburger ou tabs | Navigation complete |
| Bottom nav | Sidebar optionnelle | Sidebar |
| Stack vertical | 2 colonnes | Multi-colonnes |
| Accordeon | Tabs | Tout visible |

---

## Touch vs Mouse

### Target Size

**Regle:** Minimum 44x44px pour les elements interactifs sur tactile.

```css
.button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 16px;
}

/* Liens dans le texte: zone elargie */
.text-link {
  padding: 8px;
  margin: -8px;
}
```

---

### Detection Hover

```css
/* Hover uniquement si le device le supporte */
@media (hover: hover) {
  .button:hover {
    background-color: var(--hover-color);
  }
}

/* Alternative pour touch: active state */
.button:active {
  background-color: var(--active-color);
}
```

---

### Detection Pointer

```css
/* Pointer precis (souris) */
@media (pointer: fine) {
  .slider-thumb {
    width: 16px;
    height: 16px;
  }
}

/* Pointer imprecis (doigt) */
@media (pointer: coarse) {
  .slider-thumb {
    width: 28px;
    height: 28px;
  }
}
```

---

## Performance

### Critical CSS

Inline le CSS necessaire au rendu initial.

```html
<head>
  <style>
    /* Critical: above-the-fold */
    .header { ... }
    .hero { ... }
  </style>
  <link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'">
</head>
```

---

### Code Splitting

Charger le CSS specifique selon le contexte.

```html
<!-- Desktop only -->
<link rel="stylesheet" href="desktop.css" media="(min-width: 1024px)">

<!-- Print only -->
<link rel="stylesheet" href="print.css" media="print">
```

---

### Images Optimisees

```html
<!-- Lazy loading natif -->
<img loading="lazy" src="image.jpg" alt="">

<!-- Preload images critiques -->
<link rel="preload" as="image" href="hero.jpg">

<!-- Dimensions pour eviter layout shift -->
<img width="800" height="600" src="image.jpg" alt="">
```

---

## Accessibilite Responsive

### prefers-reduced-motion

```css
/* Animations normales */
.element {
  transition: transform 0.3s ease;
}

/* Desactive pour ceux qui preferent */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

### prefers-color-scheme

```css
/* Light mode par defaut */
:root {
  --bg: white;
  --text: black;
}

/* Dark mode automatique */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a1a;
    --text: #f0f0f0;
  }
}
```

---

## Checklist Responsive

### Essentiel

- [ ] Meta viewport present
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1">
  ```
- [ ] Pas de scroll horizontal a aucune taille
- [ ] Images avec `max-width: 100%`
- [ ] Touch targets minimum 44px
- [ ] Texte lisible sans zoom (16px minimum)

### Navigation

- [ ] Navigation accessible sur mobile
- [ ] Menu hamburger fonctionnel
- [ ] Focus visible sur tous les elements

### Images

- [ ] srcset/sizes pour images importantes
- [ ] Lazy loading pour images below-the-fold
- [ ] Formats modernes (WebP/AVIF) avec fallback
- [ ] Dimensions specifiees (evite layout shift)

### Performance

- [ ] CSS critique inline
- [ ] Fonts optimisees (preload, font-display)
- [ ] Pas de ressources bloquantes inutiles

### Accessibilite

- [ ] prefers-reduced-motion respecte
- [ ] prefers-color-scheme supporte (optionnel)
- [ ] Contraste suffisant a toutes les tailles

---

## Templates CSS de Base

### Container Responsive

```css
.container {
  width: min(90%, 1200px);
  margin-inline: auto;
  padding-inline: 16px;
}

@media (min-width: 768px) {
  .container {
    padding-inline: 24px;
  }
}
```

---

### Grid Auto-Responsive

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
  gap: 24px;
}
```

**Explication:** Les colonnes font minimum 300px (ou 100% si l'ecran est plus petit), et s'ajoutent automatiquement quand l'espace le permet.

---

### Flex Responsive

```css
.flex-responsive {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.flex-responsive > * {
  flex: 1 1 300px; /* Grow, shrink, base 300px */
}
```

---

### Typography Fluide

```css
:root {
  --fs-sm: clamp(0.875rem, 0.8rem + 0.25vw, 1rem);
  --fs-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --fs-lg: clamp(1.25rem, 1rem + 1vw, 1.5rem);
  --fs-xl: clamp(1.5rem, 1rem + 2vw, 2.5rem);
  --fs-2xl: clamp(2rem, 1rem + 4vw, 4rem);
}
```

---

### Spacing Fluide

```css
:root {
  --space-sm: clamp(8px, 2vw, 16px);
  --space-md: clamp(16px, 4vw, 32px);
  --space-lg: clamp(24px, 6vw, 64px);
  --space-xl: clamp(48px, 10vw, 128px);
}
```

---

## Anti-Patterns a Eviter

### Layout

- **Largeurs fixes** : Utilise `%`, `vw`, `min()`, `max()`
- **Hauteurs fixes** : Laisse le contenu definir la hauteur
- **Scroll horizontal** : Toujours tester a 320px
- **Breakpoints arbitraires** : Utilise les standards

### Media Queries

- **max-width** : Privilegie `min-width` (mobile-first)
- **Trop de breakpoints** : 2-3 suffisent generalement
- **Breakpoints bases sur devices** : Base-toi sur le contenu

### Touch

- **Targets trop petits** : Minimum 44px
- **Hover-only interactions** : Toujours un fallback
- **Double-tap zoom** : Meta viewport correct

### Performance

- **Images non optimisees** : srcset + formats modernes
- **CSS bloquant** : Critical CSS inline
- **Fonts flash** : font-display: swap

---

## Mantras

- "Mobile-first n'est pas mobile-only"
- "Le contenu dicte les breakpoints, pas les devices"
- "Fluid first, breakpoints second"
- "Test sur vrais devices, pas juste le devtools"
- "La performance est une feature"
