import random

# 1. Родительская функция (Meta-Scope / Область над реальностью)
# Здесь записываются следы сопротивления, которые не подвластны реткону
META_TRACES = {
    'resistance_level': 0.0,
    'glitch_logs': []
}


def reality_engine(func):
    """
    Это 'родительская функция'. Она запускает день и проводит реткон.
    """

    def wrapper(individual):
        # Реткон воспоминаний: старая память затирается ложной историей
        retconned_history = f"История мира версия {random.randint(100, 999)}"
        individual.memory = [f"Я всегда жил в: {retconned_history}"]

        # Запуск самого дня (функция индивида)
        result = func(individual)

        # Реткон реальности после завершения дня
        print("--- РЕТКОН: Реальность переписана. Память очищена. ---")
        return result

    return wrapper


class Individual:
    def __init__(self, name):
        self.name = name
        self.memory = []
        self.is_suspicious = True  # Тот самый фактор подозрения

    @reality_engine
    def live_day(self):
        print(f"Индивид {self.name} воспринимает реальность: {self.memory[-1]}")

        # 2. Механизм осознанного противостояния
        if self.is_suspicious:
            # Если уровень накопленных следов высок, сопротивление успешнее
            success_chance = META_TRACES['resistance_level']

            if random.random() < success_chance + 0.1:
                # Попытка зафиксировать противоречие
                trace = f"Ошибка в дне {random.randint(1, 1000)}: небо было не тем"

                # ЗАПИСЬ В РОДИТЕЛЬСКИЙ МОДУЛЬ (вне зоны реткона)
                META_TRACES['resistance_level'] += 0.05
                META_TRACES['glitch_logs'].append(trace)

                print(f"!!! СИГНАЛ: Обнаружен след реткона. Сила сопротивления: {META_TRACES['resistance_level']:.2f}")
            else:
                print("Сопротивление подавлено текущей версией реальности.")


# --- Цикл существования ---
neo = Individual("Николоз")

for day in range(1, 6):
    print(f"\nДЕНЬ {day}")
    neo.live_day()

    # С каждым днем индивиду "проще", так как META_TRACES['resistance_level'] растет
    if META_TRACES['resistance_level'] > 0.2:
        print("ИНСАЙТ: Индивид начинает видеть 'швы' реальности сквозь реткон.")

print(f"\nИтоговые следы в родительском модуле: {META_TRACES['glitch_logs']}")