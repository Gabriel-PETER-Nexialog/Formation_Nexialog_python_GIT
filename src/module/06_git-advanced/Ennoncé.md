# Exercice — Mise en pratique des bonnes pratiques Git

## Contexte

Vous êtes développeur dans une équipe qui travaille sur un système de gestion d'assurances. Vous allez créer un dépôt Git depuis zéro et simuler un workflow collaboratif complet en appliquant **toutes les bonnes pratiques** vues en théorie.

---

## Étape 1 — Initialisation du dépôt

1. Créez un nouveau dossier `assurance-projet` et initialisez un dépôt Git :
   ```bash
   mkdir assurance-projet
   cd assurance-projet
   git init
   ```

2. Créez un fichier `README.md` avec le contenu suivant :
   ```markdown
   # Projet Gestion Assurance
   Application de gestion de contrats d'assurance.
   ```

3. Créez un fichier `.gitignore` adapté à Python :
   ```
   __pycache__/
   *.pyc
   .env
   venv/
   ```

4. Faites votre premier commit :
   ```bash
   git add README.md .gitignore
   git commit -m "ADD : initialisation du projet avec README et .gitignore"
   ```

---

## Étape 2 — Mise en place du workflow de branches

1. Créez la branche `dev` à partir de `main` :
   ```bash
   git switch -C dev
   ```

2. Vérifiez que vous êtes bien sur `dev` :
   ```bash
   git branch
   ```

> À partir de maintenant, **toutes les branches de travail partent de `dev`**, jamais de `main`.

---

## Étape 3 — Créer une feature avec les bonnes conventions

1. Depuis `dev`, créez une branche pour ajouter le modèle Client :
   ```bash
   git checkout -b feature/ajout-modele-client
   ```

2. Créez le fichier `client.py` :
   ```python
   class Client:
       def __init__(self, nom: str, prenom: str, age: int, a_impaye: bool = False):
           self.nom = nom
           self.prenom = prenom
           self.age = age
           self.a_impaye = a_impaye

       def est_majeur(self) -> bool:
           return self.age >= 18

       def est_eligible(self) -> bool:
           return self.est_majeur() and not self.a_impaye
   ```

3. Faites un commit **atomique** avec un message clair :
   ```bash
   git add client.py
   git commit -m "ADD : modèle Client avec vérification éligibilité"
   ```

4. Ajoutez maintenant une méthode `__str__` au client :
   ```python
   def __str__(self) -> str:
       return f"{self.prenom} {self.nom} ({self.age} ans)"
   ```

5. Commitez cette modification séparément :
   ```bash
   git add client.py
   git commit -m "ADD : représentation textuelle du client"
   ```

> Remarquez : **deux commits séparés** pour deux changements logiques distincts. C'est le principe du commit atomique.

---

## Étape 4 — Fusionner via une Pull Request simulée

1. Revenez sur `dev` et fusionnez votre feature :
   ```bash
   git checkout dev
   git merge --no-ff feature/ajout-modele-client -m "MERGE : feature/ajout-modele-client → dev"
   ```

   > L'option `--no-ff` force la création d'un commit de merge, ce qui garde la trace de la branche dans l'historique.

2. Supprimez la branche de feature (durée de vie courte) :
   ```bash
   git branch -d feature/ajout-modele-client
   ```

3. Vérifiez l'historique :
   ```bash
   git log --oneline --graph
   ```

---

## Étape 5 — Créer une deuxième feature en parallèle

1. Depuis `dev`, créez une branche pour le service de contrat :
   ```bash
   git checkout -b feature/service-contrat
   ```

2. Créez le fichier `contrat.py` :
   ```python
   from datetime import datetime


   class Contrat:
       _compteur = 0

       def __init__(self, type_contrat: str, client, prime: float):
           Contrat._compteur += 1
           self.numero = f"{type_contrat.upper()}-{datetime.now().year}-{Contrat._compteur:03d}"
           self.type_contrat = type_contrat
           self.client = client
           self.prime = prime
           self.actif = True

       def __str__(self) -> str:
           return f"Contrat {self.numero} - {self.type_contrat} - Prime: {self.prime}€"
   ```

3. Commitez :
   ```bash
   git add contrat.py
   git commit -m "ADD : modèle Contrat avec génération de numéro"
   ```

4. Créez le fichier `service_souscription.py` :
   ```python
   from client import Client
   from contrat import Contrat


   class ServiceSouscription:
       TAUX = {
           "auto": 0.05,
           "habitation": 3.5,
           "sante": 12,
       }

       def calculer_prime(self, type_contrat: str, valeur: float) -> float:
           if type_contrat not in self.TAUX:
               raise ValueError(f"Type de contrat inconnu : {type_contrat}")
           return valeur * self.TAUX[type_contrat]

       def appliquer_remise_fidelite(self, prime: float, anciennete: int) -> float:
           if anciennete >= 5:
               return prime * 0.9
           return prime

       def souscrire(self, client: Client, type_contrat: str, valeur: float, anciennete: int = 0) -> Contrat:
           if not client.est_eligible():
               raise ValueError(f"Client non éligible : {client}")

           prime = self.calculer_prime(type_contrat, valeur)
           prime = self.appliquer_remise_fidelite(prime, anciennete)
           return Contrat(type_contrat, client, prime)
   ```

5. Commitez :
   ```bash
   git add service_souscription.py
   git commit -m "ADD : service de souscription avec calcul de prime et remise fidélité"
   ```

---

## Étape 6 — Simuler un conflit et le résoudre

1. **Sans fusionner** `feature/service-contrat`, revenez sur `dev` :
   ```bash
   git checkout dev
   ```

2. Créez une branche de documentation :
   ```bash
   git checkout -b docs/mise-a-jour-readme
   ```

3. Modifiez `README.md` pour ajouter une section :
   ```markdown
   # Projet Gestion Assurance
   Application de gestion de contrats d'assurance.

   ## Modules
   - `client.py` — Modèle client avec vérification d'éligibilité
   ```

4. Commitez :
   ```bash
   git add README.md
   git commit -m "UPDATE : ajout de la section Modules au README"
   ```

5. Fusionnez dans `dev` :
   ```bash
   git checkout dev
   git merge --no-ff docs/mise-a-jour-readme -m "MERGE : docs/mise-a-jour-readme → dev"
   git branch -d docs/mise-a-jour-readme
   ```

6. Maintenant, fusionnez `feature/service-contrat` dans `dev` :
   ```bash
   git merge --no-ff feature/service-contrat -m "MERGE : feature/service-contrat → dev"
   ```

   > Si un conflit apparaît (par exemple sur `README.md`), résolvez-le manuellement, puis :
   ```bash
   git add .
   git commit -m "FIX : résolution du conflit de merge sur README.md"
   ```

7. Supprimez la branche :
   ```bash
   git branch -d feature/service-contrat
   ```

---

## Étape 7 — Ajouter des tests avec la bonne convention

1. Depuis `dev`, créez une branche de tests :
   ```bash
   git checkout -b tests/couverture-client
   ```

2. Créez le fichier `test_client.py` :
   ```python
   import pytest
   from client import Client


   class TestClient:
       def test_client_majeur_est_eligible(self):
           client = Client("Dupont", "Jean", 30)
           assert client.est_eligible() is True

       def test_client_mineur_non_eligible(self):
           client = Client("Martin", "Lucas", 16)
           assert client.est_eligible() is False

       def test_client_avec_impaye_non_eligible(self):
           client = Client("Durand", "Marie", 45, a_impaye=True)
           assert client.est_eligible() is False

       def test_representation_client(self):
           client = Client("Dupont", "Jean", 30)
           assert str(client) == "Jean Dupont (30 ans)"
   ```

3. Commitez :
   ```bash
   git add test_client.py
   git commit -m "ADD : tests unitaires pour le modèle Client"
   ```

4. Fusionnez dans `dev` :
   ```bash
   git checkout dev
   git merge --no-ff tests/couverture-client -m "MERGE : tests/couverture-client → dev"
   git branch -d tests/couverture-client
   ```

---

## Étape 8 — Correction de bug avec la bonne convention

1. Depuis `dev`, créez une branche bugfix :
   ```bash
   git checkout -b bugfix/validation-type-contrat
   ```

2. Modifiez `service_souscription.py` — ajoutez une validation dans la méthode `souscrire` :
   ```python
   def souscrire(self, client: Client, type_contrat: str, valeur: float, anciennete: int = 0) -> Contrat:
       if not client.est_eligible():
           raise ValueError(f"Client non éligible : {client}")
       if valeur <= 0:
           raise ValueError("La valeur assurée doit être positive")

       prime = self.calculer_prime(type_contrat, valeur)
       prime = self.appliquer_remise_fidelite(prime, anciennete)
       return Contrat(type_contrat, client, prime)
   ```

3. Commitez :
   ```bash
   git add service_souscription.py
   git commit -m "FIX : ajout validation valeur positive dans souscription"
   ```

4. Fusionnez dans `dev` :
   ```bash
   git checkout dev
   git merge --no-ff bugfix/validation-type-contrat -m "MERGE : bugfix/validation-type-contrat → dev"
   git branch -d bugfix/validation-type-contrat
   ```

---

## Étape 9 — Préparer une release

1. Depuis `dev`, créez une branche de release :
   ```bash
   git checkout -b release/v1.0.0
   ```

2. Mettez à jour `README.md` avec la version finale :
   ```markdown
   # Projet Gestion Assurance — v1.0.0
   Application de gestion de contrats d'assurance.

   ## Modules
   - `client.py` — Modèle client avec vérification d'éligibilité
   - `contrat.py` — Modèle contrat avec génération de numéro
   - `service_souscription.py` — Service de souscription avec calcul de prime

   ## Tests
   - `test_client.py` — Tests unitaires du modèle Client
   ```

3. Commitez :
   ```bash
   git add README.md
   git commit -m "UPDATE : README pour la release v1.0.0"
   ```

4. Fusionnez dans `main` :
   ```bash
   git checkout main
   git merge --no-ff release/v1.0.0 -m "MERGE : release/v1.0.0 → main"
   ```

5. Créez un tag de version :
   ```bash
   git tag -a v1.0.0 -m "Version 1.0.0 — Première release"
   ```

6. Fusionnez aussi dans `dev` pour synchroniser :
   ```bash
   git checkout dev
   git merge main -m "MERGE : synchronisation dev avec main après release v1.0.0"
   ```

7. Supprimez la branche de release :
   ```bash
   git branch -d release/v1.0.0
   ```

---

## Étape 10 — Vérification finale

1. Visualisez l'historique complet du projet :
   ```bash
   git log --oneline --graph --all
   ```

2. Vérifiez que toutes les branches de travail ont été supprimées :
   ```bash
   git branch
   ```
   > Vous ne devriez voir que `main` et `dev`.

3. Vérifiez le tag :
   ```bash
   git tag -l
   ```

---

## Récapitulatif des bonnes pratiques appliquées

| Bonne pratique                     | Où dans l'exercice                   |
|------------------------------------|--------------------------------------|
| Branches à durée de vie courte     | Étapes 3 à 8                        |
| Convention de nommage des branches | `feature/`, `docs/`, `tests/`, `bugfix/`, `release/` |
| Commits atomiques                  | Étape 3 (deux commits séparés)      |
| Messages de commit clairs          | Tous les commits avec préfixes      |
| Merge `--no-ff`                    | Toutes les fusions                  |
| Résolution de conflits             | Étape 6                             |
| Workflow main/dev                  | Étapes 2 et 9                       |
| Tags de version                    | Étape 9                             |
| Suppression des branches fusionnées| Après chaque merge                  |