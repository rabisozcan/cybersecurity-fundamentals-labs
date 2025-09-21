def check_password(password):
    if len(password) < 8:
        return "Weak: too short"
    if not any(char.isdigit() for char in password):
        return "Weak: no number"
    if not any(char.isupper() for char in password):
        return "Weak: no uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak: no lowercase letter"
    if not any(char in "!@#$%^&*()" for char in password):
        return "Weak: no special character"
    return "Strong password"

if __name__ == "__main__":
    test_passwords = ["abc123", "Password1", "P@ssword123"]
    for pw in test_passwords:
        print(f"{pw}: {check_password(pw)}")
