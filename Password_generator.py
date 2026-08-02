import random

def create_password_generator(length, symbols):
    used_passwords = set()

    def generator():
        nonlocal used_passwords
        while True:
            password = ''.join(random.choice(symbols) for _ in range(length))
            if password not in used_passwords:
                used_passwords.add(password)
                return password

    return generator