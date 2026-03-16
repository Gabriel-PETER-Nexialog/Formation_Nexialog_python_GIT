"""Exercice 3 — Singleton : Gestionnaire de connexion unique (difficile)

Créez entièrement la classe ConnexionTarification en tant que Singleton.
"""

# TODO : Créez la classe ConnexionTarification (Singleton)
#   Attributs : url (str), jeton (str), requetes_effectuees (int)
#   Méthodes :
#     - configurer(url: str, jeton: str)
#     - appeler(endpoint: str, params: dict) -> str
#     - stats() -> str


# --- Vérification ---
if __name__ == "__main__":
    conn1 = ConnexionTarification()
    conn1.configurer("https://api.tarification.fr", "token-xyz-123")

    print(conn1.appeler("prime/auto", {"valeur": 20000}))
    # GET https://api.tarification.fr/prime/auto — params: {'valeur': 20000}

    print(conn1.appeler("prime/habitation", {"surface": 75}))
    # GET https://api.tarification.fr/prime/habitation — params: {'surface': 75}

    conn2 = ConnexionTarification()
    print(conn1 is conn2)     # True
    print(conn2.stats())      # 2 requête(s) effectuée(s)