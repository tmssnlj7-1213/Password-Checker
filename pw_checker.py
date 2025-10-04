import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password is too short (minimum 8 characters).\n"

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks += "Add at least one number.\n"

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.\n"

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Add at least one lowercase letter.\n"

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        remarks += "Add at least one special character (e.g. !, @, #, etc.).\n"

    # Determine password strength
    if strength == 5:
        level = "Very Strong"
    elif strength == 4:
        level = "Strong"
    elif strength == 3:
        level = "Moderate"
    elif strength == 2:
        level = "Weak"
    else:
        level = "Very Weak"

    print(f"\nPassword Strength: {level}")
    print(remarks if remarks else "Nice job! Your password is strong.")

# Main program
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)

    