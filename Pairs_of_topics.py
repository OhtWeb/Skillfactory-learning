races = ["альтмеры", "аргониане", "босмеры", "бретоны", "данмеры", "имперцы", "норды", "орки", "редгарды", "хаджиты"]
classes_ = ['Agent', 'Alchemist', 'Apothecary', 'Assassin', 'Barbarian', 'Battlemage', 'Bookseller', 'Buoyant Armiger', 'Caravaner', 'Champion', 'Clothier', 'Commoner', 'Dreamers', 'Drillmaster', 'Enchanter', 'Enforcer', 'Farmer', 'Gondolier', 'Guard Guild Guide', 'Healer', 'Herder', 'Hunter', 'Mabrigash', 'Mage', 'Mage Service', 'Master-at-Arms', 'Merchant', 'Miner', 'Monk', 'Necromancer', 'Nightblade', 'Noble', 'Ordinator', 'Ordinator Guard', 'Pauper', 'Pawnbroker', 'Priest', 'Publican', 'Savant', 'Scout', 'Sharpshooter', 'Shipmaster', 'Slave', 'Smith', 'Smuggler', 'Sorcerer', 'Thief', 'Trader', 'Warlock', 'Wise Woman', 'Witch']
fractions = ['Ashlanders', 'Blades', 'East Empire Company', 'Fighters Guild', 'Hlaalu', 'Imperial Cult', 'Imperial Legion', 'Mages Guild', 'Morag Tong', 'Redoran', 'Telvanni', 'Thieves Guild', 'Tribunal Temple', 'Clan Aundae', 'Clan Berne', 'Clan Quarra', 'Camonna Tong', 'Census and Excise', 'Dark Brotherhood', 'Hands of Almalexia', 'Royal Guard', 'Sixth House', 'Skaal', 'Talos Cult', 'Twin Lamps', 'Imperial Knights']
locations = ["Балмора", "Альд'рун", "Садрит Мора", "Вивек", "Морнхолд", "Хуул", "Альд Велоти", "Гнисис", "Молаг Мар", "Маар Ган", "Гнаар Мок", "Хла Оуд", "Сейда Нин", "Тель Вос", "Вос", "Тель Мора", "Тель Бранора", "Тель Арун", "Тель Фир", "Кальдера", "Пелагиад", "Суран", "Эбенгард", "Дагон Фел"]
def generate_topics(race_list, class_list, fraction_list, location_list):
    for race in race_list:
        for class_ in class_list:
            for fraction in fraction_list:
                for location in location_list:
                    yield race, class_, fraction, location
topic_generator = generate_topics(races, classes_, fractions, locations)
for i, topic in enumerate(topic_generator, 1):
    print(f'#{i}: {topic}')