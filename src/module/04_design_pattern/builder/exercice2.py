"""Exercice 2 — Builder : Construction d'une offre habitation

Implémentez toutes les méthodes du OffreHabitationBuilder.
"""


class OffreHabitation:
    def __init__(self):
        self.proprietaire = ""
        self.adresse = ""
        self.surface_m2 = 0.0
        self.nb_pieces = 0
        self.type_bien = "appartement"
        self.formule = "essentielle"
        self.garanties = []
        self.franchise = 250.0

    def prime_annuelle(self) -> float:
        base = self.surface_m2 * 3.5
        coeff_formule = {"essentielle": 1.0, "confort": 1.3, "premium": 1.6}
        return base * coeff_formule.get(self.formule, 1.0)

    def __str__(self):
        return (f"Offre {self.formule} — {self.proprietaire} — "
                f"{self.type_bien} {self.surface_m2}m² à {self.adresse} — "
                f"Prime : {self.prime_annuelle():.2f}€/an — "
                f"Garanties : {self.garanties}")


class OffreHabitationBuilder:
    def __init__(self):
        self._offre = OffreHabitation()

    def avec_proprietaire(self, nom: str):
        # TODO
        pass

    def avec_adresse(self, adresse: str):
        # TODO
        pass

    def avec_surface(self, surface_m2: float, nb_pieces: int):
        # TODO
        pass

    def avec_type_bien(self, type_bien: str):
        # TODO
        pass

    def avec_formule(self, formule: str):
        # TODO
        pass

    def avec_garantie(self, garantie: str):
        # TODO
        pass

    def avec_franchise(self, franchise: float):
        # TODO
        pass

    def build(self) -> OffreHabitation:
        # TODO : vérifier que l'adresse est renseignée, puis retourner l'offre
        pass


# --- Vérification ---
if __name__ == "__main__":
    offre = (
        OffreHabitationBuilder()
        .avec_proprietaire("Martin")
        .avec_adresse("5 avenue des Champs, 75008 Paris")
        .avec_surface(85, 4)
        .avec_type_bien("appartement")
        .avec_formule("confort")
        .avec_garantie("dégât des eaux")
        .avec_garantie("vol")
        .avec_franchise(400)
        .build()
    )
    print(offre)