
from vsts.core.rsa import RSAService
from base64 import b64encode, b64decode
 

    # Generate RSA keys
def generate_rsa_keys_pem_service(key_size:int = 2048)->tuple[bytes, bytes]:
    '''
        Generate RSA keys and return them in PEM format
        return: Tuple of private key and public key in PEM format
    '''
    # Save keys to PEM files
    private_key_pem, public_key_pem =RSAService.generate_keys_pem(key_size=key_size)
    return private_key_pem, public_key_pem


def sign_message_service(private_key_pem: str, message: str) -> str:
    print("Signing message with RSAService...",message,private_key_pem)
    private_key = RSAService.pem_to_private_key(private_key_pem.encode())
    message_bytes = message.encode() 
    signature = RSAService.sign(private_key, message_bytes)
    return b64encode(signature).decode()

def verify_signature_service(public_key_pem: str, message: str, signature_b64: str) -> bool:
    public_key = RSAService.pem_to_public_key(public_key_pem.encode())
    message_bytes = message.encode()
    signature_bytes = b64decode(signature_b64.encode())
    is_valid = RSAService.verify(public_key, message_bytes, signature_bytes)
    return is_valid

def encrypt_message_service(public_key_pem: str, plaintext: str) -> str:
    public_key = RSAService.pem_to_public_key(public_key_pem.encode())
    plaintext_bytes = plaintext.encode()   
    ciphertext_bytes = RSAService.encrypt(public_key, plaintext_bytes) 
    return b64encode(ciphertext_bytes).decode()

def decrypt_message_service(private_key_pem: str, ciphertext_b64: str) -> str:
    private_key = RSAService.pem_to_private_key(private_key_pem.encode())
    ciphertext_bytes = b64decode(ciphertext_b64.encode())
    plaintext_bytes = RSAService.decrypt(private_key, ciphertext_bytes)
    return plaintext_bytes.decode()



