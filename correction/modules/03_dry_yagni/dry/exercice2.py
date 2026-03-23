"""Correction Exercice 2 — Principe DRY : Génération de relevés clients

L'en-tête, le pied de page et la structure du relevé sont factorisés.
Chaque type de contrat fournit uniquement la logique pour décrire
une ligne de contrat (libellé + calcul de prime).
"""

from datetime import date


def formater_en_tete(client: dict) -> list[str]:
    """Génère l'en-tête commun à tout relevé."""
    return [
        "=" * 50,
        f"RELEVÉ ANNUEL — {client['nom']} {client['prenom']}",
        f"Adresse : {client['adresse']}",
        f"Date : {date.today().strftime('%d/%m/%Y')}",
        "=" * 50,
    ]


def formater_pied(total: float) -> list[str]:
    """Génère le pied de page commun à tout relevé."""
    return [
        "-" * 50,
        f"TOTAL : {total:.2f}€",
        "=" * 50,
    ]


def ligne_auto(contrat: dict) -> tuple[str, float]:
    prime = contrat["valeur_vehicule"] * 0.05
    description = f"Contrat {contrat['numero']} — Véhicule : {contrat['vehicule']} — Prime : {prime:.2f}€"
    return description, prime


def ligne_habitation(contrat: dict) -> tuple[str, float]:
    prime = contrat["surface_m2"] * 3.5
    description = f"Contrat {contrat['numero']} — Bien : {contrat['adresse_bien']} — Prime : {prime:.2f}€"
    return description, prime


def ligne_sante(contrat: dict) -> tuple[str, float]:
    prime = contrat["couverture"] * 0.08
    description = f"Contrat {contrat['numero']} — Niveau : {contrat['niveau']} — Prime : {prime:.2f}€"
    return description, prime


FORMATEURS_LIGNE = {
    "auto": ligne_auto,
    "habitation": ligne_habitation,
    "sante": ligne_sante,
}


def generer_releve(client: dict, type_contrat: str, contrats: list[dict]) -> str:
    """Génère un relevé annuel pour n'importe quel type de contrat."""
    formater_ligne = FORMATEURS_LIGNE[type_contrat]

    lignes = formater_en_tete(client)

    total = 0.0
    for contrat in contrats:
        description, prime = formater_ligne(contrat)
        total += prime
        lignes.append(f"  {description}")

    lignes.extend(formater_pied(total))
    return "\n".join(lignes)


# --- Vérification  ---
if __name__ == "__main__":
    client = {"nom": "Dupont", "prenom": "Marie", "adresse": "12 rue de Paris"}

    contrats_a = [
        {"numero": "A-001", "vehicule": "Renault Clio", "valeur_vehicule": 15_000},
        {"numero": "A-002", "vehicule": "Peugeot 308", "valeur_vehicule": 22_000},
    ]
    contrats_h = [
        {"numero": "H-001", "adresse_bien": "12 rue de Paris", "surface_m2": 65},
    ]
    contrats_s = [
        {"numero": "S-001", "niveau": "confort", "couverture": 5_000},
    ]

    print(generer_releve(client, "auto", contrats_a))
    print()
    print(generer_releve(client, "habitation", contrats_h))
    print()
    print(generer_releve(client, "sante", contrats_s))