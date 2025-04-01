from cryptography.fernet import Fernet

# Desencriptado de archivo
def decrypt_file(filename: str, decrypted_filename: str, key: bytes) -> bytes:
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def run():
    filename = input('Encrypted file directory: ')
    decrypted_filename = './files/passd'
    key = input('key: ')

    decrypt_file(filename, decrypted_filename, key)        

    print(f'Save decrypted file as: {decrypted_filename}')

if __name__ == "__main__":
    run()
