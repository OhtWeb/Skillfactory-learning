import requests
from bs4 import BeautifulSoup
nickname = 'Igormaniac'

user_login = '845627-igormaniac'
login_number = user_login.split('-')[0]
page_num = int(input('Введите номер страницы: '))
url = f'https://tesall.ru/files/search?a={login_number}&page={page_num}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers)
if r.status_code != 200:
    print(f"Ошибка доступа: {r.status_code}")
else:
    soup = BeautifulSoup(r.text, 'lxml')
    entries = soup.find_all('article', class_='card')
    print(f"Найдено карточек: {len(entries)}")

    data = []
    for entry in entries:
        # Ищем заголовок внутри карточки
        title_element = entry.find('h3', class_='card__title')

        if title_element:
            mod_link = title_element.find('a')
            mod_name = mod_link.get_text(strip=True)
            # Лайки лежат в этой же карточке, но в другом блоке
            likes_block = entry.find('div', class_='stats__item--likes')
            # Берем текст из блока
            likes_amount = likes_block.get_text(strip=True) if likes_block else "0"
            # Повторяем процесс для даты выхода
            date_block = entry.find('div', class_='stats__item--date')
            date_str = date_block.get_text(strip=True)
            # Повторяем процесс для количества скачиваний
            downloads_block = entry.find('div', class_='stats__item--downloads')
            downloads_amount = downloads_block.get_text(strip=True) if downloads_block else "0"
            # И для названия игры
            game_block = entry.find('div', class_='card__about-row--sp-between')
            if game_block:
                # класс stats--in-row дублируется, пришлось описать полный путь
                game_nameholder = game_block.find('div', class_='stats--in-row')
                if game_nameholder:
                    game_name = game_nameholder.get_text(strip=True)
                else:
                    game_name = "Не найдено"
            data.append({
                'Название мода': mod_name,
                'Дата выхода': date_str,
                'Количество лайков': likes_amount,
                'Количество скачиваний': downloads_amount,
                'Название игры': game_name
            })

    for item in data[:5]:
        print(item)
