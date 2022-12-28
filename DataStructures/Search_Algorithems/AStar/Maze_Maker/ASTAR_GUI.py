from tkinter import*
from Search_Algorithems.AStar.Maze_Maker.Matrix import*
import sys
# from Queues.queue import*
from time import sleep
# from AStar.Maze_Maker.AStarImport import PriorityQueue
sys.setrecursionlimit(1500)
class PriorityQueue:
    def __init__(self):
        self.__array = []

    def is_empty(self):
        return True if self.length() <= 0 else False

    def push(self, item):
        self.__array.append(item)
        #self.__array = sorted(self.__array , key=lambda tup: tup[1] + tup[2])
        self.__array = sorted(self.__array, key=lambda matrix: (matrix[-1][1] + matrix[-1][2], matrix[-1][2]))

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

###########################################

matrixClass=MakeMatrix()
matrix=None
squareDimensions=75
sizes= [5,10,15,20,25]
walls=[0,10,15,25,40,50,60,75,100,125,150,175,200]
speeds=["Slow","Normal","Fast","Instant"]
SPEED=0
selectedWalls=None
selectedSize=None
tracker={}

###########################################


class pathFinding():
    def __init__(self):
        self.graph={}
        self.solvable=False
        self.pq = PriorityQueue()
        self.parrents = {}
        self.visited = []
        self.path=[]
        self.size=None
        self.AmountWalls=None
    def findHeuristic(self,x,y):
        Hx=self.size-x
        Hy=self.size-y

        return Hx+Hy


    def makeGraph(self,matrix):
        for n,i in enumerate(matrix):
            for p,j in enumerate(i):
                if j!=0:
                    self.graph[str(j)]=[]
                    if matrix[n][p+1]!=0:
                        r=matrix[n][p+1]
                        self.graph[str(j)].append([str(r),1,self.findHeuristic(p+1,n)])
                    if matrix[n+1][p]!=0:
                        u=matrix[n+1][p]
                        self.graph[str(j)].append([str(u),1,self.findHeuristic(p,n+1)])
                    if matrix[n][p-1]!=0:
                        l=matrix[n][p-1]
                        self.graph[str(j)].append([str(l),1,self.findHeuristic(p-1,n)])
                    if matrix[n-1][p]!=0:
                        d=matrix[n-1][p]
                        self.graph[str(j)].append([str(d),1,self.findHeuristic(p,n-1)])

    def AStar(self,start):
        self.pq.push([[str(start), 0, 165]])

        while not self.pq.is_empty() :
        # for i in range(200):
            top = self.pq.pop()  # Pop Queue & return Node with lowest Cost
            # print(top[-1])

            city = top[-1][0]  # City
            g_val = top[-1][1]  # G-value
            count=0
            for i in top:
                if i[0]=="1":
                    count+=1
            if count>=2:
                self.solvable==False
                break

            # if city in self.path:
            #     break
            if city not in self.path:
                self.path.append(city)
            if top[-1][2]==0:  # End if Reached Target
                self.solvable=True
                break;
            for adj in self.graph.get(city, []):  # Loop through neighbors
                adj[1] += g_val  # Update G-values for neighbors
                new_path = top.copy()
                new_path.append(adj)
                self.pq.push(new_path)  # Place neighbor in priority queue
        quick = []
        for i in top:
            quick.append(int(i[0]))
        slow=[]
        for i in self.path:
            slow.append(int(i))
        self.visited=quick
        self.path=slow
        return quick


p = pathFinding()


###########################################

def MakeSize(value):
    global matrix,squareDimensions,selectedSize
    selectedSize=value

    previousSize=matrixClass.Size
    matrixClass.getSize(value)
    if (matrixClass.Size**2)-2<matrixClass.AmountWalls:
        matrixClass.Size=previousSize
    if matrixClass.Size==5:
        squareDimensions=75
    elif matrixClass.Size==10:
        squareDimensions=50
    elif matrixClass.Size==15:
        squareDimensions=35
    elif matrixClass.Size==20:
        squareDimensions=30
    elif matrixClass.Size==25:
        squareDimensions=25
    canvas.delete("all")
    canvas.config(width=squareDimensions * (matrixClass.Size + 2), height=squareDimensions * (matrixClass.Size + 2))
    MakeMatrix()
    MakeWalls()
    MakeMaze()


def Walls(value):
    global matrix, selectedWalls
    # value=8
    selectedWalls=value
    MakeMatrix()
    matrixClass.getAmountWalls(value)
    if matrixClass.AmountWalls>(matrixClass.Size**2)-2:
        matrixClass.AmountWalls=0
    MakeWalls()
    MakeMaze()
    window.update()
    try:
        if IsSolvable()==False:
            Walls(value)
    except:
        print("1500 atempt limit reached")

def Speeds(value):
    global SPEED
    if value=="Slow":
        SPEED=0.1
    elif value=="Normal":
        SPEED=0.01
    elif value=="Fast":
        SPEED=0.001
    elif value=="Instant":
        SPEED=0



def MakeMatrix():
    global matrix
    matrix=matrixClass.Matrix()

def MakeWalls():
    global matrix
    matrix=matrixClass.Walls()



###########################################
def MakeMaze():
    global tracker
    tracker={}
    canvas.delete("all")

    for n,i in enumerate(matrix):
        for j, r in enumerate(i):
            xPos=j*squareDimensions
            yPos=n*squareDimensions
            tracker[r]=(xPos,yPos)

            if r==0:
                canvas.create_rectangle(j*squareDimensions,n*squareDimensions,(j*squareDimensions)+squareDimensions,(n*squareDimensions)+squareDimensions,fill="black",outline="black")

            else:
                canvas.create_rectangle(j*squareDimensions,n*squareDimensions,(j*squareDimensions)+squareDimensions,(n*squareDimensions)+squareDimensions,fill="white",outline="black")
    canvas.create_rectangle(squareDimensions,squareDimensions,squareDimensions*2,squareDimensions*2,fill="Green")
    canvas.create_rectangle(matrixClass.Size*squareDimensions,(len(matrix)-2)*squareDimensions,(matrixClass.Size*squareDimensions)+squareDimensions,((len(matrix)-2)*squareDimensions)+squareDimensions,fill="red")

###########################################
notsolvable=None
def IsSolvable():
    global p, notsolvable
    p = pathFinding()
    p.graph = {}
    p.visited = []
    p.solvable=False
    p.size=matrixClass.Size
    p.AmountWalls=matrixClass.AmountWalls
    p.path=[]
    p.parrents = {}
    notsolvable = Label(window, text="                                                       ", font=("arial", 25, "bold"))
    notsolvable.grid(row=51, columnspan=51, pady=8)


    p.makeGraph(matrix)
    p.AStar(matrix[1][1])



    if p.solvable==True:
        return True
    else:
        return False

def start():
    global notsolvable
    if IsSolvable():
        for i in p.path:
            canvas.create_rectangle(squareDimensions, squareDimensions, squareDimensions * 2, squareDimensions * 2,
                                    fill="Green")
            canvas.create_rectangle(matrixClass.Size * squareDimensions, (len(matrix) - 2) * squareDimensions,
                                    (matrixClass.Size * squareDimensions) + squareDimensions,
                                    ((len(matrix) - 2) * squareDimensions) + squareDimensions, fill="red")
            if SPEED != 0:
                sleep(SPEED)
                window.update()
            #Show Vision
            # canvas.create_rectangle(tracker[i][0], tracker[i][1], (tracker[i][0]) + squareDimensions,
            #                         (tracker[i][1]) + squareDimensions, fill="yellow", outline="black")
        canvas.create_rectangle(squareDimensions, squareDimensions, squareDimensions * 2, squareDimensions * 2,
                                fill="Green")
        canvas.create_rectangle(matrixClass.Size * squareDimensions, (len(matrix) - 2) * squareDimensions,
                                (matrixClass.Size * squareDimensions) + squareDimensions,
                                ((len(matrix) - 2) * squareDimensions) + squareDimensions, fill="red")


        for i in p.visited:
            canvas.create_rectangle(squareDimensions, squareDimensions, squareDimensions * 2, squareDimensions * 2,fill="Green")
            canvas.create_rectangle(matrixClass.Size * squareDimensions, (len(matrix) - 2) * squareDimensions,(matrixClass.Size * squareDimensions) + squareDimensions,((len(matrix) - 2) * squareDimensions) + squareDimensions, fill="red")
            if SPEED!=0:
                sleep(SPEED)
                window.update()
            canvas.create_rectangle(tracker[i][0], tracker[i][1], (tracker[i][0]) + squareDimensions,(tracker[i][1]) + squareDimensions, fill="blue", outline="black")
        canvas.create_rectangle(squareDimensions,squareDimensions,squareDimensions*2,squareDimensions*2,fill="Green")
        canvas.create_rectangle(matrixClass.Size*squareDimensions,(len(matrix)-2)*squareDimensions,(matrixClass.Size*squareDimensions)+squareDimensions,((len(matrix)-2)*squareDimensions)+squareDimensions,fill="red")

    else:
        notsolvable=Label(window,text="Not Solvable",font = ("arial", 25, "bold"))
        notsolvable.grid(row=51,columnspan=51,pady=8)

###########################################

window = Tk()
window.geometry("1000x800+0-10")

settingsFrame = LabelFrame(window, text="Change Settings")
settingsFrame.grid(row=0, column=0,padx=10,pady=10)

canvas = Canvas(window, width=squareDimensions * (matrixClass.Size + 2), height=squareDimensions * (matrixClass.Size + 2), background="white")
canvas.grid(row=1, column=0, padx=10, pady=10)
MakeMatrix()
MakeMaze()



sizeLabel=Label(settingsFrame,text="Size:")
sizeLabel.grid(row=0,column=0)


wallsLabel=Label(settingsFrame,text="Amount of Walls:")
wallsLabel.grid(row=1,column=0)


speedLabel=Label(settingsFrame,text="Speed:")
speedLabel.grid(row=2,column=0)



defaultSize=StringVar(window)
defaultSize.set(sizes[0])
sizeButton=OptionMenu(settingsFrame, defaultSize, *sizes,command=MakeSize)
sizeButton.grid(row=0,column=1)


defaultWalls=StringVar(window)
defaultWalls.set(walls[0])
wallsButton=OptionMenu(settingsFrame, defaultWalls, *walls,command=Walls)
wallsButton.grid(row=1,column=1)



defaultSpeed=StringVar(window)
defaultSpeed.set("Instant")
speedButton=OptionMenu(settingsFrame,defaultSpeed, *speeds, command=Speeds)
speedButton.grid(row=2,column=1)

startButton=Button(settingsFrame,text="Start",command=start)
startButton.grid(row=0,column=2,rowspan=2,padx=5)

window.mainloop()
###########################################
