import random
def generate_user_data(size, first_names, last_names, age_range):
    for _ in range(size):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(age_range[0], age_range[1])
        yield (first_name, last_name, age)
user_data_generator = generate_user_data(3, "", "", [15, 64])
for user in user_data_generator:
    print(user)