"""Exercice 2 — Factory : Création de notifications par canal

Implémentez les classes NotificationEmail, NotificationSMS et NotificationCourrier.
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def envoyer(self, message: str) -> str:
        pass


# TODO : Implémentez les trois classes :
#
# class NotificationEmail(Notification):
#     __init__(self, destinataire: str)
#     envoyer(message) → "EMAIL à <destinataire> : <message>"
#
# class NotificationSMS(Notification):
#     __init__(self, telephone: str)
#     envoyer(message) → "SMS à <telephone> : <message>"
#
# class NotificationCourrier(Notification):
#     __init__(self, adresse: str)
#     envoyer(message) → "COURRIER à <adresse> : <message>"


class NotificationFactory:
    @staticmethod
    def creer(canal: str, **kwargs) -> Notification:
        if canal == "email":
            return NotificationEmail(kwargs["destinataire"])
        elif canal == "sms":
            return NotificationSMS(kwargs["telephone"])
        elif canal == "courrier":
            return NotificationCourrier(kwargs["adresse"])
        else:
            raise ValueError(f"Canal inconnu : {canal}")


# --- Vérification ---
if __name__ == "__main__":
    canaux = [
        ("email", {"destinataire": "marie@mail.fr"}),
        ("sms", {"telephone": "06 12 34 56 78"}),
        ("courrier", {"adresse": "12 rue de Paris, 75001"}),
    ]
    for canal, params in canaux:
        notif = NotificationFactory.creer(canal, **params)
        print(notif.envoyer("Votre sinistre a été traité."))