from abc import ABC, abstractmethod

class CalculateurPrime(ABC):
    """Fermé à la modification — ouvert à l'extension."""
    @abstractmethod
    def calculer(self, contrat) -> float:
        pass


class PrimeAuto(CalculateurPrime):
    def calculer(self, contrat) -> float:
        return contrat.valeur_vehicule * 0.05


class PrimeHabitation(CalculateurPrime):
    def calculer(self, contrat) -> float:
        return contrat.surface_m2 * 3.5


class PrimeSante(CalculateurPrime):
    def calculer(self, contrat) -> float:
        return contrat.age_assure * 12.0


class PrimeAnimaux(CalculateurPrime):
    def calculer(self, contrat) -> float:
        return contrat.nb_animaux * 85.0


# Le moteur de tarification n'est jamais modifié
class MoteurdeTarification:
    def __init__(self, calculateur: CalculateurPrime):
        self.calculateur = calculateur

    def tarifer(self, contrat) -> float:
        return self.calculateur.calculer(contrat)