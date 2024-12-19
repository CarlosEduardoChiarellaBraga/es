import unittest
from criptografia import generate_salt, strToSHA256 

class TestHashingFunctions(unittest.TestCase):
    def testSaltLenghtGeneration(self):
        """Testa se o salt gerado tem o comprimento correto."""
        length = 16
        salt = generate_salt(length)
        self.assertEqual(len(salt), length)

    def test_strToSHA256_consistency(self):
        """Testa se o hash gerado para a mesma senha e salt é consistente."""
        password = "mypassword"
        salt = "randomsalt1234"
        hash1 = strToSHA256(password, salt)
        hash2 = strToSHA256(password, salt)
        self.assertEqual(hash1, hash2)

    def test_strToSHA256_uniqueness(self):
        """Testa se hashes diferentes são gerados para diferentes salts."""
        password = "mypassword"
        salt1 = generate_salt()
        salt2 = generate_salt()
        hash1 = strToSHA256(password, salt1)
        hash2 = strToSHA256(password, salt2)
        self.assertNotEqual(hash1, hash2)


if __name__ == '__main__':
    unittest.main()
