

db = None

class PostgresContratRepository:
    def trouver_par_id(self, contrat_id: int):
        # connexion directe à PostgreSQL
        return db.query(f"SELECT * FROM contrats WHERE id={contrat_id}")


class ServiceTarification:
    def __init__(self):
        # Dépend d'un détail concret instancié ici même
        self.repo = PostgresContratRepository()

    def calculer_prime(self, contrat_id: int) -> float:
        contrat = self.repo.trouver_par_id(contrat_id)
        return contrat.valeur * 0.05

