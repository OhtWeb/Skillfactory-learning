phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
    digits = "".join(filter(str.isdigit, number))
    return digits
formatted_numbers = list(map(format_phone_number, phone_numbers))
print(list(formatted_numbers))
