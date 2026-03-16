class ScoringRegleMetier:
    def scorer(self, assure) -> int:
        score = 100
        score -= assure.nb_sinistres * 15
        score -= max(0, 25 - assure.age) * 2
        return max(0, score)


class MoteurSouscription:
    def __init__(self):
        # Couplé à l'algorithme de scoring concret
        self.scoring = ScoringRegleMetier()

    def accepter_souscription(self, assure) -> bool:
        score = self.scoring.scorer(assure)
        return score >= 60

    def calculer_surprime(self, assure) -> float:
        score = self.scoring.scorer(assure)
        if score < 80:
            return (80 - score) * 5.0
        return 0.0