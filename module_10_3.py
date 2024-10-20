from random import randint
from threading import Thread, Lock
from time import sleep


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            x = randint(50, 500)
            self.balance += x

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            print(f'Пополнение {_ + 1}: на {x}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            x = randint(50, 500)
            print(f'Запрос {_ + 1}: на {x}')

            if x <= self.balance:
                self.balance -= x
                print(f'Снятие {_ + 1}: {x}. Баланс: {self.balance}')
            else:
                print(f'Запрос {_ + 1} отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
