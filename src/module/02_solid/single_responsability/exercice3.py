import hashlib

db = None

class GestionClient:
    def __init__(self, client):
        self.client = client

    def mettre_a_jour_adresse(self, nouvelle_adresse: str):
        self.client.adresse = nouvelle_adresse
        db.execute("UPDATE clients SET adresse=?", nouvelle_adresse)

    def calculer_score_risque(self) -> int:
        score = 100
        score -= self.client.nb_sinistres * 15
        score -= max(0, (25 - self.client.age)) * 2
        return max(0, score)

    def authentifier(self, mot_de_passe: str) -> bool:
        hash_mdp = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        return hash_mdp == self.client.hash_mdp

    def generer_releve_annuel(self) -> str:
        contrats = db.query("SELECT * FROM contrats WHERE client_id=?")
        return f"Relevé {self.client.nom} — {len(contrats)} contrat(s)"
