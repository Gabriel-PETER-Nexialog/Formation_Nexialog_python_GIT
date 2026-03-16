import unittest


def my_function():
    return 1


class TestExercice2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Activer avant le lancement des tests
        Préparation Contextuel de tout les testes
         Exemple :
         - ouverture de fichier
         - Variable global à chaque tests
         """
        print("Setting up")

    @classmethod
    def tearDownClass(cls):
        """ Activer après le lancer des tests
        Cas d'utilisation :
            - fermuture de fichier
        """
        print("Tearing down")
    
    def test_exercice2(self):
        """ Voici un exemple de test"""
        #Given Préparation du tests
        expected_value = 1
        
        #When Fait l'action qu'on veut tester
        actual_value = my_function()
        
        #Then Tester 
        self.assertEqual(actual_value, expected_value)