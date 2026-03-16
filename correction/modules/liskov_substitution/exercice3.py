from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class Contrat:
    def __init__(self, content: str, nom: str, date: datetime):
        self.content = content
        self.nom = nom
        self.date = date

    pass


@dataclass
class Tuteur:
    nom: str
    lien: str


class Assure(ABC):
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    @abstractmethod
    def souscrire_contrat(self, contrat):
        # Signature identique pour tous les sous-types
        pass


class AssureMajeur(Assure):
    def souscrire_contrat(self, contrat):
        contrat.activer(self)
        print(f"{self.nom} a souscrit le contrat.")


class AssureMineur(Assure):
    # Le tuteur est une donnée de l'objet, pas un paramètre surprise
    def __init__(self, nom: str, age: int, tuteur: Tuteur):
        super().__init__(nom, age)
        self.tuteur = tuteur

    def souscrire_contrat(self, contrat):
        # Même signature que le parent — substituable sans risque
        contrat.activer(self)
        print(f"{self.nom} (tuteur : {self.tuteur.nom}) a souscrit le contrat.")


# Fonctionne pour AssureMajeur et AssureMineur sans distinction
def souscrire_batch(assures: list[Assure], contrat):
    for a in assures:
        a.souscrire_contrat(contrat)


tuteur = Tuteur(nom="Marie Dupont", lien="mère")
assures = [
    AssureMajeur("Jean Martin", 35),
    AssureMineur("Léo Martin", 14, tuteur),
]

mon_contrat = Contrat(content="content", nom="Johne Doe", date=datetime.now())
souscrire_batch(assures, mon_contrat)
