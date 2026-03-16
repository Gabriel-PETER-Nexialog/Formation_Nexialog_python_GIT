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
