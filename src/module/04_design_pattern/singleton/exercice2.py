"""Exercice 2 — Singleton : Registre central des contrats (moyen)

Implémentez le pattern Singleton via __new__ et complétez les méthodes.
"""


class RegistreContrats:
    """Singleton — registre central de tous les contrats."""
    _instance = None

    def __new__(cls):
        # TODO : implémenter le Singleton
        pass

    def enregistrer(self, numero: str, contrat: dict) -> None:
        """Enregistre un contrat dans le registre."""
        # TODO
        pass

    def trouver(self, numero: str) -> dict | None:
        """Trouve un contrat par son numéro."""
        # TODO
        pass

    def tous(self) -> dict[str, dict]:
        """Retourne tous les contrats."""
        # TODO
        pass

    def nombre(self) -> int:
        """Retourne le nombre de contrats enregistrés."""
        # TODO
        pass


# --- Vérification ---
if __name__ == "__main__":
    registre1 = RegistreContrats()
    registre1.enregistrer("A-001", {"type": "auto", "prime": 1000})
    registre1.enregistrer("H-001", {"type": "habitation", "prime": 262.50})

    registre2 = RegistreContrats()
    registre2.enregistrer("S-001", {"type": "sante", "prime": 540})

    print(registre1 is registre2)           # True
    print(registre2.nombre())               # 3
    print(registre2.trouver("A-001"))       # {'type': 'auto', 'prime': 1000}
    print(registre1.trouver("S-001"))       # {'type': 'sante', 'prime': 540}