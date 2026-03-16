"""Correction Exercice 1 — Principe YAGNI : Le service de tarification sur-ingéniéré

On supprime la classe abstraite et toutes les méthodes non utilisées
(conversion de devise, paiement mensuel/trimestriel, taxes régionales).
Il ne reste que ce dont le code a réellement besoin aujourd'hui :
calculer une prime et appliquer une remise.
"""


class TarificationAuto:

    def calculer_prime(self, contrat: dict) -> float:
        return contrat["valeur_vehicule"] * 0.05

    def appliquer_remise(self, prime: float, client: dict) -> float:
        if client.get("anciennete_ans", 0) >= 5:
            return prime * 0.90
        return prime


# --- Utilisation ---
if __name__ == "__main__":
    tarification = TarificationAuto()

    contrat = {"valeur_vehicule": 20_000}
    client = {"nom": "Dupont", "anciennete_ans": 6}

    prime = tarification.calculer_prime(contrat)
    prime_finale = tarification.appliquer_remise(prime, client)

    print(f"Prime annuelle : {prime_finale:.2f}€")  # 900.0€