from pathlib import Path

from vsts.core.hash_service import HashService
from vsts.core.rsa_service import RSAService
from vsts.core.state_transfer_service import StateTransferService, TransferResult


def main():
    # Generate RSA keys
    private_key, public_key = RSAService.generate_keys()

    # Define file paths
    source_file = Path("data/sample_data.txt")
    encrypted_file = Path("data/encrypted_data.bin")
    decrypted_file = Path("data/decrypted_data.txt")

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
    print(f"Integrity Check Passed: {result.intergrity_ok}")

if __name__ == "__main__":
    main()  
