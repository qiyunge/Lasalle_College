from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import Response

from vsts.app.schemas.rsa import RSASignatureRequest, RSAVerifyRequest,RSASignatureResponse,RSAVerifyResponse
from vsts.app.services.rsa_services import sign_message_service, verify_signature_service

router = APIRouter()

@router.post("/rsa/sign", name="sign_message", response_model=RSASignatureResponse)
async def sign_message( request: Request,payload: RSASignatureRequest, response: Response)->RSASignatureResponse:
    """
    Endpoint for signing a message.
    """
    signature = sign_message_service(payload.private_key_pem, payload.message)
    return RSASignatureResponse( signature=signature)

@router.post("/rsa/verify", name="verify_signature", response_model=RSAVerifyResponse)
async def verify_signature(request: Request, payload: RSAVerifyRequest)-> RSAVerifyResponse:
    """
    Placeholder endpoint for verifying a digital signature.
    """
    is_valid = verify_signature_service(payload.public_key_pem, payload.message, payload.signature)
    return RSAVerifyResponse(valid=is_valid)