# Module 05 - Tests, TDD & BDD

Objectif : apprendre à écrire des tests unitaires, et à développer en suivant les méthodologies TDD et BDD.

---

## Objectifs

- Comprendre la pyramide de tests et savoir où se situent les tests unitaires
- Savoir écrire des tests unitaires avec `unittest`
- Savoir développer en TDD (Test-Driven Development)
- Savoir développer en BDD (Behavior-Driven Development)
- Respecter les bonnes pratiques vues précédemment (SOLID, Design Patterns, DRY, YAGNI)

---

## Prérequis

- Avoir terminé les modules précédents

---

## Théorie

### Pyramide de Tests

La pyramide de tests est un modèle qui classe les tests par niveau de granularité :

```
        /  E2E  \          ← peu nombreux, lents, coûteux
       / Intégration \     ← vérifient les interactions entre modules
      /  Tests Unitaires  \ ← nombreux, rapides, isolés
```

- **Tests unitaires** (base) : testent une seule fonction ou classe en isolation. Rapides, nombreux, faciles à maintenir.
- **Tests d'intégration** (milieu) : testent l'interaction entre plusieurs composants (ex. service + base de données).
- **Tests End-to-End / E2E** (sommet) : testent le système complet du point de vue utilisateur. Lents et fragiles.

Dans ce module, on se concentre sur les **tests unitaires** avec deux approches : **TDD** et **BDD**.

### Tests Unitaires

Un test unitaire vérifie le comportement d'une **unité de code isolée** (fonction, méthode, classe). Il suit la structure **Given / When / Then** (ou **Arrange / Act / Assert**) :

```python
import unittest

class TestCalculPrime(unittest.TestCase):
    def test_prime_vehicule_standard(self):
        # Given — on prépare les données
        valeur_vehicule = 20_000

        # When — on exécute le code à tester
        prime = valeur_vehicule * 0.05

        # Then — on vérifie le résultat
        self.assertEqual(prime, 1000.0)
```

Bonnes pratiques :
- Un test = un comportement précis
- Le nom du test décrit ce qu'il vérifie (`test_prime_jeune_conducteur_applique_surprime`)
- Les tests sont indépendants les uns des autres
- `setUp()` / `tearDown()` pour le contexte partagé

### TDD — Test-Driven Development

Le TDD est une méthodologie où l'on écrit les **tests avant le code**. Elle suit un cycle en trois étapes :

1. **RED** — Écrire un test qui échoue (le code n'existe pas encore)
2. **GREEN** — Écrire le minimum de code pour faire passer le test
3. **REFACTOR** — Améliorer le code sans casser les tests

```
  ┌──────┐     ┌──────┐     ┌──────────┐
  │ RED  │ ──► │GREEN │ ──► │ REFACTOR │ ──┐
  └──────┘     └──────┘     └──────────┘   │
      ▲                                     │
      └─────────────────────────────────────┘
```

**Pourquoi TDD ?**
- Force à réfléchir au comportement attendu avant de coder
- Garantit une couverture de tests élevée
- Produit un code plus simple (on n'écrit que le nécessaire → YAGNI)
- Les tests servent de documentation vivante

### BDD — Behavior-Driven Development

Le BDD étend le TDD en décrivant les comportements du système avec un **langage naturel structuré**. On utilise le format **Given / When / Then** dans les noms de tests ou dans des scénarios :

```
Scénario : Un client fidèle obtient une remise
  Étant donné un client avec 7 ans d'ancienneté
  Quand on calcule sa remise
  Alors la remise est de 10%
```

En Python avec `unittest`, le BDD se traduit par des **noms de tests descriptifs** et une structure claire :

```python
class TestRemiseClient(unittest.TestCase):
    def test_client_fidele_obtient_remise_10_pourcent(self):
        """Étant donné un client avec >= 5 ans d'ancienneté,
        quand on calcule sa remise, alors elle est de 10%."""
        # Given
        client = {"nom": "Dupont", "anciennete_ans": 7}

        # When
        remise = calculer_remise_fidelite(client)

        # Then
        self.assertEqual(remise, 0.10)
```

**Différence TDD vs BDD** :
- **TDD** se concentre sur le « comment ça marche » (perspective développeur)
- **BDD** se concentre sur le « ce que ça fait » (perspective métier/utilisateur)
- En pratique, BDD = TDD + noms de tests orientés comportement métier

## Exercices

### a) Exercice 1 : TDD — Service de gestion de sinistres

Objectif : coder un service de gestion de sinistres en suivant la méthodologie TDD. Vous devez respecter les bonnes pratiques de développement vues précédemment (SOLID, DRY, YAGNI).

**Problème** :
Une compagnie d'assurance a besoin d'un service pour gérer les sinistres. Le service doit permettre de :
- Déclarer un sinistre (numéro, type, montant, franchise, date d'événement, date de déclaration)
- Vérifier la recevabilité d'un sinistre (déclaration dans les 5 jours suivant l'événement)
- Calculer le remboursement (montant - franchise, minimum 0)
- Appliquer un plafond de remboursement (le remboursement ne peut pas dépasser le plafond du contrat)
- Détecter les sinistres suspects (montant > 15 000€ ET déclaration le jour même de l'événement)

Consigne :
    Suivez le cycle TDD (RED → GREEN → REFACTOR) :
    1. Écrivez d'abord les tests dans le fichier `test/test_modules/test_05_tests_tdd_bdd/test_tdd/test_exercice1.py`
    2. Puis implémentez le code pour faire passer les tests dans `module/05_tests_tdd_bdd/tdd/exercice1.py`

    Vos tests doivent couvrir les cas suivants :
    - Sinistre recevable (déclaré dans les 5 jours)
    - Sinistre non recevable (déclaré trop tard)
    - Calcul du remboursement standard
    - Remboursement à zéro quand la franchise dépasse le montant
    - Remboursement plafonné
    - Détection d'un sinistre suspect
    - Sinistre non suspect (montant faible ou déclaration différée)

Modifier le code dans le fichier module/05_tests_tdd_bdd/tdd/exercice1.py

```python
from datetime import date


class Sinistre:
    """À implémenter en TDD — commencez par les tests !"""
    pass


class ServiceSinistre:
    """À implémenter en TDD — commencez par les tests !"""
    pass
```

Structure des tests attendue (dans test_tdd/test_exercice1.py) :

```python
import unittest
from datetime import date


class TestSinistre(unittest.TestCase):
    """Tests unitaires pour la classe Sinistre."""

    def test_sinistre_recevable_dans_les_5_jours(self):
        """Étant donné un sinistre déclaré 3 jours après l'événement,
        quand on vérifie la recevabilité, alors il est recevable."""
        # TODO : RED → écrire le test, puis GREEN → implémenter le code
        pass

    def test_sinistre_non_recevable_apres_5_jours(self):
        # TODO
        pass

    def test_remboursement_standard(self):
        # TODO
        pass

    def test_remboursement_zero_si_franchise_superieure(self):
        # TODO
        pass


class TestServiceSinistre(unittest.TestCase):
    """Tests unitaires pour le service de gestion des sinistres."""

    def test_remboursement_plafonne(self):
        # TODO
        pass

    def test_sinistre_suspect(self):
        # TODO
        pass

    def test_sinistre_non_suspect_montant_faible(self):
        # TODO
        pass
```

### b) Exercice 2 : BDD — Service de souscription de contrats

Objectif : coder un service de souscription en suivant l'approche BDD. Les tests décrivent des **scénarios métier** avec des noms en langage naturel. Vous devez respecter les bonnes pratiques vues précédemment.

**Problème** :
Le service de souscription doit gérer l'ensemble du processus pour un nouveau contrat :
- Vérifier l'éligibilité d'un client (majeur, pièce d'identité valide, pas d'impayés)
- Calculer la prime selon le type de contrat (auto: valeur * 0.05, habitation: surface * 3.5, santé: age * 12)
- Appliquer une remise fidélité (ancienneté >= 5 ans → 10% de réduction sur la prime)
- Générer un numéro de contrat au format "TYPE-ANNEE-NUMERO" (ex: "AUTO-2026-001")
- Refuser la souscription si le client n'est pas éligible

Consigne :
    Suivez l'approche BDD :
    1. Écrivez les tests sous forme de scénarios métier dans `test/test_modules/test_05_tests_tdd_bdd/test_bdd/test_exercice2.py`
    2. Puis implémentez le code dans `module/05_tests_tdd_bdd/bdd/exercice1.py`

    Vos scénarios doivent couvrir :
    - Un client majeur éligible peut souscrire
    - Un client mineur est refusé
    - Un client avec impayés est refusé
    - La prime auto est correctement calculée
    - La prime habitation est correctement calculée
    - Un client fidèle obtient 10% de réduction
    - Le numéro de contrat suit le bon format

Modifier le code dans le fichier module/05_tests_tdd_bdd/bdd/exercice1.py

```python
from datetime import date


class Client:
    
    """À implémenter en BDD — commencez par les scénarios !"""
    pass


class ServiceSouscription:
    """À implémenter en BDD — commencez par les scénarios !"""
    pass
```

Structure des tests attendue (dans test_bdd/test_exercice2.py) :

```python
import unittest
from datetime import date


class TestEligibiliteSouscription(unittest.TestCase):
    """Scénarios d'éligibilité à la souscription."""

    def test_client_majeur_avec_papiers_valides_est_eligible(self):
        """Étant donné un client de 30 ans avec une pièce d'identité valide et sans impayés,
        quand on vérifie son éligibilité,
        alors il est éligible à la souscription."""
        # TODO
        pass

    def test_client_mineur_est_refuse(self):
        """Étant donné un client de 16 ans,
        quand on vérifie son éligibilité,
        alors il est refusé."""
        # TODO
        pass

    def test_client_avec_impayes_est_refuse(self):
        """Étant donné un client avec des cotisations impayées,
        quand on vérifie son éligibilité,
        alors il est refusé."""
        # TODO
        pass


class TestCalculPrime(unittest.TestCase):
    """Scénarios de calcul de prime."""

    def test_prime_auto_est_5_pourcent_de_la_valeur_vehicule(self):
        """Étant donné un contrat auto pour un véhicule à 20 000€,
        quand on calcule la prime,
        alors elle est de 1 000€."""
        # TODO
        pass

    def test_client_fidele_obtient_10_pourcent_de_reduction(self):
        """Étant donné un client avec 7 ans d'ancienneté et un contrat auto à 20 000€,
        quand on calcule la prime avec remise fidélité,
        alors la prime est réduite de 10%."""
        # TODO
        pass


class TestNumerotationContrat(unittest.TestCase):
    """Scénarios de génération de numéros de contrat."""

    def test_numero_contrat_auto_suit_le_format_attendu(self):
        """Étant donné une souscription auto en 2026,
        quand on génère le numéro de contrat,
        alors il est au format AUTO-2026-001."""
        # TODO
        pass
```

## Correction
Tout les exercices ont la correction dans le dossier correction.
Afin de vous améliorer et de comprendre, veuillez la regarder seulement après avoir effectué les exercices.