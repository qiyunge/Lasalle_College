# 🔐 RSA Crypto API

A lightweight cryptographic API built with FastAPI, providing RSA-based encryption, decryption, digital signatures, and key management.

---

## 🚀 Features

* 🔑 Generate RSA key pairs (PKCS#8 PEM)
* 🔒 Encrypt / Decrypt messages (RSA-OAEP)
* ✍️ Sign / Verify messages (RSA-PSS)
* 🔄 Base64 encoding for safe JSON transport
* 📦 Clean layered architecture (route → service → core)

---

## 🛠️ Tech Stack

* Python 3.10+
* FastAPI
* Pydantic
* cryptography

---

## 📂 Project Structure

```
app/
├─ core/
│   └─ rsa.py              # Pure cryptographic logic
├─ services/
│   └─ rsa_service.py     # Encoding / orchestration
├─ routes/
│   └─ rsa.py             # FastAPI endpoints
├─ schemas/
│   └─ rsa.py             # Pydantic models
```

---

## 📡 API Endpoints

### 🔑 Generate RSA Key Pair

**POST** `/api/rsa/generate-keys`

#### Request

```json
{
  "key_size": 2048
}
```

#### Response

```json
{
  "public_key": "-----BEGIN PUBLIC KEY-----...",
  "private_key": "-----BEGIN PRIVATE KEY-----..."
}
```

---

### 🔒 Encrypt

**POST** `/api/rsa/encrypt`

#### Request

```json
{
  "plaintext": "hello world",
  "public_key_pem": "-----BEGIN PUBLIC KEY-----..."
}
```

#### Response

```json
{
  "ciphertext_base64": "SGVsbG8..."
}
```

---

### 🔓 Decrypt

**POST** `/api/rsa/decrypt`

#### Request

```json
{
  "ciphertext_base64": "SGVsbG8...",
  "private_key_pem": "-----BEGIN PRIVATE KEY-----..."
}
```

#### Response

```json
{
  "plaintext": "hello world"
}
```

---

### ✍️ Sign

**POST** `/api/rsa/sign`

#### Request

```json
{
  "message": "hello world",
  "private_key_pem": "-----BEGIN PRIVATE KEY-----..."
}
```

#### Response

```json
{
  "signature_base64": "MEUCIQD..."
}
```

---

### ✅ Verify

**POST** `/api/rsa/verify`

#### Request

```json
{
  "message": "hello world",
  "signature_base64": "MEUCIQD...",
  "public_key_pem": "-----BEGIN PUBLIC KEY-----..."
}
```

#### Response

```json
{
  "valid": true
}
```

---

## 🧠 Design Notes

### 🔹 Serialization Strategy

* Keys → PEM (text format)
* Signature / ciphertext → Base64 (safe for JSON)
* Internal processing → bytes

```
str (JSON)
↓
encode / decode
↓
bytes (crypto)
```

---

### 🔹 Security Principles

* RSA-OAEP for encryption (confidentiality)
* RSA-PSS for signatures (authenticity & integrity)
* Strict separation of layers:

  * Core: pure cryptographic logic
  * Service: encoding + orchestration
  * Route: HTTP interface

---

## 🧪 Example (curl)

```bash
curl -X POST http://localhost:8000/api/rsa/generate-keys \
  -H "Content-Type: application/json" \
  -d '{"key_size": 2048}'
```

---

## ▶️ Running the Project


### Using pip

```bash
pip install -e .
uvicorn main_web:app --reload
```

---

## 📖 Interactive Docs

FastAPI automatically provides:

* Swagger UI → http://localhost:8000/docs
* ReDoc → http://localhost:8000/redoc

---

## 📌 Future Improvements

* Add AES hybrid encryption
* Add key storage / management
* Add JWT signing support
* Add rate limiting & auth

---

## 👤 Author

**Ace (Qiyun Ge)**  
- 📧 Email: Grantnj.ge@gmail.com  
- 💼 LinkedIn: https://...  
- 🐙 GitHub: https://github.com/qiyunge

---
