"""Correction des tests — BDD : Service de souscription de contrats

Ces tests suivent l'approche BDD :
- Noms de tests en langage naturel (scénarios métier)
- Structure Given / When / Then
- Perspective utilisateur/métier
"""

import unittest
from datetime import date

from exercice1 import Client, ServiceSouscription


class TestEligibiliteSouscription(unittest.TestCase):
    """Scénarios d'éligibilité à la souscription."""

    def setUp(self):
        self.service = ServiceSouscription()

    def test_client_majeur_avec_papiers_valides_est_eligible(self):
        """Étant donné un client de 30 ans avec une pièce d'identité valide et sans impayés,
        quand on vérifie son éligibilité,
        alors il est éligible à la souscription."""
        # Given
        client = Client(nom="Dupont", age=30, piece_identite_valide=True, impayes=0)

        # When
        eligible = self.service.est_eligible(client)

        # Then
        self.assertTrue(eligible)

    def test_client_mineur_est_refuse(self):
        """Étant donné un client de 16 ans,
        quand on vérifie son éligibilité,
        alors il est refusé."""
        # Given
        client = Client(nom="Martin", age=16)

        # When
        eligible = self.service.est_eligible(client)

        # Then
        self.assertFalse(eligible)

    def test_client_sans_piece_identite_est_refuse(self):
        """Étant donné un client sans pièce d'identité valide,
        quand on vérifie son éligibilité,
        alors il est refusé."""
        # Given
        client = Client(nom="Durand", age=35, piece_identite_valide=False)

        # When / Then
        self.assertFalse(self.service.est_eligible(client))

    def test_client_avec_impayes_est_refuse(self):
        """Étant donné un client avec des cotisations impayées,
        quand on vérifie son éligibilité,
        alors il est refusé."""
        # Given
        client = Client(nom="Bernard", age=40, impayes=2)

        # When / Then
        self.assertFalse(self.service.est_eligible(client))

    def test_souscription_refusee_leve_une_erreur(self):
        """Étant donné un client mineur,
        quand on tente de souscrire un contrat,
        alors une ValueError est levée."""
        # Given
        client = Client(nom="Petit", age=15)

        # When / Then
        with self.assertRaises(ValueError):
            self.service.souscrire(client, "auto", 2026, valeur_vehicule=20_000)


class TestCalculPrime(unittest.TestCase):
    """Scénarios de calcul de prime."""

    def setUp(self):
        self.service = ServiceSouscription()

    def test_prime_auto_est_5_pourcent_de_la_valeur_vehicule(self):
        """Étant donné un contrat auto pour un véhicule à 20 000€,
        quand on calcule la prime,
        alors elle est de 1 000€."""
        # Given
        valeur_vehicule = 20_000

        # When
        prime = self.service.calculer_prime("auto", valeur_vehicule=valeur_vehicule)

        # Then
        self.assertEqual(prime, 1_000.0)

    def test_prime_habitation_est_3_5_par_m2(self):
        """Étant donné un contrat habitation pour 75 m²,
        quand on calcule la prime,
        alors elle est de 262.50€."""
        # Given / When
        prime = self.service.calculer_prime("habitation", surface_m2=75)

        # Then
        self.assertEqual(prime, 262.50)

    def test_prime_sante_est_12_fois_age(self):
        """Étant donné un contrat santé pour un assuré de 45 ans,
        quand on calcule la prime,
        alors elle est de 540€."""
        # Given / When
        prime = self.service.calculer_prime("sante", age=45)

        # Then
        self.assertEqual(prime, 540.0)

    def test_type_contrat_inconnu_leve_une_erreur(self):
        """Étant donné un type de contrat inconnu,
        quand on calcule la prime,
        alors une ValueError est levée."""
        # When / Then
        with self.assertRaises(ValueError):
            self.service.calculer_prime("voyage")


class TestRemiseFidelite(unittest.TestCase):
    """Scénarios de remise fidélité."""

    def setUp(self):
        self.service = ServiceSouscription()

    def test_client_fidele_obtient_10_pourcent_de_reduction(self):
        """Étant donné un client avec 7 ans d'ancienneté et une prime de 1000€,
        quand on applique la remise fidélité,
        alors la prime est réduite à 900€."""
        # Given
        client = Client(nom="Dupont", age=35, anciennete_ans=7)
        prime_base = 1_000.0

        # When
        prime_finale = self.service.appliquer_remise_fidelite(prime_base, client)

        # Then
        self.assertEqual(prime_finale, 900.0)

    def test_client_recent_ne_beneficie_pas_de_remise(self):
        """Étant donné un client avec 2 ans d'ancienneté,
        quand on applique la remise fidélité,
        alors la prime reste inchangée."""
        # Given
        client = Client(nom="Martin", age=28, anciennete_ans=2)
        prime_base = 1_000.0

        # When
        prime_finale = self.service.appliquer_remise_fidelite(prime_base, client)

        # Then
        self.assertEqual(prime_finale, 1_000.0)

    def test_client_exactement_5_ans_obtient_la_remise(self):
        """Étant donné un client avec exactement 5 ans d'ancienneté,
        quand on applique la remise fidélité,
        alors la prime est réduite de 10%."""
        # Given
        client = Client(nom="Durand", age=40, anciennete_ans=5)
        prime_base = 500.0

        # When
        prime_finale = self.service.appliquer_remise_fidelite(prime_base, client)

        # Then
        self.assertEqual(prime_finale, 450.0)


class TestNumerotationContrat(unittest.TestCase):
    """Scénarios de génération de numéros de contrat."""

    def setUp(self):
        self.service = ServiceSouscription()

    def test_numero_contrat_auto_suit_le_format_attendu(self):
        """Étant donné une souscription auto en 2026,
        quand on génère le numéro de contrat,
        alors il est au format AUTO-2026-001."""
        # When
        numero = self.service.generer_numero("auto", 2026)

        # Then
        self.assertEqual(numero, "AUTO-2026-001")

    def test_numero_contrat_habitation_suit_le_format_attendu(self):
        """Étant donné une souscription habitation en 2026,
        quand on génère le numéro,
        alors il est au format HABITATION-2026-001."""
        # When
        numero = self.service.generer_numero("habitation", 2026)

        # Then
        self.assertEqual(numero, "HABITATION-2026-001")

    def test_numeros_successifs_sont_incrementes(self):
        """Étant donné deux souscriptions successives,
        quand on génère les numéros,
        alors le compteur s'incrémente."""
        # When
        numero1 = self.service.generer_numero("auto", 2026)
        numero2 = self.service.generer_numero("auto", 2026)

        # Then
        self.assertEqual(numero1, "AUTO-2026-001")
        self.assertEqual(numero2, "AUTO-2026-002")


class TestSouscriptionComplete(unittest.TestCase):
    """Scénarios de souscription complète (parcours de bout en bout)."""

    def setUp(self):
        self.service = ServiceSouscription()

    def test_souscription_auto_complete_avec_remise(self):
        """Étant donné un client fidèle éligible et un véhicule à 20 000€,
        quand il souscrit un contrat auto,
        alors le contrat est créé avec la prime remisée."""
        # Given
        client = Client(nom="Dupont", age=35, anciennete_ans=7)

        # When
        contrat = self.service.souscrire(
            client, "auto", 2026, valeur_vehicule=20_000
        )

        # Then
        self.assertEqual(contrat["numero"], "AUTO-2026-001")
        self.assertEqual(contrat["client"], "Dupont")
        self.assertEqual(contrat["type"], "auto")
        self.assertEqual(contrat["prime"], 900.0)  # 1000 * 0.90

    def test_souscription_sans_remise(self):
        """Étant donné un nouveau client éligible et un véhicule à 20 000€,
        quand il souscrit un contrat auto,
        alors la prime est sans remise."""
        # Given
        client = Client(nom="Martin", age=28, anciennete_ans=1)

        # When
        contrat = self.service.souscrire(
            client, "auto", 2026, valeur_vehicule=20_000
        )

        # Then
        self.assertEqual(contrat["prime"], 1_000.0)


if __name__ == "__main__":
    unittest.main()