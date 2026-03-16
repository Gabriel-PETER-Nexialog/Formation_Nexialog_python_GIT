

db = None;

class EmailManager:

    def send_confirm(self, to, subject, body):
        pass

class PdfManager:
    def create(self, titre, assure, prime):
        pass

class ContratAuto:
    """Responsabilité : modéliser et calculer la prime."""
    def __init__(self, assure, vehicule, age_permis):
        self.assure     = assure
        self.vehicule   = vehicule
        self.age_permis = age_permis

    def calculer_prime(self) -> float:
        base = self.vehicule.valeur * 0.05
        if self.age_permis < 3:
            base *= 1.5
        return base


class ContratRepository:
    """Responsabilité : persister les contrats."""
    def sauvegarder(self, contrat: ContratAuto):
        db.execute("INSERT INTO contrats ...",
                   contrat.assure, contrat.vehicule)


class NotificationService:
    """Responsabilité : envoyer des notifications."""
    def envoyer_confirmation(self, contrat: ContratAuto):
        EmailManager.send_confirm(to=contrat.assure.email,
                  subject="Votre contrat auto",
                  body=f"Prime : {contrat.calculer_prime()}€")


class ContratPdfGenerator:
    """Responsabilité : générer les documents PDF."""
    def generer(self, contrat: ContratAuto):
        PdfManager.create(titre="Contrat Auto",
                   assure=contrat.assure.nom,
                   prime=contrat.calculer_prime())