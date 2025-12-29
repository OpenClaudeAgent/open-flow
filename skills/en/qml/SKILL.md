---
name: qml
description: QML/Qt best practices - Conventions, patterns and theme system
---

# QML Best Practices Skill

This skill contains QML coding conventions, Qt best practices, and recommended patterns for Qt Quick applications.

---

## QML File Structure

### Attribute Order (Qt official)

Always structure a QML object in this order, separated by blank lines:

```qml
Item {
    id: root                                    // 1. id first

    property string name: ""                    // 2. Property declarations
    property alias content: container.children
    
    signal clicked(string value)                // 3. Signal declarations
    
    function doSomething() {                    // 4. JavaScript functions
        return true
    }
    
    color: Theme.surface                        // 5. Object properties
    width: 200
    height: 100
    
    Rectangle {                                 // 6. Child objects
        id: container
    }
}
```

### ID Naming

- `root` or `<componentName>Root` for root element (e.g., `playerRoot`, `cardRoot`)
- Descriptive IDs in camelCase
- Avoid generic IDs like `item1`, `rect2`

---

## Theme System

### Principle

Centralize colors, spacing, and animation durations in a singleton or imported JavaScript file.

### Recommended Color Tokens

| Token | Usage |
|-------|-------|
| `Theme.windowBackground` | Window background |
| `Theme.surface` | Component surfaces |
| `Theme.surfaceHover` | Surfaces on hover |
| `Theme.accent` | Accent color |
| `Theme.primaryText` | Primary text |
| `Theme.secondaryText` | Secondary text |
| `Theme.divider` | Separators |

### Spacing

```qml
Theme.spacingSmall   // 8px  - Between related elements
Theme.spacingMedium  // 16px - Standard padding
Theme.spacingLarge   // 24px - Between sections
```

### Animation Durations

```qml
Theme.animFast       // 80ms  - Click feedback
Theme.animNormal     // 150ms - Hover
Theme.animSlow       // 200ms - Card animations
Theme.animPanel      // 300ms - Panels/drawers
```

---

## Qt Official Best Practices

### Prefer Declarative Bindings

```qml
// GOOD - Declarative
Rectangle {
    color: mouseArea.containsMouse ? Theme.accent : Theme.surface
}

// BAD - Imperative
Rectangle {
    Component.onCompleted: color = Theme.surface
}
```

### Explicit Types (no var)

```qml
// GOOD
property string name
property int count
property bool visible

// BAD
property var name
```

### Required Properties for External Data

```qml
// GOOD - Explicit and type-safe
Item {
    required property string itemId
    required property var itemData
}
```

### Don't Store State in Delegates

```qml
// BAD - State lost when delegate is recycled
ListView {
    delegate: Button {
        property bool wasClicked: false
        onClicked: wasClicked = true
    }
}

// GOOD - Store in model
ListView {
    delegate: Button {
        onClicked: model.wasClicked = true
    }
}
```

### Interaction Signals vs Change Signals

```qml
// GOOD - Explicit interaction signal
Slider {
    onMoved: backend.setValue(value)  // Only when user moves
}

// CAUTION - Can trigger cascading
Slider {
    onValueChanged: backend.setValue(value)  // Also when backend changes
}
```

---

## Anti-patterns to Avoid

### 1. Magic Numbers

```qml
// BAD
Rectangle { width: 180; height: 220; radius: 12 }

// GOOD
Rectangle { 
    width: cardWidth
    height: cardHeight
    radius: Theme.cornerRadius 
}
```

### 2. Hardcoded Colors

```qml
// BAD
Rectangle { color: "#141c2a" }

// GOOD
Rectangle { color: Theme.surface }
```

### 3. Complex Inline Bindings

Extract complex logic into functions.

---

## Internationalization (i18n)

Always wrap user-facing text:

```qml
Text { text: qsTr("Search...") }
Text { text: qsTr("Speed %1x").arg(speed.toFixed(2)) }
```

---

## Performance

### Loader for Heavy Conditional Content

```qml
Loader {
    active: currentView === "details"
    source: "DetailsView.qml"
}
```

### Async Images

```qml
Image {
    source: imageUrl
    asynchronous: true  // Don't block UI
    cache: true
}
```

---

## Checklist Before Commit

- [ ] No hardcoded colors (use Theme)
- [ ] No magic numbers (use constants/properties)
- [ ] User text wrapped in qsTr()
- [ ] Images with asynchronous: true and cache: true
- [ ] Attribute order respected (id, props, signals, functions, props, children)
- [ ] Explicit types (no var unless necessary)
- [ ] Animations with theme durations and appropriate easing
