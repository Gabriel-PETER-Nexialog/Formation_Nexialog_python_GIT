


class Assure:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def souscrire_contrat(self, contrat):
        # Précondition parent : aucune, tout assuré peut souscrire
        contrat.activer(self)
        print(f"{self.nom} a souscrit le contrat.")


class AssureMineur(Assure):

    def souscrire_contrat(self, contrat, tuteur=None):
        # Précondition renforcée : exige un tuteur que le parent ne demandait pas
        if tuteur is None:
            raise ValueError("Un tuteur légal est obligatoire pour un mineur.")
        contrat.activer(self)
        print(f"{self.nom} (tuteur : {tuteur}) a souscrit le contrat.")


# Erreur si assure est un AssureMineur sans tuteur
def souscrire_batch(assures: list[Assure], contrat):
    for a in assures:
        a.souscrire_contrat(contrat)