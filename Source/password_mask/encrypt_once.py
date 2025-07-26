from passwordUtils import method
from cryptography.fernet import Fernet

# Generate key and save to file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("✅ Key saved to 'secret.key'")

if __name__ == "__main__":
    # Uncomment this only the first time
    #generate_key()

    # Replace with your real MySQL root password
    encrypted = encrypt_password("root")
    print("🔐 Encrypted password (copy this to password_utils.py):")