import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user preferences
    all_chars = lowercase_letters
    if use_uppercase:
        all_chars += uppercase_letters
    if use_digits:
        all_chars += digits
    if use_special_chars:
        all_chars += special_chars

    # Ensure the password length is at least 4 characters
    length = max(length, 4)

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Example usage:
password = generate_password(length=16, use_uppercase=True, use_digits=True, use_special_chars=True)
print("Generated Password:", password)
