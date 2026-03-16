from abc import ABC, abstractmethod
from enum import Enum, auto

class StatutSinistre(Enum):
    EN_COURS  = auto()
    ACCEPTE   = auto()
    REFUSE    = auto()


class Sinistre(ABC):
    def __init__(self, montant: float, franchise: float):
        self.montant   = montant
        self.franchise = franchise

    @abstractmethod
    def calculer_remboursement(self) -> float:
        pass

    @abstractmethod
    def statut(self) -> StatutSinistre:
        pass


class SinistreAccepte(Sinistre):
    def calculer_remboursement(self) -> float:
        return max(0.0, self.montant - self.franchise)

    def statut(self) -> StatutSinistre:
        return StatutSinistre.ACCEPTE


class SinistreRefuse(Sinistre):
    def calculer_remboursement(self) -> float:
        # Retourne 0 mais le statut est explicite et interrogeable
        return 0.0

    def statut(self) -> StatutSinistre:
        return StatutSinistre.REFUSE


# Le code appelant peut distinguer les cas sans isinstance
def total_remboursements(sinistres: list[Sinistre]) -> float:
    return sum(s.calculer_remboursement() for s in sinistres)

def rapport_sinistres(sinistres: list[Sinistre]):
    for s in sinistres:
        print(f"Statut : {s.statut().name} — {s.calculer_remboursement()}€")