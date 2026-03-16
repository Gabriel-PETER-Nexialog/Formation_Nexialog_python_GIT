from abc import ABC, abstractmethod

class INotification(ABC):
    # Tous les canaux regroupés dans une seule interface
    @abstractmethod
    def envoyer_email(self, destinataire: str, message: str): pass
    @abstractmethod
    def envoyer_sms(self, telephone: str, message: str): pass
    @abstractmethod
    def envoyer_courrier(self, adresse: str, contenu: str): pass


class ServiceSMSAssurance(INotification):
    def envoyer_sms(self, telephone: str, message: str):
        print(f"SMS → {telephone} : {message}")

    def envoyer_email(self, destinataire: str, message: str):
        # Méthode vide imposée par l'interface
        pass

    def envoyer_courrier(self, adresse: str, contenu: str):
        # Idem — pollution de l'implémentation
        pass