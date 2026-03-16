"""Exercice 1 — Principe YAGNI : Le service de tarification sur-ingéniéré

"""

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


# --- Utilisation réelle dans le code métier ---
if __name__ == "__main__":
    tarification = TarificationAuto()

    contrat = {"valeur_vehicule": 20_000}
    client = {"nom": "Dupont", "anciennete_ans": 6}

    # Seules ces deux opérations sont réellement utilisées aujourd'hui
    prime = tarification.calculer_prime(contrat)
    prime_finale = tarification.appliquer_remise(prime, client)

    print(f"Prime annuelle : {prime_finale:.2f}€")  # 900.0€