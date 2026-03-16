
db = None

class EmailManager:

    def send_confirm(self, to, subject, body):
        pass

class PdfManager:
    def create(self, titre, assure, prime):
        pass

class GestionContratAuto:
    def __init__(self, assure, vehicule, age_permis):
        self.assure = assure
        self.vehicule = vehicule
        self.age_permis = age_permis

    def calculer_prime(self) -> float:
        base = self.vehicule.valeur * 0.05
        if self.age_permis < 3:
            base *= 1.5
        return base

    def sauvegarder_en_base(self):
        # connexion directe à la BDD
        db.execute("INSERT INTO contrats ...", self.assure, self.vehicule)

    def envoyer_email_confirmation(self):
        EmailManager.send_confirm(to=self.assure.email,
                                  subject="Votre contrat auto",
                                  body=f"Prime : {self.calculer_prime()}€")

    def generer_pdf(self):
        PdfManager.create(titre="Contrat Auto",
                   assure=self.assure.nom,
                   prime=self.calculer_prime())
