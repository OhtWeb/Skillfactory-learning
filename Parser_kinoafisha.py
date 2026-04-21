import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

print("Доброго дня! Для оптимального результата давайте уточним Ваши предпочтения.")

#В настоящее время функционал программы поддерживает только три города и только в РФ
input_city = int(input('''Выберите интересующий Вас город. 
                          Для Москвы введите «1»
                          Для Санкт-Петербурга введите «2»
                          Для Новосибирска введите «3»: '''))
if input_city == 1:
    city = 'msk'
elif input_city == 2:
    city = 'spb'
elif input_city == 3:
    city = 'nsk'
else:
    print('Ошибка ввода, производим поиск по Москве')
    city = 'msk'

while True:
    input_date = input('Введите дату киносеанса в формате дд.мм.гггг: ')
    try:
        date_obj = datetime.strptime(input_date, "%d.%m.%Y")
        new_date_str = date_obj.strftime("%Y-%m-%d")
        break
    except ValueError:
        print('Ошибка ввода даты, пожалуйста, используйте формат дд.мм.гггг')


input_sort = int(input('''Для сортировки фильмов по рейтингу введите «1» 
Для сортировки по названию введите «2» 
Для сортировке по популярности введите «3»: '''))
if input_sort == 1:
    sort_path = 'rating/'
elif input_sort == 2:
    sort_path = 'name/'
elif input_sort == 3:
    sort_path = ''
else:
    print('Ошибка ввода, используем стандартную сортировку')
    sort_path = ''

#Основной функционал программы начинается здесь:
url = f'https://www.kinoafisha.info/russia/{city}/movies/{sort_path}/?date={new_date_str}'
#Притворяемся, что мы настоящий браузер:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers)
#Сразу проверяем, есть ли отклик от сервера и какой:
if r.status_code != 200:
    print(f"Ошибка доступа: {r.status_code}")
else:
    soup = BeautifulSoup(r.text, 'lxml')
    #Ищем на странице перечень фильмов и выводим их количество
    entries = soup.find_all('div', class_='movieList_item')
    print(f"Найдено фильмов: {len(entries)}")

    data = []
    for entry in entries:
        #Ищем название фильма
        title_element = entry.find('a', class_='movieItem_title')
        if title_element:
            #Извлекаем название фильма в текстовом формате
            film_title = title_element.text
            #Повторяем процедуру для жанра
            film_genre = entry.find('span', class_='movieItem_genres').text
            # -для оценки
            mark = entry.find('span', class_='mark_num').text
            # -для даты релиза и страны происхождения
            release_date_country = entry.find('span', class_='movieItem_year').text
            # Так как на сайте дата и страна слиты воедино, разделяем их
            parts = release_date_country.split(',')
            release_date = parts[0].strip()
            release_country = parts[1].strip() if len(parts) > 1 else 'не указана'
            #Составляем лист по парам ключ-значение
            data.append({
                'Название фильма': film_title,
                'Жанр': film_genre,
                'Оценка': mark,
                'Дата выхода': release_date,
                'Страна выпуска': release_country
            })
    print(f'{input_date} в кинотеатрах указанного города демонстрируются следующие фильмы:')
    #Выводим в консоль первые пять фильмов в зависимости от выбранной сортировки
    for item in data [:5]:
        print(item)
    #Выводим отсортированные выбранным способом фильмы в файл
    movies_release = pd.DataFrame(data)
    movies_release.to_excel('Movies.xlsx', index=False)
    movies_release.to_csv('Movies.csv', index=False, encoding='utf-8')

    print("Файлы Movies.xlsx, Movies.csv созданы в папке с проектом.")