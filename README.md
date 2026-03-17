# Module 06 — Git avancé

Objectif : apprendre à utiliser Git de manière approfondie en respectant les conventions de collaboration avec Git.

---

## Objectifs pédagogiques

- Comprendre la logique des branches et leurs catégories
- Savoir rédiger et utiliser des Pull Requests (PR) / Merge Requests (MR)
- Savoir rédiger des messages de commit clairs et précis
- Comprendre le cycle de vie d'un projet collaboratif
- Gérer les conflits et la synchronisation d'un dépôt

---

## Prérequis

- Avoir terminé les modules précédents
- Avoir Git installé et configuré (`git config --global user.name` / `user.email`)

---

## Théorie

### 1. Workflow basé sur des branches protégées

Le workflow repose sur une branche `main` protégée et une branche `dev` pour l'intégration des fonctionnalités. Les branches de travail ont une **durée de vie courte** et sont supprimées après fusion.

```
main  ← branche stable, protégée (jamais de commit direct)
 └── dev  ← branche d'intégration des features
      ├── feature/ajout-calcul-prime
      ├── bugfix/correction-montant-sinistre
      └── docs/mise-a-jour-readme
```

### 2. Convention de nommage des branches

Format : `<type>/<description-courte>`

| Préfixe        | Usage                                  | Exemple                            |
|----------------|----------------------------------------|------------------------------------|
| `feature/`     | Nouvelle fonctionnalité                | `feature/ajout-calcul-prime`       |
| `bugfix/`      | Correction de bug                      | `bugfix/correction-montant-sinistre` |
| `hotfix/`      | Urgence production                     | `hotfix/fix-crash-souscription`    |
| `chore/`       | Tâche diverse (config, dépendances)    | `chore/mise-a-jour-requirements`   |
| `refactor/`    | Restructuration de code                | `refactor/simplifier-calcul-prime` |
| `docs/`        | Documentation seule                    | `docs/ajout-guide-contribution`    |
| `tests/`       | Ajout ou modification de tests         | `tests/couverture-service-contrat` |
| `experiment/`  | Test expérimental                      | `experiment/nouveau-moteur-calcul` |
| `release/`     | Préparation d'une version              | `release/v1.2.0`                   |
| `implement/`   | Résolution de conflits d'intégration   | `implement/merge-feature-calcul`   |

### 3. Convention de nommage des commits

Les commits doivent être **atomiques** (un changement logique par commit) et **fréquents**.

Format : `VERBE : description courte`

| Préfixe      | Usage                              | Exemple                                     |
|--------------|------------------------------------|---------------------------------------------|
| `ADD`        | Ajout d'une fonctionnalité         | `ADD : calcul de prime auto`                |
| `FIX`        | Correction d'un bug                | `FIX : montant sinistre négatif`            |
| `EXTRACT`    | Extraction de logique              | `EXTRACT : validation client en service`    |
| `REFACTOR`   | Restructuration sans changement fonctionnel | `REFACTOR : simplification du calcul` |
| `HANDLE`     | Gestion d'un cas particulier       | `HANDLE : client mineur refusé`             |
| `UPDATE`     | Mise à jour d'un élément existant  | `UPDATE : règles d'éligibilité`             |
| `DELETE`     | Suppression de code ou fichier     | `DELETE : ancien service inutilisé`         |
| `RENAME`     | Renommage                          | `RENAME : ContratService → SouscriptionService` |

### 4. Pull Request / Merge Request

Avant de fusionner, chaque branche doit passer par une **PR/MR** avec :
- Une **description précise** des changements
- Une **revue de code** par un pair
- Un **rebase** ou **squash** pour garder un historique propre

#### Template de PR

```markdown
## Description
Explication claire des changements apportés.

Fixes #<numéro d'issue>

## Type de changement
- [ ] Correction de bug
- [ ] Nouvelle fonctionnalité
- [ ] Mise à jour de documentation

## Checklist
- [ ] Le code respecte les conventions du projet
- [ ] Les tests sont ajoutés/mis à jour
- [ ] La documentation est à jour
```

#### Template d'Issue — Bug Report

```markdown
## Description du bug
Description claire du problème.

## Étapes pour reproduire
1. Aller sur '...'
2. Cliquer sur '...'
3. Observer l'erreur

## Comportement attendu
Ce qui devrait se passer.

## Environnement
- OS : [ex. Windows 11]
- Version : [ex. v2.3.4]
```

#### Template d'Issue — Idée / Discussion

```markdown
## Résumé
Description brève de l'idée.

## Problème
Quel problème cela résout-il ?

## Solution proposée
Quelle approche suggérez-vous ?

## Bénéfices
Pourquoi cette idée devrait-elle être considérée ?
```

### 5. Gestion des conflits et synchronisation

- Faire `git pull` **régulièrement** pour rester à jour
- Résoudre les conflits **dans la PR**, pas sur `main`
- Ne **jamais** faire de `force-push` sur une branche partagée — privilégier la création d'une branche `implement/` pour résoudre les conflits

---

## Exercices

Les exercices sont détaillés dans le fichier **[Ennoncé.md](src/module/06_git-advanced/Ennoncé.md)**.

---

## Correction

Toutes les corrections sont dans le dossier `correction/`.
Consultez-les **uniquement après** avoir réalisé les exercices afin de maximiser votre apprentissage.