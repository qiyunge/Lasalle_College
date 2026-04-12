from fastapi import APIRouter, Request,Response

from vsts.app.schemas.rsa import RSAEncrytionRequest, RSADecryptionRequest, RSAEncryptionResponse, RSADecryptionResponse
from vsts.app.services.rsa_services import encrypt_message_service,decrypt_message_service
router = APIRouter()

@router.post("/rsa/encrypt", name = "rsa_encrypt")
async def rsa_encrypt(request: Request, response: Response, payload: RSAEncrytionRequest)-> RSAEncryptionResponse:
    """
    Placeholder API endpoint for RSA encryption.
    """
    ciphertext = encrypt_message_service(payload.public_key_pem, payload.plaintext)  # Call the RSA encryption service (implementation pending)

    return RSAEncryptionResponse(ciphertext=ciphertext)

@router.post("/rsa/decrypt", name = "rsa_decrypt")
async def rsa_decrypt(request: Request, response: Response, payload: RSADecryptionRequest)-> RSADecryptionResponse:
    """
    Placeholder API endpoint for RSA decryption.
    """
    plaintext = decrypt_message_service(payload.private_key_pem, payload.ciphertext)  # Call the RSA decryption service (implementation pending)

    return RSADecryptionResponse(plaintext=plaintext)