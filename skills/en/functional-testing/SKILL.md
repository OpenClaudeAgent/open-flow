---
name: functional-testing
description: Functional UI tests Qt Quick Test - Patterns, SignalSpy, inline mocks and debugging
---

# Functional Testing Skill (Qt Quick)

Patterns, conventions and best practices for functional UI tests with Qt Quick Test.

---

## Tech Stack

| Technology | Role |
|------------|------|
| **Qt Quick Test** | Test framework for QML (native Qt 6) |
| **TestCase** | Base type for writing tests |
| **SignalSpy** | Captures and verifies emitted signals |
| **CTest** | CMake integration |

---

## File Structure

```
tests/functional/
├── main.cpp              # C++ entry point with QML setup
├── tst_MyComponent.qml   # Tests for a component
├── tst_OtherComp.qml     # Tests for another component
└── helpers/
    └── TestUtils.qml     # Shared utilities (optional)
```

---

## Naming Convention

### Test files

```
tst_<ComponentName>.qml
```

### Test functions

```qml
function test_<element>_<action>_<expectedResult>() { }
// or short form
function test_<element>_<behavior>() { }
```

Examples:
- `test_button_click_emitsSignal()`
- `test_slider_drag_updatesValue()`
- `test_input_enterKey_triggersSearch()`

---

## AAA Pattern (Arrange-Act-Assert)

Every test MUST follow this structure:

```qml
function test_button_click_togglesMute() {
    // Arrange - Prepare context
    var button = findChild(myComponent, "muteButton")
    verify(button !== null, "muteButton should exist")
    myComponent.muted = false
    
    // Act - Execute action
    mouseClick(button)
    
    // Assert - Verify result
    compare(muteSpy.count, 1, "muteClicked should be emitted once")
}
```

---

## Two Structure Patterns

### Pattern 1: Component + createTemporaryObject (simple)

For simple components or when import works well.

### Pattern 2: Item + Inline Mock (RECOMMENDED)

**More robust and more control.** Use this pattern for:
- Complex tests
- Components with dependencies
- Better control over structure

```qml
Item {
    id: root
    width: 400
    height: 400

    // Mock component (reproduces public API)
    Item {
        id: myComponent
        property string text: ""
        signal clicked()
        function reset() { text = "" }
    }

    SignalSpy { id: clickedSpy; target: myComponent; signalName: "clicked" }

    TestCase {
        name: "MyComponentTests"
        when: windowShown
        
        function init() {
            myComponent.reset()
            clickedSpy.clear()
            wait(50)
        }
        
        function test_defaultValues() {
            compare(myComponent.text, "", "Default text is empty")
        }
    }
}
```

---

## Async Handling

### tryCompare for async values

```qml
function test_asyncValue() {
    triggerAsyncOperation()
    tryCompare(target, "loading", false, 5000)
}
```

### tryVerify for async conditions

```qml
function test_asyncCondition() {
    triggerAsyncOperation()
    tryVerify(function() { return target.items.length > 0 }, 5000)
}
```

### wait() as last resort

Only if tryCompare/tryVerify don't work.

---

## Anti-Patterns to Avoid

1. **Tests depending on order** - Each test must be independent
2. **Empty assertions** - `verify(true)` verifies nothing
3. **Magic numbers** - Use named constants
4. **Excessive fixed delays** - Use tryCompare instead of wait()
5. **Too long tests** - Max 20 lines per test
6. **Testing implementation** - Test observable behavior, not internals

---

## Available Test Actions

### Mouse

```qml
mouseClick(item)                    // Simple click at center
mouseDoubleClick(item)              // Double click
mousePress(item)                    // Press (without release)
mouseRelease(item)                  // Release
mouseDrag(item, x1, y1, dx, dy)     // Drag
```

### Keyboard

```qml
keyClick(Qt.Key_Space)              // Single key
keyClick(Qt.Key_A)                  // Letter
keySequence("Ctrl+S")               // Combination
```

### Assertions

```qml
verify(condition, message)          // Boolean condition
compare(actual, expected, message)  // Strict equality
fuzzyCompare(a, b, delta)           // Approximate equality (floats)
tryCompare(obj, prop, val, timeout) // Async wait
tryVerify(func, timeout)            // Async condition
```

---

## Checklist Before Commit

- [ ] AAA pattern respected (Arrange-Act-Assert)
- [ ] Descriptive naming (`test_element_action`)
- [ ] Independent test (no order dependency)
- [ ] Meaningful assertions (no `verify(true)`)
- [ ] No magic numbers
- [ ] No `wait()` without justification
- [ ] `tryCompare()` for async
- [ ] Deterministic test (no flakiness)
- [ ] Time < 1 second per test
- [ ] Elements have `objectName` for `findChild()`
