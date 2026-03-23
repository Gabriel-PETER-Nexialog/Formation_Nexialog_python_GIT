"""Correction Exercice 1 — Builder : Construction d'un contrat auto """


class ContratAuto:
    def __init__(self):
        self.assure_nom = ""
        self.assure_age = 0
        self.vehicule = ""
        self.valeur_vehicule = 0.0
        self.formule = "tiers"
        self.franchise = 300.0
        self.options = []

    def __str__(self):
        return (f"Contrat {self.formule} — {self.assure_nom} ({self.assure_age} ans) — "
                f"{self.vehicule} ({self.valeur_vehicule}€) — "
                f"Franchise : {self.franchise}€ — Options : {self.options}")


class ContratAutoBuilder:
    def __init__(self):
        self._contrat = ContratAuto()

    def avec_assure(self, nom: str, age: int):
        self._contrat.assure_nom = nom
        self._contrat.assure_age = age
        return self

    def avec_vehicule(self, nom: str, valeur: float):
        self._contrat.vehicule = nom
        self._contrat.valeur_vehicule = valeur
        return self

    def avec_formule(self, formule: str):
        self._contrat.formule = formule
        return self

    def avec_franchise(self, franchise: float):
        self._contrat.franchise = franchise
        return self

    def avec_option(self, option: str):
        self._contrat.options.append(option)
        return self

    def build(self) -> ContratAuto:
        return self._contrat


# --- Vérification ---
if __name__ == "__main__":
    contrat = (
        ContratAutoBuilder()
        .avec_assure("Dupont", 35)
        .avec_vehicule("Renault Clio", 15_000)
        .avec_formule("tous_risques")
        .avec_franchise(500)
        .avec_option("assistance 0km")
        .avec_option("bris de glace")
        .build()
    )
    print(contrat)