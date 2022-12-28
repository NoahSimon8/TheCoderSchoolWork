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

operand=Stack()
operator=Stack()
LstOperator=["+","-","*","/","%"]
equ="(5+((4/2)*(2-3)))"
for i in equ:
    print("operand:")
    operand.printStack()
    # print("operator:")
    # operator.printStack()

    if i.isdigit():
        i=int(i)
        operand.push(i)
    elif i in LstOperator:
        operator.push(i)
    elif i ==")":
        var1=operand.peak()
        operand.pop()
        var2=operand.peak()
        operand.pop()
        if operator.peak()=="+":
            operator.pop()
            total=var1+var2
            operand.push(total)
        elif operator.peak()=="-":
            operator.pop()
            total=var2-var1
            operand.push(total)
        elif operator.peak()=="*":
            operator.pop()
            total=var1*var2
            operand.push(total)
        elif operator.peak()=="/":
            operator.pop()
            total=var2/var1
            operand.push(total)
        elif operator.peak()=="%":
            operator.pop()
            total=var2%var1
            operand.push(total)
operand.printStack()
operator.printStack()

