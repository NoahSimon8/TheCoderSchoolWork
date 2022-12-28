from Linked_Lists.LinearLinkedLists import*

class Queue():
    def __init__(self):
        self.__array=LinkedLists()

    def push(self,item):
        self.__array.insertEnd(item)

    def isEmpty(self):
        if self.__array.length==0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty()==False:
            self.__array.deleteFront()
        else:
            print("UnderFLow Error, queue is empty")

    def Peak(self):
        if self.isEmpty()==False:
            return self.__array.head.data
        else:
            print("Can't Peak, queue is empty")
            return None

    def length(self):
        return self.__array.length

    def printQueue(self):
        self.__array.display()

    def clear(self):
        self.__array.deleteALL()
# q=Queue()
#
# q.push(7)
# q.push(8)
# q.push(9)
# q.pop()
# q.printQueue()
# print(q.Peak())
# q.clear()
# q.printQueue()


