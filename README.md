# Module 01 - Git Basics

Objectif : apprendre les bases de Git en pratiquant un petit flux de travail.

---

## Objectifs

- Voir un fichier non suivi dans `git status`
- Voir un fichier modifié dans `git status`
- Créer des commits simples
- Lire l'historique

---

## Prérequis

- Avoir terminé le module 00
- Avoir Git installé et accessible dans le terminal

---

## Exercice

### 1) Créer un fichier de notes

Créez `notes/git.md` avec 3 lignes (au choix) sur Git.

Exemple :
```md
- Git garde l'historique du code
- Git fonctionne par commits
- Git permet de collaborer
```

Vérifiez l'état de votre dépôt :
```bash
git status
```

### 2) Premier commit

```bash
git add notes/git.md
git commit -m "docs: add git notes"
```

### 3) Modifier le fichier

Ajoutez les 2 lignes suivantes à `notes/git.md` :

```md
- `git status` : affiche l'etat du depot
- `git log --oneline` : affiche l'historique court
```

Vérifiez :
```bash
git status
git diff
```

### 4) Second commit

```bash
git add notes/git.md
git commit -m "docs: extend git notes"
```

### 5) Lire l'historique

```bash
git log --oneline -n 5
```

---

## Validation

- `git status` doit être propre
- Le fichier `notes/git.md` contient au moins 5 lignes
- L'historique affiche 2 commits successifs

---

## Correction

Ce module n'a pas de correction : l'objectif est de pratiquer le flux Git.
