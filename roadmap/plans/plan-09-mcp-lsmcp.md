# Plan 09 - Integration du serveur MCP lsmcp (outils LSP)

## Contexte

Les agents Claude dans OpenCode n'ont pas acces aux fonctionnalites avancees d'analyse de code que fournissent les Language Server Protocol (LSP). Ils ne peuvent pas :
- Obtenir les informations de type au survol
- Naviguer vers les definitions
- Trouver toutes les references d'un symbole
- Voir les erreurs et warnings du compilateur
- Renommer un symbole dans tout le projet
- Obtenir des suggestions de quick-fix

Le projet open-source **lsmcp** (MIT License) de @mizchi fournit exactement ces fonctionnalites via un serveur MCP qui fait le pont entre Claude et les serveurs LSP existants (typescript-language-server, pyright, gopls, rust-analyzer, etc.).

## Objectif

Integrer lsmcp comme serveur MCP dans OpenFlow pour donner aux agents Claude un acces complet aux outils LSP, sans reimplementer ce qui existe deja.

## Comportement attendu

### Installation

L'utilisateur execute `./install.sh` (ou `./install.sh mcp`) :
1. Le script verifie que Node.js >= 22 est installe
2. Si Node.js n'est pas disponible ou version insuffisante, un warning est affiche et lsmcp est ignore
3. Si Node.js est OK, le script configure lsmcp dans `opencode.json`
4. L'utilisateur voit "Configured MCP: lsmcp" dans le resume d'installation

### Utilisation par Claude

Une fois installe, Claude a acces aux outils suivants :

| Outil | Description |
|-------|-------------|
| `get_hover` | Informations de type et documentation au survol |
| `get_definitions` | Naviguer vers la definition d'un symbole |
| `find_references` | Trouver toutes les utilisations d'un symbole |
| `get_document_symbols` | Liste des symboles dans un fichier (outline) |
| `get_workspace_symbols` | Recherche de symboles dans tout le projet |
| `get_diagnostics` | Erreurs et warnings d'un fichier |
| `get_all_diagnostics` | Diagnostics de tout le projet |
| `get_completion` | Suggestions d'autocompletion |
| `get_signature_help` | Aide sur les signatures de fonctions |
| `format_document` | Formater un fichier |
| `get_code_actions` | Quick-fixes et refactorings disponibles |
| `rename_symbol` | Renommer un symbole dans tout le projet |
| `check_capabilities` | Voir les capacites LSP supportees |

### Langages supportes

lsmcp supporte automatiquement les langages pour lesquels un serveur LSP est installe :
- TypeScript/JavaScript (typescript-language-server)
- Python (pyright, basedpyright, ruff)
- Go (gopls)
- Rust (rust-analyzer)
- C/C++ (clangd)
- Et bien d'autres...

### Prerequis utilisateur

- Node.js >= 22 installe sur la machine
- Les serveurs LSP des langages souhaites (souvent installes automatiquement par les IDE)

## Checklist de validation

- [ ] Dossier `servers/lsmcp/` cree avec README.md et configure.py
- [ ] `install.sh` modifie pour gerer lsmcp (verification Node.js, appel configure.py)
- [ ] Configuration ajoutee correctement dans `opencode.json` apres installation
- [ ] Warning clair si Node.js < 22 ou absent
- [ ] Claude peut utiliser `get_hover` sur un fichier TypeScript
- [ ] Claude peut utiliser `find_references` pour trouver les usages d'une fonction
- [ ] Claude peut utiliser `get_diagnostics` pour voir les erreurs
- [ ] Documentation dans `servers/lsmcp/README.md` complete
