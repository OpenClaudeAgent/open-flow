---
name: bmad-quick-dev
description: BMAD Quick Dev - Rapid end-to-end implementation following tech spec for Quick Flow
---

# Skill BMAD - Quick Dev

Ce skill guide l'implémentation rapide end-to-end d'une feature en suivant le tech spec.

## Objectif

Implémenter rapidement mais proprement en suivant le tech spec avec TDD léger.

## Principes Quick Dev

1. **Ship > Perfect** : Code qui marche maintenant > code parfait plus tard
2. **TDD Léger** : Tests pour happy path + edge cases critiques
3. **Iterate Fast** : Commit souvent, teste souvent
4. **Self-Contained** : Chaque story = feature complète

## Workflow Quick Dev

### Phase 1 : Setup

**Charge le Tech Spec** :
```
Lis _bmad-output/quick-flow/tech-spec.md
```

**Vérifie que les tests passent** :
```bash
npm test  # ou pytest, make test, etc.
# Tous doivent passer ✅
```

### Phase 2 : Pour Chaque Story

#### Step 1: Implement Happy Path

**Focus sur le cas normal d'abord** :

```javascript
// Example: Dark Mode Toggle - Story 1
// 1. Create component
const ThemeToggle = () => {
  const [theme, setTheme] = useState('light');
  
  const toggle = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };
  
  return <button onClick={toggle}>Toggle Theme</button>;
};

// 2. Quick test
it('toggles theme on click', () => {
  render(<ThemeToggle />);
  const button = screen.getByText('Toggle Theme');
  
  fireEvent.click(button);
  // Visual check or simple assertion
});
```

#### Step 2: Add Edge Cases

**Gère les cas importants** :

```javascript
// Handle edge cases
const ThemeToggle = () => {
  const [theme, setTheme] = useState(() => {
    // Load from localStorage (edge case: first visit)
    return localStorage.getItem('theme') || 'light';
  });
  
  const toggle = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);  // Persist
  };
  
  return <button onClick={toggle}>🌙</button>;
};
```

#### Step 3: Quick Validation

**Teste manuellement ou avec tests légers** :

```bash
# Lance le dev server
npm run dev

# Teste dans le browser:
# 1. Click toggle → theme change ✅
# 2. Reload page → theme persists ✅
# 3. Edge case: clear localStorage → defaults to light ✅
```

#### Step 4: Commit & Move On

```bash
git add .
git commit -m "feat: add dark mode toggle"
```

**Ne perfectionne PAS** - passe à la story suivante !

### Phase 3 : Integration

**Une fois toutes les stories implémentées** :

1. **Quick Integration Test**
   ```bash
   npm test
   # Vérifie que tout marche ensemble
   ```

2. **Manual E2E Check**
   - Lance l'app
   - Teste le user flow complet
   - Vérifie les edge cases

3. **Quick Polish** (optionnel)
   - Loading states
   - Error messages
   - UX tweaks

### Phase 4 : Finalization

**Checklist finale** :

- [ ] Toutes les stories implémentées
- [ ] Happy path fonctionne
- [ ] Edge cases critiques gérés
- [ ] Tests passent
- [ ] Commits propres
- [ ] Ready for code review

## Quick Dev Mindset

### ✅ DO

- Ship working code fast
- Test happy path + critical edge cases
- Commit souvent (après chaque story)
- Keep it simple
- Iterate based on feedback

### ❌ DON'T

- Over-engineer
- Aim for perfection
- Write tests exhaustifs (sauf si critique)
- Spend hours on edge cases rares
- Refactor avant que ça marche

## Time Budget

**Par Story** :
- Story 1 (Core): 30-60min
- Story 2 (Edge Cases): 20-40min
- Story 3 (Polish): 15-30min

**Total Quick Dev** : 1-2h max

## Example Complet

### Story 1: Theme Toggle (45min)

```javascript
// ThemeContext.jsx (15min)
export const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <div className={theme}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
};

// ThemeToggle.jsx (20min)
export const ThemeToggle = () => {
  const { theme, setTheme } = useContext(ThemeContext);
  
  const toggle = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };
  
  return (
    <button onClick={toggle} aria-label="Toggle theme">
      {theme === 'light' ? '🌙' : '☀️'}
    </button>
  );
};

// Quick test (10min)
it('toggles theme', () => {
  render(
    <ThemeProvider>
      <ThemeToggle />
    </ThemeProvider>
  );
  
  const button = screen.getByLabelText('Toggle theme');
  expect(button.textContent).toBe('🌙');
  
  fireEvent.click(button);
  expect(button.textContent).toBe('☀️');
});
```

✅ Commit: `feat: add theme toggle component`

### Story 2: Persist Theme (30min)

```javascript
// Update ThemeProvider
export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem('theme') || 'light';
  });
  
  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
  };
  
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div className={theme}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
};
```

✅ Commit: `feat: persist theme preference`

### Story 3: Dark Mode Styles (25min)

```css
/* styles.css */
:root {
  --bg: white;
  --text: black;
}

.dark {
  --bg: #1a1a1a;
  --text: #f0f0f0;
}

body {
  background: var(--bg);
  color: var(--text);
}
```

✅ Commit: `style: add dark mode colors`

**Total** : ~100min = 1h40 ✅

## Output

- Code implémenté
- Tests basiques
- Commits propres
- Feature fonctionnelle

## Next Steps

Après Quick Dev :

1. **Code Review** → Utilise `/quick-flow` (nouveau contexte) + skill `bmad-code-review`
2. **Iterate** → Si feedback, améliore et re-commit
3. **Ship** → Merge et deploy !
