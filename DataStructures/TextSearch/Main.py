#  AVL Tree, Linked lists, . and operator overloading
#hashtables
from Linked_Lists.LinearLinkedLists import *
from BinarySearchTrees.AVL.AVL import*
from Hash_Tables.HashTable import *

class Word:
    def __init__(self,word,line=0,spot=0):
        self.word=word
        self.lst = LinkedLists()
        self.lst.insertEnd((line,spot))
        self.count=1



    def __lt__(self, other):
        return self.word<other.word

    def __le__(self, other):
        return self.word<=other.word

    def __gt__(self, other):
        return self.word>other.word

    def __ge__(self, other):
        return self.word>=other.word

    def __eq__(self, other):
        return self.word==other.word

    def __ne__(self, other):
        return self.word!=other.word

    def __str__(self):
        return self.word

def clean(line):

    ommit = "`~!@#$%^&*()_+-={}[]|:;'<,>.?\\\""
    line2 = []
    for word in line:
        word = word.replace("\n", "")
        for c in ommit:
            word = word.replace(c, "")
        if word!="":
            word=word.lower()
            line2.append(word)
    return line2

def omit(dictionary):
    with open("Common","r") as file:
        for line in file:
            dictionary.insert(line.replace("\n",''))

dictionary=HashTable()
avl=AVLTree()
omit(dictionary)

ll = LinkedLists()

passage=""
with open("passage","r") as file:
    n=1
    for line in file:
        line=clean(line.split())
        # print(line)

        j=1
        for word in line:
            if not dictionary.search(word):
                object=Word(word,n,j)
                searched=avl.search(object)
                if not searched:
                    avl.insert(object)
                else:
                    searched.count += 1
                    searched.lst.insertEnd((n,j))
            j+=1
        n+=1
# print(avl.root.left.data)
# print(avl.root.left.data.count)
# print(avl.root.left.data.lst)
# print(avl)
while True:
    userInput=input("enter a word to search:")
    found=avl.search(Word(userInput))
    if found:
        print(found.word, "; Occurences: "+str(found.count))
        print(found.lst)
        print()