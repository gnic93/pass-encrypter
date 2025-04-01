from cryptography.fernet import Fernet
import secrets
import binascii

# Generar una clave de cifrado para el archivo
key: bytes = Fernet.generate_key()
f: bytes = Fernet(key)

def generate_password(length: int) -> str:
    password_bytes: bytes = secrets.token_bytes(length)
    password: str = binascii.hexlify(password_bytes).decode('utf-8')
    return password

def save_encrypted_password(password: str, filename: str) -> bytes:
    encrypted_password: bytes = f.encrypt(password.encode())
    with open(filename, 'wb') as file:
        file.write(encrypted_password)

def save_key_to_file(key: bytes, filename: str) -> bytes:
    with open(filename, 'wb') as file:
        file.write(key)
