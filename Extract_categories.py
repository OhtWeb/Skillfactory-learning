def extract_categories(categories, parent_path=''):
    paths = []
    for key, value in categories.items():
        current_path = f"{parent_path}/{key}" if parent_path else key
        paths.append(current_path)
        if isinstance(value, dict):
            paths.extend(extract_categories(value, current_path))

    return paths

categories = {
   "Электроника": {
       "Телефоны": {
           "Смартфоны": {},
           "Проводные": {}
       },
       "Компьютеры": {
           "Ноутбуки": {},
           "Стационарные": {
               "Игровые": {},
               "Для работы": {}
           }
       }
   },
   "Одежда": {
       "Мужская": {
           "Джинсы": {},
           "Куртки": {}
       }
   }
}
paths = extract_categories(categories, parent_path='root')
for path in paths:
   print(path)