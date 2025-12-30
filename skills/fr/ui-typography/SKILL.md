---
name: ui-typography
description: Typographie UI - Échelles, hiérarchie, lisibilité, responsive, accessibilité
---

# Typographie UI

## Classifications des Polices

### Serif
- Empattements aux extrémités des lettres
- Classique, traditionnel, formel
- **Usage** : Longs textes imprimés, éditorial, luxe
- **Exemples** : Georgia, Times New Roman, Merriweather

### Sans-serif
- Sans empattements, lignes épurées
- Moderne, minimaliste, lisible sur écran
- **Usage** : UI, web, mobile, corps de texte digital
- **Exemples** : Inter, Roboto, Open Sans, SF Pro

### Monospace
- Largeur fixe pour chaque caractère
- Technique, code, données
- **Usage** : Éditeurs de code, terminaux, tableaux de données
- **Exemples** : JetBrains Mono, Fira Code, SF Mono

### Display
- Décoratives, expressives, impact visuel
- **Usage** : Titres, logos, accroches (jamais body text)
- **Exemples** : Playfair Display, Lobster, Impact

---

## Hiérarchie Typographique

Échelle basée sur le ratio 1.25 (Major Third) :

```
h1    → 2.441rem  (39px)  — Titre principal
h2    → 1.953rem  (31px)  — Sections majeures
h3    → 1.563rem  (25px)  — Sous-sections
h4    → 1.25rem   (20px)  — Sous-titres
body  → 1rem      (16px)  — Texte courant
small → 0.8rem    (13px)  — Annotations, légendes
```

### Règles de hiérarchie
- **Maximum 3-4 niveaux** visibles simultanément
- **Contraste suffisant** entre chaque niveau (min 1.25x)
- **Cohérence** : même police pour tous les headings

---

## Échelle Typographique

### Ratio 1.25 (Major Third) — Recommandé
```
base × 1.25^n

n=-1 → 0.8rem    (small)
n=0  → 1rem      (body)
n=1  → 1.25rem   (h4)
n=2  → 1.563rem  (h3)
n=3  → 1.953rem  (h2)
n=4  → 2.441rem  (h1)
```

### Autres ratios courants
| Ratio | Nom | Usage |
|-------|-----|-------|
| 1.125 | Major Second | Interfaces compactes |
| 1.25  | Major Third | UI générale (recommandé) |
| 1.333 | Perfect Fourth | Éditorial |
| 1.5   | Perfect Fifth | Titres impact |

### Variables CSS
```css
:root {
  --type-ratio: 1.25;
  --font-size-base: 1rem;
  --font-size-sm: calc(var(--font-size-base) / var(--type-ratio));
  --font-size-lg: calc(var(--font-size-base) * var(--type-ratio));
  --font-size-xl: calc(var(--font-size-lg) * var(--type-ratio));
  --font-size-2xl: calc(var(--font-size-xl) * var(--type-ratio));
  --font-size-3xl: calc(var(--font-size-2xl) * var(--type-ratio));
}
```

---

## Lisibilité

### Line Height (Interligne)
```css
body     → line-height: 1.5;    /* Texte courant */
headings → line-height: 1.2;    /* Titres */
compact  → line-height: 1.3;    /* UI dense */
```

### Letter Spacing (Approche)
```css
body     → letter-spacing: 0;           /* Normal */
headings → letter-spacing: -0.02em;     /* Titres resserrés */
uppercase → letter-spacing: 0.05em;     /* Majuscules espacées */
small    → letter-spacing: 0.01em;      /* Petits textes légèrement espacés */
```

### Longueur de ligne optimale
```css
.content {
  max-width: 65ch;  /* 45-75 caractères recommandés */
}
```

| Contexte | Largeur | Caractères |
|----------|---------|------------|
| Optimal | 65ch | ~65 caractères |
| Minimum | 45ch | ~45 caractères |
| Maximum | 75ch | ~75 caractères |

---

## Typographie Responsive

### Fluid Typography avec clamp()
```css
/* Base responsive */
html {
  font-size: clamp(1rem, 0.5vw + 0.875rem, 1.25rem);
}

/* Titre responsive */
h1 {
  font-size: clamp(1.75rem, 4vw + 1rem, 3rem);
}

/* Formule générique */
font-size: clamp(min, preferred, max);
```

### Breakpoints typographiques
```css
:root {
  --font-size-base: 1rem;
}

@media (min-width: 768px) {
  :root {
    --font-size-base: 1.0625rem; /* 17px */
  }
}

@media (min-width: 1200px) {
  :root {
    --font-size-base: 1.125rem; /* 18px */
  }
}
```

---

## Font Pairing (Appariement)

### Règles fondamentales
1. **Contraste, pas conflit** — Associer des polices différentes mais complémentaires
2. **Maximum 2-3 familles** — Au-delà, incohérence visuelle
3. **Même x-height** — Hauteur de x similaire pour harmonie

### Combinaisons classiques

| Headings | Body | Style |
|----------|------|-------|
| Playfair Display | Source Sans Pro | Éditorial élégant |
| Montserrat | Open Sans | Moderne professionnel |
| Roboto Slab | Roboto | Google Material |
| Lora | Lato | Chaleureux accessible |
| Inter | Inter | Minimaliste (une seule famille) |

### Anti-patterns
- ❌ Deux serif similaires
- ❌ Deux sans-serif trop proches
- ❌ Plus de 3 familles
- ❌ Display font en body text

---

## System Fonts vs Custom

### Stack système recommandé
```css
:root {
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, 
               'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  
  --font-mono: ui-monospace, 'SF Mono', 'Cascadia Code', 
               'Source Code Pro', Menlo, Consolas, monospace;
}
```

### Avantages System Fonts
- ✅ Zéro téléchargement, performance optimale
- ✅ Familiarité native pour l'utilisateur
- ✅ Rendu optimisé par l'OS

### Quand utiliser Custom Fonts
- Branding fort nécessitant une identité unique
- Caractères spéciaux (langues, icônes)
- Exigences typographiques spécifiques

### Fallbacks obligatoires
```css
/* Toujours terminer par une famille générique */
font-family: 'Custom Font', 'Fallback Font', sans-serif;
font-family: 'Code Font', 'Fallback Mono', monospace;
```

---

## Accessibilité

### Taille minimum
```css
body {
  font-size: 1rem;      /* 16px minimum absolu */
  font-size: 1.125rem;  /* 18px recommandé */
}

/* Jamais inférieur à 12px */
.small-text {
  font-size: max(0.75rem, 12px);
}
```

### Contraste texte/fond
| Niveau | Ratio | Usage |
|--------|-------|-------|
| AA | 4.5:1 | Texte normal |
| AA Large | 3:1 | Texte ≥18px ou bold ≥14px |
| AAA | 7:1 | Accessibilité renforcée |

### WCAG Text Spacing
Supporter les ajustements utilisateur sans perte de contenu :
```css
/* L'UI doit rester fonctionnelle avec : */
line-height: 1.5;           /* 1.5× la taille de police */
letter-spacing: 0.12em;     /* 0.12× la taille de police */
word-spacing: 0.16em;       /* 0.16× la taille de police */
/* Espacement paragraphes : 2× la taille de police */
```

### Bonnes pratiques
- ✅ Ne jamais désactiver le zoom utilisateur
- ✅ Utiliser `rem`/`em` (pas `px` pour font-size)
- ✅ Tester avec zoom 200%
- ✅ Éviter le texte justifié (justify)

---

## Tokens CSS Complets

```css
:root {
  /* Tailles */
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  
  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-snug: 1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose: 2;
  
  /* Font Weights */
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Letter Spacing */
  --letter-spacing-tighter: -0.05em;
  --letter-spacing-tight: -0.025em;
  --letter-spacing-normal: 0;
  --letter-spacing-wide: 0.025em;
  --letter-spacing-wider: 0.05em;
  
  /* Font Families */
  --font-sans: system-ui, -apple-system, sans-serif;
  --font-serif: Georgia, Cambria, serif;
  --font-mono: ui-monospace, monospace;
}
```

---

## Checklist Typographie

- [ ] Base font-size ≥ 16px
- [ ] Échelle cohérente (ratio 1.25)
- [ ] Line-height 1.5 pour body text
- [ ] Max-width ~65ch pour les paragraphes
- [ ] Maximum 2-3 familles de polices
- [ ] Fallbacks génériques définis
- [ ] Contraste ≥ 4.5:1 (AA)
- [ ] Unités relatives (rem/em)
- [ ] Test zoom 200% OK
- [ ] Responsive avec clamp() ou media queries
