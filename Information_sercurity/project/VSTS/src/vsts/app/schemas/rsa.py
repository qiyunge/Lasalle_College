from pydantic import BaseModel, Field

class RSAEncrytionRequest(BaseModel):
    plaintext: str = Field(..., description="The plaintext to be encrypted")
    public_key_pem: str = Field(..., description="The RSA public key in PEM format")

class RSAEncryptionResponse(BaseModel):
    ciphertext: str = Field(..., description="The resulting ciphertext after encryption")

class RSADecryptionRequest(BaseModel):
    ciphertext: str = Field(..., description="The ciphertext to be decrypted")
    private_key_pem: str = Field(..., description="The RSA private key in PEM format")
class RSADecryptionResponse(BaseModel):
    plaintext: str = Field(..., description="The resulting plaintext after decryption")

class RSAKeyPairRequest(BaseModel):
    key_size: int = Field(2048, description="The size of the RSA key pair to generate (e.g., 2048, 4096)")
   
class RSAKeyPairResponse(BaseModel):
    public_key_pem: str = Field(..., description="The generated RSA public key in PEM format")
    private_key_pem: str = Field(..., description="The generated RSA private key in PEM format")


class RSASignatureRequest(BaseModel):
    message: str = Field(..., description="The message to be signed")
    private_key_pem: str = Field(..., description="The RSA private key in PEM format")

class RSASignatureResponse(BaseModel):
    signature: str = Field(..., description="The resulting digital signature in Base64 format")

class RSAVerifyRequest(BaseModel):
    message: str = Field(..., description="The original message that was signed")
    signature: str = Field(..., description="The digital signature to be verified (Base64 format)")
    public_key_pem: str = Field(..., description="The RSA public key in PEM format")    

class RSAVerifyResponse(BaseModel):
    valid: bool = Field(..., description="Indicates whether the signature is valid or not")

