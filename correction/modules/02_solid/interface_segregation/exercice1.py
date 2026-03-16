from abc import ABC, abstractmethod

# Chaque interface a une capacité métier cohérente
class ICalculPrime(ABC):
    @abstractmethod
    def calculer_prime(self) -> float: pass

class IResiliable(ABC):
    @abstractmethod
    def resilier(self): pass

class IEpargne(ABC):
    @abstractmethod
    def gerer_epargne(self, montant: float): pass

class IAccident(ABC):
    @abstractmethod
    def declarer_accident(self): pass

class IHospitalisation(ABC):
    @abstractmethod
    def rembourser_hospitalisation(self): pass


# ContratVoyage n'implémente que ce qui le concerne
class ContratVoyage(ICalculPrime, IResiliable, IHospitalisation):
    def calculer_prime(self) -> float:
        return 120.0

    def resilier(self):
        print("Contrat voyage résilié.")

    def rembourser_hospitalisation(self):
        print("Remboursement frais médicaux voyage.")


# ContratVie n'implémente que ses propres capacités
class ContratVie(ICalculPrime, IEpargne):
    def calculer_prime(self) -> float:
        return 250.0

    def gerer_epargne(self, montant: float):
        print(f"Versement épargne vie : {montant}€")


# ContratAuto combine exactement les capacités d'un véhicule
class ContratAuto(ICalculPrime, IResiliable, IAccident):
    def calculer_prime(self) -> float:
        return 480.0

    def resilier(self):
        print("Contrat auto résilié.")

    def declarer_accident(self):
        print("Accident déclaré, expertise planifiée.")