
from __future__ import annotations

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes   

class RSAService:
    @staticmethod
    def generate_keys( key_size = 2048):
        private_key = rsa.generate_private_key(
            public_exponent = 65537,
            key_size = key_size
        )

        public_key = private_key.public_key()
        return private_key, public_key
    
    @staticmethod
    def save_private_key(private_key, filename, password=None):
        with open(filename, 'wb') as f:
            if password:
                password_bytes = password.encode() if isinstance(password, str) else password
                encryption_algorithm = serialization.BestAvailableEncryption(password_bytes)
            else:
                encryption_algorithm = serialization.NoEncryption()

            f.write(private_key.private_bytes(
                encoding = serialization.Encoding.PEM,
                format = serialization.PrivateFormat.PKCS8,
                encryption_algorithm = encryption_algorithm
            ))

    @staticmethod
    def load_private_key(filename, password=None):
        with open(filename, 'rb') as f:
            password_bytes = password.encode() if isinstance(password, str) else password
            return serialization.load_pem_private_key(f.read(), 
                                                      password=password_bytes if password else None)

    @staticmethod
    def save_public_key(public_key, filename):
        with open(filename, 'wb') as f:
            f.write(public_key.public_bytes(
                encoding = serialization.Encoding.PEM,
                format = serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    @staticmethod
    def load_public_key(filename):
        with open(filename, 'rb') as f:
            return serialization.load_pem_public_key(f.read())  
        
    @staticmethod
    def encrypt(public_key, plaintext:bytes|str):
        plaintext_bytes = plaintext.encode() if isinstance(plaintext, str) else plaintext
        ciphertext = public_key.encrypt(
            plaintext_bytes,
            padding.OAEP(
                mgf = padding.MGF1(algorithm=hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None
            )
        )
        return ciphertext
    
    @staticmethod
    def decrypt(private_key, ciphertext:bytes):
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf = padding.MGF1(algorithm=hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None
            )
        )
        return plaintext
    
    
