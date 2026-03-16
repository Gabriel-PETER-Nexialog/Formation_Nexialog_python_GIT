db = None

class Sinistre:
    """Responsabilité : modéliser le sinistre et ses règles de validation."""
    def __init__(self, sinistre):
        self.sinistre = sinistre

    def est_recevable(self) -> bool:
        return (self.sinistre.date_declaration <=
                self.sinistre.date_evenement + timedelta(days=5))


class CalculateurRemboursement:
    """Responsabilité : calculer les montants financiers."""
    FRANCHISE = 300

    def calculer(self, sinistre) -> float:
        return max(0, sinistre.montant - self.FRANCHISE)


class SinistreRepository:
    """Responsabilité : gérer la persistance des sinistres."""
    def mettre_a_jour_statut(self, sinistre_id: int, statut: str):
        db.execute("UPDATE sinistres SET statut=?", statut, sinistre_id)


class DetecteurFraude:
    """Responsabilité : analyser les risques de fraude."""
    SEUIL_SINISTRES = 3

    def est_suspect(self, assure_id: int) -> bool:
        nb = db.query("SELECT COUNT(*) FROM sinistres ...")
        return nb > self.SEUIL_SINISTRES