---
name: testability-patterns
description: Anti-patterns de testabilite et patterns de resolution - SOLID, injection de dependances, isolation
---

# Skill Testability Patterns

Ce skill contient les anti-patterns qui rendent le code difficile a tester et les patterns de resolution pour ameliorer la testabilite.

---

## Principes Fondamentaux

### SOLID

- **S**ingle Responsibility : Une classe = une raison de changer
- **O**pen/Closed : Ouvert a l'extension, ferme a la modification
- **L**iskov Substitution : Les sous-types doivent etre substituables
- **I**nterface Segregation : Interfaces specifiques plutot que generales
- **D**ependency Inversion : Dependre des abstractions, pas des implementations

### Testabilite

Un code testable est un code ou :
- Les dependances sont injectables (pas creees en interne)
- Les effets de bord sont isoles et controlables
- L'etat global est absent ou minimal
- Les interfaces permettent le mocking

---

## Anti-Patterns de Testabilite

### 1. Dependances Hard-Codees

**Description** : Une classe cree ses propres dependances dans le constructeur au lieu de les recevoir.

**Pourquoi c'est un probleme** :
- Impossible d'injecter un mock pour les tests
- Couplage fort entre les classes
- Changement de dependance = modification de la classe

**Comment identifier** :
- `new` dans un constructeur (sauf pour objets valeur)
- Appels directs a des singletons
- Creation de clients reseau, timers, acces fichiers dans le constructeur

**Comment resoudre** :
- Extraire une interface pour la dependance
- Passer la dependance via le constructeur (Dependency Injection)
- Utiliser une factory pour la creation en production

**Exemple conceptuel** :
```
AVANT: class Service { Service() { client = new HttpClient(); } }
APRES: class Service { Service(IHttpClient* client) { this->client = client; } }
```

---

### 2. Etat Global et Singletons

**Description** : Utilisation de variables statiques, singletons, ou etat partage entre instances.

**Pourquoi c'est un probleme** :
- Les tests s'influencent mutuellement
- Ordre d'execution des tests devient important
- Impossible de tester en parallele
- Etat imprevisible entre les tests

**Comment identifier** :
- Variables `static` mutables
- Pattern Singleton
- Classes avec uniquement des methodes statiques
- Acces a `QSettings` ou equivalent sans abstraction

**Comment resoudre** :
- Transformer en instance injectable
- Creer une interface et injecter l'implementation
- Pour les loggers : utiliser une interface ILogger injectable
- Reset explicite de l'etat dans les tests si inevitable

---

### 3. Effets de Bord dans les Constructeurs

**Description** : Le constructeur effectue des operations complexes (I/O, reseau, fichiers).

**Pourquoi c'est un probleme** :
- Impossible de creer l'objet sans declencher les effets
- Tests lents a cause d'I/O reelles
- Echecs imprevisibles dans les tests

**Comment identifier** :
- Lecture/ecriture de fichiers dans le constructeur
- Appels reseau dans le constructeur
- Chargement de configuration dans le constructeur
- Connexions a des services externes

**Comment resoudre** :
- Deplacer l'initialisation dans une methode `init()` explicite
- Passer les donnees deja chargees au constructeur
- Utiliser le pattern "two-phase initialization"

---

### 4. Variables d'Environnement Directes

**Description** : Lecture directe de variables d'environnement dans le code.

**Pourquoi c'est un probleme** :
- Tests dependent de l'environnement d'execution
- Configuration non injectable
- Comportement different en CI vs local

**Comment identifier** :
- Appels a `getenv()`, `qgetenv()`, `std::getenv()`
- Lecture de `process.env` ou equivalent

**Comment resoudre** :
- Creer une structure/classe de configuration
- Passer la configuration au constructeur
- Factory method `fromEnvironment()` pour la production

---

### 5. Chemins de Fichiers Hard-Codes

**Description** : Chemins absolus ou relatifs codes en dur dans le source.

**Pourquoi c'est un probleme** :
- Ne fonctionne que sur une machine specifique
- Impossible de tester avec des fichiers temporaires
- Cree des fichiers indesirables pendant les tests

**Comment identifier** :
- Chaines contenant `/home/`, `/Users/`, `C:\`
- Chemins relatifs assumes (`./config`, `../data`)

**Comment resoudre** :
- Passer les chemins en parametre
- Utiliser des repertoires temporaires dans les tests
- Abstraction du systeme de fichiers si necessaire

---

### 6. Couplage Temporel

**Description** : Des methodes doivent etre appelees dans un ordre specifique non explicite.

**Pourquoi c'est un probleme** :
- API fragile et error-prone
- Tests doivent connaitre l'ordre magique
- Bugs subtils en production

**Comment identifier** :
- Methodes `init()`, `setup()`, `configure()` obligatoires
- Documentation disant "appeler X avant Y"
- Exceptions si methodes appelees dans le mauvais ordre

**Comment resoudre** :
- Rendre les dependances explicites via le constructeur
- Builder pattern pour construction complexe
- Etats invalides impossibles par design

---

### 7. Classes God Object

**Description** : Une classe qui fait trop de choses et connait trop de details.

**Pourquoi c'est un probleme** :
- Difficile a tester (trop de dependances)
- Difficile a maintenir (changements frequents)
- Viole Single Responsibility

**Comment identifier** :
- Plus de 500-1000 lignes
- Plus de 10 dependances
- Nom vague (Manager, Handler, Processor, Service sans precision)
- Beaucoup de methodes sans rapport entre elles

**Comment resoudre** :
- Extraire des classes specialisees
- Facade pattern si coordination necessaire
- Identifier les responsabilites distinctes

---

### 8. Law of Demeter Violations

**Description** : Chaines d'appels traversant plusieurs objets.

**Pourquoi c'est un probleme** :
- Couplage a la structure interne des objets
- Fragile aux changements de structure
- Difficile a mocker (beaucoup de niveaux)

**Comment identifier** :
- Chaines comme `a.getB().getC().doSomething()`
- Plus de 2 points dans une expression

**Comment resoudre** :
- Tell, Don't Ask : demander a l'objet de faire l'action
- Deleguer les responsabilites
- Fournir des methodes de haut niveau

---

## Patterns de Resolution

### Dependency Injection

Passer les dependances au constructeur plutot que les creer.

```cpp
// AVANT
class Service {
    Service() { client = new HttpClient(); }
};

// APRES
class Service {
    Service(IHttpClient* client) : client(client) {}
};
```

### Interface Extraction

Creer une interface pour une dependance concrete, permettant le mocking.

```cpp
// Interface
class IHttpClient {
    virtual Response get(string url) = 0;
};

// Implementation production
class HttpClient : public IHttpClient { ... };

// Mock pour tests
class MockHttpClient : public IHttpClient { ... };
```

### Factory Method

Methode statique pour creer l'objet avec ses vraies dependances en production.

```cpp
class Service {
public:
    static Service* createDefault() {
        return new Service(new HttpClient());
    }
    
    // Constructeur pour tests
    Service(IHttpClient* client);
};
```

### Configuration Object

Regrouper la configuration dans un objet injectable.

```cpp
struct Config {
    string apiUrl;
    int timeout;
    bool debugMode;
    
    static Config fromEnvironment();  // Factory pour production
};

class Service {
    Service(const Config& config);  // Injectable pour tests
};
```

### Repository Pattern

Abstraire l'acces aux donnees derriere une interface.

```cpp
class IUserRepository {
    virtual User findById(int id) = 0;
    virtual void save(User user) = 0;
};

// Implementation SQLite pour production
class SqliteUserRepository : public IUserRepository { ... };

// Implementation en memoire pour tests
class InMemoryUserRepository : public IUserRepository { ... };
```

---

## Checklist de Testabilite

Avant de commit, verifier :

- [ ] Pas de `new` dans les constructeurs (sauf objets valeur)
- [ ] Pas de singletons ou etat global mutable
- [ ] Pas d'I/O dans les constructeurs
- [ ] Pas de lecture directe de variables d'environnement
- [ ] Pas de chemins de fichiers hard-codes
- [ ] Pas de couplage temporel implicite
- [ ] Classes < 500 lignes, < 10 dependances
- [ ] Pas de chaines d'appels > 2 niveaux

---

## Messages de Commit

Format : `refactor(<scope>): <description>`

Exemples :
- `refactor(core): extract IHttpClient interface`
- `refactor(auth): inject dependencies via constructor`
- `refactor(config): replace env vars with config object`
