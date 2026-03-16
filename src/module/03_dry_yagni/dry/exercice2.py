"""Exercice 2 — Principe DRY : Génération de relevés clients

"""

from datetime import date


def generer_releve_auto(client: dict, contrats_auto: list[dict]) -> str:
    """Génère un relevé annuel pour les contrats auto d'un client."""
    lignes = []
    lignes.append("=" * 50)
    lignes.append(f"RELEVÉ ANNUEL — {client['nom']} {client['prenom']}")
    lignes.append(f"Adresse : {client['adresse']}")
    lignes.append(f"Date : {date.today().strftime('%d/%m/%Y')}")
    lignes.append("=" * 50)

    total = 0.0
    for contrat in contrats_auto:
        prime = contrat["valeur_vehicule"] * 0.05
        total += prime
        lignes.append(f"  Contrat {contrat['numero']} — Véhicule : {contrat['vehicule']} — Prime : {prime:.2f}€")

    lignes.append("-" * 50)
    lignes.append(f"TOTAL : {total:.2f}€")
    lignes.append("=" * 50)
    return "\n".join(lignes)


def generer_releve_habitation(client: dict, contrats_habitation: list[dict]) -> str:
    """Génère un relevé annuel pour les contrats habitation d'un client."""
    lignes = []
    lignes.append("=" * 50)
    lignes.append(f"RELEVÉ ANNUEL — {client['nom']} {client['prenom']}")
    lignes.append(f"Adresse : {client['adresse']}")
    lignes.append(f"Date : {date.today().strftime('%d/%m/%Y')}")
    lignes.append("=" * 50)

    total = 0.0
    for contrat in contrats_habitation:
        prime = contrat["surface_m2"] * 3.5
        total += prime
        lignes.append(f"  Contrat {contrat['numero']} — Bien : {contrat['adresse_bien']} — Prime : {prime:.2f}€")

    lignes.append("-" * 50)
    lignes.append(f"TOTAL : {total:.2f}€")
    lignes.append("=" * 50)
    return "\n".join(lignes)


def generer_releve_sante(client: dict, contrats_sante: list[dict]) -> str:
    """Génère un relevé annuel pour les contrats santé d'un client."""
    lignes = []
    lignes.append("=" * 50)
    lignes.append(f"RELEVÉ ANNUEL — {client['nom']} {client['prenom']}")
    lignes.append(f"Adresse : {client['adresse']}")
    lignes.append(f"Date : {date.today().strftime('%d/%m/%Y')}")
    lignes.append("=" * 50)

    total = 0.0
    for contrat in contrats_sante:
        prime = contrat["couverture"] * 0.08
        total += prime
        lignes.append(f"  Contrat {contrat['numero']} — Niveau : {contrat['niveau']} — Prime : {prime:.2f}€")

    lignes.append("-" * 50)
    lignes.append(f"TOTAL : {total:.2f}€")
    lignes.append("=" * 50)
    return "\n".join(lignes)


# --- Vérification rapide ---
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

    print(generer_releve_auto(client, contrats_a))
    print()
    print(generer_releve_habitation(client, contrats_h))
    print()
    print(generer_releve_sante(client, contrats_s))