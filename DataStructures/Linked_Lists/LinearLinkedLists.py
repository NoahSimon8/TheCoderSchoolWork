


class Node:
    def __init__(self,d):
        self.data=d
        self.next=None



class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail=self.head
        self.length=0



    def insertEnd(self,d):
        if self.head==None:
            self.head=Node(d)
            self.tail=self.head
        else:
            self.tail.next=Node(d)
            self.tail=self.tail.next
        self.length+=1

    def insertFront(self,d):
        d=Node(d)
        d.next=self.head
        self.head=d
        self.tail = self.head
        self.length+=1

    def insertMiddle(self,pos,d):
        if self.head==None:
            self.head=Node(d)
            self.tail=self.head

        else:
            if pos<=0:
                self.insertFront(d)
            elif pos>=self.length:
                self.insertEnd(d)
            else:
                d=Node(d)
                cur=self.head
                for i in range(pos-1):
                    cur=cur.next
                d.next=cur.next
                cur.next=d
        self.length+=1





    def deleteEnd(self):
        if self.length!=0:
            if self.head==self.tail:
                self.head=None
                self.tail=None
                self.length-=1
            else:
                cur = self.head
                while cur.next != self.tail:
                    cur=cur.next
                self.tail=cur
                cur.next=None
                self.length-=1

    def deleteMiddle(self,pos):
        if self.length != 0:

            if pos<=0:
                self.deleteFront()
            elif pos>=self.length:
                self.deleteEnd()
            else:
                cur=self.head
                for i in range(pos-1):
                        cur=cur.next
                cur.next=cur.next.next
            self.length-=1


    def deleteFront(self):
        if self.length!=0:

            self.head=self.head.next
            self.length-=1

    def deleteALL(self):
        self.head=None
        self.tail=None
        self.length=0

    def reverse(self):
        if self.length!=0:
            self.tail = self.head
            prev = None
            while self.head.next:
                cur = self.head
                self.head = self.head.next
                cur.next=prev
                prev=cur
            self.head.next=prev

    def search(self,d):
        cur=self.head
        while cur:
            if cur.data==d:
                return True
            cur=cur.next
        return False


    def display(self):
        printlist=[]
        cur=self.head
        while cur:
            printlist.append(cur.data)
            cur=cur.next
        print(printlist)
    #
    # def test(self,tests):
    #     if "insert"in tests:
    #         self.insertFront(1)
    #         self.insertMiddle(1,2)
    #         self.insertEnd(3)
    #     if "delete" in tests:
    #         self.deleteMiddle(0)
    #         self.deleteFront()
    #         self.deleteEnd()
    #     self.reverse()
    #     self.search(1)
    #     self.display()

    def __str__(self):
        cur=self.head
        printing=""
        while cur:
            printing+=str(cur.data)
            if cur.next:
                printing+=" --> "
            cur=cur.next
        return printing

