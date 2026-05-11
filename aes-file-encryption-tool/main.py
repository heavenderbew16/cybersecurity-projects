from cryptography.fernet import Fernet

# Generate and save key
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Key generated and saved as secret.key")


# Load key
def load_key():
    return open("secret.key", "rb").read()


# Encrypt file
def encrypt_file(filename, key):
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"{filename} encrypted successfully.")


# Decrypt file
def decrypt_file(filename, key):
    fernet = Fernet(key)

    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"{filename} decrypted successfully.")


# Main menu
def main():
    print("==== AES File Encryption Tool ====")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")

    choice = input("Choose an option: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        filename = input("Enter file name to encrypt: ")
        key = load_key()
        encrypt_file(filename, key)

    elif choice == "3":
        filename = input("Enter file name to decrypt: ")
        key = load_key()
        decrypt_file(filename, key)

    else:
        print("Invalid option")


if name == "main":
    main()
