---
name: qt-cpp
description: Official Qt/C++ best practices - Conventions, API design, memory management, signals/slots
---

# Qt/C++ Best Practices Skill

This skill contains official Qt best practices for C++ development, based on Qt Wiki documentation.

Sources:
- https://wiki.qt.io/Coding_Conventions
- https://wiki.qt.io/API_Design_Principles

---

## C++ Rules for Qt

### What NOT to Use

| Forbidden | Reason |
|-----------|--------|
| Exceptions | Qt doesn't use exceptions |
| RTTI (`dynamic_cast`, `typeid`) | Use `qobject_cast` for QObject |
| Excessive templates | Use with moderation |

### Casting

```cpp
// BAD - C-style cast
int x = (int)myFloat;

// GOOD - C++ casts
int x = static_cast<int>(myFloat);

// For QObject - use qobject_cast
if (auto* button = qobject_cast<QPushButton*>(widget)) {
    button->click();
}
```

---

## QObject and Signals/Slots

### Golden Rule

Every class deriving from QObject MUST have the Q_OBJECT macro:

```cpp
class MyClass : public QObject
{
    Q_OBJECT  // ALWAYS, even without signals/slots

public:
    explicit MyClass(QObject *parent = nullptr);
};
```

**Why?** Without Q_OBJECT, `qobject_cast` silently fails.

### Connections

```cpp
// Modern syntax (Qt 5+) - RECOMMENDED
connect(sender, &Sender::valueChanged,
        receiver, &Receiver::updateValue);

// With lambda
connect(button, &QPushButton::clicked, this, [this]() {
    doSomething();
});

// AVOID - old string-based syntax
connect(sender, SIGNAL(valueChanged(int)),
        receiver, SLOT(updateValue(int)));
```

---

## Memory Management

### Parent-Child Ownership

```cpp
// Child is automatically deleted when parent is destroyed
auto* button = new QPushButton("Click", parentWidget);
// No delete needed - parent handles it

// WARNING: Without parent, you must manage memory
auto* orphan = new QPushButton("Orphan");
// ... must be deleted manually or via smart pointer
```

### Global Objects

```cpp
// BAD - constructor called at undefined time
static const QString globalString = "Hello";  // WRONG

// GOOD - statically initialized
static const char globalText[] = "Hello";  // OK

// GOOD - for complex objects, use Q_GLOBAL_STATIC
Q_GLOBAL_STATIC(QString, globalString)
```

---

## Naming Conventions

### Functions and Properties

```cpp
// Getters - no get prefix
QString text() const;        // GOOD
QString getText() const;     // BAD

// Setters - set prefix
void setText(const QString &text);

// Booleans - is/has/can prefix
bool isVisible() const;
bool hasChildren() const;
bool canFetch() const;
```

---

## API Design (Qt Style)

### Six Characteristics of a Good API

1. **Minimal**: Few classes, few public functions
2. **Complete**: All expected features are there
3. **Clear semantics**: Principle of least surprise
4. **Intuitive**: Usable without documentation for simple cases
5. **Memorable**: Consistent conventions, no abbreviations
6. **Readable code**: Code using the API is easy to read

### Avoid Boolean Parameters

```cpp
// BAD - unclear when reading
widget->repaint(false);  // false = what?

// GOOD - explicit enum
widget->update(Qt::PartialUpdate);
```

---

## Virtual Functions

### Override

```cpp
class MyWidget : public QWidget
{
    // No 'virtual' - use override
    void paintEvent(QPaintEvent *event) override;
    bool event(QEvent *e) override;
};
```

---

## Const Correctness

### Parameters

```cpp
// Small type (< 16 bytes, trivial) - by value
void setAge(int age);
void setPoint(QPoint point);

// Large or non-trivial type - by const ref
void setName(const QString &name);
void setItems(const QList<Item> &items);
```

---

## Float Comparison

```cpp
// BAD - direct comparison
if (value == 0.0) { }

// GOOD - use Qt functions
if (qIsNull(value)) { }
if (qFuzzyCompare(a, b)) { }
```

---

## QString

```cpp
// Literals - use QStringLiteral for performance
QString s = QStringLiteral("Hello");

// Formatting
QString msg = QString("Value: %1, Count: %2").arg(value).arg(count);
```

---

## Lambdas

```cpp
// Short - one line
connect(button, &QPushButton::clicked, []() { doSomething(); });

// Long - multi-line
connect(button, &QPushButton::clicked, [this]() {
    processData();
    updateUI();
});

// Always write parentheses
[]() { }  // GOOD
[] { }    // BAD

// Explicit capture - RECOMMENDED
[this, &data]() { }

// Avoid implicit capture
[=]() { }  // Avoid
[&]() { }  // Avoid
```

---

## Checklist Before Commit

- [ ] Q_OBJECT present in all QObject classes
- [ ] No dynamic_cast (use qobject_cast)
- [ ] No exceptions
- [ ] C++ casts (static_cast, etc.) not C-style
- [ ] Float comparisons with qFuzzyCompare
- [ ] Override on reimplemented virtual functions
- [ ] Include guards (not #pragma once in public headers)
- [ ] Qt-style naming (no get, is/has for bool)
- [ ] const& parameters for large types
- [ ] No global objects with constructor (use Q_GLOBAL_STATIC)
