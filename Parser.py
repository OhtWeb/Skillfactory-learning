import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

input_date = input('Введите дату в формате дд.мм.гггг: ')
date_obj = datetime.strptime(input_date, "%d.%m.%Y")
new_date_str = date_obj.strftime("%Y-%m-%d")
url = f'https://www.kinoafisha.info/russia/spb/movies/?date={new_date_str}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers)
if r.status_code != 200:
    print(f"Ошибка доступа: {r.status_code}")
else:
    soup = BeautifulSoup(r.text, 'lxml')
    entries = soup.find_all('div', class_='movieList_item')
    print(f"Найдено фильмов: {len(entries)}")

    data = []
    for entry in entries:
        title_element = entry.find('a', class_='movieItem_title')
        if title_element:
            film_title = title_element.text
            film_genre = entry.find('span', class_='movieItem_genres').text
            mark = entry.find('span', class_='mark_num').text
            release_date_country = entry.find('span', class_='movieItem_year').text
            release_date = release_date_country.split(',')[0]
            release_country = release_date_country.split(',')[1]
            data.append({
                'Название фильма': film_title,
                'Жанр': film_genre,
                'Оценка': mark,
                'Дата выхода': release_date,
                'Страна выпуска': release_country
            })
    print(f'{input_date} в кинотеатрах С-пб демонстрируются следующие фильмы:')
    for item in data [:5]:
        print(item)
    movies_release = pd.DataFrame(data)
    movies_release.to_excel('Movies.xlsx', index=False)
    movies_release.to_csv('Movies.csv', index=False, encoding='utf-8')

    print("Файлы Movies.xlsx, Movies.csv созданы в папке с проектом.")