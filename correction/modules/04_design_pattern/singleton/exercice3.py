"""Correction Exercice 3 — Singleton : Gestionnaire de connexion unique """


class ConnexionTarification:
    """Singleton — connexion unique au service de tarification."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.url = ""
            cls._instance.jeton = ""
            cls._instance.requetes_effectuees = 0
        return cls._instance

    def configurer(self, url: str, jeton: str):
        self.url = url
        self.jeton = jeton

    def appeler(self, endpoint: str, params: dict) -> str:
        self.requetes_effectuees += 1
        return f"GET {self.url}/{endpoint} — params: {params}"

    def stats(self) -> str:
        return f"{self.requetes_effectuees} requête(s) effectuée(s)"


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