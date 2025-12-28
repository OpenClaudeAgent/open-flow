---
name: qml
description: Best practices QML/Qt - Conventions, patterns et theme system
---

# Skill QML Best Practices

Ce skill contient les conventions de codage QML, les best practices Qt, et les patterns recommandes pour les applications Qt Quick.

---

## Structure des fichiers QML

### Ordre des attributs (Qt officiel)

Toujours structurer un objet QML dans cet ordre, separe par des lignes vides :

```qml
Item {
    id: root                                    // 1. id en premier

    property string name: ""                    // 2. Declarations de proprietes
    property alias content: container.children
    
    signal clicked(string value)                // 3. Declarations de signaux
    
    function doSomething() {                    // 4. Fonctions JavaScript
        return true
    }
    
    color: Theme.surface                        // 5. Proprietes de l'objet
    width: 200
    height: 100
    
    Rectangle {                                 // 6. Objets enfants
        id: container
    }
}
```

### Nommage des IDs

- `root` ou `<componentName>Root` pour l'element racine (ex: `playerRoot`, `cardRoot`)
- IDs descriptifs en camelCase
- Eviter les IDs generiques comme `item1`, `rect2`

---

## Theme System

### Principe

Centraliser les couleurs, espacements et durees d'animation dans un singleton ou un fichier JavaScript importe.

### Import type

```qml
import "themes/Theme.js" as Theme
// ou via singleton
import MyApp.Theme 1.0
```

### Tokens de couleur recommandes

| Token | Usage |
|-------|-------|
| `Theme.windowBackground` | Fond de fenetre |
| `Theme.surface` | Surfaces de composants |
| `Theme.surfaceHover` | Surfaces au hover |
| `Theme.accent` | Couleur d'accent |
| `Theme.primaryText` | Texte principal |
| `Theme.secondaryText` | Texte secondaire |
| `Theme.mutedText` | Texte discret |
| `Theme.divider` | Separateurs |
| `Theme.success` | Succes |
| `Theme.warning` | Avertissement |
| `Theme.error` | Erreur |

### Espacements

```qml
Theme.spacingSmall   // 8px  - Entre elements lies
Theme.spacingMedium  // 16px - Padding standard
Theme.spacingLarge   // 24px - Entre sections
```

### Durees d'animation

```qml
Theme.animFast       // 80ms  - Feedback de clic
Theme.animNormal     // 150ms - Hover
Theme.animSlow       // 200ms - Animations de cartes
Theme.animPanel      // 300ms - Panels/drawers
```

### Typographie

```qml
font.family: Theme.fontFamily
```

---

## Patterns de composants

### Cards avec hover

```qml
Item {
    id: cardRoot
    
    // Proprietes publiques
    property string title: ""
    property bool isPlaceholder: false
    
    // Signal de clic avec parametres
    signal clicked(string id, string name)
    
    implicitWidth: 180
    implicitHeight: 220
    
    Rectangle {
        id: cardBackground
        anchors.fill: parent
        radius: 12
        color: cardRoot.isPlaceholder ? Theme.surfaceHover : Theme.surface
        border.color: Theme.divider
        border.width: 1
        
        // Hover state
        states: [
            State {
                name: "hovered"
                when: mouseArea.containsMouse
                PropertyChanges {
                    target: cardBackground
                    color: Theme.surfaceHover
                    scale: 1.02
                }
            }
        ]
        
        transitions: Transition {
            NumberAnimation {
                properties: "scale"
                duration: Theme.animSlow
                easing.type: Easing.OutCubic
            }
            ColorAnimation {
                duration: Theme.animSlow
                easing.type: Easing.OutCubic
            }
        }
    }
    
    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
        cursorShape: Qt.PointingHandCursor
        onClicked: cardRoot.clicked(cardRoot.id, cardRoot.title)
    }
}
```

### Images avec chargement asynchrone

```qml
Image {
    id: thumbnailImage
    source: imageUrl
    fillMode: Image.PreserveAspectCrop
    asynchronous: true  // Ne bloque pas l'UI
    cache: true         // Cache Qt automatique
    
    // Fade-in au chargement
    opacity: status === Image.Ready ? 1 : 0
    Behavior on opacity {
        NumberAnimation { 
            duration: Theme.animSlow
            easing.type: Easing.OutCubic 
        }
    }
}

// Placeholder pendant le chargement
Rectangle {
    anchors.fill: thumbnailImage
    color: Theme.surfaceHover
    visible: thumbnailImage.status !== Image.Ready
    
    BusyIndicator {
        anchors.centerIn: parent
        running: parent.visible
    }
}
```

### Acces aux services globaux (contexte C++)

```qml
// Pattern recommande : fonction pour eviter les boucles de binding
function getService() {
    return typeof myService !== "undefined" ? myService : null
}

// Utilisation
var service = getService()
if (service) {
    service.refresh()
}

// Connections avec guard
Connections {
    target: getService()
    enabled: getService() !== null
    
    function onDataChanged() {
        // Handler
    }
}
```

### Debouncing pour la recherche

```qml
Timer {
    id: searchDebounceTimer
    interval: 400  // 400ms standard
    onTriggered: {
        if (searchField.text.length > 0) {
            performSearch(searchField.text)
        }
    }
}

TextField {
    id: searchField
    onTextChanged: {
        searchDebounceTimer.stop()
        if (text.length > 0) {
            searchDebounceTimer.start()
        }
    }
}
```

---

## Best Practices Qt Officielles

### Preferer les bindings declaratifs

```qml
// BON - Declaratif
Rectangle {
    color: mouseArea.containsMouse ? Theme.accent : Theme.surface
}

// MAUVAIS - Imperatif
Rectangle {
    Component.onCompleted: color = Theme.surface
}
```

### Types explicites (pas de var)

```qml
// BON
property string name
property int count
property bool visible

// MAUVAIS
property var name
property var count
```

### Required properties pour les donnees externes

```qml
// BON - Explicite et type-safe
Item {
    required property string itemId
    required property var itemData
}

// MAUVAIS - Lookup implicite
Item {
    // Depend de proprietes parentes non explicites
}
```

### Ne pas stocker d'etat dans les delegates

```qml
// MAUVAIS - L'etat sera perdu quand le delegate est recycle
ListView {
    delegate: Button {
        property bool wasClicked: false
        onClicked: wasClicked = true
    }
}

// BON - Stocker dans le modele
ListView {
    delegate: Button {
        onClicked: model.wasClicked = true
    }
}
```

### Signaux d'interaction vs signaux de changement

```qml
// BON - Signal d'interaction explicite
Slider {
    onMoved: backend.setValue(value)  // Uniquement quand l'utilisateur bouge
}

// ATTENTION - Peut declencher en cascade
Slider {
    onValueChanged: backend.setValue(value)  // Aussi quand le backend change
}
```

### Layouts - Dos and Don'ts

```qml
// BON - Layout.preferredWidth dans un Layout
RowLayout {
    Rectangle {
        Layout.preferredWidth: 100
        Layout.fillHeight: true
    }
}

// MAUVAIS - anchors dans un enfant direct de Layout
RowLayout {
    Rectangle {
        anchors.left: parent.left  // Ne pas faire ca!
    }
}
```

---

## Animations et Easing

### Easing recommandes

| Animation | Easing |
|-----------|--------|
| Hover/Focus | `Easing.OutCubic` |
| Navigation | `Easing.InOutCubic` |
| Press feedback | `Easing.OutQuart` |
| Bounce/Spring | `Easing.OutBack` |

### Pattern d'animation de visibilite

```qml
Rectangle {
    id: panel
    opacity: visible ? 1.0 : 0.0
    visible: opacity > 0
    
    Behavior on opacity {
        NumberAnimation {
            duration: Theme.animPanel
            easing.type: Easing.InOutCubic
        }
    }
}
```

---

## Anti-patterns a eviter

### 1. Magic numbers

```qml
// MAUVAIS
Rectangle { width: 180; height: 220; radius: 12 }

// BON
Rectangle { 
    width: cardWidth
    height: cardHeight
    radius: Theme.cornerRadius 
}
```

### 2. Couleurs hardcodees

```qml
// MAUVAIS
Rectangle { color: "#141c2a" }

// BON
Rectangle { color: Theme.surface }
```

### 3. Bindings complexes inline

```qml
// MAUVAIS
Text {
    text: someCondition ? (anotherCondition ? "A" : "B") : (yetAnother ? "C" : "D")
}

// BON
Text {
    text: computeText()
}

function computeText() {
    if (someCondition) {
        return anotherCondition ? "A" : "B"
    }
    return yetAnother ? "C" : "D"
}
```

### 4. console.log en production

Utiliser les regions pour le debug :

```qml
// #region debug
console.log(JSON.stringify({location:'File.qml:55', message:'debug', data:{}}))
// #endregion
```

---

## Internationalisation (i18n)

Toujours wrapper les textes utilisateur :

```qml
// BON
Text { text: qsTr("Search...") }
Button { text: qsTr("Now playing") }

// Avec parametres
Text { text: qsTr("Speed %1x").arg(speed.toFixed(2)) }
```

---

## Performance

### Loader pour contenu conditionnel lourd

```qml
Loader {
    active: currentView === "details"
    source: "DetailsView.qml"
    
    onItemChanged: {
        if (item) {
            item.setup()
        }
    }
}
```

### clip: true pour le contenu scrollable

```qml
ScrollView {
    clip: true  // Evite le rendu hors limites
    // ...
}
```

### asynchronous: true pour les images

Toujours utiliser pour les images chargees depuis le reseau.

---

## Checklist avant commit

- [ ] Pas de couleurs hardcodees (utiliser Theme)
- [ ] Pas de magic numbers (utiliser constantes/proprietes)
- [ ] Textes utilisateur wrapes dans qsTr()
- [ ] Images avec asynchronous: true et cache: true
- [ ] Ordre des attributs respecte (id, props, signals, functions, props, children)
- [ ] Types explicites (pas de var sauf necessaire)
- [ ] Animations avec durees du theme et easing approprie
