import unittest
import bloqueadorDeAcesso
import databaseManager

class TestAutenticador(unittest.TestCase):
    def testIncrementarAcessosNegados(self):
        """Verificar o funcionamento do incremento de acessos negados. Garantir que database.populateDataBase() gera username_1"""
        databaseManager.populateDatabase()
        user = "username_1"
        acessosNegadosAntes = bloqueadorDeAcesso.getAcessosNegados(user)
        bloqueadorDeAcesso.incrementarAcessosNegados(user)
        acessossNegadosDepois = bloqueadorDeAcesso.getAcessosNegados(user)
        self.assertEqual(acessosNegadosAntes+1, acessossNegadosDepois)
    
    def testResetarAcessosNegados(self):
        """Testa ResetarAcessosNegados. Garantir que database.populateDataBase() gera username_1"""
        databaseManager.populateDatabase()
        user = "username_1"

        bloqueadorDeAcesso.incrementarAcessosNegados(user)
        bloqueadorDeAcesso.resetarAcessosNegados(user)
        acessosNegados =  bloqueadorDeAcesso.getAcessosNegados(user)

        self.assertEqual(acessosNegados, 0)

    def testcheckUserCooldown(self):
        """Testa ResetarAcessosNegados. Garantir que database.populateDataBase() gera username_1, e que o teste rode em menos de 10^-1 segundo"""
        databaseManager.populateDatabase()
        user = "username_1"
        bloqueadorDeAcesso.incrementarAcessosNegados(user)

        self.assertAlmostEqual(bloqueadorDeAcesso.checkUserCooldown(user), 10, 1)

if __name__ == '__main__':
    unittest.main()
