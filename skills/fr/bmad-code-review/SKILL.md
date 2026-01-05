---
name: bmad-code-review
description: Revue de Code BMAD - Revue de code approfondie en contexte propre suivant les standards de qualité BMAD
---

# Skill BMAD - Code Review

Ce skill guide une revue de code approfondie en contexte propre selon les standards de qualité BMAD.

## Objectif

Effectuer une revue de code complète pour identifier bugs, améliorer qualité, et assurer alignement avec standards BMAD.

## Principes BMAD Code Review

1. **Fresh Context** : Nouveau contexte + LLM différent si possible
2. **Story Alignment** : Code matche story file et acceptance criteria
3. **Test Coverage** : Tests existent et passent
4. **Clean Code** : Lisibilité, maintenabilité, best practices
5. **Security** : Pas de vulnérabilités évidentes

## Workflow Code Review

### Phase 0 : Préparation

**Charge en contexte frais** :

1. **Story File** : `_bmad-output/stories/story-X.md`
2. **Code Changes** : Tous les fichiers modifiés
3. **Tests** : Tous les fichiers de test
4. **Dev Agent Record** : `_bmad-output/dev-records/story-X.md` (si existe)

### Phase 1 : Story Alignment Review

**Vérifier que le code implémente la story** :

**Questions** :
- [ ] Chaque acceptance criterion est-il implémenté ?
- [ ] Chaque task/subtask est-elle complète ?
- [ ] Le code fait-il quelque chose NON dans la story ?
- [ ] Des features manquantes ?

**Red Flags** :
- ❌ Acceptance criterion ignoré
- ❌ Code extra non demandé (scope creep)
- ❌ Tasks marquées [x] mais pas implémentées

**Example** :
```markdown
Story AC: "User sees error for weak password"

Code Review:
✅ Error check exists
✅ Error message displayed
❌ MISSING: Pas de définition de "weak" (< 8 chars?)
```

### Phase 2 : Test Coverage Review

**Analyser les tests** :

**Checklist** :
- [ ] Tests existent pour chaque acceptance criterion
- [ ] Happy path est testé
- [ ] Edge cases critiques sont testés
- [ ] Tests passent tous à 100%
- [ ] Pas de tests skippés ou commentés
- [ ] Coverage > 80% pour code modifié

**Red Flags** :
- ❌ Pas de tests
- ❌ Tests qui échouent
- ❌ Tests mockés de manière incorrecte
- ❌ Tests qui testent l'implémentation, pas le comportement

**Example** :
```javascript
// ❌ BAD: Test l'implémentation
it('calls bcrypt.hash', () => {
  expect(bcrypt.hash).toHaveBeenCalled();
});

// ✅ GOOD: Test le comportement
it('hashes password before saving', async () => {
  const user = await createUser({ password: 'plain' });
  expect(user.password).not.toBe('plain');
  expect(user.password).toMatch(/^\$2[ayb]\$.{56}$/); // bcrypt format
});
```

### Phase 3 : Code Quality Review

**Analyser la qualité du code** :

#### 3.1 Readability

**Questions** :
- [ ] Noms de variables/fonctions clairs et descriptifs ?
- [ ] Fonctions font une seule chose ?
- [ ] Complexité cyclomatique raisonnable ?
- [ ] Comments justifiés (WHY, pas WHAT) ?

**Example** :
```javascript
// ❌ BAD
function f(x, y) {
  let z = 0;
  if (x > y) z = 1; else z = 2;
  return z;
}

// ✅ GOOD
function compareNumbers(first, second) {
  const FIRST_IS_LARGER = 1;
  const SECOND_IS_LARGER = 2;
  
  return first > second 
    ? FIRST_IS_LARGER 
    : SECOND_IS_LARGER;
}
```

#### 3.2 Maintainability

**Questions** :
- [ ] DRY (pas de duplication) ?
- [ ] SOLID principles respectés ?
- [ ] Dependency injection utilisée ?
- [ ] Magic numbers évités (constants nommées) ?

**Red Flags** :
- ❌ Code dupliqué (copy-paste)
- ❌ God objects (trop de responsabilités)
- ❌ Hardcoded values (URLs, credentials)
- ❌ Tight coupling

#### 3.3 Performance

**Questions** :
- [ ] Pas de N+1 queries ?
- [ ] Pas de boucles inutiles ?
- [ ] Caching approprié ?
- [ ] Pas de memory leaks évidents ?

**Red Flags** :
- ❌ Database queries dans des boucles
- ❌ Synchronous operations bloquantes
- ❌ Pas de pagination pour grandes listes

#### 3.4 Security

**Questions** :
- [ ] Input validation présente ?
- [ ] SQL injection prévenue (prepared statements) ?
- [ ] XSS prevented (output escaping) ?
- [ ] Credentials pas en plaintext ?
- [ ] Rate limiting pour APIs ?

**Red Flags** :
- ❌ String concatenation pour SQL
- ❌ User input directement dans HTML
- ❌ Passwords en plaintext
- ❌ Pas d'authentication checks

### Phase 4 : Architecture Alignment

**Vérifier alignement avec architecture** :

**Questions** :
- [ ] Suit les patterns définis dans Architecture Doc ?
- [ ] Components placés dans bons layers ?
- [ ] API contracts respectés ?
- [ ] Pas de violations de boundaries ?

### Phase 5 : Feedback Generation

**Générer feedback structuré** :

**Template Code Review Report** :
```markdown
# Code Review: Story X.Y

## Summary
[1-2 sentences: overall quality assessment]

## Story Alignment: ✅ | ⚠️ | ❌
- ✅ All acceptance criteria implemented
- ✅ All tasks complete
- ⚠️ Minor: [describe]

## Test Coverage: [%] - ✅ | ⚠️ | ❌
- ✅ Happy path tested
- ✅ Edge cases covered
- ❌ BLOCKER: Missing test for [scenario]

## Code Quality: ✅ | ⚠️ | ❌

### Readability
- ✅ Clear naming
- ⚠️ Function `processData` is too long (50 lines) - consider extracting

### Maintainability
- ❌ BLOCKER: Code duplication in [file1.js] and [file2.js]
  ```javascript
  // Duplicated code:
  const result = await db.query(...)
  ```
  **Recommendation**: Extract to shared function

### Performance
- ✅ No obvious issues
- ⚠️ Consider adding index on `users.email` for faster lookups

### Security
- ❌ BLOCKER: SQL injection risk in [file.js:42]
  ```javascript
  // UNSAFE
  db.query(`SELECT * FROM users WHERE id = ${userId}`)
  
  // FIX
  db.query('SELECT * FROM users WHERE id = ?', [userId])
  ```

## Architecture Alignment: ✅ | ⚠️ | ❌
- ✅ Follows MVC pattern
- ✅ API contracts respected

## Blockers (Must Fix)
1. [Security] SQL injection in user query
2. [Tests] Missing test for password reset edge case

## Recommendations (Should Fix)
1. Extract duplicated validation logic
2. Add JSDoc comments to public functions

## Nice to Have (Optional)
1. Consider adding loading states
2. Could optimize with memoization

## Decision: ✅ APPROVE | ⏸️ APPROVE WITH CHANGES | ❌ REJECT
**Status**: APPROVE WITH CHANGES

**Action Required**:
- Fix blockers (2 items)
- Address recommendations if time permits
```

### Phase 6 : Follow-Up

**Si changes requises** :

1. Developer fixe les issues
2. Re-review les changes
3. Approve quand tout est ✅

## Code Review Checklist Complète

### ✅ Story & Requirements
- [ ] All acceptance criteria implemented
- [ ] All tasks from story file complete
- [ ] No scope creep (extra features)

### ✅ Tests
- [ ] Tests exist for all ACs
- [ ] Happy path tested
- [ ] Edge cases tested
- [ ] All tests pass
- [ ] Coverage > 80%

### ✅ Code Quality
- [ ] Clear, descriptive names
- [ ] Functions < 30 lines
- [ ] No code duplication
- [ ] DRY, KISS, YAGNI
- [ ] SOLID principles

### ✅ Security
- [ ] Input validation
- [ ] No SQL injection
- [ ] No XSS vulnerabilities
- [ ] Credentials secured
- [ ] Auth/authz checks

### ✅ Performance
- [ ] No N+1 queries
- [ ] Appropriate caching
- [ ] No obvious bottlenecks

### ✅ Architecture
- [ ] Follows architecture doc
- [ ] Correct layer placement
- [ ] API contracts respected

## Output

Génère le rapport dans : `_bmad-output/code-reviews/story-X-review.md`

## Next Steps

Après Code Review :

1. **Si APPROVED** → Story complete ! Move to next story
2. **Si CHANGES REQUIRED** → Developer fixes → Re-review
3. **Si REJECTED** → Discuss with team → Re-implement
