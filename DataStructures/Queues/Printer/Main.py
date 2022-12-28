from random import*
from time import sleep
import threading
TotalTime=0
TimePast=0
sleepTime=0
class Queue():
    def __init__(self):
        self.__array=[]

    def push(self,item):
        self.__array.append(item)

    def isEmpty(self):
        if self.__array==[]:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty()==False:
            self.__array.pop(0)
        else:
            print("UnderFLow Error, stack is empty")
    def Peak(self):
        if self.isEmpty()==False:
            return self.__array[0]
        else:
            print("Can't Peak, stack is empty")
            return None

    def length(self):
        return len(self.__array)

    def printQueue(self):
        print(self.__array)

q=Queue()

class Person():
    def __init__(self,ID,P,T):
        self.ID=ID
        self.Pages=P
        self.PrintTime=round(self.Pages*uniform(0.1,0.4),2)
        self.TotalTime=round(T+self.PrintTime,2)

    def PrintInfo(self):
        print(self.ID+": "+str(self.Pages)+" Pages; "+str(self.PrintTime)+"sec; Total Time: "+str(self.TotalTime))

    def TotalTimeUpdate(self):
        return self.TotalTime

def func1():
    global TimePast, TotalTime, sleepTime
    for i in range(20):
        sleepTime=round(uniform(0.2,1),2)
        print(sleepTime)
        sleep(sleepTime)

        pages=randint(1,100)
        if pages>30:
            pages = randint(1, 100)
        if pages>50:
            pages = randint(1, 100)
        if pages>80:
            pages = randint(1, 100)

        p=Person("Person %d"%(i+1),pages,TotalTime)
        q.push(p)
        TotalTime=p.TotalTimeUpdate()
        TotalTime-=sleepTime
        p.PrintInfo()
        # print(TotalTime)
        if TimePast>=q.Peak().TotalTime:
            print(q.Peak().ID+" is complete")
            TotalTime-=q.Peak().PrintTime

            q.pop()


def func2():
    global TimePast, sleepTime
    sleep(0.01)
    TimePast+=0.01
t3=threading.Thread(target=func2)

t2=threading.Thread(target=func1)

t2.start()
t3.start()
t2.join()
t3.join()
