---
name: qt-cpp
description: Bonnes pratiques Qt/C++ officielles - Conventions, API design, memory management, signals/slots
---

# Skill Qt/C++ Best Practices

Ce skill contient les bonnes pratiques officielles Qt pour le developpement C++, basees sur la documentation Qt Wiki.

Sources :
- https://wiki.qt.io/Coding_Conventions
- https://wiki.qt.io/API_Design_Principles

---

## Regles C++ pour Qt

### Ce qu'on n'utilise PAS

| Interdit | Raison |
|----------|--------|
| Exceptions | Qt n'utilise pas les exceptions |
| RTTI (`dynamic_cast`, `typeid`) | Utiliser `qobject_cast` pour QObject |
| Templates excessifs | Utiliser avec moderation |

### Casting

```cpp
// MAUVAIS - C-style cast
int x = (int)myFloat;

// BON - C++ casts
int x = static_cast<int>(myFloat);
const auto* ptr = static_cast<const MyClass*>(obj);

// BON - Constructeur pour types simples
int x = int(myFloat);

// Pour QObject - utiliser qobject_cast
if (auto* button = qobject_cast<QPushButton*>(widget)) {
    button->click();
}
```

---

## QObject et Signaux/Slots

### Regle d'or

Toute classe derivant de QObject DOIT avoir la macro Q_OBJECT :

```cpp
class MyClass : public QObject
{
    Q_OBJECT  // TOUJOURS, meme sans signals/slots

public:
    explicit MyClass(QObject *parent = nullptr);
};
```

**Pourquoi ?** Sans Q_OBJECT, `qobject_cast` echoue silencieusement.

### Connexions

```cpp
// Syntaxe moderne (Qt 5+) - RECOMMANDEE
connect(sender, &Sender::valueChanged,
        receiver, &Receiver::updateValue);

// Avec lambda
connect(button, &QPushButton::clicked, this, [this]() {
    doSomething();
});

// EVITER - ancienne syntaxe string-based
connect(sender, SIGNAL(valueChanged(int)),
        receiver, SLOT(updateValue(int)));
```

### Deconnexion automatique

```cpp
// Le QObject gere la deconnexion automatiquement quand il est detruit
// Pas besoin de disconnect() manuel dans le destructeur
```

---

## Gestion Memoire

### Parent-Child Ownership

```cpp
// L'enfant est automatiquement delete quand le parent est detruit
auto* button = new QPushButton("Click", parentWidget);
// Pas de delete necessaire - le parent s'en charge

// ATTENTION : Sans parent, vous devez gerer la memoire
auto* orphan = new QPushButton("Orphan");
// ... doit etre delete manuellement ou via smart pointer
```

### Smart Pointers avec Qt

```cpp
// Pour les QObject avec parent - pas besoin de smart pointer
auto* widget = new QWidget(parent);  // OK, parent gere la memoire

// Pour les QObject sans parent ou objets non-QObject
auto uniquePtr = std::make_unique<MyNonQObjectClass>();
QScopedPointer<MyClass> scopedPtr(new MyClass);

// Pour les objets partages
QSharedPointer<Data> shared = QSharedPointer<Data>::create();
```

### Objets Globaux

```cpp
// MAUVAIS - constructeur appele a un moment indefini
static const QString globalString = "Hello";  // WRONG
static QString mutableGlobal;  // SUPER WRONG

// BON - initialise statiquement
static const char globalText[] = "Hello";  // OK
static int globalInt = 42;  // OK

// BON - pour objets complexes, utiliser Q_GLOBAL_STATIC
Q_GLOBAL_STATIC(QString, globalString)

void foo() {
    globalString()->append(" World");
}
```

---

## Conventions de Nommage

### Classes

```cpp
// Prefixe Q pour les classes Qt
class QMyWidget : public QWidget { };

// Pas de prefixe pour les classes applicatives
class MainWindow : public QMainWindow { };
class UserSettings { };
```

### Fonctions et Proprietes

```cpp
// Getters - pas de prefixe get
QString text() const;        // BON
QString getText() const;     // MAUVAIS

// Setters - prefixe set
void setText(const QString &text);

// Booleens - prefixe is/has/can
bool isVisible() const;
bool hasChildren() const;
bool canFetch() const;

// EXCEPTION : pluriel sans prefixe
bool scrollBarsEnabled() const;  // pas areScrollBarsEnabled()
```

### Parametres

```cpp
// Noms descriptifs dans les headers
void doSomething(QRegion clientRegion, QPoint gravitySource);

// MAUVAIS - noms cryptiques
void doSomething(QRegion rgn, QPoint p);
```

---

## API Design (Qt Style)

### Six Caracteristiques d'une Bonne API

1. **Minimale** : Peu de classes, peu de fonctions publiques
2. **Complete** : Toutes les fonctionnalites attendues sont la
3. **Semantique claire** : Principe de moindre surprise
4. **Intuitive** : Utilisable sans documentation pour les cas simples
5. **Memorable** : Conventions coherentes, pas d'abreviations
6. **Code lisible** : Le code qui utilise l'API est facile a lire

### Property-Based API

```cpp
// BON - proprietes orthogonales, ordre quelconque
QTimer timer;
timer.setInterval(1000);
timer.setSingleShot(true);
timer.start();

// ou
timer.setSingleShot(true);
timer.setInterval(1000);
timer.start();

// Convenience
timer.start(1000);
```

### Eviter les Parametres Booleens

```cpp
// MAUVAIS - pas clair a la lecture
widget->repaint(false);  // false = quoi ?

// BON - enum explicite
widget->update(Qt::PartialUpdate);

// BON - fonction separee
widget->repaintWithoutErasing();
```

### Constructeurs Simples

```cpp
// MAUVAIS - trop de parametres
QSlider* slider = new QSlider(12, 18, 3, 13, Qt::Vertical, nullptr, "volume");

// BON - construction incrementale
QSlider* slider = new QSlider(Qt::Vertical);
slider->setRange(12, 18);
slider->setPageStep(3);
slider->setValue(13);
slider->setObjectName("volume");
```

---

## Fonctions Virtuelles

### Quand utiliser virtual

```cpp
// Utiliser virtual SEULEMENT si :
// 1. Qt (ou le framework) appelle cette fonction
// 2. Le polymorphisme est vraiment necessaire

// MAUVAIS - virtual inutile si seul l'utilisateur appelle
virtual void resetFormat();  // Personne dans Qt n'appelle ca

// BON - virtual car Qt appelle event() en interne
virtual bool event(QEvent *e) override;
```

### Override

```cpp
class MyWidget : public QWidget
{
    // Pas de 'virtual' - utiliser override
    void paintEvent(QPaintEvent *event) override;
    bool event(QEvent *e) override;
};
```

### Problemes avec virtual

- On ne peut pas ajouter/supprimer sans casser la compatibilite binaire
- Empeche l'inlining et l'optimisation
- Rend la classe difficile a copier par valeur
- Appels 2-3x plus lents

---

## Headers et Includes

### Include Guards

```cpp
// Dans les headers publics - TOUJOURS les guards traditionnels
#ifndef MYCLASS_H
#define MYCLASS_H

// ... declarations

#endif // MYCLASS_H

// #pragma once - seulement pour code interne/tests
```

### Ordre des Includes

```cpp
// 1. Header correspondant (dans .cpp)
#include "myclass.h"

// 2. Headers Qt specifiques
#include <QtCore/QString>
#include <QtWidgets/QWidget>

// 3. Headers STL
#include <vector>
#include <memory>

// 4. Headers systeme
#include <cstdlib>
```

### Forward Declarations

```cpp
// Dans les headers - preferer forward declaration
class QWidget;  // au lieu de #include <QWidget>

class MyClass
{
    QWidget* m_widget;  // OK avec forward declaration
};

// Dans les .cpp - inclure ce dont on a besoin
#include <QWidget>
```

---

## Const Correctness

### Parametres

```cpp
// Petit type (< 16 bytes, trivial) - par valeur
void setAge(int age);
void setPoint(QPoint point);

// Grand type ou non-trivial - par const ref
void setName(const QString &name);
void setItems(const QList<Item> &items);
```

### Fonctions Const

```cpp
class MyClass
{
public:
    // Const si ne modifie pas l'etat visible
    QString text() const;
    int count() const;
    
    // Non-const si modifie l'etat
    void setText(const QString &text);
    void clear();
};
```

### Retour par Valeur vs Const Ref

```cpp
// Preferer retour par valeur (plus flexible pour refactoring)
QString text() const;  // BON

// Const ref seulement si performance critique
const QString& text() const;  // OK si vraiment necessaire
```

---

## Comparaison de Floats

```cpp
// MAUVAIS - comparaison directe
if (value == 0.0) { }
if (a == b) { }

// BON - utiliser les fonctions Qt
if (qIsNull(value)) { }
if (qFuzzyCompare(a, b)) { }
if (qFuzzyIsNull(value)) { }
```

---

## Enums

### Enums Scoped (C++11)

```cpp
// RECOMMANDE - enum class
enum class Color {
    Red,
    Green,
    Blue
};

Color c = Color::Red;
```

### Flags avec QFlags

```cpp
// Definition
enum class AlignmentFlag {
    AlignLeft = 0x01,
    AlignRight = 0x02,
    AlignTop = 0x04,
    AlignBottom = 0x08
};
Q_DECLARE_FLAGS(Alignment, AlignmentFlag)
Q_DECLARE_OPERATORS_FOR_FLAGS(Alignment)

// Utilisation
Alignment align = AlignmentFlag::AlignLeft | AlignmentFlag::AlignTop;
```

---

## QString

### Construction

```cpp
// Litteraux - utiliser QStringLiteral pour performance
QString s = QStringLiteral("Hello");

// Concatenation
QString result = firstName + " " + lastName;

// Formatage
QString msg = QString("Value: %1, Count: %2").arg(value).arg(count);
```

### Comparaison

```cpp
// Case-insensitive
if (str.compare(other, Qt::CaseInsensitive) == 0) { }

// Contient
if (str.contains("search", Qt::CaseInsensitive)) { }
```

---

## Containers Qt vs STL

### Quand utiliser Qt

```cpp
// Pour integration avec Qt (signals, QVariant, etc.)
QList<QString> names;
QMap<QString, int> scores;
QSet<int> uniqueIds;
```

### Quand utiliser STL

```cpp
// Pour performance pure ou interop avec code non-Qt
std::vector<int> data;
std::unordered_map<int, Data> cache;
```

### Iteration

```cpp
// Range-based for (C++11) - RECOMMANDE
for (const QString& name : names) {
    qDebug() << name;
}

// Avec modification
for (QString& name : names) {
    name = name.toUpper();
}

// EVITER - iterateurs mixtes const/non-const
for (auto it = list.begin(); it != list.end(); ++it)  // attention au type
for (auto it = list.cbegin(); it != list.cend(); ++it)  // OK, explicitement const
```

---

## Auto Keyword

### Quand utiliser auto

```cpp
// Evite repetition
auto widget = new QWidget(parent);
auto* button = qobject_cast<QPushButton*>(sender());
auto list = QStringList() << "a" << "b";

// Iterateurs
auto it = map.constBegin();
```

### Quand eviter auto

```cpp
// Quand le type n'est pas evident
auto result = compute();  // Quel type ?

// Preferer explicite
int result = compute();
QString name = getName();
```

---

## Lambdas

### Formatage

```cpp
// Court - une ligne
connect(button, &QPushButton::clicked, []() { doSomething(); });

// Long - multi-lignes
connect(button, &QPushButton::clicked, [this]() {
    processData();
    updateUI();
});

// Toujours ecrire les parentheses
[]() { }  // BON
[] { }    // MAUVAIS
```

### Capture

```cpp
// Capture explicite - RECOMMANDE
[this, &data]() { }

// Eviter capture implicite
[=]() { }  // Eviter
[&]() { }  // Eviter
```

---

## Checklist avant Commit

- [ ] Q_OBJECT present dans toutes les classes QObject
- [ ] Pas de dynamic_cast (utiliser qobject_cast)
- [ ] Pas d'exceptions
- [ ] Casts C++ (static_cast, etc.) pas C-style
- [ ] Comparaisons float avec qFuzzyCompare
- [ ] Override sur les fonctions virtuelles reimplementees
- [ ] Include guards (pas #pragma once dans les headers publics)
- [ ] Nommage Qt-style (pas de get, is/has pour bool)
- [ ] Parametres const& pour les grands types
- [ ] Pas d'objets globaux avec constructeur (utiliser Q_GLOBAL_STATIC)
