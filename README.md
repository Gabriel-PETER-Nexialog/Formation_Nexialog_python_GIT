# Module 02 - Principe SOLID

Objectif : apprendre les principes SOLID afin d'améliorer la qualité de code .

---

## Objectifs

- Comprendre le principe SOLID `git status`
- Savoir appliquer les principes sur un cas concret `git status`
- Détecter le non respect des principes dans un code legacy

---

## Prérequis

- Avoir terminé le module 00 et module 01
- Avoir l'environnement conda de fonctionnel et git d'installé 

---

## Théorie 

Les principes SOLID est un ensemble de principe de développement logiciel 

- **S** : Single Responsibility 

Une classe = une seule raison de changer. Chaque classe ne doit avoir qu'une responsabilité unique et bien définie.

```python
# Classe qui est responsable de trois actions
class Contrat:
    def calculer_prime(self): ...
    def envoyer_email_client(self): ...
    def sauvegarder_en_base(self): ...

# Découplage des actions en trois classe 
class Contrat:
    def calculer_prime(self): ...

class NotificationService:
    def envoyer_email_client(self, contrat): ...

class ContratRepository:
    def sauvegarder(self, contrat):
```
- **O** : Open/Closed 

Ouvert à l'extension, fermé à la modification. 
On ajoute de nouveaux comportements sans toucher au code existant.

```python 

from abc import ABC, abstractmethod

# Base fermée à la modification
class CalculateurPrime(ABC):
    @abstractmethod
    def calculer(self, contrat) -> float:
        pass

# Ouvert à l'extension : on ajoute un type sans modifier l'existant
class PrimeAuto(CalculateurPrime):
    def calculer(self, contrat) -> float:
        return contrat.valeur_vehicule * 0.05

class PrimeSante(CalculateurPrime):
    def calculer(self, contrat) -> float:
        return contrat.age_assure * 12.0

class PrimeMaison(CalculateurPrime):  # Nouveau type, aucune modif ailleurs
    def calculer(self, contrat) -> float:
        return contrat.surface_m2 * 3.5
```

- **L** : Liskov Substitution

Un sous-type doit pouvoir remplacer son type parent sans altérer le comportement du programme.


```python 
# Classe parent Sinistre
class Sinistre: 
    def declarer(self, montant: float) -> str:
        return f"Sinistre déclaré pour {montant}€"

# Classe enfants qui hérite de Sinistre
class SinistreAuto(Sinistre):
    def declarer(self, montant: float) -> str:
        return f"Sinistre auto déclaré pour {montant}€, expertise planifiée"

class SinistreHabitation(Sinistre):
    def declarer(self, montant: float) -> str:
        return f"Sinistre habitation pour {montant}€, expert mandaté"
    
def traiter_sinistre(sinistre: Sinistre, montant: float):
    """
    Chaque classe enfants peuvent remplacer le type parent sans alterer 
    la fonction traiter_sinistre qui utilise les classes enfants
    """
    print(sinistre.declarer(montant)) 

traiter_sinistre(SinistreAuto(), 3000)
traiter_sinistre(SinistreHabitation(), 15000)

```
- **I** : Interface Segregation 

Aucun client ne doit dépendre de méthodes qu'il n'utilise pas. Mieux vaut plusieurs interfaces spécialisées qu'une seule interface générale.

```python 
from abc import ABC, abstractmethod

# Example d'interface trop généraliste
class IGestionAssurance(ABC):
    def calculer_prime(self): ...
    def rembourser_sinistre(self): ...
    def gerer_epargne(self): ...  
# -----------------
# Application du principe Interface Segregation 

class ICalculPrime(ABC):
    @abstractmethod
    def calculer_prime(self) -> float: pass

class IRemboursement(ABC):
    @abstractmethod
    def rembourser(self, montant: float): pass

class IGestionEpargne(ABC):
    @abstractmethod
    def versement_epargne(self, montant: float): pass

# Un contrat  implémente seulement les interfaces qu'il a besoins

class ContratAuto(ICalculPrime, IRemboursement):
    def calculer_prime(self) -> float:
        return 450.0

    def rembourser(self, montant: float):
        print(f"Remboursement auto : {montant}€")


class ContratVie(ICalculPrime, IGestionEpargne):
    def calculer_prime(self) -> float:
        return 200.0

    def versement_epargne(self, montant: float):
        print(f"Versement épargne vie : {montant}€")

```
- **D** : Dependency Inversion 

Les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Les deux doivent dépendre d'abstractions.

```python 
from abc import ABC, abstractmethod

# Abstraction (interface)
class IStockageContrat(ABC):
    @abstractmethod
    def sauvegarder(self, contrat): pass

    @abstractmethod
    def charger(self, id: str): pass

# Implémentations concrètes de bas niveau
class StockagePostgres(IStockageContrat):
    def sauvegarder(self, contrat):
        print(f"Sauvegarde PostgreSQL : {contrat}")

    def charger(self, id: str):
        print(f"Chargement depuis PostgreSQL : {id}")

class StockageS3(IStockageContrat):
    def sauvegarder(self, contrat):
        print(f"Archivage S3 : {contrat}")

    def charger(self, id: str):
        print(f"Chargement depuis S3 : {id}")

# Module de haut niveau dépend de l'abstraction, pas de l'implémentation
class GestionnaireContrat:
    def __init__(self, stockage: IStockageContrat):
        self.stockage = stockage  # Injection de dépendance

    def creer_contrat(self, contrat):
        self.stockage.sauvegarder(contrat)

# Flexibilité totale au moment de l'injection
gestionnaire = GestionnaireContrat(StockagePostgres())

```
## Exercices

### 1) Principe Single Responsability

#### a) Exercice 1 : La classe GestionContratAuto
Cette classe gère à la fois le calcul de la prime, 
la persistance en base de données et l'envoi de notifications.
Identifiez les violations du Single Responsability et refactorisez.

Modifier la fonction dans le dossier module/02_solid/exercice1.py

```python
class GestionContratAuto:
    def __init__(self, assure, vehicule, age_permis):
        self.assure   = assure
        self.vehicule = vehicule
        self.age_permis = age_permis   
class GestionContratAuto:
    def __init__(self, assure, vehicule, age_permis):
        self.assure = assure
        self.vehicule = vehicule
        self.age_permis = age_permis

    def calculer_prime(self) -> float:
        base = self.vehicule.valeur * 0.05
        if self.age_permis < 3:
            base *= 1.5
        return base

    def sauvegarder_en_base(self):
        # connexion directe à la BDD
        db.execute("INSERT INTO contrats ...", self.assure, self.vehicule)

    def envoyer_email_confirmation(self):
        EmailManager.send_confirm(to=self.assure.email,
                                  subject="Votre contrat auto",
                                  body=f"Prime : {self.calculer_prime()}€")

    def generer_pdf(self):
        PdfManager.create(titre="Contrat Auto",
                   assure=self.assure.nom,
                   prime=self.calculer_prime())
```
#### b) Exercice 2 : La classe GestionSinistre
Cette classe mélange la validation d'un sinistre, le calcul du remboursement, la mise à jour du dossier et la génération d'un rapport de fraude.

Identifiez les violations du Single Responsability et refactorisez.

Modifier la fonction dans le dossier module/02_solid/exercice2.py

```python 

class GestionSinistre:
    def __init__(self, sinistre):
        self.sinistre = sinistre

    def valider_recevabilite(self) -> bool:
        return (self.sinistre.date_declaration <=
                self.sinistre.date_evenement + timedelta(days=5))

    def calculer_remboursement(self) -> float:
        franchise = 300
        return max(0, self.sinistre.montant - franchise)

    def mettre_a_jour_statut(self, statut: str):
        db.execute("UPDATE sinistres SET statut=?", statut, self.sinistre.id)

    def detecter_fraude(self) -> bool:
        # heuristique : > 3 sinistres en 12 mois
        nb = db.query("SELECT COUNT(*) FROM sinistres ...")
        return nb > 3
```

#### c) Exercice 3 : La classe GestionClient
Cette classe cumule la gestion du profil client, le scoring de risque, la génération de rapports et l'authentification. C'est un "God Object" classique.

Identifiez les violations du Single Responsability et refactorisez.

Modifier la fonction dans le dossier module/02_solid/exercice3.py

```python 
class GestionClient:
    def __init__(self, client):
        self.client = client

    def mettre_a_jour_adresse(self, nouvelle_adresse: str):
        self.client.adresse = nouvelle_adresse
        db.execute("UPDATE clients SET adresse=?", nouvelle_adresse)

    def calculer_score_risque(self) -> int:
        score = 100
        score -= self.client.nb_sinistres * 15
        score -= max(0, (25 - self.client.age)) * 2
        return max(0, score)

    def authentifier(self, mot_de_passe: str) -> bool:
        hash_mdp = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        return hash_mdp == self.client.hash_mdp

    def generer_releve_annuel(self) -> str:
        contrats = db.query("SELECT * FROM contrats WHERE client_id=?")
        return f"Relevé {self.client.nom} — {len(contrats)} contrat(s)"
```

### 2) Open/Closed

#### a) Exercice 1 : Le calculateur de prime avec if/elif
À chaque nouveau type de contrat (habitation, voyage, animaux…), un développeur doit ouvrir cette classe et ajouter un elif. La classe n'est pas fermée à la modification.

Modifier la fonction dans modules/02_solid/open_closed/exercice1.py
```python 
class CalculateurPrime:

    def calculer(self, contrat) -> float:
        if contrat.type == "auto":
            return contrat.valeur_vehicule * 0.05

        elif contrat.type == "habitation":
            return contrat.surface_m2 * 3.5

        elif contrat.type == "sante":
            return contrat.age_assure * 12.0

        # ← à chaque nouveau contrat, on rouvre cette classe
        else:
            raise ValueError(f"Type inconnu : {contrat.type}")

```
#### b) Exercice 2 : Le gestionnaire de remise commerciale
Le service commercial veut régulièrement ajouter de nouvelles règles de remise (fidélité, multi-contrats, parrainage…). En l'état, chaque nouvelle règle nécessite de modifier la classe centrale.

Modifier la fonction dans modules/02_solid/open_closed/exercice2.py
```python 

class GestionnaireRemise:

    def calculer_remise(self, client) -> float:
        remise = 0.0

        if client.anciennete_ans >= 5:
            remise += 0.05 

        if len(client.contrats) >= 3:
            remise += 0.10  

        if client.a_parraine:
            remise += 0.03  

        return min(remise, 0.20) 

```
#### c) Exercice 3 : Le générateur de rapport de sinistre
L'entreprise veut pouvoir exporter les rapports en PDF, Excel et bientôt en JSON pour son API. Actuellement, ajouter un format impose de modifier la classe de génération.

Modifier la fonction dans modules/02_solid/open_closed/exercice3.py
```python 

class GenerateurRapportSinistre:

    def __init__(self, sinistre):
        self.sinistre = sinistre

    def exporter(self, format: str):
        if format == "pdf":
            return pdf_lib.render(
                titre="Rapport sinistre",
                contenu=self.sinistre.description
            )
        elif format == "excel":
            return excel_lib.write([
                ["ID", self.sinistre.id],
                ["Montant", self.sinistre.montant],
            ])
        # ← ajouter "json" impose de modifier cette méthode
        else:
            raise ValueError(f"Format non supporté : {format}")

```
### 3) Liskov Substitution

#### a) Exercice 1 : Le contrat non résiliable qui lève une exception

La classe ContratVieEntier hérite de Contrat mais lève une exception sur resilier(). Tout code qui manipule un Contrat se retrouve cassé si on lui passe un ContratVieEntier.

Modifier la fonction dans modules/02_solid/liskov_substitution/exercice1.py
```python 

class Contrat:
    def __init__(self, numero: str, prime: float):
        self.numero = numero
        self.prime  = prime

    def resilier(self):
        print(f"Contrat {self.numero} résilié.")

    def calculer_prime(self) -> float:
        return self.prime


class ContratVieEntier(Contrat):
    """Un contrat vie entier ne peut jamais être résilié."""

    def resilier(self):
        raise NotImplementedError("Ce contrat ne peut pas être résilié.")


# Ce code explose si on lui passe un ContratVieEntier
def resilier_tous(contrats: list[Contrat]):
    for c in contrats:
        c.resilier() # Erreur en cas d'éxécution 

```

#### b) Exercice 2 : Le sinistre refusé qui retourne toujours zéro

SinistreRefuse hérite de Sinistre mais son calculer_remboursement() retourne toujours 0 en ignorant silencieusement les paramètres. Le code appelant ne peut pas se fier au contrat de la méthode parente.

Modifier la fonction dans modules/02_solid/liskov_substitution/exercice2.py
```python 

class Sinistre:
    def __init__(self, montant: float, franchise: float):
        self.montant = montant
        self.franchise = franchise

    def calculer_remboursement(self) -> float:
        return max(0.0, self.montant - self.franchise)


class SinistreRefuse(Sinistre):
    """Sinistre dont la prise en charge a été refusée."""

    def calculer_remboursement(self) -> float:
        # Retourne 0 sans signaler que le sinistre est refusé
        # Affaiblit la postcondition : le calcul promis ne se fait pas
        return 0.0


# Ce total est silencieusement faux si la liste contient des SinistreRefuse
def total_remboursements(sinistres: list[Sinistre]) -> float:
    return sum(s.calculer_remboursement() for s in sinistres)
```

#### c) Exercice 3 : L'assurée mineure qui renforce les préconditions
AssureMineur hérite de Assure mais sa méthode souscrire_contrat() ajoute une précondition supplémentaire (présence d'un tuteur). Le code qui travaille avec des Assure ne connaît pas cette contrainte et crashe.

Modifier la fonction dans modules/02_solid/liskov_substitution/exercice3.py

```python 
class Assure:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def souscrire_contrat(self, contrat):
        # Précondition parent : aucune, tout assuré peut souscrire
        contrat.activer(self)
        print(f"{self.nom} a souscrit le contrat.")


class AssureMineur(Assure):

    def souscrire_contrat(self, contrat, tuteur=None):
        # Précondition renforcée : exige un tuteur que le parent ne demandait pas
        if tuteur is None:
            raise ValueError("Un tuteur légal est obligatoire pour un mineur.")
        contrat.activer(self)
        print(f"{self.nom} (tuteur : {tuteur}) a souscrit le contrat.")


# Erreur si assure est un AssureMineur sans tuteur
def souscrire_batch(assures: list[Assure], contrat):
    for a in assures:
        a.souscrire_contrat(contrat)
```

### 4) Interface Segregation

#### a) Exercice 1 : L'interface contrat universelle

L'interface IContrat regroupe toutes les opérations possibles sur un contrat. Un ContratVoyage est forcé d'implémenter gerer_epargne() et declarer_accident() qui n'ont aucun sens pour lui.

Modifier la fonction dans modules/02_solid/integration_segregation/exercice1.py afin de respecter le principe de la segregation des interfaces

```python 
from abc import ABC, abstractmethod

class IContrat(ABC):
    # Interface global qui mélange toutes les responsabilités
    @abstractmethod
    def calculer_prime(self) -> float: pass
    @abstractmethod
    def resilier(self): pass
    @abstractmethod
    def gerer_epargne(self, montant: float): pass
    @abstractmethod
    def declarer_accident(self): pass
    @abstractmethod
    def rembourser_hospitalisation(self): pass


class ContratVoyage(IContrat):
    def calculer_prime(self) -> float:
        return 120.0

    def resilier(self):
        print("Contrat voyage résilié.")

    def gerer_epargne(self, montant: float):
        # Forcé d'implémenter une méthode absurde
        raise NotImplementedError("Un contrat voyage n'a pas d'épargne.")

    def declarer_accident(self):
        # Idem
        raise NotImplementedError("Pas d'accident sur un contrat voyage.")

    def rembourser_hospitalisation(self):
        print("Remboursement frais médicaux voyage.")

```

#### b) Exercice 2 : Le service de notification multi-canal 

L'interface INotification impose d'implémenter email, SMS et courrier postal. Un service qui ne fait qu'envoyer des SMS est contraint d'implémenter les deux autres canaux avec des méthodes vides.

Modifier la fonction dans modules/02_solid/integration_segregation/exercice2.py afin de respecter le principe de la segregation des interfaces
```python 

from abc import ABC, abstractmethod

class INotification(ABC):
    # Tous les canaux regroupés dans une seule interface
    @abstractmethod
    def envoyer_email(self, destinataire: str, message: str): pass
    @abstractmethod
    def envoyer_sms(self, telephone: str, message: str): pass
    @abstractmethod
    def envoyer_courrier(self, adresse: str, contenu: str): pass


class ServiceSMSAssurance(INotification):
    def envoyer_sms(self, telephone: str, message: str):
        print(f"SMS → {telephone} : {message}")

    def envoyer_email(self, destinataire: str, message: str):
        # Méthode vide imposée par l'interface
        pass

    def envoyer_courrier(self, adresse: str, contenu: str):
        # Idem — pollution de l'implémentation
        pass

```

#### c) Exercice 3 : Le gestionnaire de sinistre aux méthodes forcées

L'interface IGestionnaireSinistre mélange instruction du dossier, expertise terrain et recouvrement juridique. Un gestionnaire back-office qui instruit des dossiers n'a rien à faire avec diligenter_expert() ni engager_recours().

Modifier la fonction dans modules/02_solid/integration_segregation/exercice3.py afin de respecter le principe de la segregation des interfaces

```python 
from abc import ABC, abstractmethod

class IGestionnaireSinistre(ABC):
    # Trois métiers distincts dans une seule interface
    @abstractmethod
    def instruire_dossier(self, sinistre_id: int): pass
    @abstractmethod
    def valider_remboursement(self, montant: float): pass
    @abstractmethod
    def diligenter_expert(self, adresse: str): pass
    @abstractmethod
    def rediger_rapport_terrain(self) -> str: pass
    @abstractmethod
    def engager_recours(self, dossier_id: int): pass
    @abstractmethod
    def suivre_procedure_judiciaire(self): pass

class GestionnaireBackOffice(IGestionnaireSinistre):
    def instruire_dossier(self, sinistre_id: int):
        print(f"Dossier {sinistre_id} instruit.")

    def valider_remboursement(self, montant: float):
        print(f"Remboursement de {montant}€ validé.")

    def diligenter_expert(self, adresse: str):
        raise NotImplementedError  

    def rediger_rapport_terrain(self) -> str:
        raise NotImplementedError 

    def engager_recours(self, dossier_id: int):
        raise NotImplementedError  

    def suivre_procedure_judiciaire(self):
        raise NotImplementedError
```

### 5) Dependency Inversion

#### a) Exercice 1 : Le service de tarification couplé à une BDD concrète
ServiceTarification instancie directement PostgresContratRepository dans son constructeur. Le module de haut niveau dépend d'un détail technique bas niveau — impossible de tester sans base de données réelle, impossible de changer de base sans modifier la classe métier.

Modifier la fonction dans modules/02_solid/dependency_inversion/exercice1.py afin de respectey le principe d'inversion des dépendances

```python 

class PostgresContratRepository:
    def trouver_par_id(self, contrat_id: int):
        # connexion directe à PostgreSQL
        return db.query(f"SELECT * FROM contrats WHERE id={contrat_id}")


class ServiceTarification:
    def __init__(self):
        # Dépend d'un détail concret instancié ici même
        self.repo = PostgresContratRepository()

    def calculer_prime(self, contrat_id: int) -> float:
        contrat = self.repo.trouver_par_id(contrat_id)
        return contrat.valeur * 0.05


# En test, on ne peut pas remplacer la vraie BDD :
# service = ServiceTarification()  ← toujours PostgreSQL !

```
#### b) Exercice 2 : Le gestionnaire de sinistre couplé au service SMTP

GestionnaireSinistre instancie directement ServiceSMTP pour envoyer les notifications. La logique métier de sinistralité est couplée à un détail d'infrastructure — si l'entreprise passe à SendGrid ou veut envoyer des SMS, il faut modifier la classe métier.

Modifier la fonction dans modules/02_solid/dependency_inversion/exercice2.py afin de respectey le principe d'inversion des dépendances
```python 
class ServiceSMTP:
    def envoyer(self, destinataire: str, sujet: str, corps: str):
        # envoi via serveur SMTP interne
        smtp_client.sendmail(destinataire, sujet, corps)


class GestionnaireSinistre:
    def __init__(self):
        # Instancie directement le détail technique
        self.notifier = ServiceSMTP()

    def traiter_sinistre(self, sinistre):
        remboursement = max(0, sinistre.montant - 300)
        sinistre.statut = "traité"
        # Couplé à SMTP — aucune flexibilité
        self.notifier.envoyer(
            sinistre.assure.email,
            "Sinistre traité",
            f"Remboursement : {remboursement}€"
        )

```
#### c) Exercice 3 : Le moteur de scoring couplé à un algorithme concret
MoteurSouscription instancie directement ScoringRegleMetier. Si l'équipe actuariale veut expérimenter un modèle ML ou un scoring externe, il faut modifier le moteur de souscription lui-même — qui est le composant le plus critique du système.

Modifier la fonction dans modules/02_solid/dependency_inversion/exercice3.py afin de respectey le principe d'inversion des dépendances

```python 
class ScoringRegleMetier:
    def scorer(self, assure) -> int:
        score = 100
        score -= assure.nb_sinistres * 15
        score -= max(0, 25 - assure.age) * 2
        return max(0, score)


class MoteurSouscription:
    def __init__(self):
        # Couplé à l'algorithme de scoring concret
        self.scoring = ScoringRegleMetier()

    def accepter_souscription(self, assure) -> bool:
        score = self.scoring.scorer(assure)
        return score >= 60

    def calculer_surprime(self, assure) -> float:
        score = self.scoring.scorer(assure)
        if score < 80:
            return (80 - score) * 5.0
        return 0.0
```
## Correction
Tout les exercices ont la correction dans le dossier correction.
Afin de vous améliorer et de comprendre, veuillez la regarder seulement après avoir effectué les exercices.
