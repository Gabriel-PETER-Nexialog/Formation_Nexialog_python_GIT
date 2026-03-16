


class CalculateurPrime:

    def calculer(self, contrat) -> float:
        if contrat.type == "auto":
            return contrat.valeur_vehicule * 0.05

        elif contrat.type == "habitation":
            return contrat.surface_m2 * 3.5

        elif contrat.type == "sante":
            return contrat.age_assure * 12.0

        # ← à chaque nouveau contrat, on rouvre cette classe
        else:
            raise ValueError(f"Type inconnu : {contrat.type}")
