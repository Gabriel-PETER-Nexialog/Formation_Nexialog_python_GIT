"""Exercice 2 — Principe YAGNI : Le modèle de sinistre surchargé

"""

from datetime import date, datetime


class Sinistre:
    """Modèle de sinistre avec de nombreux attributs et méthodes anticipés."""

    def __init__(
        self,
        numero: str,
        type_sinistre: str,
        montant: float,
        franchise: float,
        date_evenement: date,
        date_declaration: date,
        # --- Attributs anticipés jamais utilisés ---
        coordonnees_gps: tuple[float, float] | None = None,
        photos: list[str] | None = None,
        temoin_principal: dict | None = None,
        niveau_priorite: int = 0,
        tags: list[str] | None = None,
        canal_declaration: str = "agence",
        historique_modifications: list[dict] | None = None,
    ):
        self.numero = numero
        self.type_sinistre = type_sinistre
        self.montant = montant
        self.franchise = franchise
        self.date_evenement = date_evenement
        self.date_declaration = date_declaration
        self.coordonnees_gps = coordonnees_gps
        self.photos = photos or []
        self.temoin_principal = temoin_principal
        self.niveau_priorite = niveau_priorite
        self.tags = tags or []
        self.canal_declaration = canal_declaration
        self.historique_modifications = historique_modifications or []

    def calculer_remboursement(self) -> float:
        """Calcul utilisé en production."""
        return max(0.0, self.montant - self.franchise)

    def est_recevable(self) -> bool:
        """Vérification utilisée en production."""
        delai = (self.date_declaration - self.date_evenement).days
        return delai <= 5

    # --- Méthodes anticipées jamais appelées dans le code ---

    def ajouter_photo(self, chemin: str) -> None:
        """Prévu pour un futur module de gestion de photos."""
        self.photos.append(chemin)

    def geolocaliser(self) -> str:
        """Prévu pour un futur affichage cartographique."""
        if self.coordonnees_gps:
            lat, lon = self.coordonnees_gps
            return f"https://maps.example.com/?lat={lat}&lon={lon}"
        return "Coordonnées non disponibles"

    def ajouter_tag(self, tag: str) -> None:
        """Prévu pour un futur système de classification."""
        if tag not in self.tags:
            self.tags.append(tag)

    def historiser_modification(self, champ: str, ancienne_valeur, nouvelle_valeur) -> None:
        """Prévu pour un futur audit trail."""
        self.historique_modifications.append({
            "date": datetime.now().isoformat(),
            "champ": champ,
            "ancien": ancienne_valeur,
            "nouveau": nouvelle_valeur,
        })

    def exporter_json(self) -> dict:
        """Prévu pour une future API REST."""
        return {
            "numero": self.numero,
            "type": self.type_sinistre,
            "montant": self.montant,
            "franchise": self.franchise,
            "date_evenement": self.date_evenement.isoformat(),
            "date_declaration": self.date_declaration.isoformat(),
            "gps": self.coordonnees_gps,
            "photos": self.photos,
            "temoin": self.temoin_principal,
            "priorite": self.niveau_priorite,
            "tags": self.tags,
            "canal": self.canal_declaration,
        }

    def calculer_score_fraude(self) -> float:
        """Prévu pour un futur module anti-fraude."""
        score = 0.0
        if self.montant > 10_000:
            score += 30
        if (self.date_declaration - self.date_evenement).days == 0:
            score += 20
        if not self.temoin_principal:
            score += 10
        return score


# --- Utilisation réelle dans le code métier ---
if __name__ == "__main__":
    sinistre = Sinistre(
        numero="SIN-2024-042",
        type_sinistre="dégât des eaux",
        montant=8_500.0,
        franchise=300.0,
        date_evenement=date(2024, 3, 10),
        date_declaration=date(2024, 3, 12),
    )

    # Seules ces deux méthodes sont réellement utilisées aujourd'hui
    print(f"Recevable : {sinistre.est_recevable()}")          # True
    print(f"Remboursement : {sinistre.calculer_remboursement():.2f}€")  # 8200.00€