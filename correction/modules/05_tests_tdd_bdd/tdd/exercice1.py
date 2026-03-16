"""Correction Exercice 1 — TDD : Service de gestion de sinistres"""

from datetime import date


class Sinistre:
    def __init__(
        self,
        numero: str,
        type_sinistre: str,
        montant: float,
        franchise: float,
        date_evenement: date,
        date_declaration: date,
    ):
        self.numero = numero
        self.type_sinistre = type_sinistre
        self.montant = montant
        self.franchise = franchise
        self.date_evenement = date_evenement
        self.date_declaration = date_declaration

    def est_recevable(self) -> bool:
        """Un sinistre est recevable s'il est déclaré dans les 5 jours."""
        delai = (self.date_declaration - self.date_evenement).days
        return delai <= 5

    def calculer_remboursement(self) -> float:
        """Remboursement = montant - franchise, minimum 0."""
        return max(0.0, self.montant - self.franchise)


class ServiceSinistre:
    def __init__(self, plafond: float):
        self.plafond = plafond

    def remboursement_plafonne(self, sinistre: Sinistre) -> float:
        """Le remboursement ne peut pas dépasser le plafond du contrat."""
        remboursement = sinistre.calculer_remboursement()
        return min(remboursement, self.plafond)

    def est_suspect(self, sinistre: Sinistre) -> bool:
        """Un sinistre est suspect si montant > 15000 ET déclaré le jour même."""
        delai = (sinistre.date_declaration - sinistre.date_evenement).days
        return sinistre.montant > 15_000 and delai == 0