"""Exercice 3 — Factory : Création de calculateurs de remise (difficile)

Créez entièrement les classes Remise, RemiseFidelite, RemiseMultiContrats,
RemiseParrainage et RemiseFactory.
"""

# TODO : Créez la classe abstraite Remise (ABC)
#   - calculer(client: dict) -> float   (taux de remise)
#   - nom() -> str                       (nom de la remise)

# TODO : Créez RemiseFidelite(Remise)
#   - calculer : 0.10 si client["anciennete_ans"] >= 5, sinon 0.0
#   - nom : "Fidélité"

# TODO : Créez RemiseMultiContrats(Remise)
#   - calculer : 0.08 si len(client["contrats"]) >= 3, sinon 0.0
#   - nom : "Multi-contrats"

# TODO : Créez RemiseParrainage(Remise)
#   - calculer : 0.05 si client["a_parraine"] est True, sinon 0.0
#   - nom : "Parrainage"

# TODO : Créez RemiseFactory
#   - creer(type_remise: str) -> Remise


# --- Vérification ---
if __name__ == "__main__":
    client = {
        "nom": "Dupont",
        "anciennete_ans": 7,
        "contrats": ["auto", "habitation", "sante"],
        "a_parraine": True,
    }

    for type_r in ["fidelite", "multi_contrats", "parrainage"]:
        remise = RemiseFactory.creer(type_r)
        taux = remise.calculer(client)
        print(f"Remise {remise.nom()} : {taux * 100:.0f}%")