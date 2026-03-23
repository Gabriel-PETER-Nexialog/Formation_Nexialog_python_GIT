"""Exercice 3 — Builder : Construction d'un devis santé

Créez entièrement la classe DevisSante et son DevisSanteBuilder.
"""


# TODO : Créez la classe DevisSante avec les attributs :
#   - assure_nom (str), assure_age (int)
#   - niveau ("base", "confort", "premium")
#   - beneficiaires (list[str])
#   - plafond_annuel (float, défaut 5000)
#   - taux_remboursement (float, défaut 0.70)
#
# Méthode cotisation_mensuelle() -> float :
#   (age * 2.5) * coeff_niveau
#   coefficients : base=1.0, confort=1.4, premium=1.8
#
# Méthode __str__() pour afficher le devis


# TODO : Créez la classe DevisSanteBuilder
#   - avec_assure(nom, age)
#   - avec_niveau(niveau)
#   - avec_beneficiaire(nom)
#   - avec_plafond(montant)
#   - avec_taux_remboursement(taux)
#   - build() → DevisSante (vérifier nom et age renseignés)


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
    # DevisSante confort — Dupont (42 ans) — Cotisation : 147.00€/mois —
    # Bénéficiaires : ['Marie Dupont', 'Lucas Dupont'] —
    # Plafond : 10000€ — Remboursement : 80%