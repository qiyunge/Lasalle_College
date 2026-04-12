from vsts.core.state_transfer_service import StateTransferService, TransferResult
from vsts.core.rsa import RSAService


def test_transfer_small_file(tmp_path):
    # Generate RSA keys
    private_key, public_key = RSAService.generate_keys()

    # Create a small test file
    source_file = tmp_path / "source.txt"
    file_content = "This is a test file for state transfer."
    source_file.write_text(file_content)

    encrypted_file = tmp_path / "encrypted.bin"
    decrypted_file = tmp_path / "decrypted.txt"

    # Perform state transfer
    result = StateTransferService.transfer_state(source_file, encrypted_file, decrypted_file, public_key, private_key)

    # Assertions
    assert result.source_path == source_file
    assert result.encrypted_file == encrypted_file
    assert result.decrypted_file == decrypted_file
    assert result.original_hash == result.decrypted_hash
    assert result.integrity_ok
    assert decrypted_file.read_text() == file_content

