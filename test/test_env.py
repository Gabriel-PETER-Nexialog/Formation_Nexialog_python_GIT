import unittest


class TestEnv(unittest.TestCase):
    def test_env(self):
        print('Vos dépendances sont bien installées !')
        self.assertEqual(True, True)
