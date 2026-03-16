from abc import ABC, abstractmethod


api_risque = None
mon_modele_xgboost = None

# Abstraction orientée par le besoin du moteur de souscription
class IScoringRisque(ABC):
    @abstractmethod
    def scorer(self, assure) -> int:
        """Retourne un score entre 0 (risque max) et 100 (risque nul)."""
        pass


# Algorithme historique par règles métier
class ScoringRegleMetier(IScoringRisque):
    def scorer(self, assure) -> int:
        score = 100
        score -= assure.nb_sinistres * 15
        score -= max(0, 25 - assure.age) * 2
        return max(0, score)


# Nouveau modèle ML — aucune modification du moteur nécessaire
class ScoringML(IScoringRisque):
    def __init__(self, modele):
        self.modele = modele

    def scorer(self, assure) -> int:
        features = [assure.age, assure.nb_sinistres, assure.anciennete]
        return int(self.modele.predict([features])[0])


# Scoring externe via API partenaire
class ScoringAPIExterne(IScoringRisque):
    def scorer(self, assure) -> int:
        reponse = api_risque.get(f"/score/{assure.id}")
        return reponse.json()["score"]


# Moteur de souscription pur — ignorant de l'algorithme de scoring
class MoteurSouscription:
    SEUIL_ACCEPTATION = 60
    SEUIL_SURPRIME    = 80

    def __init__(self, scoring: IScoringRisque):
        self.scoring = scoring

    def accepter_souscription(self, assure) -> bool:
        return self.scoring.scorer(assure) >= self.SEUIL_ACCEPTATION

    def calculer_surprime(self, assure) -> float:
        score = self.scoring.scorer(assure)
        if score < self.SEUIL_SURPRIME:
            return (self.SEUIL_SURPRIME - score) * 5.0
        return 0.0


# Production : règles métier classiques
moteur_prod = MoteurSouscription(ScoringRegleMetier())

# Expérimentation : modèle ML sans toucher au moteur
moteur_ml = MoteurSouscription(ScoringML(mon_modele_xgboost))
