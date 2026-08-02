class User:
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance
    def login(self, email, password):
        if email and password and self.email == email and self.password == password:
            return True
        else:
            return False
    def update_balance(self, amount):
        self.balance += amount

user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# False
print(user.login("gosha@roskino.org", "qwerty"))
# True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# 19700
