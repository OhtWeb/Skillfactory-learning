def binary_search(data_list, target):
    # Шаг 5: Если список пуст, значит, элемента нет
    if len(data_list) == 0:
        return False

    # Шаг 1: Определяем средний элемент
    mid = len(data_list) // 2
    guess = data_list[mid]

    # Шаг 2: Если нашли — возвращаем True
    if guess == target:
        return True

    # Шаг 3: Если искомое меньше — повторяем поиск в ЛЕВОЙ половине
    if target < guess:
        # Рекурсивный вызов: передаем список от начала до mid (не включая его)
        return binary_search(data_list[:mid], target)

    # Шаг 4: Если искомое больше — повторяем поиск в ПРАВОЙ половине
    else:
        # Рекурсивный вызов: передаем список от mid + 1 до конца
        return binary_search(data_list[mid + 1:], target)

print(binary_search([1,2,3,4,5,6,7,8,9,10], 15))