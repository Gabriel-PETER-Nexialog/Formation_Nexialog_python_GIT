"""Correction des tests — TDD : Service de gestion de sinistres

Ces tests suivent le cycle TDD :
- Chaque test vérifie un comportement précis
- Structure Given / When / Then
"""

import unittest
from datetime import date

from exercice1 import Sinistre, ServiceSinistre


class TestSinistreRecevabilite(unittest.TestCase):
    """Tests de recevabilité d'un sinistre."""

    def test_sinistre_recevable_dans_les_5_jours(self):
        """Étant donné un sinistre déclaré 3 jours après l'événement,
        quand on vérifie la recevabilité, alors il est recevable."""
        # Given
        sinistre = Sinistre(
            numero="SIN-001",
            type_sinistre="dégât des eaux",
            montant=5_000,
            franchise=300,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 13),
        )

        # When
        recevable = sinistre.est_recevable()

        # Then
        self.assertTrue(recevable)

    def test_sinistre_recevable_le_jour_meme(self):
        """Étant donné un sinistre déclaré le jour même,
        quand on vérifie la recevabilité, alors il est recevable."""
        # Given
        sinistre = Sinistre(
            numero="SIN-002",
            type_sinistre="vol",
            montant=3_000,
            franchise=200,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 10),
        )

        # When / Then
        self.assertTrue(sinistre.est_recevable())

    def test_sinistre_recevable_exactement_5_jours(self):
        """Étant donné un sinistre déclaré exactement 5 jours après,
        quand on vérifie la recevabilité, alors il est recevable."""
        # Given
        sinistre = Sinistre(
            numero="SIN-003",
            type_sinistre="incendie",
            montant=20_000,
            franchise=500,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 15),
        )

        # When / Then
        self.assertTrue(sinistre.est_recevable())

    def test_sinistre_non_recevable_apres_5_jours(self):
        """Étant donné un sinistre déclaré 6 jours après l'événement,
        quand on vérifie la recevabilité, alors il est non recevable."""
        # Given
        sinistre = Sinistre(
            numero="SIN-004",
            type_sinistre="bris de glace",
            montant=800,
            franchise=100,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 16),
        )

        # When
        recevable = sinistre.est_recevable()

        # Then
        self.assertFalse(recevable)


class TestSinistreRemboursement(unittest.TestCase):
    """Tests de calcul du remboursement."""

    def test_remboursement_standard(self):
        """Étant donné un sinistre de 5000€ avec 300€ de franchise,
        quand on calcule le remboursement, alors il est de 4700€."""
        # Given
        sinistre = Sinistre(
            numero="SIN-005",
            type_sinistre="dégât des eaux",
            montant=5_000,
            franchise=300,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 11),
        )

        # When
        remboursement = sinistre.calculer_remboursement()

        # Then
        self.assertEqual(remboursement, 4_700.0)

    def test_remboursement_zero_si_franchise_superieure(self):
        """Étant donné un sinistre de 200€ avec 300€ de franchise,
        quand on calcule le remboursement, alors il est de 0€."""
        # Given
        sinistre = Sinistre(
            numero="SIN-006",
            type_sinistre="bris de glace",
            montant=200,
            franchise=300,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 10),
        )

        # When
        remboursement = sinistre.calculer_remboursement()

        # Then
        self.assertEqual(remboursement, 0.0)

    def test_remboursement_zero_si_franchise_egale_montant(self):
        """Étant donné un sinistre dont la franchise égale le montant,
        quand on calcule le remboursement, alors il est de 0€."""
        # Given
        sinistre = Sinistre(
            numero="SIN-007",
            type_sinistre="vol",
            montant=500,
            franchise=500,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 10),
        )

        # When / Then
        self.assertEqual(sinistre.calculer_remboursement(), 0.0)


class TestServiceSinistre(unittest.TestCase):
    """Tests du service de gestion des sinistres."""

    def test_remboursement_plafonne(self):
        """Étant donné un sinistre de 20000€ avec 300€ de franchise et un plafond de 10000€,
        quand on calcule le remboursement plafonné, alors il est de 10000€."""
        # Given
        sinistre = Sinistre(
            numero="SIN-008",
            type_sinistre="incendie",
            montant=20_000,
            franchise=300,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 11),
        )
        service = ServiceSinistre(plafond=10_000)

        # When
        remboursement = service.remboursement_plafonne(sinistre)

        # Then
        self.assertEqual(remboursement, 10_000.0)

    def test_remboursement_sous_le_plafond(self):
        """Étant donné un sinistre dont le remboursement est sous le plafond,
        quand on calcule, alors le remboursement normal est retourné."""
        # Given
        sinistre = Sinistre(
            numero="SIN-009",
            type_sinistre="dégât des eaux",
            montant=3_000,
            franchise=300,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 11),
        )
        service = ServiceSinistre(plafond=10_000)

        # When
        remboursement = service.remboursement_plafonne(sinistre)

        # Then
        self.assertEqual(remboursement, 2_700.0)

    def test_sinistre_suspect_montant_eleve_et_declaration_immediate(self):
        """Étant donné un sinistre de 20000€ déclaré le jour même,
        quand on vérifie s'il est suspect, alors il l'est."""
        # Given
        sinistre = Sinistre(
            numero="SIN-010",
            type_sinistre="vol",
            montant=20_000,
            franchise=500,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 10),
        )
        service = ServiceSinistre(plafond=50_000)

        # When
        suspect = service.est_suspect(sinistre)

        # Then
        self.assertTrue(suspect)

    def test_sinistre_non_suspect_montant_faible(self):
        """Étant donné un sinistre de 5000€ déclaré le jour même,
        quand on vérifie s'il est suspect, alors il ne l'est pas."""
        # Given
        sinistre = Sinistre(
            numero="SIN-011",
            type_sinistre="bris de glace",
            montant=5_000,
            franchise=200,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 10),
        )
        service = ServiceSinistre(plafond=50_000)

        # When / Then
        self.assertFalse(service.est_suspect(sinistre))

    def test_sinistre_non_suspect_declaration_differee(self):
        """Étant donné un sinistre de 20000€ déclaré 2 jours après,
        quand on vérifie s'il est suspect, alors il ne l'est pas."""
        # Given
        sinistre = Sinistre(
            numero="SIN-012",
            type_sinistre="incendie",
            montant=20_000,
            franchise=500,
            date_evenement=date(2026, 3, 10),
            date_declaration=date(2026, 3, 12),
        )
        service = ServiceSinistre(plafond=50_000)

        # When / Then
        self.assertFalse(service.est_suspect(sinistre))


if __name__ == "__main__":
    unittest.main()