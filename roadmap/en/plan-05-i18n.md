# Plan 05 - Repository Internationalization

## Context

The repo contains agents, skills, and documentation in French. To allow wider adoption, the installation system must support multiple languages.

## Objective

Allow installing files (agents, skills, rules, roadmap) in different languages via an installer parameter.

## Expected Behavior

### File Structure

Files are organized by language in subfolders:

```
agents/
  fr/
    executeur.md
    ...
  en/
    executor.md
    ...
skills/
  fr/
    agentic-flow/SKILL.md
    ...
  en/
    agentic-flow/SKILL.md
    ...
roadmap/
  fr/
    README.md
    plan-01-notify-pyobjc.md
    ...
  en/
    README.md
    ...
AGENTS.fr.md
AGENTS.en.md
```

### Installation

The user runs installation with a language parameter:

```bash
./install.sh install --lang=fr   # Install in French
./install.sh install --lang=en   # Install in English
./install.sh install             # Default language (French)
```

### Fallback

- Default language: **French**
- If a file doesn't exist in the requested language, the installer uses the **French** version
- The installer shows a warning when using fallback

### Display

The installer indicates the language used in the installation summary:

```
Language: fr (default)
```

or

```
Language: en
  - executor.md (fallback: fr)
```

## Validation Checklist

- [ ] Language folder structure created
- [ ] Existing files migrated to `fr/`
- [ ] `--lang` or `-l` parameter working
- [ ] French fallback operational
- [ ] Warning displayed on fallback
- [ ] Installation summary shows language
