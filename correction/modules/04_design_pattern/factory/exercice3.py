"""Correction Exercice 3 — Factory : Création de calculateurs de remise """

from abc import ABC, abstractmethod


class Remise(ABC):
    @abstractmethod
    def calculer(self, client: dict) -> float:
        pass

    @abstractmethod
    def nom(self) -> str:
        pass


class RemiseFidelite(Remise):
    def calculer(self, client: dict) -> float:
        if client.get("anciennete_ans", 0) >= 5:
            return 0.10
        return 0.0

    def nom(self) -> str:
        return "Fidélité"


class RemiseMultiContrats(Remise):
    def calculer(self, client: dict) -> float:
        if len(client.get("contrats", [])) >= 3:
            return 0.08
        return 0.0

    def nom(self) -> str:
        return "Multi-contrats"


class RemiseParrainage(Remise):
    def calculer(self, client: dict) -> float:
        if client.get("a_parraine"):
            return 0.05
        return 0.0

    def nom(self) -> str:
        return "Parrainage"


class RemiseFactory:
    @staticmethod
    def creer(type_remise: str) -> Remise:
        if type_remise == "fidelite":
            return RemiseFidelite()
        elif type_remise == "multi_contrats":
            return RemiseMultiContrats()
        elif type_remise == "parrainage":
            return RemiseParrainage()
        else:
            raise ValueError(f"Type de remise inconnu : {type_remise}")


# --- Vérification ---
if __name__ == "__main__":
    client = {
        "nom": "Dupont",
        "anciennete_ans": 7,
        "contrats": ["auto", "habitation", "sante"],
        "a_parraine": True,
    }

    for type_r in ["fidelite", "multi_contrats", "parrainage"]:
        remise = RemiseFactory.creer(type_r)
        taux = remise.calculer(client)
        print(f"Remise {remise.nom()} : {taux * 100:.0f}%")