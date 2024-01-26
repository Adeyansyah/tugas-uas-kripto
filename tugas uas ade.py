import base64
import random
import string

def generate_captcha():
    # Generate a random string as CAPTCHA
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    # Encode the CAPTCHA using Base64
    encoded_captcha = base64.b64encode(captcha_text.encode()).decode()

    return encoded_captcha

# Example usage
captcha = generate_captcha()

print("Original CAPTCHA:", captcha)

# Simulate the process of user input (for verification)
user_input = input("Enter the CAPTCHA (first 10 characters): ")

# Trim the user input to the first 10 characters
trimmed_input = user_input[:10]

# Verify the trimmed input
if trimmed_input == captcha[:10]:
    print("CAPTCHA verification successful!")
else:
    print("CAPTCHA verification failed.")
