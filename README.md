# Formation Python Avancée & Git

> *Bienvenue dans cette formation complète dédiée aux bonnes pratiques de développement Python et à la maîtrise de Git.*  
> Que vous soyez développeur intermédiaire souhaitant structurer votre code ou équipe cherchant à adopter des standards professionnels, cette formation vous accompagne pas à pas.

---

##  Table des matières

- [Bienvenue](#-bienvenue)
- [Contenu de la formation](#-contenu-de-la-formation)
- [Getting Started](#-getting-started)
- [Structure de la formation](#-structure-de-la-formation)
- [Conventions & Bonnes pratiques Git](#-conventions--bonnes-pratiques-git)

---

##  Bienvenue

Cette formation a été conçue pour vous donner les outils concrets pour écrire un code **propre, maintenable et testable**, tout en collaborant efficacement grâce à **Git**.

Vous apprendrez à :
- Appliquer les principes fondamentaux du développement logiciel (SOLID, DRY, YAGNI)
- Concevoir votre code avec des **design patterns** reconnus
- Écrire des **tests robustes** selon les approches TDD et BDD
- Utiliser **Git** de manière professionnelle en équipe

---

##  Contenu de la formation

###  Bonnes pratiques de développement Python

#### Principes fondamentaux
| Principe           | Description                                                                             |
|--------------------|-----------------------------------------------------------------------------------------|
| **SOLID**          | Single Responsibility, Open/Closed, Liskov, Interface Segregation, Dependency Inversion |
| **DRY**            | *Don't Repeat Yourself* — éviter la duplication de logique                              |
| **YAGNI**          | *You Aren't Gonna Need It* — ne pas sur-concevoir                                       |


#### Design Patterns
-  **Singleton** — instance unique partagée
-  **Factory** — création d'objets découplée
-  **Builder** — construction d'objets complexes étape par étape
-    **Documentaiton** —  *Catalog Desing Pattern* : https://refactoring.guru/design-patterns/python 
---

###  Architecture des tests

| Type | Approche | Outil principal |
|------|----------|-----------------|
| **Tests Unitaires** | Tester une unité isolée | `pytest` |
| **TDD** | *Test Driven Development* — écrire le test avant le code | `pytest` |
| **BDD** | *Behavior Driven Development* — tester le comportement métier | `behave` |

Architecture recommandée :
```
tests/
├── unit/
│   └── test_*.py
├── integration/
│   └── test_*.py
└── features/           # BDD
    ├── *.feature
    └── steps/
```

---

###  Git — Utilisation & Bonnes pratiques

#### Commandes essentielles couvertes
```bash
git clone        # Cloner un dépôt
git fetch        # Récupérer les changements distants
git pull         # Fetch + merge
git add          # Indexer les modifications
git commit       # Valider les modifiactions Indexer
git push         # Pousser vers le dépôt distant
git branch       # Gérer les branches
git merge        # Fusionner des branches
git rebase       # Réécrire l'historique proprement
git stash        # Mettre de côté des modifications
git log          # Consulter l'historique
```

#### Stratégie de branches
```
main / master   ←  Protégée — production stable
dev             ←  Protégée — intégration continue
feature/xxx     ← Développement de fonctionnalités
fix/xxx         ← Corrections de bugs
hotfix/xxx      ← Correctifs urgents en production
release/x.x.x   ← Préparation d'une version
```

#### Convention de nommage des commits
```
feat:     nouvelle fonctionnalité
fix:      correction de bug
docs:     documentation uniquement
style:    formatage, pas de changement logique
refactor: refactorisation sans ajout de feature
test:     ajout ou modification de tests
chore:    maintenance, dépendances
```

Exemples :
```
feat: add singleton pattern implementation
fix: resolve infinite loop in factory builder
test: add unit tests for DRY principle module
```

pour plus de détails visiter ce site : [**git-cheat-sheet**](https://git-scm.com/cheat-sheet)

---


##  Getting Started

### Prérequis

Avant de commencer, assurez-vous d'avoir installé :

-  [**Anaconda**](https://www.anaconda.com/download) (dernière version)
-  [**Git**](https://git-scm.com/downloads) (2.x ou supérieur)
-  Un terminal (PowerShell, bash ou le terminal Anaconda)

Vérifiez vos installations :
```bash
conda --version
git --version
```

---

### Installation de l'environnement

**1. Clonez le dépôt de la formation**
```bash
git clone https://github.com/<organisation>/formation-python-git.git
cd formation-python-git
```

**2. Lancez le script d'initialisation**

>  **Windows** — Double-cliquez sur le fichier ou exécutez dans un terminal :
```bash
conda_init.bat
```

> **Linux / macOS**
```bash
bash conda_init.sh
```


> Dans l'invite de commande mettez le noms de l'environnement conda `formation_env` puis choissiez la version de python **Python 3.13**

Le script va automatiquement :
- Installer toutes les dépendances nécessaires (`pytest`, `behave`, etc.)
- Vérifier que l'environnement est prêt

> ⚠️ **Important** : Vous devez nommer votre environnement **`formation_env`** — le script le vérifie automatiquement.

**3. Activez l'environnement**
```bash
conda activate formation_env
```

**4. Vérifiez que tout est opérationnel**
```bash
python --version    # doit afficher Python 3.13.x
pytest --version
behave --version
```

---

##  Structure de la formation

La formation est organisée **de branche en branche**. Chaque branche correspond à un module indépendant que vous explorez dans l'ordre.
Le format est volontairement **court et direct** pour tenir sur une journée.
```
main
└── module/00-introduction          ← Point de départ
    └── module/01-git-basics         ← Git fondamentaux
        └── module/02-solid          ← Principes SOLID
            └── module/03-dry-yagni  ← DRY & YAGNI
                └── module/04-patterns ← Design Patterns
                    └── module/05-tests-tdd ← Tests + TDD (workflow)
                        └── module/06-git-advanced ← Git avancé
                                  
```

### Navigation entre les modules

Pour passer au module suivant :
```bash
# Voir tous les modules disponibles
git branch 

# Aller sur le premier module
git switch module/00-introduction

# Passer au module suivant
git switch module/01-git-basics
```

Chaque branche contient :
-  Un `README.md` dédié avec l'explication de la théorie, les objectifs et les consignes
-  Des exercices à compléter
-  Une correction dans un sous-dossier `correction/`

---

##  Conventions & Bonnes pratiques Git

### Branches protégées

| Branche | Protection | Règle |
|---------|---------|-------|
| `main` / `master` |  **Stricte** | Merge via Pull Request uniquement, 1 reviewer minimum |
| `dev` |  **Modérée** | Merge via Pull Request, CI verte obligatoire |
| `feature/*` | Libre | Nommage obligatoire `feature/nom-explicite` |

### Règles d'or
1. **Ne jamais pusher directement** sur `main` ou `dev`
2. **Une branche = une fonctionnalité** (courte durée de vie)
3. **Commits atomiques** — un commit = une modification logique
4. **Messages de commit en anglais**, format `type: description`
5. **Toujours pull avant de push** pour éviter les conflits

---

*Bonne formation à tous !*
