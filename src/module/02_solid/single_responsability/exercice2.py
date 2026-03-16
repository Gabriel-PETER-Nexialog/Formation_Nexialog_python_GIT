from datetime import timedelta

db = None

class GestionSinistre:
    def __init__(self, sinistre):
        self.sinistre = sinistre

    def valider_recevabilite(self) -> bool:
        return (self.sinistre.date_declaration <=
                self.sinistre.date_evenement + timedelta(days=5))

    def calculer_remboursement(self) -> float:
        franchise = 300
        return max(0, self.sinistre.montant - franchise)

    def mettre_a_jour_statut(self, statut: str):
        db.execute("UPDATE sinistres SET statut=?", statut, self.sinistre.id)

    def detecter_fraude(self) -> bool:
        # heuristique : > 3 sinistres en 12 mois
        nb = db.query("SELECT COUNT(*) FROM sinistres ...")
        return nb > 3