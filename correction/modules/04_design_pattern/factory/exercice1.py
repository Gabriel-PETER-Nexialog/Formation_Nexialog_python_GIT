"""Correction Exercice 1 — Factory : Création de contrats par type """

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


class ContratSante(Contrat):
    def __init__(self, age_assure: int):
        self.age_assure = age_assure

    def calculer_prime(self) -> float:
        return self.age_assure * 12.0

    def description(self) -> str:
        return f"Contrat Santé — {self.age_assure} ans"


class ContratFactory:
    @staticmethod
    def creer(type_contrat: str, **kwargs) -> Contrat:
        if type_contrat == "auto":
            return ContratAuto(kwargs["valeur_vehicule"])
        elif type_contrat == "habitation":
            return ContratHabitation(kwargs["surface_m2"])
        elif type_contrat == "sante":
            return ContratSante(kwargs["age_assure"])
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