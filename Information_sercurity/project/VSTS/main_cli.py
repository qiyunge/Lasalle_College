from pathlib import Path

from vsts.core.hash_service import HashService
from vsts.core.rsa import RSAService as A
from vsts.core.rsa import RSAService 

from vsts.core.rsa import RSAService as B


# assert A is B, "RSAService should be the same class regardless of import style"

from vsts.core.state_transfer_service import StateTransferService, TransferResult



def main():
    # Generate RSA keys
    private_key, public_key = RSAService.generate_keys()


    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data"

    source_file = DATA_DIR / "sample_data.txt"
    encrypted_file = DATA_DIR / "encrypted_data.bin"
    decrypted_file = DATA_DIR / "decrypted_data.txt"

    # Define file paths


    # Create a sample source file
    if not source_file.exists():
        source_file.write_text("This is a sample file for encryption and decryption testing.")

    # Perform state transfer (encryption + decryption)
    result = StateTransferService.transfer_state(
        source_path=source_file,
        encrypted_file=encrypted_file,
        decrypted_file=decrypted_file,
        public_key=public_key,
        private_key=private_key
    )

    # Print results
    print(f"Source File: {result.source_path}")
    print(f"Encrypted File: {result.encrypted_file}")
    print(f"Decrypted File: {result.decrypted_file}")
    print(f"Original Hash: {result.original_hash}")
    print(f"Decrypted Hash: {result.decrypted_hash}")
    print(f"Integrity Check Passed: {result.integrity_ok}")

if __name__ == "__main__":
    main()  
