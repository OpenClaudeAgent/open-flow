---
name: ui-colors
description: Theorie des couleurs UI - Palettes, harmonies, contraste WCAG, dark mode
---

# Skill UI Colors

Ce skill contient la theorie des couleurs appliquee au design d'interface utilisateur : creation de palettes, harmonies, accessibilite et adaptation au dark mode.

---

## Fondamentaux

### Roue Chromatique

La roue chromatique est l'outil fondamental pour comprendre les relations entre couleurs.

**Couleurs Primaires:**
- Rouge, Jaune, Bleu
- Ne peuvent pas etre creees par melange

**Couleurs Secondaires:**
- Orange (rouge + jaune)
- Vert (jaune + bleu)
- Violet (bleu + rouge)

**Couleurs Tertiaires:**
- Melange d'une primaire et d'une secondaire adjacente
- Ex: Rouge-orange, Bleu-vert, Jaune-vert

---

### Modele HSL (Hue, Saturation, Lightness)

Le modele HSL est plus intuitif que RGB pour creer des palettes coherentes.

**Hue (Teinte) : 0-360°**
```
0°/360° : Rouge
60°     : Jaune
120°    : Vert
180°    : Cyan
240°    : Bleu
300°    : Magenta
```

**Saturation : 0-100%**
- 0% : Gris (aucune couleur)
- 50% : Couleur desaturee/douce
- 100% : Couleur pure et vive

**Lightness (Luminosite) : 0-100%**
- 0% : Noir
- 50% : Couleur pure
- 100% : Blanc

**Regle pratique:**
- Pour des variations d'une meme couleur, garde le Hue fixe
- Ajuste Saturation et Lightness pour creer tes nuances

---

## Harmonies de Couleurs

### 1. Monochromatique

Une seule teinte avec variations de saturation et luminosite.

**Avantages:**
- Toujours harmonieux
- Elegant et sophistique
- Facile a implementer

**Usage UI:**
- Interfaces minimalistes
- Dashboards data-focused
- Applications professionnelles

---

### 2. Analogues

2-3 couleurs adjacentes sur la roue (30° d'ecart).

**Exemples:**
- Bleu → Bleu-vert → Vert
- Orange → Rouge-orange → Rouge

**Avantages:**
- Naturellement harmonieux
- Transition douce
- Confortable pour l'oeil

**Usage UI:**
- Applications creatives
- Sites lifestyle/bien-etre
- Interfaces douces et accueillantes

---

### 3. Complementaires

Couleurs opposees sur la roue (180°).

**Exemples:**
- Bleu ↔ Orange
- Rouge ↔ Vert
- Violet ↔ Jaune

**Avantages:**
- Fort contraste
- Dynamique et energique
- Attire l'attention

**Usage UI:**
- Call-to-action
- Elements a mettre en valeur
- Attention : utiliser avec parcimonie

---

### 4. Split-Complementaires

Une couleur + les deux adjacentes de sa complementaire.

**Exemple:**
- Bleu + Orange-jaune + Orange-rouge

**Avantages:**
- Contraste fort mais moins tendu
- Plus de flexibilite que complementaires pures

---

### 5. Triadiques

Trois couleurs equidistantes (120°).

**Exemples:**
- Rouge, Jaune, Bleu (primaires)
- Orange, Vert, Violet (secondaires)

**Avantages:**
- Equilibre visuel
- Palette riche mais harmonieuse

**Usage UI:**
- Applications ludiques
- Interfaces enfants
- Marques expressives

---

### Regle 60-30-10

Distribution ideale des couleurs dans une interface:

```
60% : Couleur dominante (fond, surfaces)
      → Neutre ou couleur tres claire

30% : Couleur secondaire (composants, cartes)
      → Variations de la dominante ou secondaire douce

10% : Couleur d'accent (CTA, liens, focus)
      → Couleur primaire vive
```

**Exemple concret:**
- 60% : Fond blanc/gris clair
- 30% : Cartes blanches, texte gris fonce
- 10% : Boutons bleus, liens, icones actives

---

## Psychologie des Couleurs

### Bleu
- **Associations:** Confiance, stabilite, professionnalisme, calme
- **Usage:** Finance, tech, reseaux sociaux, sante
- **Exemples:** Facebook, LinkedIn, PayPal, IBM

### Rouge
- **Associations:** Urgence, energie, passion, danger, excitation
- **Usage:** Alertes, promotions, nourriture, divertissement
- **Exemples:** YouTube, Netflix, Coca-Cola

### Vert
- **Associations:** Succes, nature, croissance, sante, argent
- **Usage:** Validation, eco-friendly, finance, sante
- **Exemples:** Spotify, WhatsApp, Starbucks

### Orange
- **Associations:** Energie, creativite, accessibilite, chaleur
- **Usage:** CTA, avertissements doux, marques jeunes
- **Exemples:** Firefox, SoundCloud, Amazon (boutons)

### Jaune
- **Associations:** Optimisme, attention, avertissement
- **Usage:** Highlights, warnings, marques joyeuses
- **Attention:** Difficile a lire sur fond clair

### Violet
- **Associations:** Luxe, creativite, mystere, sagesse
- **Usage:** Marques premium, tech creative
- **Exemples:** Twitch, Cadbury

### Noir
- **Associations:** Elegance, luxe, sophistication, puissance
- **Usage:** Mode, luxe, tech premium
- **Exemples:** Apple, Chanel, Nike

### Blanc
- **Associations:** Purete, simplicite, minimalisme, espace
- **Usage:** Fond par defaut, interfaces clean

---

## Structure d'une Palette UI

```
Palette UI Complete
├── Primary (1-2 couleurs d'accent)
│   └── primary-50 → primary-900 (10 nuances)
│
├── Secondary (optionnel)
│   └── secondary-50 → secondary-900
│
├── Accent (1 couleur)
│   └── Pour highlights specifiques
│
├── Neutrals (gris)
│   ├── neutral-50   (presque blanc)
│   ├── neutral-100
│   ├── neutral-200
│   ├── neutral-300
│   ├── neutral-400
│   ├── neutral-500  (gris moyen)
│   ├── neutral-600
│   ├── neutral-700
│   ├── neutral-800
│   └── neutral-900  (presque noir)
│
└── Semantic (couleurs fonctionnelles)
    ├── Success (vert)
    │   └── success-light, success, success-dark
    ├── Warning (orange/jaune)
    │   └── warning-light, warning, warning-dark
    ├── Error (rouge)
    │   └── error-light, error, error-dark
    └── Info (bleu)
        └── info-light, info, info-dark
```

### Generation d'une Echelle de Couleurs

Pour creer une echelle de 50 a 900 depuis une couleur base:

```
50   : Lightness 97%  (fond tres clair)
100  : Lightness 94%
200  : Lightness 86%
300  : Lightness 74%
400  : Lightness 62%
500  : Lightness 50%  (couleur base)
600  : Lightness 40%
700  : Lightness 32%
800  : Lightness 24%
900  : Lightness 16%  (texte sur fond clair)
```

---

## Contraste et Accessibilite (WCAG)

### Ratios de Contraste Minimum

**Niveau AA (minimum recommande):**
- Texte normal : 4.5:1
- Grand texte (18px+ ou 14px+ bold) : 3:1
- Elements UI et graphiques : 3:1

**Niveau AAA (optimal):**
- Texte normal : 7:1
- Grand texte : 4.5:1

### Calcul du Ratio

```
Ratio = (L1 + 0.05) / (L2 + 0.05)

Ou L1 = luminance de la couleur la plus claire
   L2 = luminance de la couleur la plus foncee
```

### Usages par Ratio

| Ratio | Usage recommande |
|-------|------------------|
| 21:1  | Maximum (noir sur blanc) |
| 7:1+  | Texte principal (AAA) |
| 4.5:1 | Texte principal (AA), grand texte (AAA) |
| 3:1   | Grand texte (AA), icones, bordures |
| < 3:1 | Decoratif uniquement |

### Checklist Accessibilite Couleurs

- [ ] Texte principal sur fond : ratio ≥ 4.5:1
- [ ] Texte secondaire sur fond : ratio ≥ 4.5:1
- [ ] Liens distinguables (pas uniquement par couleur)
- [ ] Etats focus visibles : ratio ≥ 3:1
- [ ] Bordures des inputs : ratio ≥ 3:1
- [ ] Icones fonctionnelles : ratio ≥ 3:1
- [ ] Ne pas transmettre info uniquement par couleur
- [ ] Test avec simulateur de daltonisme

### Types de Daltonisme

**Protanopie/Deuteranopie (rouge-vert):**
- ~8% des hommes affectes
- Rouge et vert se confondent
- Solution : Ne pas opposer rouge/vert seuls

**Tritanopie (bleu-jaune):**
- Plus rare
- Bleu et jaune se confondent

**Achromatopsie:**
- Vision en nuances de gris
- Tres rare

---

## Dark Mode

### Principes Fondamentaux

**Ne pas simplement inverser les couleurs!**

Le dark mode n'est pas `filter: invert(1)`. Il necessite une reflexion specifique.

### Surfaces et Elevation

En dark mode, les surfaces elevees sont PLUS CLAIRES (inverse du light mode).

```
Light Mode:           Dark Mode:
Surface haute  ──┐    Surface haute  ──┐
  (ombre)        │      (plus clair)   │
Surface base ────┘    Surface base ────┘
```

**Echelle d'elevation dark:**
```
dp0  : #121212 (surface de base)
dp1  : #1e1e1e (cards)
dp2  : #232323 (navigation)
dp3  : #252525 (drawers)
dp4  : #272727 (app bars)
dp6  : #2c2c2c (menus)
dp8  : #2e2e2e (modals)
dp12 : #333333 (dialogs)
dp16 : #353535 (pickers)
dp24 : #383838 (elevation max)
```

### Couleurs en Dark Mode

**Saturation:**
- Reduire la saturation des couleurs primaires (70-80%)
- Les couleurs trop vives agressent sur fond sombre

**Couleurs semantiques:**
- Success : Passer d'un vert sature a un vert desature
- Error : Rouge moins vif, plus saumon
- Warning : Orange moins intense

**Texte:**
- Texte principal : #FFFFFF avec 87% opacite
- Texte secondaire : #FFFFFF avec 60% opacite
- Texte desactive : #FFFFFF avec 38% opacite

### Tokens pour Dual Theme

```css
/* Light Mode */
:root {
  --color-surface: #ffffff;
  --color-surface-elevated: #f5f5f5;
  --color-text-primary: rgba(0, 0, 0, 0.87);
  --color-text-secondary: rgba(0, 0, 0, 0.60);
  --color-primary: hsl(220, 90%, 50%);
}

/* Dark Mode */
[data-theme="dark"] {
  --color-surface: #121212;
  --color-surface-elevated: #1e1e1e;
  --color-text-primary: rgba(255, 255, 255, 0.87);
  --color-text-secondary: rgba(255, 255, 255, 0.60);
  --color-primary: hsl(220, 70%, 60%); /* desature + eclairci */
}
```

### Checklist Dark Mode

- [ ] Surfaces elevees plus claires (pas d'ombres noires)
- [ ] Couleurs primaires desaturees
- [ ] Contraste texte verifie (≥ 4.5:1)
- [ ] Pas de blanc pur (#fff) → utiliser opacite
- [ ] Pas de noir pur (#000) comme surface → #121212
- [ ] Couleurs semantiques ajustees
- [ ] Icones et illustrations adaptees
- [ ] Test en conditions reelles (ecran OLED)

---

## Design Tokens CSS Recommandes

### Structure Complete

```css
:root {
  /* === PRIMARY === */
  --color-primary-50: hsl(220, 90%, 97%);
  --color-primary-100: hsl(220, 90%, 94%);
  --color-primary-200: hsl(220, 90%, 86%);
  --color-primary-300: hsl(220, 90%, 74%);
  --color-primary-400: hsl(220, 90%, 62%);
  --color-primary-500: hsl(220, 90%, 50%);
  --color-primary-600: hsl(220, 90%, 40%);
  --color-primary-700: hsl(220, 90%, 32%);
  --color-primary-800: hsl(220, 90%, 24%);
  --color-primary-900: hsl(220, 90%, 16%);

  /* === NEUTRALS (teinte de blue) === */
  --color-neutral-50: hsl(220, 20%, 98%);
  --color-neutral-100: hsl(220, 15%, 95%);
  --color-neutral-200: hsl(220, 12%, 88%);
  --color-neutral-300: hsl(220, 10%, 75%);
  --color-neutral-400: hsl(220, 8%, 60%);
  --color-neutral-500: hsl(220, 6%, 45%);
  --color-neutral-600: hsl(220, 8%, 35%);
  --color-neutral-700: hsl(220, 10%, 25%);
  --color-neutral-800: hsl(220, 12%, 18%);
  --color-neutral-900: hsl(220, 15%, 10%);

  /* === SEMANTIC === */
  /* Success */
  --color-success-light: hsl(145, 65%, 92%);
  --color-success: hsl(145, 65%, 42%);
  --color-success-dark: hsl(145, 65%, 32%);

  /* Warning */
  --color-warning-light: hsl(38, 95%, 92%);
  --color-warning: hsl(38, 95%, 50%);
  --color-warning-dark: hsl(38, 95%, 38%);

  /* Error */
  --color-error-light: hsl(0, 85%, 95%);
  --color-error: hsl(0, 85%, 55%);
  --color-error-dark: hsl(0, 85%, 40%);

  /* Info */
  --color-info-light: hsl(205, 85%, 92%);
  --color-info: hsl(205, 85%, 50%);
  --color-info-dark: hsl(205, 85%, 38%);

  /* === SURFACES === */
  --color-background: var(--color-neutral-50);
  --color-surface: #ffffff;
  --color-surface-elevated: var(--color-neutral-100);

  /* === TEXT === */
  --color-text-primary: var(--color-neutral-900);
  --color-text-secondary: var(--color-neutral-600);
  --color-text-disabled: var(--color-neutral-400);
  --color-text-inverse: #ffffff;

  /* === BORDERS === */
  --color-border: var(--color-neutral-200);
  --color-border-strong: var(--color-neutral-300);
}
```

### Usage des Tokens

```css
.button-primary {
  background-color: var(--color-primary-500);
  color: var(--color-text-inverse);
}

.button-primary:hover {
  background-color: var(--color-primary-600);
}

.card {
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
}

.alert-success {
  background-color: var(--color-success-light);
  color: var(--color-success-dark);
  border-left: 4px solid var(--color-success);
}
```

---

## Outils Recommandes

### Creation de Palettes

- **Coolors** (coolors.co) - Generation rapide
- **Adobe Color** (color.adobe.com) - Harmonies avancees
- **Huemint** (huemint.com) - IA pour palettes
- **Realtime Colors** (realtimecolors.com) - Preview en contexte

### Verification du Contraste

- **WebAIM Contrast Checker** (webaim.org/resources/contrastchecker)
- **Colour Contrast Analyser** (TPGi) - Application desktop
- **Stark** - Plugin Figma/Sketch

### Test Daltonisme

- **Sim Daltonism** (macOS) - Simulation temps reel
- **Colorblindly** - Extension Chrome
- **Coblis** (color-blindness.com/coblis-color-blindness-simulator)

### Extensions Dev

- **VisBug** - Inspection visuelle
- **CSS Overview** (Chrome DevTools) - Analyse des couleurs utilisees
- **ColorZilla** - Pipette avancee

---

## Checklist Finale Couleurs

### Palette
- [ ] Palette limitee (1-2 primaires, 1 accent, neutres, semantiques)
- [ ] Echelle de nuances complete (50-900)
- [ ] Neutrals teintes (pas de gris purs)
- [ ] Couleurs semantiques definies

### Harmonie
- [ ] Schema de couleurs identifie (mono, analogues, etc.)
- [ ] Regle 60-30-10 respectee
- [ ] Coherence dans toute l'application

### Accessibilite
- [ ] Contraste texte ≥ 4.5:1 (AA)
- [ ] Contraste elements UI ≥ 3:1
- [ ] Info non transmise uniquement par couleur
- [ ] Test daltonisme effectue

### Dark Mode (si applicable)
- [ ] Surfaces elevees plus claires
- [ ] Couleurs desaturees
- [ ] Texte avec opacite (pas blanc/noir purs)
- [ ] Tokens CSS pour switch facile

---

## Anti-Patterns

- **Trop de couleurs** : 3-4 couleurs max + neutres
- **Gris pur** : Toujours teinter subtilement
- **Saturation maximale partout** : Fatigant pour l'oeil
- **Couleur = seule differenciation** : Ajouter forme/texte/icone
- **Dark mode = inversion** : Necessite design specifique
- **Ignorer les contrastes** : Toujours verifier WCAG
- **Couleurs aleatoires** : Toujours partir d'une harmonie

---

## Mantras

- "Moins de couleurs, plus d'impact"
- "Le contraste n'est pas optionnel"
- "Les neutres font 90% du travail"
- "Saturation elevee = a utiliser avec parcimonie"
- "Dark mode est un design, pas un filtre"
