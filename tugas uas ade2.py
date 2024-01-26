from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

def encrypt_json(data, key):
    # Convert JSON data to string
    json_str = json.dumps(data)

    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(16)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CTR, iv=iv)

    # Encrypt the JSON string
    encrypted_json = cipher.encrypt(json_str.encode('utf-8'))

    # Combine IV and encrypted data
    combined_data = iv + encrypted_json

    # Encode the combined data using Base64
    encoded_data = base64.b64encode(combined_data).decode('utf-8')

    return encoded_data

def decrypt_json(encoded_data, key):
    # Decode the Base64 encoded data
    combined_data = base64.b64decode(encoded_data)

    # Extract IV from the combined data
    iv = combined_data[:16]

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CTR, iv=iv)

    # Decrypt the data
    decrypted_json = cipher.decrypt(combined_data[16:]).decode('utf-8')

    # Convert the JSON string to a Python object
    data = json.loads(decrypted_json)

    return data

# Example usage
encryption_key = get_random_bytes(32)  # 256-bit key for AES-256

# JSON data to be encrypted
json_data = {"name": "John Doe", "age": 30, "city": "Example City"}

# Encrypt JSON data
encoded_data = encrypt_json(json_data, encryption_key)
print("Encoded Data:", encoded_data)

# Decrypt JSON data
decoded_data = decrypt_json(encoded_data, encryption_key)
print("Decoded Data:", decoded_data)
