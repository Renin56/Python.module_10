from threading import Thread
from random import randint
from queue import Queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = self.find_free_table()
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол под номером {free_table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    # Если гость за столом закончил приём пищи
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'\033[1;30mСтол номер {table.number} свободен\033[0;30m')
                        table.guest = None  # Освобождаем стол

                        # Проверяем очередь
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

            sleep(1)  # Задержка для имитации обслуживания гостей


if __name__ == "__main__":
    cafe = Cafe(Table(1), Table(2), Table(3), Table(4), Table(5))

    # Создаем гостей
    guests = [
        Guest('Maria'), Guest('Oleg'), Guest('Vakhtang'), Guest('Sergey'), Guest('Darya'), Guest('Arman'),
        Guest('Vitoria'), Guest('Nikita'), Guest('Galina'), Guest('Pavel'), Guest('Ilya'), Guest('Alexandra')
    ]

    # Прибытие гостей в кафе
    cafe.guest_arrival(*guests)

    # Начинаем обсуждение (обслуживание) гостей
    cafe.discuss_guests()
