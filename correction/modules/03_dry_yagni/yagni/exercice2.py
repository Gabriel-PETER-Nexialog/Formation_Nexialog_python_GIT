"""Correction Exercice 2 — Principe YAGNI : Le modèle de sinistre surchargé

On ne conserve que les attributs et méthodes réellement utilisés
en production : numéro, type, montant, franchise, dates,
plus calculer_remboursement() et est_recevable().
Tout le reste (photos, GPS, tags, historique, export JSON,
score de fraude) est supprimé.
"""

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

    def calculer_remboursement(self) -> float:
        return max(0.0, self.montant - self.franchise)

    def est_recevable(self) -> bool:
        delai = (self.date_declaration - self.date_evenement).days
        return delai <= 5


# --- Utilisation ---
if __name__ == "__main__":
    sinistre = Sinistre(
        numero="SIN-2024-042",
        type_sinistre="dégât des eaux",
        montant=8_500.0,
        franchise=300.0,
        date_evenement=date(2024, 3, 10),
        date_declaration=date(2024, 3, 12),
    )

    print(f"Recevable : {sinistre.est_recevable()}")                    # True
    print(f"Remboursement : {sinistre.calculer_remboursement():.2f}€")  # 8200.00€