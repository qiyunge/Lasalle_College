from .web.page_routes import router as page_web_router
from .web.security_routes import router as security_web_router
from .api.system_api import router as system_api_router  
from .api.crypto_api import router as crypto_api_router
from .api.signature_api import router as signature_api_router
from .api.keys_gen_api import router as keys_gen_api_router