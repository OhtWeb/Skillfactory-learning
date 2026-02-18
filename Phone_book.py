Phones_book = {'Key':'123', 'Lancelot':'456', 'Galahad':'789', 'Parsifal': '951'}
print(Phones_book.keys())
print(Phones_book.values())
for key, value in Phones_book.items():
    print(f'{key}: {value}')
Name = input('Введите запись, которую хотите удалить: ')
if Name in Phones_book.keys():
    print(f'Удаляем из словаря: {Name} - {Phones_book[Name]}')
    del Phones_book[Name]
else:
    print('Этого имени в книге нет')
        # выводим полученный словарь
print(f'Полученный справочник: {Phones_book}')
Name = input('Введите имя, которое хотите добавить: ')
if Name in Phones_book.keys():
    print('Это слово уже есть в справочнике')
else:
    phone=input('Введите номер телефона: ')
    Phones_book[Name] = phone
Phones_book['Sagamore'] = '242352'
Phones_book['Lohengrin'] = '99644'
for key, value in Phones_book.items():
    print(f'{key}: {value}')