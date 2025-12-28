---
name: ui-design-principles
description: Principes de design UI - Hierarchie visuelle, espacement, couleurs, typographie, composants
---

# Skill UI Design Principles

Ce skill contient les principes fondamentaux du design d'interface utilisateur pour creer des UIs elegantes et modernes.

---

## Philosophie

> "Le bon design est invisible. L'utilisateur ne remarque pas l'interface, il accomplit simplement ses objectifs avec plaisir."

Privilegier :
- **L'elegance** sur la complexite
- **L'espace** sur l'encombrement
- **La subtilite** sur l'exuberance
- **La coherence** sur la variete
- **La clarte** sur la decoration

---

## Principes Visuels Fondamentaux

### 1. Hierarchie Visuelle

L'oeil doit savoir immediatement ou regarder.

**Techniques:**
- Taille : Les elements importants sont plus grands
- Poids : Le texte important est plus gras
- Couleur : Les accents attirent l'attention
- Position : Le contenu cle est place en haut/centre
- Espace : L'isolation cree de l'importance

**Regle:** Un seul point focal par ecran/section. Si tout est important, rien ne l'est.

---

### 2. Espace Blanc (Negative Space)

L'espace vide n'est pas du gaspillage, c'est du design.

**Principes:**
- Padding genereux a l'interieur des composants
- Marges confortables entre les elements
- Les groupes sont separes par plus d'espace que leurs elements internes
- Le contenu respire, il n'est jamais colle aux bords

**Regle d'or:** Quand tu hesites, ajoute plus d'espace. Une UI aeree parait toujours plus professionnelle qu'une UI dense.

---

### 3. Systeme d'Espacement

Utilise un systeme coherent base sur un multiplicateur.

**Echelle recommandee (base 4px ou 8px):**
```
xs:  4px   - Espacement minimal, details fins
sm:  8px   - Entre elements lies
md:  16px  - Padding standard des composants
lg:  24px  - Entre sections liees
xl:  32px  - Entre sections distinctes
2xl: 48px  - Separations majeures
3xl: 64px  - Marges de page, grands espaces
```

**Regle:** Ne jamais utiliser de valeurs arbitraires. Tout espacement doit etre un multiple du systeme.

---

### 4. Couleurs

#### Palette Moderne

**Structure d'une bonne palette:**
- 1 couleur primaire (action principale, accent)
- 1-2 couleurs neutres (texte, fonds, bordures)
- 1 couleur de succes (vert)
- 1 couleur d'erreur (rouge)
- 1 couleur d'avertissement (orange/jaune)

**Neutres sophistiques:**
Ne jamais utiliser du gris pur (#808080). Ajoute une teinte subtile:
- Gris chaud : teinte de beige/brun
- Gris froid : teinte de bleu
- Gris colore : teinte de ta couleur primaire

**Ratios recommandes:**
- 60% : Couleur dominante (fond, surfaces)
- 30% : Couleur secondaire (composants, cartes)
- 10% : Couleur d'accent (boutons, liens, focus)

**Contraste:**
- Texte principal : ratio minimum 7:1
- Texte secondaire : ratio minimum 4.5:1
- Elements interactifs : clairement distinguables

---

### 5. Typographie

#### Hierarchie

```
Display/Hero:   32-48px  - Titres de page, hero sections
Heading 1:      24-32px  - Titres de section
Heading 2:      20-24px  - Sous-sections
Heading 3:      16-18px  - Titres de composants
Body:           14-16px  - Texte principal
Caption:        12-14px  - Texte secondaire, labels
Small:          10-12px  - Mentions legales, timestamps
```

#### Regles

- **2 fonts maximum** : Une pour les titres, une pour le corps (ou une seule partout)
- **Line-height confortable** : 1.4-1.6 pour le corps de texte
- **Largeur de ligne** : 60-80 caracteres max pour la lisibilite
- **Poids** : Utilise les variations (300, 400, 500, 600, 700) pour la hierarchie

#### Fonts Modernes Recommandees

**Sans-serif (clean, moderne):**
- Inter, SF Pro, Segoe UI
- Plus rond : Nunito, Poppins, Quicksand

**Monospace (code, donnees):**
- JetBrains Mono, Fira Code, SF Mono

---

### 6. Ombres et Elevation

Les ombres creent la profondeur et la hierarchie.

**Principes:**
- Ombres douces et diffuses, jamais dures
- Plus l'element est eleve, plus l'ombre est large et douce
- Couleur d'ombre : noir avec opacite faible (5-15%), ou teintee

**Echelle d'elevation:**
```
Level 0 (flat):     Pas d'ombre - elements au niveau de la surface
Level 1 (raised):   Ombre subtile - cartes, boutons au repos
Level 2 (floating): Ombre moyenne - dropdowns, popovers
Level 3 (overlay):  Ombre prononcee - modals, dialogues
```

**Exemple conceptuel:**
```
Subtle:  0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06)
Medium:  0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06)
Large:   0 10px 20px rgba(0,0,0,0.10), 0 6px 6px rgba(0,0,0,0.06)
```

---

### 7. Coins Arrondis

Les coins arrondis adoucissent l'interface et la rendent plus accueillante.

**Echelle:**
```
none:   0px     - Elements qui doivent se fondre (full-width)
sm:     4px     - Petits elements (badges, chips)
md:     8px     - Elements standards (boutons, inputs)
lg:     12-16px - Cartes, conteneurs
xl:     24px    - Grandes cartes, modals
full:   9999px  - Pills, avatars circulaires
```

**Regle de coherence:** Les elements enfants ont des coins egaux ou plus petits que leurs parents.

---

### 8. Bordures

Les bordures definissent et separent.

**Principes:**
- Epaisseur : 1px suffit presque toujours
- Couleur : Subtile, jamais noire pure (utilise gris clair ou couleur attenuee)
- Usage : Pour delimiter, pas pour decorer

**Alternatives aux bordures:**
- Difference de couleur de fond
- Espace blanc
- Ombre subtile

---

## Patterns de Composants

### Boutons

**Hierarchie:**
1. **Primary** : Action principale, couleur pleine, contraste fort
2. **Secondary** : Actions secondaires, outline ou fond neutre
3. **Ghost/Text** : Actions tertiaires, fond transparent

**Etats:**
- Default : Etat de base
- Hover : Legere modification (assombrir/eclaircir 10%)
- Pressed : Plus prononce que hover
- Focused : Ring/outline visible pour accessibilite
- Disabled : Opacite reduite (50-60%), curseur interdit

**Tailles:**
- Small : Padding reduit, contextes denses
- Medium : Taille par defaut
- Large : CTAs importants, hero sections

---

### Cards

**Anatomie:**
- Fond distinct de la surface (plus clair ou plus sombre)
- Padding interne genereux (16-24px)
- Coins arrondis coherents (8-16px)
- Ombre optionnelle pour l'elevation

**Spacing interne:**
- Header/Body/Footer clairement separes
- Hierarchie visuelle dans le contenu
- Actions groupees en bas ou en haut a droite

---

### Inputs et Forms

**Principes:**
- Labels toujours visibles (pas de placeholder-only)
- Etats clairs : default, focus, error, disabled
- Messages d'erreur sous le champ, en rouge
- Espacement vertical genereux entre les champs (16-24px)

**Focus state:**
- Ring/outline colore (couleur primaire)
- Jamais juste un changement de bordure subtil

---

### Navigation

**Principes:**
- Element actif clairement distinguable
- Hover states subtils mais visibles
- Coherence dans tout l'app
- Icones + texte > icones seules (sauf espace contraint)

---

## Checklist "Belle UI"

Avant de finaliser, verifier:

### Couleurs
- [ ] Palette limitee et coherente
- [ ] Contraste suffisant pour la lisibilite
- [ ] Pas de couleurs criardes ou saturees a l'exces
- [ ] Les gris ont une teinte subtile

### Espacement
- [ ] Systeme d'espacement coherent
- [ ] Assez d'espace blanc
- [ ] Padding genereux dans les composants
- [ ] Groupes visuels clairs

### Typographie
- [ ] Hierarchie claire (tailles, poids)
- [ ] Maximum 2 fonts
- [ ] Texte lisible (taille, contraste, line-height)

### Composants
- [ ] Coins arrondis coherents
- [ ] Ombres subtiles et appropriees
- [ ] Etats interactifs definis (hover, focus, active)
- [ ] Bordures subtiles ou absentes

### Harmonie
- [ ] Un seul point focal par vue
- [ ] Alignements respectes
- [ ] Coherence dans tout le design

---

## Anti-Patterns a Eviter

### Visuels

- **Trop de couleurs** : Limite-toi a ta palette
- **Ombres dures** : Toujours diffuses et subtiles
- **Bordures epaisses** : 1px max, couleur attenuee
- **Coins arrondis inconsistants** : Meme rayon pour elements similaires
- **Texte sur image sans overlay** : Toujours assurer la lisibilite
- **Gris pur (#808080, #cccccc)** : Toujours teinter subtilement

### Spacing

- **Elements colles aux bords** : Toujours du padding
- **Espacement inconsistant** : Utilise ton systeme
- **Manque d'air** : En cas de doute, ajoute de l'espace
- **Valeurs arbitraires** : Pas de "13px" ou "27px"

### Typographie

- **Trop de fonts** : 2 maximum
- **Trop de tailles** : Utilise une echelle definie
- **Texte trop petit** : 14px minimum pour le corps
- **Lignes trop longues** : 80 caracteres max

### Interactions

- **Hover invisible** : Doit etre perceptible
- **Focus invisible** : Critique pour l'accessibilite
- **Etats manquants** : Chaque element interactif a tous ses etats

---

## Processus de Design

### 1. Structure d'abord
- Definis la hierarchie de l'information
- Place les elements principaux
- Etablis la grille/layout

### 2. Spacing ensuite
- Applique ton systeme d'espacement
- Cree les groupes visuels
- Assure-toi que ca respire

### 3. Couleurs et style
- Applique ta palette
- Ajoute les ombres/elevations
- Finalise les details visuels

### 4. Polish
- Verifie les alignements
- Harmonise les details
- Teste les etats interactifs

---

## Mantras

- "Quand tu hesites, enleve plutot qu'ajoute"
- "L'espace blanc est ton ami"
- "La coherence bat l'originalite"
- "Simple n'est pas ennuyeux, simple est elegant"
- "Chaque pixel doit avoir une raison d'etre"
