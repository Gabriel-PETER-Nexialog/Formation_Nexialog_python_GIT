"""Exercice 3 — Principe DRY : Notifications de sinistres

"""


def notifier_sinistre_email(sinistre: dict) -> str:
    """Envoie une notification par e-mail pour un sinistre."""
    destinataire = sinistre["assure_email"]

    if sinistre["montant"] > 10_000:
        urgence = "URGENT"
    elif sinistre["montant"] > 5_000:
        urgence = "PRIORITAIRE"
    else:
        urgence = "NORMAL"

    remboursement = max(0, sinistre["montant"] - sinistre["franchise"])

    message = (
        f"[{urgence}] Sinistre n°{sinistre['numero']}\n"
        f"Type : {sinistre['type']}\n"
        f"Montant déclaré : {sinistre['montant']:.2f}€\n"
        f"Franchise : {sinistre['franchise']:.2f}€\n"
        f"Remboursement estimé : {remboursement:.2f}€"
    )
    return f"EMAIL à {destinataire} : {message}"


def notifier_sinistre_sms(sinistre: dict) -> str:
    """Envoie une notification par SMS pour un sinistre."""
    telephone = sinistre["assure_telephone"]

    if sinistre["montant"] > 10_000:
        urgence = "URGENT"
    elif sinistre["montant"] > 5_000:
        urgence = "PRIORITAIRE"
    else:
        urgence = "NORMAL"

    remboursement = max(0, sinistre["montant"] - sinistre["franchise"])

    message = (
        f"[{urgence}] Sinistre n°{sinistre['numero']}\n"
        f"Type : {sinistre['type']}\n"
        f"Montant déclaré : {sinistre['montant']:.2f}€\n"
        f"Franchise : {sinistre['franchise']:.2f}€\n"
        f"Remboursement estimé : {remboursement:.2f}€"
    )
    return f"SMS à {telephone} : {message}"


def notifier_sinistre_courrier(sinistre: dict) -> str:
    """Envoie une notification par courrier pour un sinistre."""
    adresse = sinistre["assure_adresse"]

    if sinistre["montant"] > 10_000:
        urgence = "URGENT"
    elif sinistre["montant"] > 5_000:
        urgence = "PRIORITAIRE"
    else:
        urgence = "NORMAL"

    remboursement = max(0, sinistre["montant"] - sinistre["franchise"])

    message = (
        f"[{urgence}] Sinistre n°{sinistre['numero']}\n"
        f"Type : {sinistre['type']}\n"
        f"Montant déclaré : {sinistre['montant']:.2f}€\n"
        f"Franchise : {sinistre['franchise']:.2f}€\n"
        f"Remboursement estimé : {remboursement:.2f}€"
    )
    return f"COURRIER à {adresse} : {message}"


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

    print(notifier_sinistre_email(sinistre))
    print()
    print(notifier_sinistre_sms(sinistre))
    print()
    print(notifier_sinistre_courrier(sinistre))