---
name: ui-a11y
description: Accessibilité UI - WCAG 2.1, ARIA, contraste, navigation clavier, screen readers
---

# Accessibilité UI (a11y)

## Standards de Référence

| Standard | Description | Obligatoire |
|----------|-------------|-------------|
| **WCAG 2.1/2.2** | Web Content Accessibility Guidelines | Référence mondiale |
| **Section 508** | US Federal accessibility | USA |
| **EN 301 549** | European accessibility standard | Europe |

### Niveaux de Conformité WCAG

- **Niveau A** : Minimum absolu (bloquants critiques)
- **Niveau AA** : Standard recommandé (cible pour la plupart des projets)
- **Niveau AAA** : Excellence (pas toujours atteignable pour tout contenu)

---

## Principes POUR (WCAG)

### 1. Perceivable (Perceptible)
L'information doit être présentable de manière perceptible par tous les utilisateurs.

- Alternatives textuelles pour contenus non-textuels
- Captions et alternatives pour médias temporels
- Contenu adaptable (différentes présentations)
- Contenu distinguable (séparation premier/arrière-plan)

### 2. Operable (Utilisable)
Les composants UI et la navigation doivent être utilisables.

- Accessible au clavier
- Temps suffisant pour lire/interagir
- Pas de contenu causant des crises (flash)
- Navigation facilitée

### 3. Understandable (Compréhensible)
L'information et l'UI doivent être compréhensibles.

- Texte lisible et compréhensible
- Comportement prévisible
- Assistance à la saisie (erreurs)

### 4. Robust (Robuste)
Le contenu doit être interprétable par une variété d'agents utilisateurs.

- Compatible avec les technologies d'assistance
- Parsing correct du markup

---

## Contraste WCAG

| Type de Contenu | Niveau AA | Niveau AAA |
|-----------------|-----------|------------|
| **Texte normal** (<18pt) | 4.5:1 | 7:1 |
| **Grand texte** (>=18pt ou 14pt bold) | 3:1 | 4.5:1 |
| **UI Components / Graphics** | 3:1 | 3:1 |

### Vérification du Contraste

```css
/* Exemples de bons contrastes */
.good-contrast {
  color: #1a1a1a;           /* Texte sombre */
  background: #ffffff;       /* Fond clair */
  /* Ratio: 16.1:1 - AAA */
}

.minimum-aa {
  color: #767676;           /* Gris */
  background: #ffffff;
  /* Ratio: 4.54:1 - AA pour texte normal */
}
```

---

## Navigation Clavier

### Règles Fondamentales

1. **Tab order logique** : Ordre de focus suit l'ordre visuel/logique
2. **Focus visible obligatoire** : Indicateur de focus toujours visible
3. **Skip links** : Liens pour sauter au contenu principal
4. **Pas de piège clavier** : L'utilisateur peut toujours sortir d'un composant

### Touches Standard

| Touche | Action |
|--------|--------|
| `Tab` | Élément focusable suivant |
| `Shift+Tab` | Élément focusable précédent |
| `Enter` | Activer bouton/lien |
| `Space` | Activer bouton, cocher checkbox |
| `Escape` | Fermer modal/menu |
| `Arrow keys` | Navigation dans composants (tabs, menus) |

### Focus Visible

```css
/* Ne JAMAIS faire */
*:focus { outline: none; }

/* Toujours prévoir un style focus */
:focus-visible {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}

/* Focus personnalisé acceptable */
button:focus-visible {
  box-shadow: 0 0 0 3px rgba(0, 95, 204, 0.5);
}
```

### Skip Link

```html
<body>
  <a href="#main-content" class="skip-link">
    Aller au contenu principal
  </a>
  <header>...</header>
  <main id="main-content" tabindex="-1">
    <!-- Contenu principal -->
  </main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  left: 10px;
  top: 10px;
  z-index: 9999;
}
```

---

## ARIA (Accessible Rich Internet Applications)

### Règle d'Or

> **"No ARIA is better than bad ARIA"**
> 
> Utilisez d'abord les éléments HTML natifs. ARIA en dernier recours.

### Landmarks (Régions)

```html
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<aside role="complementary">...</aside>
<footer role="contentinfo">...</footer>
```

**Note** : Les éléments HTML5 ont des rôles implicites. `role` explicite utile pour support ancien.

### Labels et Descriptions

```html
<!-- aria-label : label invisible -->
<button aria-label="Fermer la modal">
  <svg>...</svg>
</button>

<!-- aria-labelledby : référence un élément -->
<dialog aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirmation</h2>
</dialog>

<!-- aria-describedby : description additionnelle -->
<input 
  type="password" 
  aria-describedby="password-help"
>
<p id="password-help">
  Minimum 8 caractères, 1 majuscule, 1 chiffre
</p>
```

### Live Regions

Pour annoncer des changements dynamiques aux screen readers.

```html
<!-- Annonces polies (attend fin de lecture) -->
<div aria-live="polite" aria-atomic="true">
  3 résultats trouvés
</div>

<!-- Annonces urgentes (interrompt) -->
<div role="alert" aria-live="assertive">
  Erreur: Session expirée
</div>

<!-- Status (poli par défaut) -->
<div role="status">
  Chargement en cours...
</div>
```

### Patterns ARIA Courants

#### Dialog (Modal)

```html
<div 
  role="dialog" 
  aria-modal="true"
  aria-labelledby="modal-title"
>
  <h2 id="modal-title">Titre</h2>
  <p>Contenu...</p>
  <button>Fermer</button>
</div>
```

#### Tabs

```html
<div role="tablist" aria-label="Options">
  <button role="tab" aria-selected="true" aria-controls="panel1">
    Tab 1
  </button>
  <button role="tab" aria-selected="false" aria-controls="panel2">
    Tab 2
  </button>
</div>
<div role="tabpanel" id="panel1" aria-labelledby="tab1">
  Contenu panel 1
</div>
<div role="tabpanel" id="panel2" aria-labelledby="tab2" hidden>
  Contenu panel 2
</div>
```

#### Menu

```html
<button aria-haspopup="true" aria-expanded="false">
  Menu
</button>
<ul role="menu">
  <li role="menuitem">Option 1</li>
  <li role="menuitem">Option 2</li>
</ul>
```

---

## Formulaires Accessibles

### Labels Associés

```html
<!-- Méthode 1: for/id (recommandée) -->
<label for="email">Email</label>
<input type="email" id="email" name="email">

<!-- Méthode 2: wrapping -->
<label>
  Email
  <input type="email" name="email">
</label>

<!-- Méthode 3: aria-labelledby -->
<span id="email-label">Email</span>
<input type="email" aria-labelledby="email-label">
```

### Erreurs Accessibles

```html
<label for="email">Email</label>
<input 
  type="email" 
  id="email"
  aria-invalid="true"
  aria-describedby="email-error"
>
<p id="email-error" role="alert">
  Format d'email invalide
</p>
```

### Autocomplete

```html
<input 
  type="text" 
  name="name"
  autocomplete="name"
>
<input 
  type="email" 
  autocomplete="email"
>
<input 
  type="tel" 
  autocomplete="tel"
>
```

### Groupement avec Fieldset

```html
<fieldset>
  <legend>Adresse de livraison</legend>
  <label for="street">Rue</label>
  <input type="text" id="street">
  <!-- ... -->
</fieldset>
```

---

## Images et Médias

### Alt Text Contextuel

```html
<!-- Image informative -->
<img src="chart.png" alt="Ventes Q3 2024: 45% hausse vs Q2">

<!-- Image décorative -->
<img src="decoration.png" alt="" role="presentation">

<!-- Image complexe -->
<figure>
  <img src="infographic.png" alt="Infographie processus" aria-describedby="desc">
  <figcaption id="desc">
    Description détaillée de l'infographie...
  </figcaption>
</figure>

<!-- Image-lien -->
<a href="/home">
  <img src="logo.png" alt="Accueil - Nom de l'entreprise">
</a>
```

### Vidéos Accessibles

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions-fr.vtt" srclang="fr" label="Français">
  <track kind="descriptions" src="descriptions.vtt" srclang="fr">
</video>

<!-- Ou lien vers transcript -->
<p><a href="transcript.html">Lire la transcription</a></p>
```

---

## Motion et Animations

### Respect des Préférences Utilisateur

```css
/* Réduire les animations si demandé */
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

### Règles pour les Animations

| Règle | Description |
|-------|-------------|
| **Pause obligatoire** | Animations >5s doivent pouvoir être pausées |
| **Pas de flash** | Maximum 3 flashs par seconde |
| **Auto-play** | Éviter ou permettre de stopper |

```html
<!-- Bouton pause pour animation -->
<button aria-pressed="false" onclick="toggleAnimation()">
  Pause animation
</button>
```

---

## Checklist Niveau AA

### Contenu

- [ ] Alt text pour toutes les images informatives
- [ ] `alt=""` pour images décoratives
- [ ] Captions pour vidéos
- [ ] Transcripts disponibles

### Structure

- [ ] Hiérarchie de titres logique (h1 → h2 → h3)
- [ ] Landmarks ARIA ou HTML5
- [ ] Langue de la page déclarée (`<html lang="fr">`)
- [ ] Changements de langue marqués (`<span lang="en">`)

### Navigation

- [ ] Navigation clavier complète
- [ ] Focus visible sur tous les éléments
- [ ] Tab order logique
- [ ] Skip link vers contenu principal
- [ ] Pas de piège clavier

### Formulaires

- [ ] Labels associés à tous les champs
- [ ] Messages d'erreur accessibles
- [ ] Instructions claires
- [ ] Autocomplete approprié

### Visuel

- [ ] Contraste texte 4.5:1 minimum
- [ ] Contraste UI 3:1 minimum
- [ ] Zoom 200% sans perte de contenu
- [ ] Pas d'information par couleur seule

### Interactif

- [ ] États focus/hover/active distincts
- [ ] Cibles tactiles minimum 44x44px
- [ ] Feedback sur actions (loading, success, error)

---

## Outils de Test

### Automatisés

| Outil | Type | Usage |
|-------|------|-------|
| **axe DevTools** | Extension | Audit détaillé, intégration CI |
| **Lighthouse** | Chrome | Audit rapide, score |
| **WAVE** | Extension | Visualisation des problèmes |
| **Pa11y** | CLI | Intégration CI/CD |

### Manuels

| Test | Comment |
|------|---------|
| **Clavier seul** | Débrancher la souris, naviguer avec Tab |
| **Screen reader** | VoiceOver (Mac), NVDA (Windows), TalkBack (Android) |
| **Zoom 200%** | Ctrl/Cmd + jusqu'à 200% |
| **Mode contraste élevé** | Paramètres système |

### Commandes Screen Reader

#### VoiceOver (Mac)

- `Cmd + F5` : Activer/désactiver
- `Ctrl + Option + flèches` : Naviguer
- `Ctrl + Option + Space` : Activer

#### NVDA (Windows)

- `Insert + Space` : Mode formulaire
- `H` : Titre suivant
- `Tab` : Élément focusable suivant

---

## Anti-Patterns

| Anti-Pattern | Problème | Solution |
|--------------|----------|----------|
| `outline: none` sans alternative | Focus invisible | Style `:focus-visible` |
| `div` cliquable sans role | Non accessible clavier | `<button>` ou `role="button"` + tabindex |
| Placeholder comme label | Disparaît au focus | Label visible + placeholder |
| `aria-hidden="true"` sur contenu focusable | Confusion screen reader | Retirer du tab order aussi |
| Auto-play vidéo avec son | Perturbant | Muet par défaut ou pas d'auto-play |
