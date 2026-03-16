"""Correction Exercice 2 — Singleton : Registre central des contrats (moyen)"""


class RegistreContrats:
    """Singleton — registre central de tous les contrats."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._contrats = {}
        return cls._instance

    def enregistrer(self, numero: str, contrat: dict) -> None:
        self._contrats[numero] = contrat

    def trouver(self, numero: str) -> dict | None:
        return self._contrats.get(numero)

    def tous(self) -> dict[str, dict]:
        return dict(self._contrats)

    def nombre(self) -> int:
        return len(self._contrats)


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