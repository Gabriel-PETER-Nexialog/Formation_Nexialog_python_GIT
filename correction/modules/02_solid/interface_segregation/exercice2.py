from abc import ABC, abstractmethod

# Une interface par canal — indépendantes et combinables
class INotificationEmail(ABC):
    @abstractmethod
    def envoyer_email(self, destinataire: str, message: str): pass

class INotificationSMS(ABC):
    @abstractmethod
    def envoyer_sms(self, telephone: str, message: str): pass

class INotificationCourrier(ABC):
    @abstractmethod
    def envoyer_courrier(self, adresse: str, contenu: str): pass


# Chaque service n'implémente que son canal
class ServiceSMSAssurance(INotificationSMS):
    def envoyer_sms(self, telephone: str, message: str):
        print(f"SMS → {telephone} : {message}")


class ServiceEmailAssurance(INotificationEmail):
    def envoyer_email(self, destinataire: str, message: str):
        print(f"Email → {destinataire} : {message}")


# Un service multicanal combine librement ce dont il a besoin
class ServiceNotificationComplet(
    INotificationEmail, INotificationSMS, INotificationCourrier
):
    def envoyer_email(self, destinataire: str, message: str):
        print(f"Email → {destinataire} : {message}")

    def envoyer_sms(self, telephone: str, message: str):
        print(f"SMS → {telephone} : {message}")

    def envoyer_courrier(self, adresse: str, contenu: str):
        print(f"Courrier → {adresse}")


# Les fonctions exigent uniquement ce qu'elles utilisent vraiment
def alerter_sinistre_sms(service: INotificationSMS, tel: str):
    service.envoyer_sms(tel, "Votre sinistre a été enregistré.")