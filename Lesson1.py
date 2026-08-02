class PasswordChecker:
    def __init__(self, min_len: int = 5, max_len: int = 10):
        self.min_len = min_len
        self.max_len = max_len

    def _is_valid(self, password: str) -> bool:
        """Вспомогательный метод для проверки одного пароля"""
        checks = [
            self.min_len <= len(password) <= self.max_len, # Проверка длины
            any(char.isdigit() for char in password),      # Есть цифра
            any(char.isupper() for char in password),      # Есть заглавная буква
            any(char.islower() for char in password),      # Есть строчная буква
        ]
        # all() вернет True, только если ВСЕ элементы в списке True
        return all(checks)

    def check_passwords_list(self, passwords_list: list) -> list:
        # Теперь генератор списка выглядит идеально чисто
        return [pwd for pwd in passwords_list if self._is_valid(pwd)]

checker = PasswordChecker(5, 15)
print(checker.check_passwords_list(['qwer', 'Fool67', 'gHjo478hl404', 'FastLegs1']))