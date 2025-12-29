---
name: clean-code
description: Principes de code propre - Nommage, fonctions, DRY, KISS, YAGNI
---

# Skill Clean Code

Ce skill contient les principes fondamentaux pour ecrire du code propre, lisible et maintenable.

---

## Principes fondamentaux

### DRY - Don't Repeat Yourself

Chaque piece de connaissance doit avoir une representation unique et non ambigue.

**Symptomes de violation** :
- Copier-coller de code
- Logique dupliquee dans plusieurs endroits
- Constantes repetees

**Solutions** :
- Extraire en fonction/methode
- Creer des abstractions
- Centraliser les constantes

### KISS - Keep It Simple, Stupid

La simplicite est la sophistication ultime.

**Symptomes de violation** :
- Sur-ingenierie
- Abstractions prematurees
- Solutions complexes pour problemes simples

**Solutions** :
- Commencer simple, complexifier si necessaire
- Preferer la lisibilite a la cleverness
- Resoudre le probleme actuel, pas les futurs hypothetiques

### YAGNI - You Ain't Gonna Need It

Ne pas implementer quelque chose tant que ce n'est pas necessaire.

**Symptomes de violation** :
- Features "au cas ou"
- Abstractions pour des cas d'usage inexistants
- Configuration pour des scenarios improbables

**Solutions** :
- Implementer le minimum requis
- Ajouter quand le besoin est reel
- Refactorer plutot que prevoir

---

## Nommage

### Variables

| Type | Convention | Exemple |
|------|------------|---------|
| Boolean | is/has/can/should prefix | `isVisible`, `hasError`, `canEdit` |
| Collection | Pluriel | `users`, `items`, `errors` |
| Compteur | count/num suffix | `userCount`, `numItems` |

### Fonctions

| Type | Convention | Exemple |
|------|------------|---------|
| Action | Verbe + nom | `getUser`, `saveDocument`, `validateInput` |
| Boolean | is/has/can prefix | `isValid`, `hasPermission` |
| Transformation | to + type | `toString`, `toJson` |
| Event handler | on + event | `onClick`, `onSubmit` |

### Classes

| Type | Convention | Exemple |
|------|------------|---------|
| Entite | Nom singulier | `User`, `Document` |
| Service | Nom + Service | `AuthService`, `PaymentService` |
| Repository | Nom + Repository | `UserRepository` |
| Factory | Nom + Factory | `ConnectionFactory` |

### Regles generales

- Noms descriptifs et prononçables
- Eviter les abreviations obscures
- Longueur proportionnelle au scope
- Coherence dans tout le projet

---

## Fonctions

### Taille

- **Idealement** : 5-15 lignes
- **Maximum** : 20-30 lignes
- Si plus long : extraire des sous-fonctions

### Parametres

| Nombre | Verdict |
|--------|---------|
| 0 | Ideal |
| 1-2 | Bien |
| 3 | Acceptable |
| 4+ | Refactorer (objet parametre) |

### Single Responsibility

Une fonction = une seule chose.

```
// MAUVAIS
function processUser(user) {
    validate(user);
    save(user);
    sendEmail(user);
    log(user);
}

// BON
function processUser(user) {
    validateUser(user);
    saveUser(user);
    notifyUser(user);
}
```

### Niveau d'abstraction

Une fonction doit rester a un seul niveau d'abstraction.

```
// MAUVAIS - Melange haut et bas niveau
function renderPage() {
    const html = "<html>";
    loadData();
    processTemplates();
    return html + "</html>";
}

// BON - Un seul niveau
function renderPage() {
    const data = loadData();
    const content = processTemplates(data);
    return wrapInHtml(content);
}
```

---

## Commentaires

### Bons commentaires

- **Intention** : Pourquoi, pas comment
- **Clarification** : Regex complexes, algos
- **Warning** : Consequences, pieges
- **TODO** : Temporaires, avec ticket

### Mauvais commentaires

- Paraphrase du code
- Code commente
- Journaux de modifications
- Bruit ("constructeur par defaut")

### Regle d'or

Si tu as besoin d'un commentaire, demande-toi d'abord si le code peut etre plus clair.

---

## Structure

### Early return

```
// MAUVAIS
function process(data) {
    if (data) {
        if (data.valid) {
            // ... 50 lignes
        }
    }
}

// BON
function process(data) {
    if (!data) return;
    if (!data.valid) return;
    // ... 50 lignes
}
```

### Avoid nesting

Maximum 2-3 niveaux d'indentation.

### Positive conditions

```
// MAUVAIS
if (!isNotValid)

// BON
if (isValid)
```

---

## Code smells

| Smell | Description | Solution |
|-------|-------------|----------|
| Long method | Fonction trop longue | Extraire |
| Large class | Classe trop grosse | Separer responsabilites |
| Long parameter list | Trop de params | Objet parametre |
| Duplicate code | Copier-coller | Extraire fonction/classe |
| Dead code | Code non utilise | Supprimer |
| Magic numbers | Valeurs hardcodees | Constantes nommees |
| Feature envy | Methode utilise trop une autre classe | Deplacer |
| Data clumps | Groupes de donnees repetees | Creer objet |

---

## Checklist

- [ ] Noms descriptifs et coherents
- [ ] Fonctions courtes (< 20 lignes)
- [ ] Fonctions avec peu de parametres (< 4)
- [ ] Un seul niveau d'abstraction par fonction
- [ ] Pas de duplication
- [ ] Pas de magic numbers
- [ ] Pas de code commente
- [ ] Early returns utilises
- [ ] Maximum 2-3 niveaux d'indentation
