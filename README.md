# Module 04 - Design Patterns

Objectif : apprendre les design pattern afin d'améliorer la qualité de code en utilisant des patterns connus.

---

## Objectifs

- Comprendre le principes de Design pattern
- Savoir appliquer les design patterns Builder , Factory , Singleton
- Savoir déterminer choisir le design pattern le plus adapter aux besoins
- Sensibilisation aux autres design patterns

---

## Prérequis

- Avoir terminé les modules précédents

---

## Théorie

###  Les Design Pattern

Les design patterns (ou patrons de conception) sont des solutions éprouvées à des problèmes récurrents en programmation orientée objet. Ils ne sont pas du code prêt à copier-coller, mais des **schémas de conception** que l'on adapte à son contexte.

Pourquoi les utiliser :
- Ils offrent un **vocabulaire commun** entre développeurs (dire « c'est un Builder » est plus clair que d'expliquer toute la mécanique).
- Ils évitent de réinventer la roue face à des problèmes déjà résolus.
- Ils favorisent un code **extensible, maintenable et testable**.

On distingue trois grandes familles :
- **Créationnels** : gèrent la création d'objets (Builder, Factory, Singleton…)
- **Structurels** : organisent les relations entre objets (Adapter, Decorator, Facade…)
- **Comportementaux** : gèrent les interactions et responsabilités (Strategy, Observer, State…)

Dans ce module, nous nous concentrons sur trois patterns créationnels : **Builder**, **Factory** et **Singleton**.

Pour en savoir plus je vous invite à regarder les design pattern sur [**RefactoringGuruDesignPattern**](https://refactoring.guru/design-patterns)
###  Builder

Le pattern Builder sépare la **construction** d'un objet complexe de sa **représentation**. Il est utile quand un objet a de nombreux paramètres optionnels ou quand sa construction nécessite plusieurs étapes.

Sans Builder, on se retrouve avec des constructeurs à 10+ paramètres difficiles à lire :
```python
contrat = ContratAuto("Dupont", "Marie", 35, "Renault Clio", 15000, True, False, 3, "tous_risques", 500)
```

Avec le pattern Builder, la construction devient lisible et guidée :
```python
contrat = (
    ContratAutoBuilder()
    .avec_assure("Dupont", "Marie", 35)
    .avec_vehicule("Renault Clio", 15_000)
    .avec_formule("tous_risques")
    .avec_franchise(500)
    .build()
)
```

Voici un exemple complet  :
```python
class DevisAuto:
    """Objet complexe à construire."""
    def __init__(self):
        self.assure_nom = ""
        self.vehicule = ""
        self.valeur_vehicule = 0.0
        self.formule = "tiers"
        self.franchise = 300.0
        self.options = []

    def __str__(self):
        return (f"Devis {self.formule} pour {self.assure_nom} — "
                f"{self.vehicule} ({self.valeur_vehicule}€) — "
                f"Franchise {self.franchise}€ — Options : {self.options}")


class DevisAutoBuilder:
    """Builder qui construit un DevisAuto étape par étape."""
    def __init__(self):
        self._devis = DevisAuto()

    def avec_assure(self, nom: str):
        self._devis.assure_nom = nom
        return self  # retourne self pour chaîner les appels

    def avec_vehicule(self, nom: str, valeur: float):
        self._devis.vehicule = nom
        self._devis.valeur_vehicule = valeur
        return self

    def avec_formule(self, formule: str):
        self._devis.formule = formule
        return self

    def avec_franchise(self, franchise: float):
        self._devis.franchise = franchise
        return self

    def avec_option(self, option: str):
        self._devis.options.append(option)
        return self

    def build(self) -> DevisAuto:
        return self._devis


# Utilisation
devis = (
    DevisAutoBuilder()
    .avec_assure("Dupont")
    .avec_vehicule("Renault Clio", 15_000)
    .avec_formule("tous_risques")
    .avec_franchise(500)
    .avec_option("assistance 0km")
    .build()
)
print(devis)
```

###  Factory

Le pattern Factory délègue la **création d'objets** à une méthode ou une classe dédiée, plutôt que d'utiliser directement le constructeur. Le code appelant ne connaît pas la classe concrète instanciée : il demande un objet par type et la factory choisit la bonne classe.

Sans Factory, le code appelant est couplé aux classes concrètes :
```python
if type_contrat == "auto":
    contrat = ContratAuto(...)
elif type_contrat == "habitation":
    contrat = ContratHabitation(...)
elif type_contrat == "sante":
    contrat = ContratSante(...)
```

Avec le pattern Factory, la création est centralisée :
```python
contrat = ContratFactory.creer(type_contrat, **params)
```

Voici un exemple complet :
```python
from abc import ABC, abstractmethod


class Contrat(ABC):
    @abstractmethod
    def calculer_prime(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class ContratAuto(Contrat):
    def __init__(self, valeur_vehicule: float):
        self.valeur_vehicule = valeur_vehicule

    def calculer_prime(self) -> float:
        return self.valeur_vehicule * 0.05

    def description(self) -> str:
        return f"Contrat Auto — Véhicule : {self.valeur_vehicule}€"


class ContratHabitation(Contrat):
    def __init__(self, surface_m2: float):
        self.surface_m2 = surface_m2

    def calculer_prime(self) -> float:
        return self.surface_m2 * 3.5

    def description(self) -> str:
        return f"Contrat Habitation — {self.surface_m2} m²"


class ContratFactory:
    """Factory qui crée le bon type de contrat."""

    @staticmethod
    def creer(type_contrat: str, **kwargs) -> Contrat:
        if type_contrat == "auto":
            return ContratAuto(kwargs["valeur_vehicule"])
        elif type_contrat == "habitation":
            return ContratHabitation(kwargs["surface_m2"])
        else:
            raise ValueError(f"Type de contrat inconnu : {type_contrat}")


# Utilisation — le code ne connaît pas les classes concrètes
contrat = ContratFactory.creer("auto", valeur_vehicule=20_000)
print(contrat.description())       # Contrat Auto — Véhicule : 20000€
print(contrat.calculer_prime())     # 1000.0
```

###  Singleton

Le pattern Singleton garantit qu'une classe n'a **qu'une seule instance** dans toute l'application, et fournit un point d'accès global à cette instance. Il est utile pour des ressources partagées : configuration, pool de connexions, cache, registre central.

Sans Singleton, on risque de créer plusieurs instances incohérentes :
```python
config1 = Configuration()    # une instance
config2 = Configuration()    # une autre instance 
config1.set("timeout", 30)
print(config2.get("timeout"))  
```

Avec le pattern Singleton, toutes les références pointent vers le même objet :
```python
config1 = Configuration()
config2 = Configuration()
config1.set("timeout", 30)
print(config2.get("timeout"))  # Le résultat est 30 car c'est la même instance
```

Voici un exemple d'implémentation en Python avec `__new__` :
```python
class ConfigurationAssurance:
    """Singleton — une seule configuration pour toute l'application."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._parametres = {}
        return cls._instance

    def set(self, cle: str, valeur):
        self._parametres[cle] = valeur

    def get(self, cle: str, defaut=None):
        return self._parametres.get(cle, defaut)


config_a = ConfigurationAssurance()
config_a.set("franchise_defaut", 300)

config_b = ConfigurationAssurance()
print(config_b.get("franchise_defaut")) 
print(config_a is config_b)             
```

## Exercices

### 1) Design pattern Builder

#### a) Exercice 1 : Construction d'un contrat auto 

**Problème** :
On souhaite construire des objets `ContratAuto` qui ont plusieurs attributs optionnels (formule, franchise, options d'assistance). Le Builder est quasiment complet, mais il manque deux méthodes.

Consigne :
    Complétez les méthodes `avec_franchise()` et `avec_option()` du builder
    en suivant le même patron que les méthodes existantes.

Modifier le code dans le fichier module/04_design_pattern/builder/exercice1.py

```python
class ContratAuto:
    def __init__(self):
        self.assure_nom = ""
        self.assure_age = 0
        self.vehicule = ""
        self.valeur_vehicule = 0.0
        self.formule = "tiers"
        self.franchise = 300.0
        self.options = []

    def __str__(self):
        return (f"Contrat {self.formule} — {self.assure_nom} ({self.assure_age} ans) — "
                f"{self.vehicule} ({self.valeur_vehicule}€) — "
                f"Franchise : {self.franchise}€ — Options : {self.options}")


class ContratAutoBuilder:
    def __init__(self):
        self._contrat = ContratAuto()

    def avec_assure(self, nom: str, age: int):
        self._contrat.assure_nom = nom
        self._contrat.assure_age = age
        return self

    def avec_vehicule(self, nom: str, valeur: float):
        self._contrat.vehicule = nom
        self._contrat.valeur_vehicule = valeur
        return self

    def avec_formule(self, formule: str):
        self._contrat.formule = formule
        return self

    def avec_franchise(self, franchise: float):
        # TODO : affecter la franchise au contrat et retourner self
        pass

    def avec_option(self, option: str):
        # TODO : ajouter l'option à la liste et retourner self
        pass

    def build(self) -> ContratAuto:
        return self._contrat


# --- Vérification ---
if __name__ == "__main__":
    contrat = (
        ContratAutoBuilder()
        .avec_assure("Dupont", 35)
        .avec_vehicule("Renault Clio", 15_000)
        .avec_formule("tous_risques")
        .avec_franchise(500)
        .avec_option("assistance 0km")
        .avec_option("bris de glace")
        .build()
    )
    print(contrat)

```

#### b) Exercice 2 : Construction d'une offre habitation 

**Problème** :
On souhaite construire des objets `OffreHabitation` avec un Builder. La classe `OffreHabitation` est donnée, ainsi que la structure du Builder avec les signatures de méthodes. Il faut implémenter le corps de chaque méthode du Builder.

Consigne :
    Implémentez toutes les méthodes du `OffreHabitationBuilder`.
    Chaque méthode doit affecter les bons attributs de l'offre et retourner `self`.
    La méthode `build()` doit vérifier que l'adresse est renseignée (lever une `ValueError` sinon).

Modifier le code dans le fichier module/04_design_pattern/builder/exercice2.py

```python
class OffreHabitation:
    def __init__(self):
        self.proprietaire = ""
        self.adresse = ""
        self.surface_m2 = 0.0
        self.nb_pieces = 0
        self.type_bien = "appartement"  
        self.formule = "essentielle"    
        self.garanties = []
        self.franchise = 250.0

    def prime_annuelle(self) -> float:
        base = self.surface_m2 * 3.5
        coeff_formule = {"essentielle": 1.0, "confort": 1.3, "premium": 1.6}
        return base * coeff_formule.get(self.formule, 1.0)

    def __str__(self):
        return (f"Offre {self.formule} — {self.proprietaire} — "
                f"{self.type_bien} {self.surface_m2}m² à {self.adresse} — "
                f"Prime : {self.prime_annuelle():.2f}€/an — "
                f"Garanties : {self.garanties}")


class OffreHabitationBuilder:
    def __init__(self):
        self._offre = OffreHabitation()

    def avec_proprietaire(self, nom: str):
        # TODO
        pass

    def avec_adresse(self, adresse: str):
        # TODO
        pass

    def avec_surface(self, surface_m2: float, nb_pieces: int):
        # TODO
        pass

    def avec_type_bien(self, type_bien: str):
        # TODO
        pass

    def avec_formule(self, formule: str):
        # TODO
        pass

    def avec_garantie(self, garantie: str):
        # TODO
        pass

    def avec_franchise(self, franchise: float):
        # TODO
        pass

    def build(self) -> OffreHabitation:
        # TODO : vérifier que l'adresse est renseignée, puis retourner l'offre
        pass


# --- Vérification ---
if __name__ == "__main__":
    offre = (
        OffreHabitationBuilder()
        .avec_proprietaire("Martin")
        .avec_adresse("5 avenue des Champs, 75008 Paris")
        .avec_surface(85, 4)
        .avec_type_bien("appartement")
        .avec_formule("confort")
        .avec_garantie("dégât des eaux")
        .avec_garantie("vol")
        .avec_franchise(400)
        .build()
    )
    print(offre)
```

#### c) Exercice 3 : Construction d'un devis santé 

**Problème** :
On souhaite construire des objets `DevisSante` qui représentent un devis d'assurance santé avec : nom de l'assuré, âge, niveau de couverture (`base`, `confort`, `premium`), liste de bénéficiaires, plafond annuel et taux de remboursement.

Le calcul de la cotisation mensuelle est : `(age * 2.5) * coeff_niveau` où les coefficients sont : base=1.0, confort=1.4, premium=1.8.

Consigne :
    Créez la classe `DevisSante` et son `DevisSanteBuilder` entièrement.
    Le builder doit proposer les méthodes : `avec_assure(nom, age)`,
    `avec_niveau(niveau)`, `avec_beneficiaire(nom)`, `avec_plafond(montant)`,
    `avec_taux_remboursement(taux)`.
    La méthode `build()` doit vérifier que le nom et l'âge sont renseignés.

Modifier le code dans le fichier module/04_design_pattern/builder/exercice3.py

```python
# TODO : Créez la classe DevisSante avec les attributs :
#   - assure_nom (str), assure_age (int)
#   - niveau ("base", "confort", "premium")
#   - beneficiaires (list[str])
#   - plafond_annuel (float, défaut 5000)
#   - taux_remboursement (float, défaut 0.70)
#
# Méthode cotisation_mensuelle() -> float :
#   (age * 2.5) * coeff_niveau
#   coefficients : base=1.0, confort=1.4, premium=1.8
#
# Méthode __str__() pour afficher le devis


# TODO : Créez la classe DevisSanteBuilder
#   - avec_assure(nom, age)
#   - avec_niveau(niveau)
#   - avec_beneficiaire(nom)
#   - avec_plafond(montant)
#   - avec_taux_remboursement(taux)
#   - build() → DevisSante (vérifier nom et age renseignés)


# --- Vérification ---
if __name__ == "__main__":
    devis = (
        DevisSanteBuilder()
        .avec_assure("Dupont", 42)
        .avec_niveau("confort")
        .avec_beneficiaire("Marie Dupont")
        .avec_beneficiaire("Lucas Dupont")
        .avec_plafond(10_000)
        .avec_taux_remboursement(0.80)
        .build()
    )
    print(devis)
    # DevisSante confort — Dupont (42 ans) — Cotisation : 147.00€/mois —
    # Bénéficiaires : ['Marie Dupont', 'Lucas Dupont'] —
    # Plafond : 10000€ — Remboursement : 80%
```

### 2) Factory

#### a) Exercice 1 : Création de contrats par type 

**Problème** :
On souhaite créer des contrats d'assurance via une Factory. La Factory et deux types de contrats (auto, habitation) sont déjà implémentés. Il manque le type `ContratSante`.

Consigne :
    Complétez la classe `ContratSante` en suivant le patron des deux autres contrats,
    puis ajoutez-la dans la méthode `creer()` de la Factory.
    La prime santé se calcule ainsi : `age_assure * 12.0`.

Modifier le code dans le fichier module/04_design_pattern/factory/exercice1.py

```python
from abc import ABC, abstractmethod


class Contrat(ABC):
    @abstractmethod
    def calculer_prime(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class ContratAuto(Contrat):
    def __init__(self, valeur_vehicule: float):
        self.valeur_vehicule = valeur_vehicule

    def calculer_prime(self) -> float:
        return self.valeur_vehicule * 0.05

    def description(self) -> str:
        return f"Contrat Auto — Véhicule : {self.valeur_vehicule}€"


class ContratHabitation(Contrat):
    def __init__(self, surface_m2: float):
        self.surface_m2 = surface_m2

    def calculer_prime(self) -> float:
        return self.surface_m2 * 3.5

    def description(self) -> str:
        return f"Contrat Habitation — {self.surface_m2} m²"


# TODO : Créez la classe ContratSante(Contrat)
#   - __init__ prend age_assure (int)
#   - calculer_prime() retourne age_assure * 12.0
#   - description() retourne "Contrat Santé — <age> ans"


class ContratFactory:
    @staticmethod
    def creer(type_contrat: str, **kwargs) -> Contrat:
        if type_contrat == "auto":
            return ContratAuto(kwargs["valeur_vehicule"])
        elif type_contrat == "habitation":
            return ContratHabitation(kwargs["surface_m2"])
        # TODO : ajouter le cas "sante"
        else:
            raise ValueError(f"Type de contrat inconnu : {type_contrat}")


# --- Vérification ---
if __name__ == "__main__":
    for type_c, params in [
        ("auto", {"valeur_vehicule": 20_000}),
        ("habitation", {"surface_m2": 75}),
        ("sante", {"age_assure": 45}),
    ]:
        contrat = ContratFactory.creer(type_c, **params)
        print(f"{contrat.description()} — Prime : {contrat.calculer_prime():.2f}€")
    # Contrat Auto — Véhicule : 20000€ — Prime : 1000.00€
    # Contrat Habitation — 75 m² — Prime : 262.50€
    # Contrat Santé — 45 ans — Prime : 540.00€
```

#### b) Exercice 2 : Création de notifications par canal 

**Problème** :
Le service de notification doit envoyer des messages aux assurés via différents canaux (email, SMS, courrier). On souhaite utiliser une Factory pour créer le bon canal de notification. La classe abstraite `Notification` et la Factory sont données. Il faut implémenter les trois classes concrètes.

Consigne :
    Implémentez les classes `NotificationEmail`, `NotificationSMS` et
    `NotificationCourrier`. Chacune reçoit un destinataire dans son constructeur
    et implémente `envoyer(message)` qui retourne une chaîne formatée.

Modifier le code dans le fichier module/04_design_pattern/factory/exercice2.py

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def envoyer(self, message: str) -> str:
        pass


# TODO : Implémentez les trois classes :
#
# class NotificationEmail(Notification):
#     __init__(self, destinataire: str)
#     envoyer(message) → "EMAIL à <destinataire> : <message>"
#
# class NotificationSMS(Notification):
#     __init__(self, telephone: str)
#     envoyer(message) → "SMS à <telephone> : <message>"
#
# class NotificationCourrier(Notification):
#     __init__(self, adresse: str)
#     envoyer(message) → "COURRIER à <adresse> : <message>"


class NotificationFactory:
    @staticmethod
    def creer(canal: str, **kwargs) -> Notification:
        if canal == "email":
            return NotificationEmail(kwargs["destinataire"])
        elif canal == "sms":
            return NotificationSMS(kwargs["telephone"])
        elif canal == "courrier":
            return NotificationCourrier(kwargs["adresse"])
        else:
            raise ValueError(f"Canal inconnu : {canal}")


# --- Vérification ---
if __name__ == "__main__":
    canaux = [
        ("email", {"destinataire": "marie@mail.fr"}),
        ("sms", {"telephone": "06 12 34 56 78"}),
        ("courrier", {"adresse": "12 rue de Paris, 75001"}),
    ]
    for canal, params in canaux:
        notif = NotificationFactory.creer(canal, **params)
        print(notif.envoyer("Votre sinistre a été traité."))
    # EMAIL à marie@mail.fr : Votre sinistre a été traité.
    # SMS à 06 12 34 56 78 : Votre sinistre a été traité.
    # COURRIER à 12 rue de Paris, 75001 : Votre sinistre a été traité.
```

#### c) Exercice 3 : Création de calculateurs de remise 

**Problème** :
Le service commercial applique des remises selon le profil du client : fidélité (ancienneté >= 5 ans → 10%), multi-contrats (>= 3 contrats → 8%), ou parrainage (a parrainé → 5%). On souhaite créer les calculateurs de remise via une Factory.

Consigne :
    Créez entièrement :
    1. Une classe abstraite `Remise` avec une méthode `calculer(client) -> float`
       qui retourne le taux de remise (entre 0.0 et 1.0)
       et une méthode `nom() -> str` qui retourne le nom de la remise.
    2. Trois classes concrètes : `RemiseFidelite`, `RemiseMultiContrats`, `RemiseParrainage`.
    3. Une `RemiseFactory` avec une méthode `creer(type_remise) -> Remise`.

Modifier le code dans le fichier module/04_design_pattern/factory/exercice3.py

```python
# TODO : Créez la classe abstraite Remise (ABC)
#   - calculer(client: dict) -> float   (taux de remise)
#   - nom() -> str                       (nom de la remise)

# TODO : Créez RemiseFidelite(Remise)
#   - calculer : 0.10 si client["anciennete_ans"] >= 5, sinon 0.0
#   - nom : "Fidélité"

# TODO : Créez RemiseMultiContrats(Remise)
#   - calculer : 0.08 si len(client["contrats"]) >= 3, sinon 0.0
#   - nom : "Multi-contrats"

# TODO : Créez RemiseParrainage(Remise)
#   - calculer : 0.05 si client["a_parraine"] est True, sinon 0.0
#   - nom : "Parrainage"

# TODO : Créez RemiseFactory
#   - creer(type_remise: str) -> Remise


# --- Vérification ---
if __name__ == "__main__":
    client = {
        "nom": "Dupont",
        "anciennete_ans": 7,
        "contrats": ["auto", "habitation", "sante"],
        "a_parraine": True,
    }

    for type_r in ["fidelite", "multi_contrats", "parrainage"]:
        remise = RemiseFactory.creer(type_r)
        taux = remise.calculer(client)
        print(f"Remise {remise.nom()} : {taux * 100:.0f}%")
    # Remise Fidélité : 10%
    # Remise Multi-contrats : 8%
    # Remise Parrainage : 5%
```

### 3) Singleton

#### a) Exercice 1 : Configuration globale 

**Problème** :
L'application d'assurance a besoin d'une configuration globale unique (franchise par défaut, taux de TVA, etc.). Le Singleton est quasiment complet, mais la méthode `__new__` est incomplète.

Consigne :
    Complétez la méthode `__new__` pour que la classe ne crée qu'une seule instance.
    Si l'instance existe déjà, elle doit être retournée directement.

Modifier le code dans le fichier module/04_design_pattern/singleton/exercice1.py

```python
class ConfigurationAssurance:
    """Singleton pour la configuration globale de l'application."""
    _instance = None

    def __new__(cls):
        # TODO : si _instance est None, créer l'instance avec super().__new__(cls)
        #        et initialiser _parametres à un dict vide
        # TODO : retourner _instance
        pass

    def set(self, cle: str, valeur):
        self._parametres[cle] = valeur

    def get(self, cle: str, defaut=None):
        return self._parametres.get(cle, defaut)

    def tous(self) -> dict:
        return dict(self._parametres)


# --- Vérification ---
if __name__ == "__main__":
    config1 = ConfigurationAssurance()
    config1.set("franchise_defaut", 300)
    config1.set("tva", 0.20)

    config2 = ConfigurationAssurance()
    print(config2.get("franchise_defaut"))  # 300
    print(config2.get("tva"))               # 0.2
    print(config1 is config2)               # True
```

#### b) Exercice 2 : Registre central des contrats 

**Problème** :
On souhaite un registre central qui stocke tous les contrats de l'application. Ce registre doit être un Singleton pour garantir une source de vérité unique. La structure de la classe est donnée, il faut implémenter le Singleton et les méthodes.

Consigne :
    Implémentez le pattern Singleton via `__new__` et complétez les méthodes
    `enregistrer()`, `trouver()`, `tous()` et `nombre()`.

Modifier le code dans le fichier module/04_design_pattern/singleton/exercice2.py

```python
class RegistreContrats:
    """Singleton — registre central de tous les contrats."""
    _instance = None

    def __new__(cls):
        # TODO : implémenter le Singleton
        pass

    def enregistrer(self, numero: str, contrat: dict) -> None:
        """Enregistre un contrat dans le registre."""
        # TODO
        pass

    def trouver(self, numero: str) -> dict | None:
        """Trouve un contrat par son numéro."""
        # TODO
        pass

    def tous(self) -> dict[str, dict]:
        """Retourne tous les contrats."""
        # TODO
        pass

    def nombre(self) -> int:
        """Retourne le nombre de contrats enregistrés."""
        # TODO
        pass


# --- Vérification ---
if __name__ == "__main__":
    registre1 = RegistreContrats()
    registre1.enregistrer("A-001", {"type": "auto", "prime": 1000})
    registre1.enregistrer("H-001", {"type": "habitation", "prime": 262.50})

    registre2 = RegistreContrats()
    registre2.enregistrer("S-001", {"type": "sante", "prime": 540})

    print(registre1 is registre2)           # True
    print(registre2.nombre())               # 3
    print(registre2.trouver("A-001"))       # {'type': 'auto', 'prime': 1000}
    print(registre1.trouver("S-001"))       # {'type': 'sante', 'prime': 540}
```

#### c) Exercice 3 : Gestionnaire de connexion unique 

**Problème** :
L'application doit se connecter à un service externe de tarification via une API. Pour éviter de créer plusieurs connexions coûteuses, on souhaite un Singleton qui gère cette connexion unique. Le Singleton doit stocker l'URL de l'API, un jeton d'authentification, et un compteur de requêtes effectuées.

Consigne :
    Créez entièrement la classe `ConnexionTarification` en tant que Singleton.
    Elle doit avoir :
    - les attributs `url`, `jeton`, `requetes_effectuees` (compteur, initialisé à 0)
    - une méthode `configurer(url, jeton)` pour paramétrer la connexion
    - une méthode `appeler(endpoint, params) -> str` qui incrémente le compteur
      et retourne une chaîne simulant l'appel : "GET <url>/<endpoint> — params: <params>"
    - une méthode `stats() -> str` qui retourne "<requetes> requête(s) effectuée(s)"

Modifier le code dans le fichier module/04_design_pattern/singleton/exercice3.py

```python
# TODO : Créez la classe ConnexionTarification (Singleton)
#   Attributs : url (str), jeton (str), requetes_effectuees (int)
#   Méthodes :
#     - configurer(url: str, jeton: str)
#     - appeler(endpoint: str, params: dict) -> str
#     - stats() -> str


# --- Vérification ---
if __name__ == "__main__":
    conn1 = ConnexionTarification()
    conn1.configurer("https://api.tarification.fr", "token-xyz-123")

    print(conn1.appeler("prime/auto", {"valeur": 20000}))
    # GET https://api.tarification.fr/prime/auto — params: {'valeur': 20000}

    print(conn1.appeler("prime/habitation", {"surface": 75}))
    # GET https://api.tarification.fr/prime/habitation — params: {'surface': 75}

    conn2 = ConnexionTarification()
    print(conn1 is conn2)     # True
    print(conn2.stats())      # 2 requête(s) effectuée(s)
```

## Correction
Tout les exercices ont la correction dans le dossier correction.
Afin de vous améliorer et de comprendre, veuillez la regarder seulement après avoir effectué les exercices.