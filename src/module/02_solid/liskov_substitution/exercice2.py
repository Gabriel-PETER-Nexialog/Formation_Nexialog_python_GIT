class Sinistre:
    def __init__(self, montant: float, franchise: float):
        self.montant = montant
        self.franchise = franchise

    def calculer_remboursement(self) -> float:
        return max(0.0, self.montant - self.franchise)


class SinistreRefuse(Sinistre):
    """Sinistre dont la prise en charge a été refusée."""

    def calculer_remboursement(self) -> float:
        # Retourne 0 sans signaler que le sinistre est refusé
        # Affaiblit la postcondition : le calcul promis ne se fait pas
        return 0.0


# Ce total est silencieusement faux si la liste contient des SinistreRefuse
def total_remboursements(sinistres: list[Sinistre]) -> float:
    return sum(s.calculer_remboursement() for s in sinistres)
