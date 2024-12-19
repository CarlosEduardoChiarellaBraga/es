import unittest
import autenticador
import databaseManager

class TestAutenticador(unittest.TestCase):
    def testAuthenticate(self):
        """Verificar autorização mediante credenciais corretas. Garantir que o databaseManager.populateDatabase() gera o username_1 com senha 1234"""
        databaseManager.populateDatabase()
        self.assertEqual(autenticador.autenticar("username_1", "1234"), True)

    def testWrongPassword(self):
        """Verificar a não autorização mediante a credencial “senha” errada. Garantir que o databaseManager.populateDatabase() gera o username_1 com senha diferente de 123"""
        databaseManager.populateDatabase()
        self.assertEqual(autenticador.autenticar("username_1", "123"), False)

    def testWrongUsername(self):
        """Verificar a não autorização mediante a credencial “user” errada. Garantir que o databaseManager.populateDatabase() não gera nenhum usuário com nome WRONGUSERNAME"""
        databaseManager.populateDatabase()
        self.assertEqual(autenticador.autenticar("WRONGUSERNAME", "123"), False)


if __name__ == '__main__':
    unittest.main()
