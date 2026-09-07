import random
import string
import json

PASSWORD_FILE = "passwords.json"

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def save_password(password):
    # Load existing passwords if file exists
    try:
        with open(PASSWORD_FILE, 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = []

    # Add new password
    passwords.append(password)

    # Save back to file
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f, indent=2)

def main():
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print("Your generated password is:", password)
    save_password(password)

if __name__ == "__main__":
    main()