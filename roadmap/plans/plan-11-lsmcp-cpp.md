# Plan 11 - Support C/C++ dans lsmcp

## Contexte

Le serveur MCP lsmcp est integre dans open-flow (plan 09) et fournit des outils LSP pour Python, TypeScript, Go et Rust. Cependant, le support C/C++ via clangd n'est pas encore configure, bien que lsmcp le supporte nativement.

Les developpeurs C/C++ n'ont donc pas acces aux fonctionnalites LSP (hover, definitions, references, diagnostics, etc.) dans leurs projets.

## Objectif

Ajouter un preset C/C++ dans la configuration lsmcp pour permettre aux agents Claude d'utiliser les outils LSP sur les projets C et C++.

## Comportement attendu

### Configuration

Un nouveau preset `cpp` est ajoute dans `servers/lsmcp/configure.py` :
- Utilise `clangd` comme serveur LSP (gere C et C++)
- Ajoute a la liste des presets par defaut (installe avec `./install.sh mcp`)

### Verification de clangd

Lors de l'installation :
1. Le script verifie si `clangd` est disponible sur le systeme
2. Si absent, affiche un warning clair avec les instructions d'installation
3. Le preset est quand meme configure (l'utilisateur peut installer clangd plus tard)

### Utilisation

Une fois installe, Claude peut utiliser tous les outils LSP sur les fichiers `.c`, `.cpp`, `.h`, `.hpp` :
- `get_hover` : informations de type, documentation
- `get_definitions` : naviguer vers les definitions
- `find_references` : trouver toutes les utilisations
- `get_diagnostics` : erreurs et warnings du compilateur
- `rename_symbol` : renommer dans tout le projet
- etc.

### Instructions d'installation clangd

Le README doit documenter comment installer clangd :
- macOS : `brew install llvm` ou Xcode Command Line Tools
- Linux : `apt install clangd` ou equivalent
- Windows : via LLVM installer

## Checklist de validation

- [ ] Preset `cpp` ajoute dans `PRESETS` de configure.py
- [ ] Preset `cpp` ajoute a `DEFAULT_PRESETS`
- [ ] Verification de la presence de `clangd` avec warning si absent
- [ ] README.md mis a jour avec le preset cpp et instructions d'installation clangd
- [ ] Test : Claude peut utiliser `get_hover` sur un fichier .cpp
- [ ] Test : Claude peut utiliser `get_diagnostics` sur un fichier .c
