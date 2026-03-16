"""Correction Exercice 3 — Principe YAGNI : Le gestionnaire de clients sur-anticipé

On supprime l'interface abstraite inutile (un seul backend existe),
ainsi que les méthodes jamais utilisées (rechercher, exporter_csv,
synchroniser_crm). Le repository ne conserve que ajouter,
trouver_par_id et supprimer.
"""


class ClientRepository:
    """Repository simple en mémoire — le seul backend nécessaire aujourd'hui."""

    def __init__(self):
        self._clients: dict[int, dict] = {}
        self._prochain_id: int = 1

    def ajouter(self, client: dict) -> None:
        client["id"] = self._prochain_id
        self._clients[self._prochain_id] = client
        self._prochain_id += 1

    def trouver_par_id(self, client_id: int) -> dict | None:
        return self._clients.get(client_id)

    def supprimer(self, client_id: int) -> None:
        self._clients.pop(client_id, None)


class ServiceGestionClient:

    def __init__(self, repo: ClientRepository):
        self.repo = repo

    def inscrire_client(self, nom: str, prenom: str, age: int) -> dict:
        client = {"nom": nom, "prenom": prenom, "age": age}
        self.repo.ajouter(client)
        return client

    def obtenir_client(self, client_id: int) -> dict | None:
        return self.repo.trouver_par_id(client_id)

    def resilier_client(self, client_id: int) -> None:
        self.repo.supprimer(client_id)


# --- Utilisation ---
if __name__ == "__main__":
    repo = ClientRepository()
    service = ServiceGestionClient(repo)

    client = service.inscrire_client("Dupont", "Marie", 35)
    print(f"Client inscrit : {client}")

    retrouve = service.obtenir_client(1)
    print(f"Client retrouvé : {retrouve}")

    service.resilier_client(1)
    print(f"Client après résiliation : {service.obtenir_client(1)}")