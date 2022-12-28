from random import*
from time import*
import threading


class Queue:
    def __init__(self):
        self.__array = []

    def is_empty(self):
        return True if self.length() <= 0 else False

    def push(self, item):
        self.__array.append(item)

    def pop(self):
        if not self.is_empty():
            self.__array.pop(0)
        else:
            print("Underflow Error, Queue is Empty.")

    def peak(self):
        if not self.is_empty():
            return self.__array[0]
        else:
            print("Can't peak, Queue is empty")
            return None

    def length(self):
        return len(self.__array)

    def print_queue(self):
        print(self.__array)



class Person:
    def __init__(self, i, p):
        self.ID = i
        self.pages = p
        self.print_time = self.pages * uniform(0.05, 0.3)
        self.total_print_time = 0

    def request(self):
        print(f'\033[34mPerson {self.ID} -> {self.pages} -> print time -> {round(self.print_time,2)}'
              f' -> \033[0m\033[31mtotal time -> {round(self.total_print_time,2 )}\033[0m')

    def finished(self):
        print(f'\033[32mPerson {self.ID} -> finished')





def enqueue():
    global count, total_time
    for i in range(100):
        count += 1
        amount = randint(1, 30)
        p = Person(count, amount)
        p.total_print_time = total_time + p.print_time
        total_time = p.total_print_time
        p.request()
        q.push(p)
        sleep(0.5)


def dequeue():
    global total_time
    for i in range(100):
        if not q.is_empty():
            person = q.peak()
            sleep(person.print_time)
            total_time -= person.print_time
            person.finished()
            q.pop()



q = Queue()

total_time = 0
count = 0


t1 = threading.Thread(target=enqueue)
t2 = threading.Thread(target=dequeue)

t1.start()
sleep(0.25)
t2.start()

t1.join()
t2.join()


