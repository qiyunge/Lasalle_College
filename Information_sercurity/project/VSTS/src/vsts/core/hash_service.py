from __future__ import annotations

import hashlib
from pathlib import Path

class HashService:
    DEFAULT_HASH_ALGORITHM = 'sha256'
    CHUNK_SIZE = 8192

    @staticmethod
    def hash_bytes(data: bytes, algorithm: str = DEFAULT_HASH_ALGORITHM) -> str:
       hasher = hashlib.new(algorithm)
       hasher.update(data)
       return hasher.hexdigest()    
    
    @staticmethod
    def hash_file(file_path: str|Path, algorithm: str = DEFAULT_HASH_ALGORITHM) -> str:
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        hasher = hashlib.new(algorithm)
        with path.open('rb') as f:
            while chunk := f.read(HashService.CHUNK_SIZE):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    @staticmethod
    def verify_hash(data: bytes, expected_hash: str, algorithm: str = DEFAULT_HASH_ALGORITHM) -> bool:
        computed_hash = HashService.hash_bytes(data, algorithm)
        return computed_hash == expected_hash   
    
    @staticmethod
    def verify_file_hash(file_path: str|Path, expected_hash: str, algorithm: str = DEFAULT_HASH_ALGORITHM) -> bool:
        computed_hash = HashService.hash_file(file_path, algorithm)
        return computed_hash == expected_hash