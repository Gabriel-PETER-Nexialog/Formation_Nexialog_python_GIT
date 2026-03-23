"""Correction Exercice 2 — Factory : Création de notifications par canal """

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def envoyer(self, message: str) -> str:
        pass


class NotificationEmail(Notification):
    def __init__(self, destinataire: str):
        self.destinataire = destinataire

    def envoyer(self, message: str) -> str:
        return f"EMAIL à {self.destinataire} : {message}"


class NotificationSMS(Notification):
    def __init__(self, telephone: str):
        self.telephone = telephone

    def envoyer(self, message: str) -> str:
        return f"SMS à {self.telephone} : {message}"


class NotificationCourrier(Notification):
    def __init__(self, adresse: str):
        self.adresse = adresse

    def envoyer(self, message: str) -> str:
        return f"COURRIER à {self.adresse} : {message}"


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