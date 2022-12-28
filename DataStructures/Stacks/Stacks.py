from random import*


class Stack():
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
            self.__array.pop()
        else:
            print("UnderFLow Error, stack is empty")
    def peak(self):
        if self.isEmpty()==False:
            return self.__array[-1]
        else:
            print("Can't Peak, stack is empty")
            return None

    def length(self):
        return len(self.__array)

    def printStack(self):
        print(self.__array)



s=Stack()
# var="(3+(4-3)+((9-2)-8))"
# for i in var:
#     if i =="(":
#         s.push(i)
#     elif i ==")":
#         s.pop()
# if s.length()==0:
#     print("is valid")
# else:
#     print("Not valid")

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.printStack()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.printStack()