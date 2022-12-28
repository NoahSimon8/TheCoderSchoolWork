
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

    def clear(self):
        self.__array.clear()
# q=Queue()
#
# q.push(7)
# q.push(8)
# q.push(9)
# q.pop()
# q.printQueue()



