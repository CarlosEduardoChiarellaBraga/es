import unittest
import autenticador
import databaseManager

class TestAutenticador(unittest.TestCase):
    def testAuthenticate(self):
        """Testa se a senha certa autentica o usuário. Garantir que o databaseManager.populateDatabase() gera o username_1 com senha 1234"""
        databaseManager.populateDatabase()
        self.assertEqual(autenticador.autenticar("username_1", "1234"), True)

    def testWrongPassword(self):
        """Testa se a senha errada bloqueia o usuário. Garantir que o databaseManager.populateDatabase() gera o username_1 com senha diferente de 123"""
        databaseManager.populateDatabase()
        self.assertEqual(autenticador.autenticar("username_1", "123"), False)

    def testWrongUsername(self):
        """Testa se o usuário errado retorna false. Garantir que o databaseManager.populateDatabase() não gera nenhum usuário com nome WRONGUSERNAME"""
        databaseManager.populateDatabase()
        self.assertEqual(autenticador.autenticar("WRONGUSERNAME", "123"), False)


if __name__ == '__main__':
    unittest.main()
