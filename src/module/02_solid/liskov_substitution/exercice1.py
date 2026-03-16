class Contrat:
    def __init__(self, numero: str, prime: float):
        self.numero = numero
        self.prime = prime

    def resilier(self):
        print(f"Contrat {self.numero} résilié.")

    def calculer_prime(self) -> float:
        return self.prime


class ContratVieEntier(Contrat):
    """Un contrat vie entier ne peut jamais être résilié."""

    def resilier(self):
        raise NotImplementedError("Ce contrat ne peut pas être résilié.")


def resilier_tous(contrats: list[Contrat]):
    for c in contrats:
        c.resilier()
