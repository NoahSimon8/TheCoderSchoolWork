
class Node:
    def __init__(self,d,k):
        self.value=k
        self.key=d

    def display(self):
        return (self.key,self.value)

class PlaceHolder():
    def __str__(self):
        return "Place-Holder"

class HashTable:
    def __init__(self):
        self.size=2
        self.array=[None for i in range(self.size)]
        self.length=0

    def hash(self,key):
        realkey=key
        if isinstance(key,str):
            if key=="":
                key=1000
            else:
                key=ord(key[0])*ord(key[-1])
        i=-1
        for i in range(100):
            i+=1

            key2=(key+i)%self.size
            if not isinstance(self.array[key2],PlaceHolder):
                if self.array[key2]==None:
                    return key2
                if self.array[key2].key==realkey:
                    return key2
            # if i>0:
            #     print("Collision")

    def insert(self,key,value=None):
        self.array[self.hash(key)]=Node(key,value)
        self.length+=1
        self.CheckSize()

    def CheckSize(self):
        if (self.size/4)*3 <self.length:
            self.size*=2
            self.rehash()
        if (self.size/4) > self.length:
            self.size=int(self.size/2)
            self.rehash()

    def rehash(self):
        prev_array = self.array
        self.array = [None for _ in range(self.size)]
        for item in prev_array:
            if item is not None and not isinstance(item,PlaceHolder):
                index = self.hash(item.key)
                self.array[index] = item

    def search(self,key):
        if self.array[self.hash(key)]==None and not isinstance(self.array[self.hash(key)],PlaceHolder):
            return False
        return True

    def delete(self,key):
        if self.array[self.hash(key)] != None and not isinstance(self.array[self.hash(key)],PlaceHolder):
            self.array[self.hash(key)]=PlaceHolder()
        self.length-=1
        self.CheckSize()

    def display(self):
        length = 25
        for i, item in enumerate(self.array):
            print(f"\t|{'-' * length}|")
            if item is not None and not isinstance(item,PlaceHolder):
                dashes = length - (len(str(item.key)) + len(str(item.value))) - 3
                print(f"{i}\t|", item.key, item.value, f"{' ' * dashes}|")
            else:
                dashes = length - 3 - 3
                print(f"{i}\t|", item.__str__(), f"{' ' * dashes}|")
        print(f"\t|{'-' * length}|")


