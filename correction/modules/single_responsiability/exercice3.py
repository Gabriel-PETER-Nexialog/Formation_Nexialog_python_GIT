import hashlib

db = None

class ClientRepository:
    """Responsabilité : persistance des données client."""
    def mettre_a_jour_adresse(self, client, nouvelle_adresse: str):
        client.adresse = nouvelle_adresse
        db.execute("UPDATE clients SET adresse=?", nouvelle_adresse)


class ScoringRisque:
    """Responsabilité : évaluer le profil de risque d'un client."""
    def calculer_score(self, client) -> int:
        score = 100
        score -= client.nb_sinistres * 15
        score -= max(0, (25 - client.age)) * 2
        return max(0, score)


class AuthService:
    """Responsabilité : authentification et sécurité."""
    def authentifier(self, client, mot_de_passe: str) -> bool:
        hash_mdp = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        return hash_mdp == client.hash_mdp


class RelevéService:
    """Responsabilité : génération des documents de reporting."""
    def generer_releve_annuel(self, client) -> str:
        contrats = db.query("SELECT * FROM contrats WHERE client_id=?")
        return f"Relevé {client.nom} — {len(contrats)} contrat(s)"