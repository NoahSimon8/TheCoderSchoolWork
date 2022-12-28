class PriorityQueue:
    def __init__(self):
        self.__array = []

    def is_empty(self):
        return True if self.length() <= 0 else False

    def push(self, item):
        self.__array.append(item)
        #self.__array = sorted(self.__array , key=lambda tup: tup[1] + tup[2])
        self.__array = sorted(self.__array, key=lambda matrix: matrix[-1][1] + matrix[-1][2])

    def pop(self):
        if not self.is_empty():
            return self.__array.pop(0)
        else:
            print("Underflow Error, Queue is Empty.")

    def peak(self):
        if not self.is_empty():
            return self.__array[0]
        else:
            print("Can't peak, Queue is empty")
            return None

    def length(self):
        return len(self.__array)

    def print_queue(self):
        print(self.__array)


graph={
        "Ludendorff": [["Capital City", 50, 110],["San Fierro", 50, 100]],
        "San Fierro":[["Vice City",85,75-100], ["Capital City",45,110],["Bullworth", 30,45], ["Ludendorff", 50,165]],
        "Capital City":[["Vice City", 35, 75],["Las Venturas", 35, 150], ["Ludendorff", 50, 165],["San Fierro",45,100]],
        "Las Venturas": [["Capital City",35,110]],
        "Vice City":[["Capital City",35,110],["San Fierro",85,100],["Bullworth",85,45],["Vine Wood",30,25]],
        "Bullworth":[["San Fierro",30,100],["Vice City",85,75],["San Andreas", 15,60],["Carcer City",10,20],["Los Santos",45,0]],
        "San Andreas":[["Bullworth",15,45],["Los Santos", 60,0]],
        "Carcer City": [["Bullworth",10,45],["Los Santos",20,0],["Vine Wood",20,25]],
        "Vine Wood":[["Vice City",30,75],["Carcer City",20,20],["Los Santos",20,0]],
        "Los Santos":[["San Andreas",60,60],["Carcer City",20,20],["Bullworth",45,45],["Vine Wood",20,20]]
       }


pq = PriorityQueue()
path = []


def a_star(start, end):
    pq.push([[start, 0, 165]])
    while not pq.is_empty():

        top = pq.pop()                      # Pop Queue & return Node with lowest Cost
        city = top[-1][0]                   # City
        g_val = top[-1][1]                  # G-value
        path.append(city)

        if city == end:                     # End if Reached Target
            break;
        for adj in graph.get(city, []):     # Loop through neighbors
            adj[1] += g_val                 # Update G-values for neighbors
            new_path = top.copy()
            new_path.append(adj)
            pq.push(new_path)               # Place neighbor in priority queue

    quick=[]
    for i in top:
        quick.append(i[0])
    # print(quick)                              # print shortest path



a_star("Ludendorff", "Los Santos")
print(path)                                 # print all nodes visited



# queue = [[["Ludendorff", 50, 110], ["San Fierro", 50, 100]],
#          [["retard", 50, 110], ["Capital City", 50, 110]]]



