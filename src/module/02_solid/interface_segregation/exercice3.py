from abc import ABC, abstractmethod

class IGestionnaireSinistre(ABC):
    # Trois métiers distincts dans une seule interface
    @abstractmethod
    def instruire_dossier(self, sinistre_id: int): pass
    @abstractmethod
    def valider_remboursement(self, montant: float): pass
    @abstractmethod
    def diligenter_expert(self, adresse: str): pass
    @abstractmethod
    def rediger_rapport_terrain(self) -> str: pass
    @abstractmethod
    def engager_recours(self, dossier_id: int): pass
    @abstractmethod
    def suivre_procedure_judiciaire(self): pass


class GestionnaireBackOffice(IGestionnaireSinistre):
    def instruire_dossier(self, sinistre_id: int):
        print(f"Dossier {sinistre_id} instruit.")

    def valider_remboursement(self, montant: float):
        print(f"Remboursement de {montant}€ validé.")

    def diligenter_expert(self, adresse: str):
        raise NotImplementedError

    def rediger_rapport_terrain(self) -> str:
        raise NotImplementedError

    def engager_recours(self, dossier_id: int):
        raise NotImplementedError

    def suivre_procedure_judiciaire(self):
        raise NotImplementedError