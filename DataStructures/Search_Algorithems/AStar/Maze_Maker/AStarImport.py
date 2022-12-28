
#Does it work on a larger graph?


class PriorityQueue():
    def __init__(self):
        self.__array=[]

    def push(self,item):
        self.__array.append(item)
        # sort

        self.__array = sorted(self.__array, key=lambda tup: (tup[1]+tup[2], tup[1]))

        print("array")
        print(self.__array)

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
            if self.pq.isEmpty():
                break

            if node[2]==0:
                self.solvable==True
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
