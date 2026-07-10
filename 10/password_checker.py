passwords = [
    "hunter2",
    "Admin123",
    "Password!",
    "qwerty",
    "DevOps2026!"
]

accepted_passwords = []
failed_passwords = []

# At least 8 characters 
# Contains a number 
# Contains uppercase letter

for password in passwords:
    length = len(password) >= 8
    if length < 8:
        failed_passwords.append(password)
    if password.isdigit():
        failed_passwords.append(password)

print(failed_passwords)