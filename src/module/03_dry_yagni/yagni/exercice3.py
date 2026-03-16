"""Exercice 3 — Principe YAGNI : Le gestionnaire de clients sur-anticipé

"""

from abc import ABC, abstractmethod


class AbstractClientRepository(ABC):
    """Interface prévue pour supporter plusieurs backends de stockage."""

    @abstractmethod
    def ajouter(self, client: dict) -> None:
        pass

    @abstractmethod
    def trouver_par_id(self, client_id: int) -> dict | None:
        pass

    @abstractmethod
    def supprimer(self, client_id: int) -> None:
        pass

    @abstractmethod
    def rechercher(self, criteres: dict) -> list[dict]:
        """Recherche avancée multi-critères — prévue pour un futur back-office."""
        pass

    @abstractmethod
    def exporter_csv(self) -> str:
        """Export CSV — prévu pour un futur reporting."""
        pass

    @abstractmethod
    def synchroniser_crm(self) -> None:
        """Synchronisation CRM — prévue pour une future intégration Salesforce."""
        pass


class ClientRepositoryMemoire(AbstractClientRepository):
    """Implémentation en mémoire — la seule utilisée actuellement."""

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

    def rechercher(self, criteres: dict) -> list[dict]:
        """Implémentation complexe d'une recherche jamais utilisée."""
        resultats = []
        for client in self._clients.values():
            correspond = True
            for cle, valeur in criteres.items():
                if cle == "nom_contient":
                    if valeur.lower() not in client.get("nom", "").lower():
                        correspond = False
                elif cle == "age_min":
                    if client.get("age", 0) < valeur:
                        correspond = False
                elif cle == "age_max":
                    if client.get("age", 0) > valeur:
                        correspond = False
                elif cle == "ville":
                    if client.get("ville", "").lower() != valeur.lower():
                        correspond = False
                elif cle == "a_contrat_actif":
                    if client.get("contrat_actif") != valeur:
                        correspond = False
            if correspond:
                resultats.append(client)
        return resultats

    def exporter_csv(self) -> str:
        """Export CSV jamais appelé dans le code."""
        lignes = ["id,nom,prenom,age,ville"]
        for c in self._clients.values():
            lignes.append(f"{c['id']},{c.get('nom','')},{c.get('prenom','')},{c.get('age','')},{c.get('ville','')}")
        return "\n".join(lignes)

    def synchroniser_crm(self) -> None:
        """Synchronisation jamais appelée — le CRM n'existe pas encore."""
        raise NotImplementedError("Intégration CRM pas encore développée")


class ServiceGestionClient:
    """Service métier qui utilise le repository."""

    def __init__(self, repo: AbstractClientRepository):
        self.repo = repo

    def inscrire_client(self, nom: str, prenom: str, age: int) -> dict:
        client = {"nom": nom, "prenom": prenom, "age": age}
        self.repo.ajouter(client)
        return client

    def obtenir_client(self, client_id: int) -> dict | None:
        return self.repo.trouver_par_id(client_id)

    def resilier_client(self, client_id: int) -> None:
        self.repo.supprimer(client_id)


# --- Utilisation réelle dans le code métier ---
if __name__ == "__main__":
    repo = ClientRepositoryMemoire()
    service = ServiceGestionClient(repo)

    # Seules ces opérations sont réellement utilisées aujourd'hui
    client = service.inscrire_client("Dupont", "Marie", 35)
    print(f"Client inscrit : {client}")

    retrouve = service.obtenir_client(1)
    print(f"Client retrouvé : {retrouve}")

    service.resilier_client(1)
    print(f"Client après résiliation : {service.obtenir_client(1)}")