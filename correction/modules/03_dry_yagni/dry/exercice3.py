"""Correction Exercice 3 — Principe DRY : Notifications de sinistres

Le niveau d'urgence, le calcul du remboursement et le formatage du
message sont factorisés. L'envoi se résume à choisir le canal
(email, SMS, courrier) et le destinataire associé.
"""


def niveau_urgence(montant: float) -> str:
    """Détermine le niveau d'urgence selon le montant du sinistre."""
    if montant > 10_000:
        return "URGENT"
    elif montant > 5_000:
        return "PRIORITAIRE"
    return "NORMAL"


def formater_message_sinistre(sinistre: dict) -> str:
    """Formate le contenu commun d'une notification de sinistre."""
    urgence = niveau_urgence(sinistre["montant"])
    remboursement = max(0, sinistre["montant"] - sinistre["franchise"])

    return (
        f"[{urgence}] Sinistre n°{sinistre['numero']}\n"
        f"Type : {sinistre['type']}\n"
        f"Montant déclaré : {sinistre['montant']:.2f}€\n"
        f"Franchise : {sinistre['franchise']:.2f}€\n"
        f"Remboursement estimé : {remboursement:.2f}€"
    )


CANAUX = {
    "email": ("EMAIL", "assure_email"),
    "sms": ("SMS", "assure_telephone"),
    "courrier": ("COURRIER", "assure_adresse"),
}


def notifier_sinistre(sinistre: dict, canal: str) -> str:
    """Envoie une notification pour un sinistre via le canal choisi."""
    label, cle_destinataire = CANAUX[canal]
    destinataire = sinistre[cle_destinataire]
    message = formater_message_sinistre(sinistre)
    return f"{label} à {destinataire} : {message}"


# --- Vérification rapide ---
if __name__ == "__main__":
    sinistre = {
        "numero": "SIN-2024-042",
        "type": "dégât des eaux",
        "montant": 8_500.0,
        "franchise": 300.0,
        "assure_email": "marie.dupont@mail.fr",
        "assure_telephone": "06 12 34 56 78",
        "assure_adresse": "12 rue de Paris, 75001 Paris",
    }

    print(notifier_sinistre(sinistre, "email"))
    print()
    print(notifier_sinistre(sinistre, "sms"))
    print()
    print(notifier_sinistre(sinistre, "courrier"))