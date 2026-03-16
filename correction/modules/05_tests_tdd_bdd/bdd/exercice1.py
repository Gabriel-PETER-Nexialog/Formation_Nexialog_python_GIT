"""Correction Exercice 2 — BDD : Service de souscription de contrats"""

from datetime import date


class Client:
    def __init__(
        self,
        nom: str,
        age: int,
        piece_identite_valide: bool = True,
        impayes: int = 0,
        anciennete_ans: int = 0,
    ):
        self.nom = nom
        self.age = age
        self.piece_identite_valide = piece_identite_valide
        self.impayes = impayes
        self.anciennete_ans = anciennete_ans


class ServiceSouscription:
    def __init__(self):
        self._compteur = 0

    def est_eligible(self, client: Client) -> bool:
        """Vérifie l'éligibilité : majeur, pièce valide, pas d'impayés."""
        if client.age < 18:
            return False
        if not client.piece_identite_valide:
            return False
        if client.impayes > 0:
            return False
        return True

    def calculer_prime(self, type_contrat: str, **kwargs) -> float:
        """Calcule la prime selon le type de contrat."""
        if type_contrat == "auto":
            return kwargs["valeur_vehicule"] * 0.05
        elif type_contrat == "habitation":
            return kwargs["surface_m2"] * 3.5
        elif type_contrat == "sante":
            return kwargs["age"] * 12.0
        else:
            raise ValueError(f"Type de contrat inconnu : {type_contrat}")

    def appliquer_remise_fidelite(self, prime: float, client: Client) -> float:
        """Applique 10% de réduction si ancienneté >= 5 ans."""
        if client.anciennete_ans >= 5:
            return prime * 0.90
        return prime

    def generer_numero(self, type_contrat: str, annee: int) -> str:
        """Génère un numéro au format TYPE-ANNEE-NUMERO."""
        self._compteur += 1
        type_upper = type_contrat.upper()
        return f"{type_upper}-{annee}-{self._compteur:03d}"

    def souscrire(self, client: Client, type_contrat: str, annee: int, **kwargs) -> dict:
        """Souscrit un contrat si le client est éligible."""
        if not self.est_eligible(client):
            raise ValueError(f"Client {client.nom} non éligible à la souscription.")

        prime = self.calculer_prime(type_contrat, **kwargs)
        prime = self.appliquer_remise_fidelite(prime, client)
        numero = self.generer_numero(type_contrat, annee)

        return {
            "numero": numero,
            "client": client.nom,
            "type": type_contrat,
            "prime": prime,
        }