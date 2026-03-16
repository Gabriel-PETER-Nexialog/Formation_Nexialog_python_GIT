"""Correction Exercice 3 — Builder : Construction d'un devis santé (difficile)"""


class DevisSante:
    def __init__(self):
        self.assure_nom = ""
        self.assure_age = 0
        self.niveau = "base"
        self.beneficiaires = []
        self.plafond_annuel = 5_000.0
        self.taux_remboursement = 0.70

    def cotisation_mensuelle(self) -> float:
        coefficients = {"base": 1.0, "confort": 1.4, "premium": 1.8}
        return (self.assure_age * 2.5) * coefficients.get(self.niveau, 1.0)

    def __str__(self):
        return (f"DevisSante {self.niveau} — {self.assure_nom} ({self.assure_age} ans) — "
                f"Cotisation : {self.cotisation_mensuelle():.2f}€/mois — "
                f"Bénéficiaires : {self.beneficiaires} — "
                f"Plafond : {self.plafond_annuel:.0f}€ — "
                f"Remboursement : {self.taux_remboursement * 100:.0f}%")


class DevisSanteBuilder:
    def __init__(self):
        self._devis = DevisSante()

    def avec_assure(self, nom: str, age: int):
        self._devis.assure_nom = nom
        self._devis.assure_age = age
        return self

    def avec_niveau(self, niveau: str):
        self._devis.niveau = niveau
        return self

    def avec_beneficiaire(self, nom: str):
        self._devis.beneficiaires.append(nom)
        return self

    def avec_plafond(self, montant: float):
        self._devis.plafond_annuel = montant
        return self

    def avec_taux_remboursement(self, taux: float):
        self._devis.taux_remboursement = taux
        return self

    def build(self) -> DevisSante:
        if not self._devis.assure_nom:
            raise ValueError("Le nom de l'assuré est obligatoire.")
        if self._devis.assure_age <= 0:
            raise ValueError("L'âge de l'assuré doit être renseigné.")
        return self._devis


# --- Vérification ---
if __name__ == "__main__":
    devis = (
        DevisSanteBuilder()
        .avec_assure("Dupont", 42)
        .avec_niveau("confort")
        .avec_beneficiaire("Marie Dupont")
        .avec_beneficiaire("Lucas Dupont")
        .avec_plafond(10_000)
        .avec_taux_remboursement(0.80)
        .build()
    )
    print(devis)