
#Does it work on a larger graph?


class PriorityQueue():
    def __init__(self):
        self.__array=[]

    def push(self,item):
        self.__array.append(item)
        #sort
        self.__array = sorted(self.__array, key=lambda tup: tup[1] + tup[2])

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




Graph={
        "Ludendorff": [["Capital City", 50, 110],["San Fierro", 50, 100]],
        "San Fierro":[["Vice City",85,75], ["Capital City",45,110],["Bullworth", 30,45], ["Ludendorff", 50,165]],
        "Capital City":[["Vice City", 35, 75],["Las Venturas", 35, 150], ["Ludendorff", 50, 165],["San Fierro",45,100]],
        "Las Venturas": [["Capital City",35,110]],
        "Vice City":[["Capital City",35,110],["San Fierro",85,100],["Bullworth",85,45],["Vine Wood",30,25]],
        "Bullworth":[["San Fierro",30,100],["Vice City",85,75],["San Andreas", 15,60],["Carcer City",10,20],["Los Santos",45,0]],
        "San Andreas":[["Bullworth",15,45],["Los Santos", 60,0]],
        "Carcer City": [["Bullworth",10,45],["Los Santos",20,0],["Vine Wood",20,25]],
        "Vine Wood":[["Vice City",30,75],["Carcer City",20,20],["Los Santos",20,0]],
        "Los Santos":[["San Andreas",60,60],["Carcer City",20,20],["Bullworth",45,45],["Vine Wood",20,20]]
       }

class PathFinding():
    def __init__(self,graph):
        self.graph=graph
        self.pq=PriorityQueue()
        self.solvable=False
        self.parrents={}
        self.path=[]
    def AStar(self,node):
        node=[node,0,-1]
        self.parrents[node[0]]=node[0]
        self.pq.push(node)
        while True:
            print(node)
            if node[2]==0:
                break

            self.pq.pop()

            for neighbors in self.graph[node[0]]:
                neighbors[1]+=node[1]

            for neighbors in self.graph[node[0]]:
                self.pq.push(neighbors)
                """
                would work for breadth first search
                if neighbors[0] not in self.parrents:
                    self.parrents[neighbors[0]]=node[0]
                """
                if node[0] in self.parrents:
                    if neighbors[0] not in self.parrents[node[0]]:
                        self.parrents[neighbors[0]] = node[0]

            node=self.pq.Peak()

        #Path Tracing
        node = node[0]
        self.path.append(node)
        while True:
            if self.parrents[node]==node:
                break
            self.path.append(self.parrents[node]),
            node=self.parrents[node]
        self.path.reverse()
        return self.path
p=PathFinding(Graph)
print(p.AStar("Las Venturas"))