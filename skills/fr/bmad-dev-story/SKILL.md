---
name: bmad-dev-story
description: Implémentation Dev Story BMAD - Workflow d'implémentation TDD avec le fichier story comme source unique de vérité
---

# Skill BMAD - Dev Story Implementation

Ce skill guide l'implémentation d'une story en suivant strictement TDD (Test-Driven Development) et le story file.

## Objectif

Implémenter une story complètement en suivant le cycle red-green-refactor avec le story file comme source unique de vérité.

## Principes BMAD pour Implementation

1. **Story File = Source Unique de Vérité** : Séquence tasks/subtasks est autoritaire
2. **Red-Green-Refactor** : Test qui échoue → Implémentation → Refactoring
3. **100% Tests Passing** : Tous les tests existants + nouveaux passent
4. **No Hallucinations** : Chaque changement mappé à une task/subtask
5. **Continuous Execution** : Pas de pause jusqu'à completion ou HALT

## Workflow TDD

### Phase 0 : Préparation

**AVANT de commencer** :

1. **Charge le Story File** complet
   ```
   Lis _bmad-output/stories/story-X.md
   ```

2. **Charge project-context.md** (si existe)
   ```
   Lis **/project-context.md
   ```

3. **Vérifie l'état initial**
   ```bash
   # Lance tous les tests existants
   npm test
   # OU
   pytest
   # OU
   make test
   
   # Tous doivent passer ✅
   ```

### Phase 1 : Pour Chaque Task/Subtask

**Séquence stricte** :

#### Étape 1.1 : RED (Test qui échoue)

**Écris le test AVANT le code** :

```javascript
// Example: Story 1.1 - Sign Up Form
describe('SignUp API', () => {
  it('should create user with valid email and password', async () => {
    // Arrange
    const userData = {
      email: 'test@example.com',
      password: 'SecurePass123'
    };
    
    // Act
    const response = await request(app)
      .post('/api/auth/signup')
      .send(userData);
    
    // Assert
    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('user');
    expect(response.body).toHaveProperty('token');
    expect(response.body.user.email).toBe(userData.email);
  });
});
```

**Lance le test** :
```bash
npm test -- signup.test.js
# Résultat attendu: ❌ FAIL (le code n'existe pas encore)
```

#### Étape 1.2 : GREEN (Implémentation minimale)

**Implémente JUSTE assez pour passer le test** :

```javascript
// routes/auth.js
router.post('/signup', async (req, res) => {
  const { email, password } = req.body;
  
  // Validation
  if (!isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }
  
  // Hash password
  const passwordHash = await bcrypt.hash(password, 10);
  
  // Create user
  const user = await db.users.create({
    email,
    password_hash: passwordHash
  });
  
  // Generate token
  const token = jwt.sign({ userId: user.id }, JWT_SECRET);
  
  res.status(201).json({
    user: { id: user.id, email: user.email },
    token
  });
});
```

**Lance le test** :
```bash
npm test -- signup.test.js
# Résultat attendu: ✅ PASS
```

#### Étape 1.3 : REFACTOR (Amélioration)

**Améliore le code tout en gardant les tests verts** :

- Extract functions
- Remove duplication
- Improve naming
- Add comments si nécessaire

**Lance TOUS les tests** :
```bash
npm test
# Résultat attendu: ✅ ALL PASS
```

#### Étape 1.4 : Mark Complete

**Marque la task [x] SEULEMENT si** :
- ✅ Implémentation complète
- ✅ Tests écrits et passent
- ✅ Tous les tests existants passent
- ✅ Code reviewed (self)

**Dans le story file** :
```markdown
## Tasks
- [x] Task 1: Create signup endpoint ✅
- [ ] Task 2: Add email validation
- [ ] Task 3: Add password strength check
```

### Phase 2 : Continuous Execution

**Ne t'arrête PAS jusqu'à** :
- Toutes les tasks/subtasks complètes
- OU condition HALT explicite
- OU tous les tests passent à 100%

**Boucle** :
```
WHILE (tasks restantes) {
  1. RED: Écris test
  2. GREEN: Implémente
  3. REFACTOR: Améliore
  4. VERIFY: Lance tous tests
  5. MARK: Coche task si ✅
}
```

### Phase 3 : Documentation

**Dev Agent Record** - Documente :

```markdown
## Story X.Y Implementation Record

### What Was Implemented
- [List all features/changes]

### Tests Created
- Unit tests: [files]
- Integration tests: [files]
- Coverage: [%]

### Decisions Made
1. [Decision] - Rationale: [why]
2. [Decision] - Rationale: [why]

### Files Changed
- [file1.js] - [what changed]
- [file2.js] - [what changed]
- [test1.test.js] - [tests added]

### Test Results
✅ All tests passing (X/X)
Coverage: Y%
```

### Phase 4 : Validation Finale

**Checklist finale** :

- [ ] Story file : Toutes tasks [x]
- [ ] Tests : 100% passing
- [ ] Coverage : >80%
- [ ] No console errors
- [ ] No TypeScript errors (si applicable)
- [ ] Acceptance criteria validés
- [ ] Code self-reviewed
- [ ] Dev Agent Record complet

## Actions Critiques (À SUIVRE)

**JAMAIS** :
- ❌ Sauter une task/subtask
- ❌ Réorganiser les tasks
- ❌ Implémenter sans test d'abord
- ❌ Continuer avec tests qui échouent
- ❌ Mentir sur les tests

**TOUJOURS** :
- ✅ Lire le story file EN ENTIER d'abord
- ✅ Suivre red-green-refactor
- ✅ Lancer TOUS les tests après chaque change
- ✅ Documenter les décisions
- ✅ Mettre à jour File List

## Example Complet

Story: "User can sign up with email/password"

**Task 1: Create signup endpoint**

RED:
```javascript
it('should create user', async () => {
  const res = await request(app)
    .post('/api/auth/signup')
    .send({ email: 'test@test.com', password: 'pass123' });
  expect(res.status).toBe(201);
});
```
→ ❌ FAIL

GREEN:
```javascript
router.post('/signup', async (req, res) => {
  const user = await createUser(req.body);
  res.status(201).json(user);
});
```
→ ✅ PASS

REFACTOR:
```javascript
// Extract validation
const validateSignup = (data) => { /* ... */ };

router.post('/signup', async (req, res) => {
  validateSignup(req.body);
  const user = await createUser(req.body);
  res.status(201).json(user);
});
```
→ ✅ ALL PASS

MARK: [x] Task 1 ✅

## Output

- Code implémenté dans les fichiers source
- Tests dans les fichiers de test
- Dev Agent Record dans `_bmad-output/dev-records/story-X.md`

## Next Steps

Après Dev Story :

1. **Code Review** → Utilise `/dev` (nouveau contexte) + skill `bmad-code-review`
2. **Tests Additionnels** → Utilise `/tea` + skill `bmad-test-automate`
3. **Story Suivante** → Utilise `/sm` + skill `bmad-create-story`
