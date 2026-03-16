from abc import ABC, abstractmethod


db = None
mongo = None

#  Abstraction définie par le module de HAUT niveau
class IContratRepository(ABC):
    @abstractmethod
    def trouver_par_id(self, contrat_id: int): pass


# Détail bas niveau : implémente l'interface
class PostgresContratRepository(IContratRepository):
    def trouver_par_id(self, contrat_id: int):
        return db.query(f"SELECT * FROM contrats WHERE id={contrat_id}")


class MongoContratRepository(IContratRepository):
    def trouver_par_id(self, contrat_id: int):
        return mongo.find_one({"_id": contrat_id})


# Module haut niveau dépend de l'abstraction — injection via __init__
class ServiceTarification:
    def __init__(self, repo: IContratRepository):
        self.repo = repo  # ← la dépendance est injectée, pas construite

    def calculer_prime(self, contrat_id: int) -> float:
        contrat = self.repo.trouver_par_id(contrat_id)
        return contrat.valeur * 0.05


service_prod = ServiceTarification(PostgresContratRepository())

