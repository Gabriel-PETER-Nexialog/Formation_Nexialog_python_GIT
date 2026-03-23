"""Correction Exercice 1 — Principe DRY : Validation de dossiers d'assurance

Les vérifications communes (pièce d'identité, majorité, impayés) sont
extraites dans une fonction unique. Chaque type de contrat n'ajoute
que ses propres règles spécifiques.
"""

from datetime import date

def verifications(assure: dict) -> list[str]:
    """Vérifie les conditions communes à tout type de souscription."""
    erreurs = []

    if not assure.get("piece_identite_valide"):
        erreurs.append("Pièce d'identité manquante ou expirée")

    age = (date.today() - assure["date_naissance"]).days // 365
    if age < 18:
        erreurs.append("L'assuré doit être majeur")

    if assure.get("impayes", 0) > 0:
        erreurs.append("L'assuré a des cotisations impayées")

    return erreurs

def verifications_auto(dossier: dict) -> list[str]:
    erreurs = []
    if not dossier.get("permis_valide"):
        erreurs.append("Permis de conduire manquant ou invalide")
    if dossier.get("puissance_fiscale", 0) > 25:
        erreurs.append("Véhicule hors catégorie assurable")
    return erreurs


def verifications_habitation(dossier: dict) -> list[str]:
    erreurs = []
    if not dossier.get("diagnostic_immobilier"):
        erreurs.append("Diagnostic immobilier obligatoire manquant")
    if dossier.get("surface_m2", 0) <= 0:
        erreurs.append("Surface du bien non renseignée")
    return erreurs


def verifications_sante(dossier: dict) -> list[str]:
    erreurs = []
    if not dossier.get("questionnaire_medical"):
        erreurs.append("Questionnaire médical non rempli")
    if dossier.get("niveau_couverture") not in ("base", "confort", "premium"):
        erreurs.append("Niveau de couverture invalide")
    return erreurs


VERIFICATIONS_PAR_TYPE = {
    "auto": verifications_auto,
    "habitation": verifications_habitation,
    "sante": verifications_sante,
}


def valider_dossier(type_contrat: str, assure: dict, dossier: dict) -> list[str]:
    """Valide un dossier de souscription pour n'importe quel type de contrat."""
    erreurs = verifications(assure)

    verification_specifique = VERIFICATIONS_PAR_TYPE.get(type_contrat)
    if verification_specifique is None:
        raise ValueError(f"Type de contrat inconnu : {type_contrat}")

    erreurs.extend(verification_specifique(dossier))
    return erreurs

# --- Vérification  ---
if __name__ == "__main__":
    assure_ok = {
        "piece_identite_valide": True,
        "date_naissance": date(1990, 5, 12),
        "impayes": 0,
    }
    assure_mineur = {
        "piece_identite_valide": True,
        "date_naissance": date(2015, 1, 1),
        "impayes": 0,
    }

    dossier_auto = {"permis_valide": True, "puissance_fiscale": 7}
    dossier_habitat = {"diagnostic_immobilier": True, "surface_m2": 65}
    dossier_sante = {"questionnaire_medical": True, "niveau_couverture": "confort"}

    print(valider_dossier("auto", assure_ok, dossier_auto))              # []
    print(valider_dossier("habitation", assure_mineur, dossier_habitat))  # ["L'assuré doit être majeur"]
    print(valider_dossier("sante", assure_ok, dossier_sante))            # []