---
name: testability-patterns
description: Testability anti-patterns and resolution patterns - SOLID, dependency injection, isolation
---

# Testability Patterns Skill

This skill contains anti-patterns that make code difficult to test and resolution patterns to improve testability.

---

## Fundamental Principles

### SOLID

- **S**ingle Responsibility: One class = one reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes must be substitutable
- **I**nterface Segregation: Specific interfaces rather than general ones
- **D**ependency Inversion: Depend on abstractions, not implementations

### Testability

Testable code is code where:
- Dependencies are injectable (not created internally)
- Side effects are isolated and controllable
- Global state is absent or minimal
- Interfaces enable mocking

---

## Testability Anti-Patterns

### 1. Hard-Coded Dependencies

**Description**: A class creates its own dependencies in the constructor instead of receiving them.

**Why it's a problem**:
- Impossible to inject a mock for tests
- Tight coupling between classes
- Changing dependency = modifying the class

**How to identify**:
- `new` in a constructor (except for value objects)
- Direct calls to singletons
- Network clients, timers, file access creation in constructor

**How to resolve**:
- Extract an interface for the dependency
- Pass dependency via constructor (Dependency Injection)
- Use a factory for production creation

---

### 2. Global State and Singletons

**Description**: Use of static variables, singletons, or shared state between instances.

**Why it's a problem**:
- Tests influence each other
- Test execution order becomes important
- Impossible to test in parallel
- Unpredictable state between tests

**How to resolve**:
- Transform into injectable instance
- Create interface and inject implementation
- For loggers: use injectable ILogger interface
- Explicit state reset in tests if unavoidable

---

### 3. Side Effects in Constructors

**Description**: Constructor performs complex operations (I/O, network, files).

**Why it's a problem**:
- Impossible to create object without triggering effects
- Slow tests due to real I/O
- Unpredictable failures in tests

**How to resolve**:
- Move initialization to explicit `init()` method
- Pass already-loaded data to constructor
- Use "two-phase initialization" pattern

---

### 4. Direct Environment Variables

**Description**: Direct reading of environment variables in code.

**How to resolve**:
- Create a configuration struct/class
- Pass configuration to constructor
- Factory method `fromEnvironment()` for production

---

### 5. Hard-Coded File Paths

**Description**: Absolute or relative paths hard-coded in source.

**How to resolve**:
- Pass paths as parameters
- Use temporary directories in tests
- File system abstraction if necessary

---

### 6. Temporal Coupling

**Description**: Methods must be called in a specific non-explicit order.

**How to resolve**:
- Make dependencies explicit via constructor
- Builder pattern for complex construction
- Invalid states impossible by design

---

### 7. God Object Classes

**Description**: A class that does too much and knows too many details.

**How to identify**:
- More than 500-1000 lines
- More than 10 dependencies
- Vague name (Manager, Handler, Processor, Service without precision)

**How to resolve**:
- Extract specialized classes
- Facade pattern if coordination needed
- Identify distinct responsibilities

---

### 8. Law of Demeter Violations

**Description**: Call chains traversing multiple objects.

**How to identify**:
- Chains like `a.getB().getC().doSomething()`
- More than 2 dots in an expression

**How to resolve**:
- Tell, Don't Ask: ask object to perform action
- Delegate responsibilities
- Provide high-level methods

---

## Resolution Patterns

### Dependency Injection

Pass dependencies to constructor rather than creating them.

### Interface Extraction

Create interface for concrete dependency, enabling mocking.

### Factory Method

Static method to create object with real dependencies in production.

### Configuration Object

Group configuration in an injectable object.

### Repository Pattern

Abstract data access behind an interface.

---

## Testability Checklist

Before commit, verify:

- [ ] No `new` in constructors (except value objects)
- [ ] No singletons or mutable global state
- [ ] No I/O in constructors
- [ ] No direct environment variable reading
- [ ] No hard-coded file paths
- [ ] No implicit temporal coupling
- [ ] Classes < 500 lines, < 10 dependencies
- [ ] No call chains > 2 levels

---

## Commit Messages

Format: `refactor(<scope>): <description>`

Examples:
- `refactor(core): extract IHttpClient interface`
- `refactor(auth): inject dependencies via constructor`
- `refactor(config): replace env vars with config object`
