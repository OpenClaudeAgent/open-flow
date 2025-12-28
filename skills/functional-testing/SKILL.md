---
name: functional-testing
description: Tests fonctionnels UI Qt Quick Test pour BluePlayer - Patterns, SignalSpy, scenarios et debugging
---

# Skill Tests Fonctionnels UI

Ce skill contient les patterns, conventions et scenarios pour les tests fonctionnels UI de BluePlayer avec Qt Quick Test.

---

## Stack technique

| Technologie | Role |
|-------------|------|
| **Qt Quick Test** | Framework de test pour QML (natif Qt 6) |
| **TestCase** | Type de base pour ecrire les tests |
| **SignalSpy** | Capture et verifie les signaux emis |
| **CTest** | Integration CMake |

---

## Structure des fichiers

```
tests/functional/
├── main.cpp                    # Point d'entree C++
├── tst_PlayerControlBar.qml    # Tests du PlayerControlBar
├── tst_VideoPlayer.qml         # Tests du VideoPlayer
├── tst_HomeView.qml            # Tests du HomeView
└── helpers/
    └── TestUtils.qml           # Utilitaires partages
```

---

## Convention de nommage

### Fichiers de test

```
tst_<ComponentName>.qml
```

### Fonctions de test

```qml
function test_<element>_<action>_<expectedResult>() { }
```

Exemples :
- `test_playButton_click_emitsPlayPauseSignal()`
- `test_volumeSlider_drag_updatesVolume()`
- `test_searchInput_enterKey_triggersSearch()`

---

## Pattern AAA (Arrange-Act-Assert)

Chaque test DOIT suivre cette structure :

```qml
function test_volumeButton_click_togglesMute() {
    // Arrange - Preparer le contexte
    var button = findChild(controlBar, "volumeButton")
    verify(button !== null, "volumeButton should exist")
    controlBar.muted = false
    
    // Act - Executer l'action
    mouseClick(button)
    
    // Assert - Verifier le resultat
    compare(muteSpy.count, 1, "muteClicked should be emitted once")
}
```

---

## Structure d'un fichier de test complet

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtTest 1.15

TestCase {
    id: testCase
    name: "MyComponentTests"    // Nom affiche dans les resultats
    when: windowShown           // Attend que la fenetre soit visible
    width: 800
    height: 600

    // Composant a tester (inline ou importe)
    Component {
        id: componentUnderTest
        MyComponent { }
    }

    // Instance et spies
    property var instance: null
    SignalSpy { id: mySpy; signalName: "mySignal" }

    // Setup avant chaque test
    function init() {
        instance = createTemporaryObject(componentUnderTest, testCase)
        mySpy.target = instance
        mySpy.clear()
        waitForRendering(instance)
    }

    // Cleanup apres chaque test (automatique avec createTemporaryObject)
    function cleanup() {
        instance = null
    }

    // Tests
    function test_something() {
        // Arrange
        // Act
        // Assert
    }
}
```

---

## Patterns recommandes

### 1. SignalSpy pour capturer les signaux

```qml
// Declaration dans le TestCase
SignalSpy { 
    id: playPauseSpy 
    signalName: "playPauseClicked" 
}

function init() {
    playPauseSpy.target = controlBar
    playPauseSpy.clear()
}

function test_signal_emitted() {
    mouseClick(button)
    
    // Verifier le nombre d'emissions
    compare(playPauseSpy.count, 1)
    
    // Verifier les arguments du signal
    compare(playPauseSpy.signalArguments[0][0], expectedValue)
}
```

### 2. createTemporaryObject pour l'isolation

```qml
function init() {
    // Cree une nouvelle instance pour chaque test
    // Automatiquement detruite apres le test
    controlBar = createTemporaryObject(controlBarComponent, testCase)
    verify(controlBar !== null)
}
// Pas besoin de cleanup explicite !
```

### 3. waitForRendering pour la synchronisation

```qml
function test_stateChange_updatesVisual() {
    controlBar.playing = true
    
    // Attendre que QML mette a jour le rendu
    waitForRendering(controlBar)
    
    // Maintenant verifier l'etat visuel
    verify(button.color === activeColor)
}
```

### 4. findChild pour localiser les elements

```qml
function test_nestedElement() {
    // Trouver un element par objectName
    var button = findChild(controlBar, "playPauseButton")
    verify(button !== null, "Button should exist")
    
    mouseClick(button)
}
```

**Important** : Les elements doivent avoir un `objectName` :

```qml
// Dans le composant
Rectangle {
    id: playPauseButton
    objectName: "playPauseButton"  // Necessaire pour findChild
}
```

### 5. Tests data-driven

Pour tester plusieurs variantes avec le meme code :

```qml
function test_speedChange_data() {
    return [
        { tag: "increase", initial: 1.0, delta: 0.25, expected: 1.25 },
        { tag: "decrease", initial: 1.0, delta: -0.25, expected: 0.75 },
        { tag: "max_limit", initial: 2.75, delta: 0.5, expected: 3.0 },
        { tag: "min_limit", initial: 0.5, delta: -0.5, expected: 0.25 },
    ]
}

function test_speedChange(data) {
    // Arrange
    controlBar.playbackRate = data.initial
    
    // Act
    if (data.delta > 0) {
        mouseClick(speedUpButton)
    } else {
        mouseClick(speedDownButton)
    }
    
    // Assert
    compare(rateSpy.signalArguments[0][0], data.expected,
            "Speed change from " + data.initial + " with delta " + data.delta)
}
```

---

## Gestion de l'asynchrone

### tryCompare pour les valeurs asynchrones

```qml
function test_asyncValue() {
    triggerAsyncOperation()
    
    // Attend que la propriete atteigne la valeur (timeout 5s)
    tryCompare(target, "loading", false, 5000)
}
```

### tryVerify pour les conditions asynchrones

```qml
function test_asyncCondition() {
    triggerAsyncOperation()
    
    // Attend que la condition soit vraie
    tryVerify(function() {
        return target.items.length > 0
    }, 5000)
}
```

### wait() en dernier recours

```qml
function test_animation() {
    triggerAnimation()
    
    // Seulement si tryCompare/tryVerify ne fonctionnent pas
    wait(300)  // Duree de l'animation
    
    verify(target.animationComplete)
}
```

---

## Anti-patterns a eviter

### 1. Tests qui dependent de l'ordre

```qml
// MAUVAIS
function test_1_setPlaying() {
    controlBar.playing = true
}
function test_2_checkPlaying() {
    verify(controlBar.playing)  // Peut echouer si test_1 n'a pas ete execute
}

// BON - Chaque test est independant
function init() {
    controlBar = createTemporaryObject(...)  // Etat frais
}
```

### 2. Assertions vides ou tautologiques

```qml
// MAUVAIS
function test_nothing() {
    mouseClick(button)
    verify(true)  // Ne verifie rien !
}
```

### 3. Magic numbers

```qml
// MAUVAIS
controlBar.duration = 3600
controlBar.position = 1800

// BON
var oneHour = 3600
var halfwayPoint = oneHour / 2
controlBar.duration = oneHour
controlBar.position = halfwayPoint
```

### 4. Delais fixes (sleep)

```qml
// MAUVAIS - Fragile et lent
function test_async() {
    triggerAsyncAction()
    wait(2000)  // Attend 2 secondes peu importe
    verify(result)
}

// BON - Attend une condition
function test_async() {
    triggerAsyncAction()
    tryCompare(target, "property", expectedValue, 2000)  // Timeout de 2s max
}
```

### 5. Tests trop longs

```qml
// MAUVAIS - Un test qui fait tout
function test_everything() {
    mouseClick(playButton)
    compare(playSpy.count, 1)
    mouseClick(volumeButton)
    compare(muteSpy.count, 1)
    // ... 50 lignes de plus
}

// BON - Tests focalises
function test_playButton_click() { ... }
function test_volumeButton_click() { ... }
```

---

## Actions de test disponibles

### Souris

```qml
mouseClick(item)                    // Clic simple
mouseClick(item, x, y)              // Clic a une position
mouseDoubleClick(item)              // Double clic
mousePress(item)                    // Appui (sans relacher)
mouseRelease(item)                  // Relacher
mouseMove(item, x, y)               // Deplacer
mouseDrag(item, x1, y1, dx, dy)     // Glisser
```

### Clavier

```qml
keyClick(Qt.Key_Space)              // Touche simple
keyPress(Qt.Key_Shift)              // Appui (sans relacher)
keyRelease(Qt.Key_Shift)            // Relacher
keySequence("Ctrl+S")               // Sequence
```

### Assertions

```qml
verify(condition, message)          // Condition booleenne
compare(actual, expected, message)  // Egalite
fuzzyCompare(a, b, delta)           // Egalite approximative
tryCompare(obj, prop, val, timeout) // Attente asynchrone
tryVerify(func, timeout)            // Condition asynchrone
fail(message)                       // Echec force
skip(message)                       // Ignorer le test
```

---

## Scenarios BluePlayer

### IDs de scenarios par composant

| Prefixe | Composant |
|---------|-----------|
| PCB | PlayerControlBar |
| VOL | Volume controls |
| SPD | Speed controls |
| SEK | Seek/Timeline |
| LIV | Live/VOD mode |
| CTL | Other controls |
| HOM | HomeView |
| CAT | Categories |
| SRC | Search |
| VPL | VideoPlayer |
| LOG | LoginView |
| NAV | Navigation |
| KEY | Keyboard shortcuts |

### Scenarios prioritaires (Haute)

| ID | Scenario |
|----|----------|
| PCB-001 | Clic sur Play → emet `playPauseClicked` |
| VOL-001 | Clic sur bouton volume → emet `muteClicked` |
| VOL-002 | Drag slider volume → emet `volumeRequested` |
| SPD-001 | Clic sur + → augmente vitesse de 0.25 |
| SPD-002 | Clic sur - → diminue vitesse de 0.25 |
| CTL-001 | Clic fullscreen → emet `fullscreenClicked` |
| HOM-001 | Clic sur StreamCard → ouvre le stream |
| SRC-001 | Saisie texte → filtre les resultats |
| KEY-001 | Espace → Play/Pause |
| KEY-003 | F → Fullscreen |

---

## Debugging

### Logs de debug

```qml
function test_example() {
    console.log("Test starting...")
    console.log("Button position:", button.x, button.y)
    console.log("Button visible:", button.visible)
    
    mouseClick(button)
    
    console.log("Signal count:", spy.count)
    console.log("Signal args:", JSON.stringify(spy.signalArguments))
}
```

### Execution

```bash
# Mode verbose
./build/tests/test_functional_ui -v2

# Avec signaux
./build/tests/test_functional_ui -v2 -vs

# Test specifique
./build/tests/test_functional_ui PlayerControlBarTests::test_playButton_click

# Export JUnit pour CI
./build/tests/test_functional_ui -o results.xml,junitxml
```

### Problemes courants

| Probleme | Solution |
|----------|----------|
| "QML module not found" | Verifier `addImportPath()` dans main.cpp |
| "Component is not ready" | Ajouter `verify(component.status === Component.Ready)` |
| Tests flaky | Ajouter `waitForRendering()` ou `tryCompare()` |

---

## Checklist avant commit

- [ ] Le test suit le pattern AAA (Arrange-Act-Assert)
- [ ] Le nommage est descriptif (`test_element_action_result`)
- [ ] Le test est independant (pas de dependance d'ordre)
- [ ] Les assertions verifient quelque chose de significatif
- [ ] Pas de magic numbers
- [ ] Pas de `wait()` sans justification
- [ ] `waitForRendering()` utilise apres les changements visuels
- [ ] `tryCompare()` utilise pour les valeurs asynchrones
- [ ] Le test est deterministe (pas de flakiness)
- [ ] Le test s'execute en < 1 seconde
- [ ] Les elements ont un `objectName` pour `findChild()`

---

## Metriques cibles

| Metrique | Cible |
|----------|-------|
| Couverture des composants critiques | 100% |
| Tests par composant UI majeur | >= 10 |
| Temps d'execution total | < 30s |
| Tests flaky | 0 |
