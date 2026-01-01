# Rapport Maintainer - {{TAG_OR_DATE}}

> Genere le {{GENERATION_DATE}} par l'agent Maintainer

## Resume executif

| Indicateur | Valeur |
|------------|--------|
| Sante globale | {{HEALTH_STATUS}} |
| Actions recommandees | {{ACTION_COUNT}} |
| Fichiers a surveiller | {{FILES_TO_WATCH}} |
| Alertes critiques | {{CRITICAL_COUNT}} |

---

## Metriques d'evolution

### Comparaison avec {{PREVIOUS_TAG}}

| Metrique | Actuel | Precedent | Variation | Tendance |
|----------|--------|-----------|-----------|----------|
| Total lignes | {{TOTAL_LINES}} | {{PREV_LINES}} | {{LINES_DIFF}} | {{LINES_TREND}} |
| Total fichiers | {{TOTAL_FILES}} | {{PREV_FILES}} | {{FILES_DIFF}} | {{FILES_TREND}} |
| Lignes ajoutees | {{LINES_ADDED}} | - | - | - |
| Lignes supprimees | {{LINES_REMOVED}} | - | - | - |
| Variation nette | {{NET_CHANGE}} | - | - | - |
| Taux de churn | {{CHURN_RATE}} | {{PREV_CHURN}} | {{CHURN_DIFF}} | {{CHURN_TREND}} |

### Metriques par langage

| Langage | Fichiers | Lignes | % du projet |
|---------|----------|--------|-------------|
{{LANGUAGE_METRICS}}

---

## Alertes

### Fichiers trop grands (> 400 lignes)

| Fichier | Lignes | Severite | Recommandation |
|---------|--------|----------|----------------|
{{LARGE_FILES}}

> Seuils: WARNING > 300 lignes, CRITICAL > 500 lignes

### Code duplique detecte

{{DUPLICATE_BLOCKS}}

> Blocs similaires de plus de 10 lignes

### Architecture

{{ARCHITECTURE_ISSUES}}

### TODO/FIXME dans le code

| Type | Nombre | Fichiers concernes |
|------|--------|-------------------|
| TODO | {{TODO_COUNT}} | {{TODO_FILES}} |
| FIXME | {{FIXME_COUNT}} | {{FIXME_FILES}} |
| HACK | {{HACK_COUNT}} | {{HACK_FILES}} |

---

## Recommandations

### Priorite haute

{{HIGH_PRIORITY_RECOMMENDATIONS}}

### Priorite moyenne

{{MEDIUM_PRIORITY_RECOMMENDATIONS}}

### Priorite basse

{{LOW_PRIORITY_RECOMMENDATIONS}}

---

## Historique des metriques (5 derniers tags)

| Tag | Date | Lignes | Fichiers | Churn |
|-----|------|--------|----------|-------|
{{METRICS_HISTORY}}

---

## Commandes utilisees

```bash
# Comptage lignes de code
find . -type f \( -name "*.py" -o -name "*.ts" -o -name "*.md" \) | xargs wc -l

# Fichiers > 400 lignes
find . -type f -name "*.py" -exec wc -l {} \; | awk '$1 > 400'

# TODO/FIXME count
grep -r "TODO\|FIXME\|HACK" --include="*.py" --include="*.ts" | wc -l

# Git diff stats depuis dernier tag
git diff --stat {{PREVIOUS_TAG}}..HEAD
```

---

**Rapport genere par Agent Maintainer v1.0**
