# Module 02 - Principe SOLID

Objectif : apprendre les principes SOLID afin d'améliorer la qualité de code .

---

## Objectifs

- Comprendre les principes DRY et YAGNI `
- Savoir appliquer les principes sur des cas concrets
- Détecter le non respect des principes dans un code legacy

---

## Prérequis

- Avoir terminé les modules précédents

---

## Théorie 

Les principes deux principes DRY et YAGNI sont deux autre principes qui compémentent les principes SOLID vue dans le module précédents.


- **DRY** : Don't repeat yourself 

Le principe DRY est un principe qui consiste à éviter les redondances dans le codes. 
Si nous avons plusieurs fonction qui effectue la même tâches mais dans un contexte différents,
le principe DRY nous demande donc de créé une fonction unique qui peut fonctionner dans tout les contextes.

Voici un exemple  : 

```python
def prime_auto(age, valeur_vehicule):
    if age < 25:
        risque = 1.5
    elif age > 65:
        risque = 1.3
    else:
        risque = 1.0
    return valeur_vehicule * 0.05 * risque

def prime_habitation(age, valeur_bien):
    if age < 25:
        risque = 1.5
    elif age > 65:
        risque = 1.3
    else:
        risque = 1.0
    return valeur_bien * 0.03 * risque

def prime_sante(age, couverture):
    if age < 25:
        risque = 1.5
    elif age > 65:
        risque = 1.3
    else:
        risque = 1.0
    return couverture * 0.08 * risque
```
Application du principe 
``` python
TAUX_PAR_TYPE = {
    "auto":       0.05,
    "habitation": 0.03,
    "sante":      0.08,
}

def coefficient_risque(age: int) -> float:
    """Retourne le coefficient de risque selon l'âge de l'assuré."""
    if age < 25:
        return 1.5
    elif age > 65:
        return 1.3
    return 1.0

def calculer_prime(type_contrat: str, age: int, valeur: float) -> float:
    """Calcule la prime d'assurance pour n'importe quel type de contrat."""
    taux = TAUX_PAR_TYPE[type_contrat]
    return valeur * taux * coefficient_risque(age)

print(calculer_prime("auto",       30, 20_000))   # 1000.0
print(calculer_prime("habitation", 20, 150_000))  # 3375.0
print(calculer_prime("sante",      70, 5_000))    # 520.0

 ```
- **YAGNI** : You Ain't Gonna Need It

Le principe YAGNI consiste à ne pas implémenter de fonctionnalités tant qu'elles ne sont pas réellement nécessaires.
Ajouter du code « au cas où » ou « pour plus tard » introduit de la complexité inutile : plus de code à maintenir,
plus de tests à écrire, et souvent des abstractions qui ne correspondent pas au besoin réel quand celui-ci arrive finalement.

Voici un exemple :

```python
# ❌ Violation YAGNI — on anticipe des besoins qui n'existent pas
class ServiceNotification:
    def envoyer_email(self, destinataire, message):
        smtp.send(destinataire, message)

    def envoyer_sms(self, telephone, message):
        # "On en aura sûrement besoin un jour"
        raise NotImplementedError

    def envoyer_push(self, token, message):
        # "Le mobile arrive au Q3"
        raise NotImplementedError

    def envoyer_fax(self, numero, message):
        # "Au cas où pour les anciens clients"
        raise NotImplementedError
```
Application du principe :
```python
# ✅ On n'implémente que ce qui est utilisé aujourd'hui
class ServiceNotification:
    def envoyer_email(self, destinataire, message):
        smtp.send(destinataire, message)
```

## Exercices

### 1) DRY 

#### a) Exercice 1 : Validation de dossiers d'assurance

**Problème**:
Le service de souscription valide trois types de dossiers (auto, habitation, santé) avant d'accepter un contrat. Chaque fonction reproduit la même
logique de vérification : pièce d'identité valide, majorité de l'assuré,
et absence d'impayés. Seule la vérification spécifique au type de contrat diffère.

Cette duplication pose problème :
<ul>
<li>Si l'âge minimum légal change (ex. 16 ans pour l'émancipation), il faut
      modifier trois fonctions.</li>

<li>Si on ajoute une vérification commune (ex. vérifier le RIB), il faut
      penser à l ajouter dans chaque fonction.</li>

<li> Le risque d'incohérence augmente avec le nombre de types de contrats.</li>
</ul>

Consigne :
    Refactorisez le code pour éliminer la duplication tout en conservant
    le même comportement. Les vérifications communes doivent apparaître
    une seule fois.

Modifier le code dans le fichier module/03_yagni/dry/exercice1.py

```python

def valider_dossier_auto(assure: dict, dossier: dict) -> list[str]:
    """Valide un dossier de souscription auto. Retourne la liste des erreurs."""
    erreurs = []

    # --- vérifications communes (dupliquées) ---
    if not assure.get("piece_identite_valide"):
        erreurs.append("Pièce d'identité manquante ou expirée")

    age = (date.today() - assure["date_naissance"]).days // 365
    if age < 18:
        erreurs.append("L'assuré doit être majeur")

    if assure.get("impayes", 0) > 0:
        erreurs.append("L'assuré a des cotisations impayées")

    # --- vérification spécifique auto ---
    if not dossier.get("permis_valide"):
        erreurs.append("Permis de conduire manquant ou invalide")

    if dossier.get("puissance_fiscale", 0) > 25:
        erreurs.append("Véhicule hors catégorie assurable")

    return erreurs


def valider_dossier_habitation(assure: dict, dossier: dict) -> list[str]:
    """Valide un dossier de souscription habitation. Retourne la liste des erreurs."""
    erreurs = []

    # --- vérifications communes (dupliquées) ---
    if not assure.get("piece_identite_valide"):
        erreurs.append("Pièce d'identité manquante ou expirée")

    age = (date.today() - assure["date_naissance"]).days // 365
    if age < 18:
        erreurs.append("L'assuré doit être majeur")

    if assure.get("impayes", 0) > 0:
        erreurs.append("L'assuré a des cotisations impayées")

    # --- vérification spécifique habitation ---
    if not dossier.get("diagnostic_immobilier"):
        erreurs.append("Diagnostic immobilier obligatoire manquant")

    if dossier.get("surface_m2", 0) <= 0:
        erreurs.append("Surface du bien non renseignée")

    return erreurs


def valider_dossier_sante(assure: dict, dossier: dict) -> list[str]:
    """Valide un dossier de souscription santé. Retourne la liste des erreurs."""
    erreurs = []

    # --- vérifications communes (dupliquées) ---
    if not assure.get("piece_identite_valide"):
        erreurs.append("Pièce d'identité manquante ou expirée")

    age = (date.today() - assure["date_naissance"]).days // 365
    if age < 18:
        erreurs.append("L'assuré doit être majeur")

    if assure.get("impayes", 0) > 0:
        erreurs.append("L'assuré a des cotisations impayées")

    # --- vérification spécifique santé ---
    if not dossier.get("questionnaire_medical"):
        erreurs.append("Questionnaire médical non rempli")

    if dossier.get("niveau_couverture") not in ("base", "confort", "premium"):
        erreurs.append("Niveau de couverture invalide")

    return erreurs


```
#### b) Exercice 2 : Génération de relevés clients

**Problème** :
Le service comptable génère des relevés annuels pour chaque type de contrat (auto, habitation, santé). Les trois fonctions reproduisent la même structure : en-tête avec les informations du client, liste des contrats avec calcul de prime, et pied de page avec le total. Seuls le calcul de la prime et le libellé de chaque ligne diffèrent.

Cette duplication pose problème :
<ul>
<li>Si le format du relevé change (ex. ajout du numéro client dans l'en-tête), il faut modifier trois fonctions.</li>
<li>Si on ajoute un nouveau type de contrat, il faut copier-coller toute la structure du relevé.</li>
<li>Le risque d'incohérence visuelle entre les relevés augmente avec le temps.</li>
</ul>

Consigne :
    Refactorisez le code pour que la structure du relevé (en-tête, boucle, pied de page)
    n'apparaisse qu'une seule fois. Chaque type de contrat ne doit fournir que
    la logique spécifique à sa ligne (libellé + calcul de prime).

Modifier le code dans le fichier module/03_dry_yagni/dry/exercice2.py

```python
from datetime import date


def generer_releve_auto(client: dict, contrats_auto: list[dict]) -> str:
    """Génère un relevé annuel pour les contrats auto d'un client."""
    lignes = []
    lignes.append("=" * 50)
    lignes.append(f"RELEVÉ ANNUEL — {client['nom']} {client['prenom']}")
    lignes.append(f"Adresse : {client['adresse']}")
    lignes.append(f"Date : {date.today().strftime('%d/%m/%Y')}")
    lignes.append("=" * 50)

    total = 0.0
    for contrat in contrats_auto:
        prime = contrat["valeur_vehicule"] * 0.05
        total += prime
        lignes.append(f"  Contrat {contrat['numero']} — Véhicule : {contrat['vehicule']} — Prime : {prime:.2f}€")

    lignes.append("-" * 50)
    lignes.append(f"TOTAL : {total:.2f}€")
    lignes.append("=" * 50)
    return "\n".join(lignes)


def generer_releve_habitation(client: dict, contrats_habitation: list[dict]) -> str:
    """Génère un relevé annuel pour les contrats habitation d'un client."""
    lignes = []
    lignes.append("=" * 50)
    lignes.append(f"RELEVÉ ANNUEL — {client['nom']} {client['prenom']}")
    lignes.append(f"Adresse : {client['adresse']}")
    lignes.append(f"Date : {date.today().strftime('%d/%m/%Y')}")
    lignes.append("=" * 50)

    total = 0.0
    for contrat in contrats_habitation:
        prime = contrat["surface_m2"] * 3.5
        total += prime
        lignes.append(f"  Contrat {contrat['numero']} — Bien : {contrat['adresse_bien']} — Prime : {prime:.2f}€")

    lignes.append("-" * 50)
    lignes.append(f"TOTAL : {total:.2f}€")
    lignes.append("=" * 50)
    return "\n".join(lignes)


def generer_releve_sante(client: dict, contrats_sante: list[dict]) -> str:
    """Génère un relevé annuel pour les contrats santé d'un client."""
    lignes = []
    lignes.append("=" * 50)
    lignes.append(f"RELEVÉ ANNUEL — {client['nom']} {client['prenom']}")
    lignes.append(f"Adresse : {client['adresse']}")
    lignes.append(f"Date : {date.today().strftime('%d/%m/%Y')}")
    lignes.append("=" * 50)

    total = 0.0
    for contrat in contrats_sante:
        prime = contrat["couverture"] * 0.08
        total += prime
        lignes.append(f"  Contrat {contrat['numero']} — Niveau : {contrat['niveau']} — Prime : {prime:.2f}€")

    lignes.append("-" * 50)
    lignes.append(f"TOTAL : {total:.2f}€")
    lignes.append("=" * 50)
    return "\n".join(lignes)
```

#### c) Exercice 3 : Notifications de sinistres

**Problème** :
Le service sinistres envoie des notifications par trois canaux (e-mail, SMS, courrier). Les trois fonctions reproduisent la même logique : détermination du niveau d'urgence selon le montant, calcul du remboursement estimé, et formatage du message. Seul le canal d'envoi et le destinataire changent.

Cette duplication pose problème :
<ul>
<li>Si les seuils d'urgence changent (ex. URGENT passe à 15 000€), il faut modifier trois fonctions.</li>
<li>Si le format du message évolue (ex. ajout de la date du sinistre), il faut penser à le faire partout.</li>
<li>Si on ajoute un nouveau canal (ex. notification push), il faut dupliquer tout le bloc une quatrième fois.</li>
</ul>

Consigne :
    Refactorisez le code pour que le calcul de l'urgence, le calcul du remboursement
    et le formatage du message n'apparaissent qu'une seule fois. Chaque canal ne doit
    gérer que l'acheminement au bon destinataire.

Modifier le code dans le fichier module/03_dry_yagni/dry/exercice3.py

```python
def notifier_sinistre_email(sinistre: dict) -> str:
    """Envoie une notification par e-mail pour un sinistre."""
    destinataire = sinistre["assure_email"]

    if sinistre["montant"] > 10_000:
        urgence = "URGENT"
    elif sinistre["montant"] > 5_000:
        urgence = "PRIORITAIRE"
    else:
        urgence = "NORMAL"

    remboursement = max(0, sinistre["montant"] - sinistre["franchise"])

    message = (
        f"[{urgence}] Sinistre n°{sinistre['numero']}\n"
        f"Type : {sinistre['type']}\n"
        f"Montant déclaré : {sinistre['montant']:.2f}€\n"
        f"Franchise : {sinistre['franchise']:.2f}€\n"
        f"Remboursement estimé : {remboursement:.2f}€"
    )
    return f"EMAIL à {destinataire} : {message}"


def notifier_sinistre_sms(sinistre: dict) -> str:
    """Envoie une notification par SMS pour un sinistre."""
    telephone = sinistre["assure_telephone"]

    if sinistre["montant"] > 10_000:
        urgence = "URGENT"
    elif sinistre["montant"] > 5_000:
        urgence = "PRIORITAIRE"
    else:
        urgence = "NORMAL"

    remboursement = max(0, sinistre["montant"] - sinistre["franchise"])

    message = (
        f"[{urgence}] Sinistre n°{sinistre['numero']}\n"
        f"Type : {sinistre['type']}\n"
        f"Montant déclaré : {sinistre['montant']:.2f}€\n"
        f"Franchise : {sinistre['franchise']:.2f}€\n"
        f"Remboursement estimé : {remboursement:.2f}€"
    )
    return f"SMS à {telephone} : {message}"


def notifier_sinistre_courrier(sinistre: dict) -> str:
    """Envoie une notification par courrier pour un sinistre."""
    adresse = sinistre["assure_adresse"]

    if sinistre["montant"] > 10_000:
        urgence = "URGENT"
    elif sinistre["montant"] > 5_000:
        urgence = "PRIORITAIRE"
    else:
        urgence = "NORMAL"

    remboursement = max(0, sinistre["montant"] - sinistre["franchise"])

    message = (
        f"[{urgence}] Sinistre n°{sinistre['numero']}\n"
        f"Type : {sinistre['type']}\n"
        f"Montant déclaré : {sinistre['montant']:.2f}€\n"
        f"Franchise : {sinistre['franchise']:.2f}€\n"
        f"Remboursement estimé : {remboursement:.2f}€"
    )
    return f"COURRIER à {adresse} : {message}"
```

### 2) YAGNI

#### a) Exercice 1 : Le service de tarification sur-ingéniéré

**Problème** :
Un développeur a créé une classe abstraite `MoteurTarificationBase` avec six méthodes abstraites pour « anticiper les besoins futurs » : conversion multi-devises, paiement mensuel, paiement trimestriel, taxes régionales… En pratique, le code métier n'utilise que `calculer_prime()` et `appliquer_remise()`.

Cette sur-ingénierie pose problème :
<ul>
<li>La classe abstraite force chaque implémentation à coder des méthodes inutilisées.</li>
<li>Le code est plus difficile à lire et à maintenir pour un besoin simple.</li>
<li>Les méthodes anticipées ne correspondent probablement pas au vrai besoin quand il arrivera.</li>
</ul>

Consigne :
    Simplifiez le code en supprimant tout ce qui n'est pas utilisé aujourd'hui.
    Le comportement réel (calcul de prime + remise) doit rester identique.

Modifier le code dans le fichier module/03_dry_yagni/yagni/exercice1.py

```python
from abc import ABC, abstractmethod


class MoteurTarificationBase(ABC):
    """Classe abstraite prévue pour supporter plusieurs algorithmes de tarification."""

    @abstractmethod
    def calculer_prime(self, contrat: dict) -> float:
        pass

    @abstractmethod
    def appliquer_remise(self, prime: float, client: dict) -> float:
        pass

    @abstractmethod
    def convertir_devise(self, montant: float, devise_cible: str) -> float:
        """Conversion multi-devises — prévu pour l'international."""
        pass

    @abstractmethod
    def calculer_prime_mensuelle(self, prime_annuelle: float) -> float:
        """Paiement mensuel — prévu mais pas encore demandé par le métier."""
        pass

    @abstractmethod
    def calculer_prime_trimestrielle(self, prime_annuelle: float) -> float:
        """Paiement trimestriel — prévu mais pas encore demandé par le métier."""
        pass

    @abstractmethod
    def appliquer_taxe_regionale(self, prime: float, region: str) -> float:
        """Taxes régionales — prévu pour une future réglementation."""
        pass


class TarificationAuto(MoteurTarificationBase):

    TAUX_CHANGE = {"EUR": 1.0, "USD": 1.08, "GBP": 0.86, "CHF": 0.95}

    def calculer_prime(self, contrat: dict) -> float:
        return contrat["valeur_vehicule"] * 0.05

    def appliquer_remise(self, prime: float, client: dict) -> float:
        if client.get("anciennete_ans", 0) >= 5:
            return prime * 0.90
        return prime

    def convertir_devise(self, montant: float, devise_cible: str) -> float:
        taux = self.TAUX_CHANGE.get(devise_cible, 1.0)
        return montant * taux

    def calculer_prime_mensuelle(self, prime_annuelle: float) -> float:
        return prime_annuelle / 12

    def calculer_prime_trimestrielle(self, prime_annuelle: float) -> float:
        return prime_annuelle / 4

    def appliquer_taxe_regionale(self, prime: float, region: str) -> float:
        taxes = {"idf": 0.03, "paca": 0.02, "bretagne": 0.01}
        return prime * (1 + taxes.get(region, 0.0))
```

#### b) Exercice 2 : Le modèle de sinistre surchargé

**Problème** :
La classe `Sinistre` a été développée avec de nombreux attributs et méthodes « pour plus tard » : coordonnées GPS, gestion de photos, tags, historique de modifications, export JSON, score de fraude… En production, seuls `calculer_remboursement()` et `est_recevable()` sont appelés, et seuls les attributs de base sont renseignés.

Cette sur-ingénierie pose problème :
<ul>
<li>Le constructeur a 13 paramètres alors que 6 suffisent.</li>
<li>Les méthodes anticipées (geolocaliser, exporter_json, calculer_score_fraude) ne sont jamais appelées.</li>
<li>Le code est difficile à comprendre pour un nouveau développeur qui ne sait pas ce qui est réellement utilisé.</li>
</ul>

Consigne :
    Simplifiez la classe en ne conservant que les attributs et méthodes
    réellement utilisés en production. Le comportement réel doit rester identique.

Modifier le code dans le fichier module/03_dry_yagni/yagni/exercice2.py

```python
from datetime import date, datetime


class Sinistre:
    """Modèle de sinistre avec de nombreux attributs et méthodes anticipés."""

    def __init__(
        self,
        numero: str,
        type_sinistre: str,
        montant: float,
        franchise: float,
        date_evenement: date,
        date_declaration: date,
        # --- Attributs anticipés jamais utilisés ---
        coordonnees_gps: tuple[float, float] | None = None,
        photos: list[str] | None = None,
        temoin_principal: dict | None = None,
        niveau_priorite: int = 0,
        tags: list[str] | None = None,
        canal_declaration: str = "agence",
        historique_modifications: list[dict] | None = None,
    ):
        self.numero = numero
        self.type_sinistre = type_sinistre
        self.montant = montant
        self.franchise = franchise
        self.date_evenement = date_evenement
        self.date_declaration = date_declaration
        self.coordonnees_gps = coordonnees_gps
        self.photos = photos or []
        self.temoin_principal = temoin_principal
        self.niveau_priorite = niveau_priorite
        self.tags = tags or []
        self.canal_declaration = canal_declaration
        self.historique_modifications = historique_modifications or []

    def calculer_remboursement(self) -> float:
        """Calcul utilisé en production."""
        return max(0.0, self.montant - self.franchise)

    def est_recevable(self) -> bool:
        """Vérification utilisée en production."""
        delai = (self.date_declaration - self.date_evenement).days
        return delai <= 5

    # --- Méthodes anticipées jamais appelées dans le code ---

    def ajouter_photo(self, chemin: str) -> None:
        """Prévu pour un futur module de gestion de photos."""
        self.photos.append(chemin)

    def geolocaliser(self) -> str:
        """Prévu pour un futur affichage cartographique."""
        if self.coordonnees_gps:
            lat, lon = self.coordonnees_gps
            return f"https://maps.example.com/?lat={lat}&lon={lon}"
        return "Coordonnées non disponibles"

    def ajouter_tag(self, tag: str) -> None:
        """Prévu pour un futur système de classification."""
        if tag not in self.tags:
            self.tags.append(tag)

    def historiser_modification(self, champ, ancienne_valeur, nouvelle_valeur):
        """Prévu pour un futur audit trail."""
        self.historique_modifications.append({
            "date": datetime.now().isoformat(),
            "champ": champ,
            "ancien": ancienne_valeur,
            "nouveau": nouvelle_valeur,
        })

    def exporter_json(self) -> dict:
        """Prévu pour une future API REST."""
        return {
            "numero": self.numero,
            "type": self.type_sinistre,
            "montant": self.montant,
            "franchise": self.franchise,
            "date_evenement": self.date_evenement.isoformat(),
            "date_declaration": self.date_declaration.isoformat(),
            "gps": self.coordonnees_gps,
            "photos": self.photos,
            "temoin": self.temoin_principal,
            "priorite": self.niveau_priorite,
            "tags": self.tags,
            "canal": self.canal_declaration,
        }

    def calculer_score_fraude(self) -> float:
        """Prévu pour un futur module anti-fraude."""
        score = 0.0
        if self.montant > 10_000:
            score += 30
        if (self.date_declaration - self.date_evenement).days == 0:
            score += 20
        if not self.temoin_principal:
            score += 10
        return score
```

#### c) Exercice 3 : Le gestionnaire de clients sur-anticipé

**Problème** :
Un développeur a créé une interface abstraite `AbstractClientRepository` avec six méthodes, alors qu'une seule implémentation existe (en mémoire). Trois des méthodes (`rechercher`, `exporter_csv`, `synchroniser_crm`) ne sont jamais appelées par le code métier. L'abstraction a été créée « au cas où on change de base de données ».

Cette sur-ingénierie pose problème :
<ul>
<li>L'interface abstraite n'a aucune utilité avec un seul backend.</li>
<li>Les méthodes rechercher, exporter_csv et synchroniser_crm ajoutent du code mort.</li>
<li>Chaque nouvelle implémentation devrait implémenter ces méthodes inutiles.</li>
</ul>

Consigne :
    Simplifiez le code en supprimant l'interface abstraite et toutes les méthodes
    non utilisées. Le comportement réel (ajouter, trouver, supprimer) doit rester identique.

Modifier le code dans le fichier module/03_dry_yagni/yagni/exercice3.py

```python
from abc import ABC, abstractmethod


class AbstractClientRepository(ABC):
    """Interface prévue pour supporter plusieurs backends de stockage."""

    @abstractmethod
    def ajouter(self, client: dict) -> None:
        pass

    @abstractmethod
    def trouver_par_id(self, client_id: int) -> dict | None:
        pass

    @abstractmethod
    def supprimer(self, client_id: int) -> None:
        pass

    @abstractmethod
    def rechercher(self, criteres: dict) -> list[dict]:
        """Recherche avancée multi-critères — prévue pour un futur back-office."""
        pass

    @abstractmethod
    def exporter_csv(self) -> str:
        """Export CSV — prévu pour un futur reporting."""
        pass

    @abstractmethod
    def synchroniser_crm(self) -> None:
        """Synchronisation CRM — prévue pour une future intégration Salesforce."""
        pass


class ClientRepositoryMemoire(AbstractClientRepository):
    """Implémentation en mémoire — la seule utilisée actuellement."""

    def __init__(self):
        self._clients: dict[int, dict] = {}
        self._prochain_id: int = 1

    def ajouter(self, client: dict) -> None:
        client["id"] = self._prochain_id
        self._clients[self._prochain_id] = client
        self._prochain_id += 1

    def trouver_par_id(self, client_id: int) -> dict | None:
        return self._clients.get(client_id)

    def supprimer(self, client_id: int) -> None:
        self._clients.pop(client_id, None)

    def rechercher(self, criteres: dict) -> list[dict]:
        """Implémentation complexe d'une recherche jamais utilisée."""
        resultats = []
        for client in self._clients.values():
            correspond = True
            for cle, valeur in criteres.items():
                if cle == "nom_contient":
                    if valeur.lower() not in client.get("nom", "").lower():
                        correspond = False
                elif cle == "age_min":
                    if client.get("age", 0) < valeur:
                        correspond = False
                elif cle == "age_max":
                    if client.get("age", 0) > valeur:
                        correspond = False
                elif cle == "ville":
                    if client.get("ville", "").lower() != valeur.lower():
                        correspond = False
                elif cle == "a_contrat_actif":
                    if client.get("contrat_actif") != valeur:
                        correspond = False
            if correspond:
                resultats.append(client)
        return resultats

    def exporter_csv(self) -> str:
        """Export CSV jamais appelé dans le code."""
        lignes = ["id,nom,prenom,age,ville"]
        for c in self._clients.values():
            lignes.append(
                f"{c['id']},{c.get('nom','')},{c.get('prenom','')},{c.get('age','')},{c.get('ville','')}"
            )
        return "\n".join(lignes)

    def synchroniser_crm(self) -> None:
        """Synchronisation jamais appelée — le CRM n'existe pas encore."""
        raise NotImplementedError("Intégration CRM pas encore développée")


class ServiceGestionClient:
    """Service métier qui utilise le repository."""

    def __init__(self, repo: AbstractClientRepository):
        self.repo = repo

    def inscrire_client(self, nom: str, prenom: str, age: int) -> dict:
        client = {"nom": nom, "prenom": prenom, "age": age}
        self.repo.ajouter(client)
        return client

    def obtenir_client(self, client_id: int) -> dict | None:
        return self.repo.trouver_par_id(client_id)

    def resilier_client(self, client_id: int) -> None:
        self.repo.supprimer(client_id)
```

## Correction
Tout les exercices ont la correction dans le dossier correction.
Afin de vous améliorer et de comprendre, veuillez la regarder seulement après avoir effectué les exercices.
