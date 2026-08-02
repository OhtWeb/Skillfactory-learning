def is_valid_email(email):
    if email.count('@') == 1 and email.count(' ') == 0 and '.' in email[email.index('@')::]:
        return True
    else:
        return False
result = is_valid_email('ungabunga@gmailcom')
print(result)