import unittest
import databaseManager

class TestDatabase(unittest.TestCase):
    def testcheckUserExists(self):
        """Testa se um usuário criado realmente é achado. Garantir que o databaseManager.populateDatabase() gera o username_1"""
        user = "username_1"
        databaseManager.populateDatabase()
        output = databaseManager.checkUserExists(user)
        
        self.assertEqual(output, True)

    def testAddUsers(self):
        """Testa a criação de um usuário. Garantir o funcionamento do checkUserExists e que a populateDatabase() não gere o USUARIONOVO"""
        databaseManager.populateDatabase()
        user = "USUARIONOVO"
        databaseManager.addUser(user,"","")

        self.assertEqual(databaseManager.checkUserExists(user),True)

    def testgetUserCredencials(self):
        """Testa a recuperação das credenciais do usuário. Garantir que a populateDatabase() não gere o USUARIONOVO"""
        databaseManager.populateDatabase()
        user = "USUARIONOVO"
        databaseManager.addUser(user,"","")

        self.assertEqual(databaseManager.getUserCredencials(user),(True,"",""))

    def testincrementarAcessosNegados(self):
        """Testa o incremento dos acesso negados. Garantir que a populateDatabase() gere o username_1"""
        databaseManager.populateDatabase()
        user = "username_1"
        antes = databaseManager.getAcessosNegados(user)
        databaseManager.incrementarAcessosNegados(user)
        depois = databaseManager.getAcessosNegados(user)
        self.assertEqual(antes+1,depois)


if __name__ == '__main__':
    unittest.main()
