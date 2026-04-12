
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
    def generate_keys_pem(key_size:int = 2048)->tuple[bytes, bytes]:
        private_key, public_key = RSAService.generate_keys(key_size=key_size)
        # Save keys to PEM files
        private_key_pem = private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.PKCS8,
            encryption_algorithm = serialization.NoEncryption()
        )

        public_key_pem = public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )   
        return private_key_pem, public_key_pem
    
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
    def pem_to_private_key(pem_data: bytes, password=None):
        password_bytes = password.encode() if isinstance(password, str) else password
        return serialization.load_pem_private_key(pem_data, 
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
    def pem_to_public_key(pem_data: bytes):
       
        return serialization.load_pem_public_key(pem_data)
        
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
    
    @staticmethod
    def sign(private_key, message:bytes|str)->bytes:
        message_bytes = message.encode() if isinstance(message, str) else message
        signature = private_key.sign(
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    
    @staticmethod
    def verify(public_key, message:bytes|str, signature:bytes)->bool:
        message_bytes = message.encode() if isinstance(message, str) else message
        try:
            public_key.verify(
                signature,
                message_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False
