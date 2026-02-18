def check_password(password):
    if len(password) < 8:
        print('Пароль должен быть не менее 8 символов')
    if not any(char.isupper() for char in password):
        print('Пароль должен содержать хотя бы одну заглавную букву')
    if not any(char.islower() for char in password):
        print('Пароль должен содержать хотя бы одну строчную букву')
    if not any(char.isdigit() for char in password):
        print('Пароль должен содержать хотя бы одну цифру')
    else:
        print()
check_password("--")