---
name: functional-testing
description: Tests fonctionnels UI Qt Quick Test - Patterns, SignalSpy, mocks inline et debugging
---

# Skill Tests Fonctionnels UI Qt Quick

Patterns, conventions et bonnes pratiques pour les tests fonctionnels UI avec Qt Quick Test.

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
├── main.cpp              # Point d'entree C++ avec setup QML
├── tst_MyComponent.qml   # Tests d'un composant
├── tst_OtherComp.qml     # Tests d'un autre composant
└── helpers/
    └── TestUtils.qml     # Utilitaires partages (optionnel)
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
// ou forme courte
function test_<element>_<comportement>() { }
```

Exemples :
- `test_button_click_emitsSignal()`
- `test_slider_drag_updatesValue()`
- `test_input_enterKey_triggersSearch()`
- `test_defaultValues()`
- `test_hoverState()`

---

## Pattern AAA (Arrange-Act-Assert)

Chaque test DOIT suivre cette structure :

```qml
function test_button_click_togglesMute() {
    // Arrange - Preparer le contexte
    var button = findChild(myComponent, "muteButton")
    verify(button !== null, "muteButton should exist")
    myComponent.muted = false
    
    // Act - Executer l'action
    mouseClick(button)
    
    // Assert - Verifier le resultat
    compare(muteSpy.count, 1, "muteClicked should be emitted once")
}
```

---

## Deux patterns de structure

### Pattern 1 : Component + createTemporaryObject (simple)

Pour les composants simples ou quand l'import fonctionne bien :

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtTest 1.15

TestCase {
    id: testCase
    name: "MyComponentTests"
    when: windowShown
    width: 400
    height: 400

    Component {
        id: componentUnderTest
        MyComponent { }
    }

    property var instance: null
    SignalSpy { id: clickedSpy; signalName: "clicked" }

    function init() {
        instance = createTemporaryObject(componentUnderTest, testCase)
        clickedSpy.target = instance
        clickedSpy.clear()
    }

    function test_something() {
        // ...
    }
}
```

### Pattern 2 : Item + Mock Inline (RECOMMANDE)

**Plus robuste et plus de controle.** Utiliser ce pattern pour :
- Tests complexes
- Composants avec des dependances
- Meilleur controle sur la structure

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtTest 1.15

Item {
    id: root
    width: 400
    height: 400

    // =========================================================
    // Mock du composant (reproduit l'API publique)
    // =========================================================
    
    Item {
        id: myComponent
        objectName: "myComponent"
        anchors.centerIn: parent
        width: 100
        height: 50
        
        // Proprietes publiques
        property string text: ""
        property bool enabled: true
        property bool hovered: false
        
        // Signaux
        signal clicked()
        signal valueChanged(real newValue)
        
        // Fonction reset pour les tests
        function reset() {
            text = ""
            enabled = true
            hovered = false
        }
        
        // Structure interne simplifiee
        Rectangle {
            id: background
            objectName: "background"
            anchors.fill: parent
            color: myComponent.enabled ? "#333" : "#666"
            radius: 4
            
            Text {
                id: label
                objectName: "label"
                anchors.centerIn: parent
                text: myComponent.text
                color: "#FFF"
            }
            
            MouseArea {
                id: mouseArea
                objectName: "mouseArea"
                anchors.fill: parent
                hoverEnabled: true
                onClicked: myComponent.clicked()
                onContainsMouseChanged: myComponent.hovered = containsMouse
            }
        }
    }

    // =========================================================
    // Signal Spies
    // =========================================================
    
    SignalSpy { id: clickedSpy; target: myComponent; signalName: "clicked" }
    SignalSpy { id: valueChangedSpy; target: myComponent; signalName: "valueChanged" }

    // =========================================================
    // Test Case
    // =========================================================
    
    TestCase {
        id: testCase
        name: "MyComponentTests"
        when: windowShown
        
        function init() {
            myComponent.reset()
            clickedSpy.clear()
            valueChangedSpy.clear()
            wait(50)  // Laisser le composant s'initialiser
        }
        
        // Tests ici...
        function test_defaultValues() {
            compare(myComponent.text, "", "Default text is empty")
            compare(myComponent.enabled, true, "Default enabled is true")
        }
        
        function test_click_emitsSignal() {
            var button = findChild(myComponent, "background")
            mouseClick(button)
            compare(clickedSpy.count, 1, "clicked emitted")
        }
    }
}
```

---

## Patterns recommandes

### 1. SignalSpy pour capturer les signaux

```qml
SignalSpy { 
    id: valueSpy 
    target: myComponent
    signalName: "valueChanged" 
}

function init() {
    valueSpy.clear()
}

function test_signal_emitted() {
    myComponent.setValue(42)
    
    // Verifier le nombre d'emissions
    compare(valueSpy.count, 1, "Signal emitted once")
    
    // Verifier les arguments du signal
    compare(valueSpy.signalArguments[0][0], 42, "Correct value")
}
```

### 2. findChild pour localiser les elements

```qml
function test_nestedElement() {
    var button = findChild(myComponent, "submitButton")
    verify(button !== null, "Button should exist")
    
    mouseClick(button)
}
```

**Important** : Les elements doivent avoir un `objectName` :

```qml
Rectangle {
    id: submitButton
    objectName: "submitButton"  // Necessaire pour findChild
}
```

### 3. Tests data-driven

Pour tester plusieurs variantes avec le meme code :

```qml
function test_values_data() {
    return [
        { tag: "zero", input: 0, expected: 0 },
        { tag: "positive", input: 50, expected: 50 },
        { tag: "max", input: 100, expected: 100 },
        { tag: "overflow", input: 150, expected: 100 },  // clamped
        { tag: "negative", input: -10, expected: 0 },    // clamped
    ]
}

function test_values(data) {
    myComponent.setValue(data.input)
    compare(myComponent.value, data.expected, 
            "Input " + data.input + " -> " + data.expected)
}
```

### 4. Organisation par categories (fichiers volumineux)

Pour les fichiers avec 30+ tests, organiser par sections :

```qml
TestCase {
    name: "MyComponentTests"
    
    // =====================================================
    // Default Values Tests
    // =====================================================
    
    function test_defaultValues() { /* ... */ }
    function test_defaultSize() { /* ... */ }
    
    // =====================================================
    // Property Tests
    // =====================================================
    
    function test_property_canBeSet() { /* ... */ }
    function test_property_emitsSignal() { /* ... */ }
    
    // =====================================================
    // Interaction Tests
    // =====================================================
    
    function test_click_emitsSignal() { /* ... */ }
    function test_hover_changesState() { /* ... */ }
    
    // =====================================================
    // Edge Cases
    // =====================================================
    
    function test_rapidClicks() { /* ... */ }
    function test_disabledState() { /* ... */ }
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

## Problemes courants et solutions

### 1. mouseMove ne declenche pas onEntered

**Probleme** : Dans l'environnement de test, `mouseMove()` ne declenche pas toujours les handlers `onEntered` des MouseArea.

**Solution** : Tester le comportement hover en manipulant directement la propriete :

```qml
// PROBLEMATIQUE - peut echouer
function test_hover_showsPopup() {
    mouseMove(button, button.width/2, button.height/2)
    wait(100)
    compare(popup.visible, true)  // Peut echouer!
}

// SOLUTION - tester la logique directement
function test_hover_showsPopup_viaProperty() {
    compare(myComponent.showPopup, false, "Initially hidden")
    
    // Simuler ce que le hover fait
    myComponent.showPopup = true
    wait(50)
    
    compare(popup.visible, true, "Popup visible when showPopup=true")
}
```

### 2. Binding casse apres assignment sur Slider

**Probleme** : Quand on fait `slider.value = X`, le binding QML est casse et ne se retablit pas.

**Solution** : Utiliser `Binding` element avec `restoreMode` :

```qml
// PROBLEMATIQUE
Slider {
    id: slider
    value: myComponent.volume  // Binding casse si on fait slider.value = 0.5
}

// SOLUTION
Slider {
    id: slider
    
    Binding on value {
        value: myComponent.volume
        restoreMode: Binding.RestoreBindingOrValue
    }
}
```

### 3. Composant non visible dans les tests

**Probleme** : `control.visible` retourne `false` dans les tests.

**Solution** : Utiliser le pattern Item + Mock avec positionnement explicite :

```qml
Item {
    id: root
    width: 400
    height: 400
    
    MyComponent {
        id: myComponent
        // Position explicite dans la zone visible
        x: 100
        y: 100
        width: 200
        height: 100
    }
    
    TestCase {
        // ...
    }
}
```

### 4. Tests qui echouent en batch mais passent seuls

**Probleme** : Un test passe quand execute seul mais echoue dans la suite complete.

**Solution** : Verifier l'isolation - ajouter une fonction `reset()` robuste :

```qml
function reset() {
    // Reset TOUTES les proprietes
    text = ""
    value = 0
    enabled = true
    visible = true
    
    // Reset aussi les etats internes
    _internalState = false
}

function init() {
    myComponent.reset()
    // Clear tous les spies
    clickedSpy.clear()
    valueSpy.clear()
    wait(50)
}
```

---

## Anti-patterns a eviter

### 1. Tests qui dependent de l'ordre

```qml
// MAUVAIS
function test_1_setState() {
    component.active = true
}
function test_2_checkState() {
    verify(component.active)  // Depend de test_1!
}

// BON - Chaque test est independant
function init() {
    component.reset()  // Etat frais
}
```

### 2. Assertions vides ou tautologiques

```qml
// MAUVAIS
function test_nothing() {
    mouseClick(button)
    verify(true)  // Ne verifie rien!
}

// BON
function test_click() {
    mouseClick(button)
    compare(clickedSpy.count, 1, "Signal emitted")
}
```

### 3. Magic numbers

```qml
// MAUVAIS
component.duration = 3600
component.position = 1800

// BON
var oneHour = 3600
var halfway = oneHour / 2
component.duration = oneHour
component.position = halfway
```

### 4. Delais fixes excessifs

```qml
// MAUVAIS - Fragile et lent
function test_async() {
    triggerAction()
    wait(2000)
    verify(result)
}

// BON - Attend une condition
function test_async() {
    triggerAction()
    tryCompare(target, "ready", true, 2000)
}
```

### 5. Tests trop longs (> 20 lignes)

```qml
// MAUVAIS - Un test qui fait tout
function test_everything() {
    // 50 lignes de code...
}

// BON - Tests focalises
function test_click() { /* 5-10 lignes */ }
function test_hover() { /* 5-10 lignes */ }
function test_disabled() { /* 5-10 lignes */ }
```

### 6. Tester l'implementation plutot que le comportement

```qml
// MAUVAIS - Teste l'implementation interne
function test_internal() {
    compare(component._privateVar, 42)
}

// BON - Teste le comportement observable
function test_behavior() {
    component.increment()
    compare(component.value, 43)  // Propriete publique
}
```

---

## Actions de test disponibles

### Souris

```qml
mouseClick(item)                    // Clic simple au centre
mouseClick(item, x, y)              // Clic a une position
mouseDoubleClick(item)              // Double clic
mousePress(item)                    // Appui (sans relacher)
mouseRelease(item)                  // Relacher
mouseMove(item, x, y)               // Deplacer (hover instable)
mouseDrag(item, x1, y1, dx, dy)     // Glisser
```

### Clavier

```qml
keyClick(Qt.Key_Space)              // Touche simple
keyClick(Qt.Key_A)                  // Lettre
keyPress(Qt.Key_Shift)              // Appui maintenu
keyRelease(Qt.Key_Shift)            // Relacher
keySequence("Ctrl+S")               // Combinaison
```

### Assertions

```qml
verify(condition, message)          // Condition booleenne
compare(actual, expected, message)  // Egalite stricte
fuzzyCompare(a, b, delta)           // Egalite approximative (floats)
tryCompare(obj, prop, val, timeout) // Attente asynchrone
tryVerify(func, timeout)            // Condition asynchrone
fail(message)                       // Echec force
skip(message)                       // Ignorer le test
```

### Utilitaires

```qml
wait(ms)                            // Pause (eviter si possible)
waitForRendering(item)              // Attendre le rendu
findChild(parent, objectName)       // Trouver un enfant par nom
createTemporaryObject(comp, parent) // Creer objet auto-detruit
```

---

## Execution des tests

```bash
# Tous les tests
./build/tests/test_functional_ui

# Mode verbose
./build/tests/test_functional_ui -v2

# Un fichier specifique
./build/tests/test_functional_ui -input tst_MyComponent.qml

# Un test specifique
./build/tests/test_functional_ui MyComponentTests::test_click

# Export JUnit pour CI
./build/tests/test_functional_ui -o results.xml,junitxml

# Lister les tests
./build/tests/test_functional_ui -functions
```

---

## Debugging

### Logs dans les tests

```qml
function test_debug() {
    console.log("=== Debug Info ===")
    console.log("Component:", myComponent)
    console.log("Visible:", myComponent.visible)
    console.log("Position:", myComponent.x, myComponent.y)
    console.log("Size:", myComponent.width, "x", myComponent.height)
    
    mouseClick(button)
    
    console.log("Spy count:", clickedSpy.count)
    console.log("Spy args:", JSON.stringify(clickedSpy.signalArguments))
}
```

### Problemes courants

| Probleme | Solution |
|----------|----------|
| "QML module not found" | Verifier `addImportPath()` dans main.cpp |
| "Component is not ready" | Ajouter `wait(50)` apres creation |
| Tests flaky | Utiliser `tryCompare()` au lieu de `wait()` |
| Hover ne fonctionne pas | Tester via propriete directe |
| Binding casse | Utiliser `Binding` element |
| Test passe seul, echoue en batch | Ameliorer `reset()` |

---

## Checklist avant commit

- [ ] Pattern AAA respecte (Arrange-Act-Assert)
- [ ] Nommage descriptif (`test_element_action`)
- [ ] Test independant (pas de dependance d'ordre)
- [ ] Assertions significatives (pas de `verify(true)`)
- [ ] Pas de magic numbers
- [ ] Pas de `wait()` sans justification
- [ ] `tryCompare()` pour l'asynchrone
- [ ] Test deterministe (pas de flakiness)
- [ ] Temps < 1 seconde par test
- [ ] Elements ont un `objectName` pour `findChild()`
- [ ] Fonction `reset()` si mock inline

---

## Metriques cibles

| Metrique | Cible |
|----------|-------|
| Couverture composants critiques | 100% |
| Tests par composant UI | >= 15 |
| Temps d'execution par test | < 1s |
| Temps total suite | < 60s |
| Tests flaky | 0 |
