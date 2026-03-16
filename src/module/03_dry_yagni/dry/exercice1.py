"""Exercice 1 — Principe DRY :

"""

from datetime import date


def valider_dossier_auto(assure: dict, dossier: dict) -> list[str]:
    """Valide un dossier de souscription auto. Retourne la liste des erreurs."""
    erreurs = []

    # --- vérifications communes (dupliquées) ---
    if not assure.get("piece_identite_valide"):
        erreurs.append("Pièce d'identité manquante ou expirée")

    age = (date.today() - assure["date_naissance"]).days // 365
    if age < 18:
        erreurs.append("L'assuré doit être majeur")

    if assure.get("impayes", 0) > 0:
        erreurs.append("L'assuré a des cotisations impayées")

    # --- vérification spécifique auto ---
    if not dossier.get("permis_valide"):
        erreurs.append("Permis de conduire manquant ou invalide")

    if dossier.get("puissance_fiscale", 0) > 25:
        erreurs.append("Véhicule hors catégorie assurable")

    return erreurs


def valider_dossier_habitation(assure: dict, dossier: dict) -> list[str]:
    """Valide un dossier de souscription habitation. Retourne la liste des erreurs."""
    erreurs = []

    # --- vérifications communes (dupliquées) ---
    if not assure.get("piece_identite_valide"):
        erreurs.append("Pièce d'identité manquante ou expirée")

    age = (date.today() - assure["date_naissance"]).days // 365
    if age < 18:
        erreurs.append("L'assuré doit être majeur")

    if assure.get("impayes", 0) > 0:
        erreurs.append("L'assuré a des cotisations impayées")

    # --- vérification spécifique habitation ---
    if not dossier.get("diagnostic_immobilier"):
        erreurs.append("Diagnostic immobilier obligatoire manquant")

    if dossier.get("surface_m2", 0) <= 0:
        erreurs.append("Surface du bien non renseignée")

    return erreurs


def valider_dossier_sante(assure: dict, dossier: dict) -> list[str]:
    """Valide un dossier de souscription santé. Retourne la liste des erreurs."""
    erreurs = []

    # --- vérifications communes (dupliquées) ---
    if not assure.get("piece_identite_valide"):
        erreurs.append("Pièce d'identité manquante ou expirée")

    age = (date.today() - assure["date_naissance"]).days // 365
    if age < 18:
        erreurs.append("L'assuré doit être majeur")

    if assure.get("impayes", 0) > 0:
        erreurs.append("L'assuré a des cotisations impayées")

    # --- vérification spécifique santé ---
    if not dossier.get("questionnaire_medical"):
        erreurs.append("Questionnaire médical non rempli")

    if dossier.get("niveau_couverture") not in ("base", "confort", "premium"):
        erreurs.append("Niveau de couverture invalide")

    return erreurs


# --- Vérification rapide ---
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

    print(valider_dossier_auto(assure_ok, dossier_auto))          # []
    print(valider_dossier_habitation(assure_mineur, dossier_habitat))  # ["L'assuré doit être majeur"]
    print(valider_dossier_sante(assure_ok, dossier_sante))        # []