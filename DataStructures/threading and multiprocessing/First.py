import threading
from time import sleep

def func1():
    while True:
        sleep(0.5)

        print("hi")

def func2():
    while True:
        sleep(0.5)

        print("bye")

def func3():
    print("blanket")

t2=threading.Thread(target=func1)
t3=threading.Thread(target=func2)

t2.start()
sleep(0.25)
t3.start()

t2.join()
t3.join()
sleep(3)
print("MEEET")
func3()