from abc import ABC, abstractmethod

class RegleRemise(ABC):
    """Interface fermée. Chaque règle est une extension indépendante."""
    @abstractmethod
    def appliquer(self, client) -> float:
        pass


class RemiseFidelite(RegleRemise):
    def appliquer(self, client) -> float:
        return 0.05 if client.anciennete_ans >= 5 else 0.0


class RemiseMultiContrats(RegleRemise):
    def appliquer(self, client) -> float:
        return 0.10 if len(client.contrats) >= 3 else 0.0


class RemiseParrainage(RegleRemise):
    def appliquer(self, client) -> float:
        return 0.03 if client.a_parraine else 0.0


class RemiseEtudiant(RegleRemise):
    def appliquer(self, client) -> float:
        return 0.08 if client.statut == "etudiant" else 0.0


class GestionnaireRemise:
    PLAFOND = 0.20

    def __init__(self, regles: list[RegleRemise]):
        self.regles = regles  # injection des règles

    def calculer_remise(self, client) -> float:
        total = sum(r.appliquer(client) for r in self.regles)
        return min(total, self.PLAFOND)


# Usage : on compose librement les règles actives
gestionnaire = GestionnaireRemise([
    RemiseFidelite(),
    RemiseMultiContrats(),
    RemiseParrainage(),
])