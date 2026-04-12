from fastapi import APIRouter
from fastapi.responses import Response
# --- import local ---
from vsts.app.schemas.rsa import RSAKeyPairResponse,RSAKeyPairRequest
from vsts.app.services.rsa_services import generate_rsa_keys_pem_service

router = APIRouter()


@router.post("/rsa/generate-keys", name="generate_keypair", response_model=RSAKeyPairResponse)
async def generate_keys(payload: RSAKeyPairRequest, response: Response)-> RSAKeyPairResponse:
    """
    API endpoint to generate a new RSA key pair.
    """

    
    key_size = payload.key_size
    private_key_pem, public_key_pem = generate_rsa_keys_pem_service(key_size=key_size)

    
    return RSAKeyPairResponse(public_key_pem=public_key_pem, private_key_pem=private_key_pem)