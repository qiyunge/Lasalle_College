import unittest
import os

from vsts.core.rsa_service import RSAService

class TestRSAService(unittest.TestCase):
    def setUp(self):
        self.private_key, self.public_key = RSAService.generate_keys()
        self.message = b"hello VSTS"
        self.private_key_path = "tests/test_private.pem"
        self.public_key_path = "tests/test_public.pem"

    def tearDown(self):
        for path in [self.private_key_path, self.public_key_path]:
            if os.path.exists(path):
                os.remove(path)
        return super().tearDown()
    
    def test_encryption_decryption(self):
        ciphertext = RSAService.encrypt(self.public_key, self.message)
        decrypted_message = RSAService.decrypt(self.private_key, ciphertext)
        self.assertEqual(decrypted_message, self.message)

    def test_encrypted_message_different_from_plaintext(self):
        ciphertext = RSAService.encrypt(self.public_key, self.message)
        self.assertNotEqual(ciphertext, self.message)

    def test_loaded_keys_work(self):
        RSAService.save_private_key(self.private_key, self.private_key_path)
        RSAService.save_public_key(self.public_key, self.public_key_path)

        loaded_private = RSAService.load_private_key(self.private_key_path)
        loaded_public = RSAService.load_public_key(self.public_key_path)

        ciphertext = RSAService.encrypt(loaded_public, self.message)
        decrypted_message = RSAService.decrypt(loaded_private, ciphertext)
        self.assertEqual(decrypted_message, self.message)

if __name__ == '__main__':
    unittest.main()