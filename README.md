# Module 00 - Introduction

Bienvenue dans le premier module de la formation. L'objectif est de valider l'environnement, prendre en main la structure du dépôt et réaliser un tout premier exercice Python.

---

## Objectifs

- Vérifier que l'environnement Python et les dépendances fonctionnent
- Comprendre la structure de base du depot
- Ecrire un premier module Python simple

---

## Prerequis

- Avoir exécuté `conda_init.bat` (Windows) ou `conda_init.sh` (Linux/macOS)
- Avoir active l'environnement `formation_env`

Vérification rapide :
```bash
python --version
```

---

## Structure minimale

- `src/` : code source
- `correction/` : solutions (à consulter après l'exercice)

---

## Exercice

### 1) Tester l'environnement

- Lancez :
```bash
python src/main.py
```

Attendu :
- Le script affiche que l'environnement est fonctionnel

### 2) Implémenter `greet`

Ouvrez `src/intro.py` et complétez la fonction `greet` selon la spécification :

- Entrée : un nom (string)
- Sortie : une phrase de salutation
- Règles :
  - Si le nom est vide ou compose uniquement d'espaces, retourner `"Bonjour !"`
  - Sinon, retourner `"Bonjour, <nom>!"`

Exemples :
- `greet("Ada")` -> `"Bonjour, Ada!"`
- `greet("  ")` -> `"Bonjour !"`

### 3) Comprendre le script d'exécution

Le fichier `src/intro_main.py` est déjà prêt. Il :
- Lit un nom en ligne de commande (optionnel)
- Affiche la salutation via `greet`

Exemples d'exécution :
```bash
python src/intro_main.py Ada
python src/intro_main.py
```

---

## Validation

```bash
python src/intro_main.py Ada
```

Le script doit afficher une salutation.
Note : exécutez les commandes depuis la racine du dépôt.

---

## Correction

Une solution de référence est disponible dans `correction/`.
Ne la consultez qu'après avoir tenté l'exercice.
