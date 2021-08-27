# 1 задание
def add_cart():
    number = input("Введите номер карты: ")
    print(12 * "*",number[12:16])


# 2 задание
def pal():
    a = input("Введите слово")
    if a.isalpha():
        if a == a[::-1]:
            print("Это палиндром")
        else:
            print('Это не палиндром')
    else:
        print("Введите пожалуйста слово")


class Tomato:

    states = {0: 'Ничего нет', 1: 'Цветение', 2: 'Зеленый томат', 3: 'Красный томат'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Томат {self._index} сейчас {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num-1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник окончил работу')

    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая окончен')
        else:
            print('Ваши томаты еще не созрели')

    @staticmethod
    def knowledge_base():
        print("С агрономической точки зрения самое лучшее время для уборки плодов томата наступает в момент, когда 85-90 % плодов имеют красную или почти красную окраску.")
        print('Однако содержание аскорбиновой кислоты и каротиноидов более высокое в очень красных плодах, т. е. в полностью созревших. В них содержание каротина в три раза выше, чем в бурых плодах.')
        print('Поэтому с точки зрения биологической полноценности питания следует употреблять в пищу полностью созревшие плоды томата.')


if __name__ == '__main__':
    Gardener.knowledge_base()
    tomato_bush = TomatoBush(6)
    gardener = Gardener('Александр', tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()




