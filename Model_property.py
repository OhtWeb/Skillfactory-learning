class Model:
    Name_Min_Len = 3
    Name_Max_Len = 15
    def __init__(self):
        self.__name = None
    @classmethod
    def __validate_name(cls, name):
        # Сначала проверяем тип, потом длину
        if isinstance(name, str) and cls.Name_Min_Len <= len(name) <= cls.Name_Max_Len:
            return True
        return None  # Явно возвращаем None при ошибке
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        # Записываем значение только если валидатор вернул True
        if self.__validate_name(value):
            self.__name = value