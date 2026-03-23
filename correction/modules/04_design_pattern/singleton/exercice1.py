"""Correction Exercice 1 — Singleton : Configuration globale """


class ConfigurationAssurance:
    """Singleton pour la configuration globale de l'application."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._parametres = {}
        return cls._instance

    def set(self, cle: str, valeur):
        self._parametres[cle] = valeur

    def get(self, cle: str, defaut=None):
        return self._parametres.get(cle, defaut)

    def tous(self) -> dict:
        return dict(self._parametres)


# --- Vérification ---
if __name__ == "__main__":
    config1 = ConfigurationAssurance()
    config1.set("franchise_defaut", 300)
    config1.set("tva", 0.20)

    config2 = ConfigurationAssurance()
    print(config2.get("franchise_defaut"))  # 300
    print(config2.get("tva"))               # 0.2
    print(config1 is config2)               # True