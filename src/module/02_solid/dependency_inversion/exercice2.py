from smtplib import SMTP

smtp_client = SMTP()
smtp_client.starttls()

class ServiceSMTP:
    def envoyer(self, destinataire: str, sujet: str, corps: str):
        # envoi via serveur SMTP interne
        smtp_client.sendmail(destinataire, sujet, corps)


class GestionnaireSinistre:
    def __init__(self):
        #  Instancie directement le détail technique
        self.notifier = ServiceSMTP()

    def traiter_sinistre(self, sinistre):
        remboursement = max(0, sinistre.montant - 300)
        sinistre.statut = "traité"
        # Couplé à SMTP — aucune flexibilité
        self.notifier.envoyer(
            sinistre.assure.email,
            "Sinistre traité",
            f"Remboursement : {remboursement}€"
        )