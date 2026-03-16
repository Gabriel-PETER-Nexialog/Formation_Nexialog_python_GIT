from abc import ABC, abstractmethod
from smtplib import SMTP

import sendgrid
import sms_gateway

smtp_client = SMTP()
smtp_client.starttls()

# Abstraction définie selon le besoin du module de haut niveau
class IServiceNotification(ABC):
    @abstractmethod
    def envoyer(self, destinataire: str, sujet: str, corps: str): pass


# Détails bas niveau : implémentent l'interface
class ServiceSMTP(IServiceNotification):
    def envoyer(self, destinataire: str, sujet: str, corps: str):
        smtp_client.sendmail(destinataire, sujet, corps)


class ServiceSendGrid(IServiceNotification):
    def envoyer(self, destinataire: str, sujet: str, corps: str):
        sendgrid.send(to=destinataire, subject=sujet, content=corps)


class ServiceSMS(IServiceNotification):
    def envoyer(self, destinataire: str, sujet: str, corps: str):
        sms_gateway.send(phone=destinataire, text=f"{sujet}: {corps}")


# Logique métier pure — ignorante du canal de notification
class GestionnaireSinistre:
    def __init__(self, notificateur: IServiceNotification):
        self.notificateur = notificateur

    def traiter_sinistre(self, sinistre):
        remboursement = max(0, sinistre.montant - 300)
        sinistre.statut = "traité"
        self.notificateur.envoyer(
            sinistre.assure.email,
            "Sinistre traité",
            f"Remboursement : {remboursement}€"
        )


# Production
gestionnaire = GestionnaireSinistre(ServiceSMTP())

