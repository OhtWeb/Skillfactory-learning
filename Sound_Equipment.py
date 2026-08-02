class SoundEquipment:
    def __init__(self, state: bool = False):
        self.state = state
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False

class Microphone(SoundEquipment):
    def __init__(self, volume: int, state: bool = False):
        super().__init__(state)
        self.volume = volume if 0 <= volume <= 10 else 0
    def adjust_volume(self, volume: int):
        if 0 <= volume <= 10:
            self.volume = volume
            print(f'Volume is now: {self.volume}')

class Speaker(SoundEquipment):
    def __init__(self, bass: int, state: bool = False):
        super().__init__(state)
        self.bass = bass if 0 <= bass <= 10 else 0
    def adjust_bass(self, bass: int):
        if 0 <= bass <= 10:
            self.bass = bass
            print(f'Bass level is now: {self.bass}')

# Создаём объект микрофон с громкостью 5 состоянием "включен"
mic = Microphone(volume=5, state=True)
# Отключаем микрофон
mic.switch_off()
# Устаналиваем новый уровень громкости
mic.adjust_volume(7)

# Volume is now 7


# Создаём объект динамик с уровнем басов 7 и состоянием "выключен"
sp = Speaker(7, False)
# Включили динамик
sp.switch_on()
# Устанавливаем новый уровень басов
sp.adjust_bass(8)

# Bass level is now 8
