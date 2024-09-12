import re

def validate_password(password):
    # Check length
    if len(password) < 6 or len(password) > 12:
        return False
    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return False
    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False
    # Check for at least one digit
    if not re.search("[0-9]", password):
        return False
    # Check for at least one special character
    if not re.search("[$#@]", password):
        return False
    return True

def check_passwords(passwords):
    valid_passwords = []
    for password in passwords:
        if validate_password(password):
            valid_passwords.append(password)
    return valid_passwords

# Input: comma-separated passwords
input_passwords = input("Enter passwords separated by commas: ").split(',')

# Check the passwords
valid_passwords = check_passwords(input_passwords)

# Output the valid passwords
print("Valid passwords:", ", ".join(valid_passwords))