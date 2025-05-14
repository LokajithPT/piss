from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import hashlib
import base64
import os

def derive_key(password):
    return hashlib.sha256(password.encode()).digest()[:16]

def encrypt_file_to_string(filepath, password):
    key = derive_key(password)
    iv = get_random_bytes(16)

    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        content = f.read()

    # Combine filename and content, separated by two newlines
    combo = filename.encode() + b'\n\n' + content

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(combo, AES.block_size)
    encrypted = cipher.encrypt(padded)
    final_data = iv + encrypted

    return base64.b64encode(final_data).decode()

if __name__ == '__main__':
    path = input("📂 File to encrypt: ").strip()
    password = input("🔑 Password: ").strip()
    encrypted_string = encrypt_file_to_string(path, password)
    print("\n🔒 Encrypted Output String:\n")
    print(encrypted_string)

