from vsts.core.hash_service import HashService

def test_hash_bytes():
    data = b"hello VSTS"
    digest  = HashService.hash_bytes(data)
    assert isinstance(digest, str)
    assert len(digest) == 64  # SHA-256 produces a 64-character hexadecimal string


def test_verify_bytes():
    data = b"hello VSTS"
    digest = HashService.hash_bytes(data)
    assert HashService.verify_hash(data, digest) == True
    assert HashService.verify_hash(b"wrong data", digest) == False


def test_hash_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    content = b"hello VSTS"
    file_path.write_bytes(content)

    digest = HashService.hash_file(file_path)
    assert isinstance(digest, str)
    assert len(digest) == 64  # SHA-256 produces a 64-character hexadecimal string
    assert HashService.verify_file_hash(file_path, digest) == True
    assert HashService.verify_file_hash(file_path, "wronghash") == False

    