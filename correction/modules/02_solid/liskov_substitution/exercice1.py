from abc import ABC, abstractmethod

class Contrat(ABC):
    def __init__(self, numero: str, prime: float):
        self.numero = numero
        self.prime  = prime

    @abstractmethod
    def calculer_prime(self) -> float:
        pass

class ContratResiliable(Contrat):
    @abstractmethod
    def resilier(self):
        pass


class ContratAuto(ContratResiliable):
    def calculer_prime(self) -> float:
        return self.prime

    def resilier(self):
        print(f"Contrat auto {self.numero} résilié.")


class ContratVieEntier(Contrat):
    def calculer_prime(self) -> float:
        return self.prime


# Chaque fonction ne reçoit que ce qu'elle peut vraiment utiliser
def resilier_tous(contrats: list[ContratResiliable]):
    for c in contrats:
        c.resilier()