username = input("Enter your username: ")
password = input("Enter your password: ")

print("=" * 45)
print("         PASSWORD VALIDATION REPORT")
print("=" * 45)

print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

length_check = len(password) >= 8
digit_check = any(char.isdigit() for char in password)
uppercase_check = any(char.isupper() for char in password)

print("[{}] Minimum 8 characters ({} characters)".format(
    "PASS" if length_check else "FAIL", len(password)))

print("[{}] At least one digit".format(
    "PASS" if digit_check else "FAIL"))

print("[{}] At least one uppercase letter".format(
    "PASS" if uppercase_check else "FAIL"))

print("\n--- Result ---")

if length_check and digit_check and uppercase_check:
    print("Password is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("Password is INVALID")

print("=" * 45)