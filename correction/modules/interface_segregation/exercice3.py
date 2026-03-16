from abc import ABC, abstractmethod

# Interface 1 : instruction et validation back-office
class IInstructionDossier(ABC):
    @abstractmethod
    def instruire_dossier(self, sinistre_id: int): pass
    @abstractmethod
    def valider_remboursement(self, montant: float): pass


# Interface 2 : expertise terrain
class IExpertiseTerrain(ABC):
    @abstractmethod
    def diligenter_expert(self, adresse: str): pass
    @abstractmethod
    def rediger_rapport_terrain(self) -> str: pass


# Interface 3 : recours et contentieux juridique
class IRecours(ABC):
    @abstractmethod
    def engager_recours(self, dossier_id: int): pass
    @abstractmethod
    def suivre_procedure_judiciaire(self): pass


# Chaque classe n'implémente que son périmètre métier
class GestionnaireBackOffice(IInstructionDossier):
    def instruire_dossier(self, sinistre_id: int):
        print(f"Dossier {sinistre_id} instruit.")

    def valider_remboursement(self, montant: float):
        print(f"Remboursement de {montant}€ validé.")


class ExpertTerrain(IExpertiseTerrain):
    def diligenter_expert(self, adresse: str):
        print(f"Expert mandaté à : {adresse}")

    def rediger_rapport_terrain(self) -> str:
        return "Rapport d'expertise terrain rédigé."


class JuristeSinistre(IRecours):
    def engager_recours(self, dossier_id: int):
        print(f"Recours engagé pour le dossier {dossier_id}.")

    def suivre_procedure_judiciaire(self):
        print("Suivi procédure en cours.")


# Un gestionnaire senior peut combiner plusieurs interfaces
class GestionnaireExpert(IInstructionDossier, IExpertiseTerrain):
    def instruire_dossier(self, sinistre_id: int):
        print(f"Dossier {sinistre_id} instruit par expert.")

    def valider_remboursement(self, montant: float):
        print(f"{montant}€ validés après expertise.")

    def diligenter_expert(self, adresse: str):
        print(f"Auto-désignation terrain : {adresse}")

    def rediger_rapport_terrain(self) -> str:
        return "Rapport expert senior rédigé."