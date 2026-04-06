# 🔐 Secure File Transfer System (RSA + Hash)

## 📌 Overview

This project implements a secure file transfer system with:

* **RSA encryption** → ensures confidentiality
* **SHA-256 hashing** → ensures data integrity

It demonstrates a complete end-to-end secure transfer pipeline.

---

## ✨ Features

* 🔑 Generate RSA key pairs
* 🔒 Encrypt files using public key
* 🔓 Decrypt files using private key
* 🧾 Verify file integrity with SHA-256
* 🔄 End-to-end transfer pipeline
* 🧪 Automated testing with `pytest`

---

## ⚙️ Workflow

```text
File → Hash → Encrypt → Decrypt → Hash → Compare
```

### Steps

1. Read source file
2. Compute SHA-256 hash
3. Encrypt file using RSA public key
4. Decrypt file using RSA private key
5. Compute hash again
6. Compare hashes

---

## 🧱 Project Structure

```text
vsts/
├── core/
│   ├── rsa_service.py
│   ├── hash_service.py
│
├── infra/
│   ├── state_transfer_service.py
│
├── app/
│   └── main.py
│
tests/
├── test_rsa_service.py
├── test_hash_service.py
├── test_state_transfer_service.py
```

---

## ▶️ Run the Demo

```bash
python main.py
```

### Example Output

```text
=== Secure File Transfer Result ===
Source file     : data/source.txt
Encrypted file  : data/encrypted_data.bin
Decrypted file  : data/decrypted_data.txt
Original hash   : 8f4343...
Decrypted hash  : 8f4343...
Integrity check : OK ✅
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🧠 Key Concepts

### RSA Encryption

RSA is an asymmetric cryptographic algorithm using public/private key pairs based on modular exponentiation.

### SHA-256 Hashing

SHA-256 produces a fixed-length digest that allows verification of data integrity.

---

## ⚠️ Limitations

This implementation encrypts file data directly using RSA.

* Suitable for **small files only**
* Not efficient for large data

---

## 🚀 Future Improvements

* Hybrid encryption (RSA + AES-GCM)
* Large file support
* Streaming encryption
* CLI interface

---

## 👤 Author

**Qiyun Ge**

---

## 📄 License

This project is for educational purposes.
