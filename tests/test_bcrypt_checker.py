import unittest
from core.bcrypt_checker import hash_password, verify_password


class TestBcryptChecker(unittest.TestCase):
    def setUp(self):
        self.senha_plana = "MinhaSenhaSecreta123!"
        self.senha_hash = hash_password(self.senha_plana)

    def test_verificar_senha_correta(self):
        self.assertTrue(verify_password(self.senha_plana, self.senha_hash))

    def test_verificar_senha_incorreta(self):
        self.assertFalse(verify_password("SenhaErrada123", self.senha_hash))

    def test_hashes_diferentes_mesma_senha(self):
        novo_hash = hash_password(self.senha_plana)
        self.assertNotEqual(self.senha_hash, novo_hash)
        self.assertTrue(verify_password(self.senha_plana, novo_hash))

    def test_senha_vazia(self):
        self.assertFalse(verify_password("", self.senha_hash))

    def test_hash_invalido(self):
        hash_quebrado = b"isso_nao_e_um_hash_bcrypt_valido"
        self.assertFalse(verify_password(self.senha_plana, hash_quebrado))

if __name__ == '__main__':
    unittest.main()
