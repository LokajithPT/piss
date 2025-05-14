from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import base64

def derive_key(password):
    return hashlib.sha256(password.encode()).digest()[:16]

def decrypt_string_to_file(encrypted_str, password):
    key = derive_key(password)
    raw = base64.b64decode(encrypted_str)
    iv = raw[:16]
    encrypted = raw[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted)
    decrypted = unpad(decrypted_padded, AES.block_size)

    # Split into filename and content
    split_index = decrypted.find(b'\n\n')
    if split_index == -1:
        raise ValueError("Invalid format. Could not find filename/content separator.")

    filename = decrypted[:split_index].decode()
    content = decrypted[split_index+2:]

    with open(filename, 'wb') as f:
        f.write(content)

    print(f"✅ File '{filename}' recreated successfully!")

if __name__ == '__main__':
    print("🧾 Paste the encrypted string:")
    encrypted_input = input().strip()
    password = input("🔑 Password: ").strip()
    decrypt_string_to_file(encrypted_input, password)

