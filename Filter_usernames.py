from datetime import date
from typing import Dict, List, Any

def calculate_age(birth_date: str) -> int:
    birth_date = date.fromisoformat(birth_date)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_date = ("1988-05-04")
age = calculate_age(birth_date)
print(age)

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [user for user in users if calculate_age(user['birth_date']) >= 18]

def generate_username(first_name: str, last_name: str) -> str:
    first_letter = first_name[0].lower()
    last_name = last_name.lower()
    return f"{first_letter}.{last_name}"

users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]

filtered_users = filter_adults(users_data)
print(filtered_users)

unique_names = generate_username(users_data)
print(unique_names)

