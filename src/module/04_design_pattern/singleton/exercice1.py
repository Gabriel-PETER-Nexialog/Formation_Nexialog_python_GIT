"""Exercice 1 — Singleton : Configuration globale (facile)

Complétez la méthode __new__ pour que la classe ne crée qu'une seule instance.
"""


class ConfigurationAssurance:
    """Singleton pour la configuration globale de l'application."""
    _instance = None

    def __new__(cls):
        # TODO : si _instance est None, créer l'instance avec super().__new__(cls)
        #        et initialiser _parametres à un dict vide
        # TODO : retourner _instance
        pass

    def set(self, cle: str, valeur):
        self._parametres[cle] = valeur

    def get(self, cle: str, defaut=None):
        return self._parametres.get(cle, defaut)

    def get_all(self) -> dict:
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