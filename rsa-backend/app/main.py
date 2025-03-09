from fastapi import FastAPI
from pydantic import BaseModel
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

app = FastAPI()

# Generate RSA Keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Convert keys to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

@app.get("/")
async def root():
    return {"message": "RSA Encryptor API is running!"}

@app.get("/get_keys")
async def get_keys():
    return {"private_key": private_pem.decode(), "public_key": public_pem.decode()}

class EncryptRequest(BaseModel):
    text: str

@app.post("/encrypt")
async def encrypt(data: EncryptRequest):
    ciphertext = public_key.encrypt(
        data.text.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return {"ciphertext": ciphertext.hex()}

class DecryptRequest(BaseModel):
    ciphertext: str

@app.post("/decrypt")
async def decrypt(data: DecryptRequest):
    plaintext = private_key.decrypt(
        bytes.fromhex(data.ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return {"plaintext": plaintext.decode()}
