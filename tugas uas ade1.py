from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import base64

def encrypt_data(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.OCB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return ciphertext

def generate_key_iv():
    # In a real-world scenario, generate a secure key and IV
    key = b'secure_key_here'  # Replace with a secure key
    iv = b'secure_iv_here'    # Replace with a secure IV
    return key, iv

def generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang_distributor):
    data = f"{nomor_pengiriman}-{tanggal_kirim}-{kode_cabang_distributor}".encode('utf-8')

    # Generate key and IV
    key, iv = generate_key_iv()

    # Encrypt data using AES-256 OCB
    encrypted_data = encrypt_data(data, key, iv)

    # Calculate SHA-1 hash
    sha1_hash = hashes.Hash(hashes.SHA1(), backend=default_backend())
    sha1_hash.update(data)
    sha1_digest = sha1_hash.finalize()

    # Combine encrypted data and SHA-1 hash
    combined_data = encrypted_data + sha1_digest

    # Encode the combined data using Base64
    barcode = base64.b64encode(combined_data).decode('utf-8')

    return barcode

# Example usage
nomor_pengiriman = "12345"
tanggal_kirim = "20220127"
kode_cabang_distributor = "ABC123"

barcode = generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang_distributor)
print("Generated Barcode:", barcode)
