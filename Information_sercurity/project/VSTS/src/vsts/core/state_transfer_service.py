from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from vsts.core.hash_service import HashService
from vsts.core.rsa import RSAService

@dataclass(frozen = True)
class TransferResult:
    source_path: Path
    encrypted_file: Path
    decrypted_file: Path
    original_hash: str
    decrypted_hash: str
    integrity_ok:bool

class StateTransferService:

    @staticmethod
    def encrypt_file(source_path: str| Path, encrypted_file: str| Path, public_key, overwrite: bool = True) -> str:
        source_path = Path(source_path)
        encrypted_path = Path(encrypted_file)

        if not source_path.is_file():
            raise FileNotFoundError(f"Source file {source_path} does not exist.")
        if encrypted_path.exists() and not overwrite:
            raise FileExistsError(f"Encrypted file {encrypted_path} already exists and overwrite is set to False.")
        encrypted_path.parent.mkdir(parents=True, exist_ok=True)
        
        data =  source_path.read_bytes()
        original_hash = HashService.hash_bytes(data)

        encrypted_data =  RSAService.encrypt( public_key, data)
        encrypted_path.write_bytes(encrypted_data)
        return original_hash    
    
    @staticmethod
    def decrypt_file(encrypted_file: str| Path, decrypted_file: str| Path, private_key, overwrite: bool = True) -> str:
        encrypted_file = Path(encrypted_file)
        decrypted_file = Path(decrypted_file)

        if not encrypted_file.is_file():
            raise FileNotFoundError(f"Encrypted file {encrypted_file} does not exist.")
        if decrypted_file.exists() and not overwrite:
            raise FileExistsError(f"Decrypted file {decrypted_file} already exists and overwrite is set to False.")

        
        encrypted_data = encrypted_file.read_bytes()
        decrypted_data = RSAService.decrypt( private_key, encrypted_data)

        decrypted_file.parent.mkdir(parents=True, exist_ok=True)
        decrypted_file.write_bytes(decrypted_data)
        decrypted_hash = HashService.hash_bytes(decrypted_data)

        return decrypted_hash
    
    @staticmethod
    def transfer_state(source_path: str| Path, encrypted_file: str| Path, decrypted_file: str| Path,
                       public_key, private_key) -> TransferResult:
        
        source_path = Path(source_path)
        encrypted_path = Path(encrypted_file)
        decrypted_path = Path(decrypted_file)   

        original_hash = StateTransferService.encrypt_file(source_path, encrypted_path, public_key)
        decrypted_hash = StateTransferService.decrypt_file(encrypted_path, decrypted_path, private_key)

        integrity_ok = original_hash == decrypted_hash

        return TransferResult(
            source_path = source_path,
            encrypted_file = encrypted_path,
            decrypted_file = decrypted_path,
            original_hash = original_hash,
            decrypted_hash = decrypted_hash,
            integrity_ok = integrity_ok
        )   