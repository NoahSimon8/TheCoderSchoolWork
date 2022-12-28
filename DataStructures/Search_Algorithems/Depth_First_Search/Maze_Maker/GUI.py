from tkinter import*
from Search_Algorithems.Depth_First_Search.Maze_Maker.Matrix import*
from Queues.queue import*
from time import sleep

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
        self.visited=[]
        self.solvable=False
        self.queue=Queue()

    def makeGraph(self,matrix):
        for n,i in enumerate(matrix):
            for p,j in enumerate(i):
                if j!=0:
                    self.graph[j]=[]
                    if matrix[n][p+1]!=0:
                        r=matrix[n][p+1]
                        self.graph[j].append(r)
                    if matrix[n+1][p]!=0:
                        u=matrix[n+1][p]
                        self.graph[j].append(u)
                    if matrix[n][p-1]!=0:
                        l=matrix[n][p-1]
                        self.graph[j].append(l)
                    if matrix[n-1][p]!=0:
                        d=matrix[n-1][p]
                        self.graph[j].append(d)

    def depthFirstSearch(self,current,end):
        if self.solvable or current in self.visited:
            return
        else:
            if current==end:
                self.solvable=True
            self.visited.append(current)
            for i in self.graph[current]:
                self.depthFirstSearch(i,end)

    def bfs_limit(self, start, limit):
        self.queue.clear()
        self.queue.push(start)
        self.visited.append(start)

        while not self.queue.isEmpty():
            start = self.queue.Peak()
            if start == limit:
                self.solvable = True
                break
            for adj in self.graph[start]:
                if adj not in self.visited:
                    self.queue.push(adj)
                    self.visited.append(adj)
            self.queue.pop()


p=pathFinding()





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
    selectedWalls=value
    MakeMatrix()
    matrixClass.getAmountWalls(value)
    if matrixClass.AmountWalls>(matrixClass.Size**2)-2:
        matrixClass.AmountWalls=0
    MakeWalls()
    if IsSolvable()==False:
        Walls(value)
    MakeMaze()

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
def IsSolvable():
    p.graph = {}
    p.visited = []
    p.solvable=False
    p.makeGraph(matrix)
    p.bfs_limit(matrix[1][1], matrix[-2][-2])
    print(p.visited)
    if p.solvable==True:
        return True
    else:
        return False

def start():
    IsSolvable()
    for i in p.visited:
        canvas.create_rectangle(squareDimensions, squareDimensions, squareDimensions * 2, squareDimensions * 2,fill="Green")
        canvas.create_rectangle(matrixClass.Size * squareDimensions, (len(matrix) - 2) * squareDimensions,(matrixClass.Size * squareDimensions) + squareDimensions,((len(matrix) - 2) * squareDimensions) + squareDimensions, fill="red")
        if SPEED!=0:
            sleep(SPEED)
            window.update()
        canvas.create_rectangle(tracker[i][0], tracker[i][1], (tracker[i][0]) + squareDimensions,(tracker[i][1]) + squareDimensions, fill="blue", outline="black")
    canvas.create_rectangle(squareDimensions,squareDimensions,squareDimensions*2,squareDimensions*2,fill="Green")
    canvas.create_rectangle(matrixClass.Size*squareDimensions,(len(matrix)-2)*squareDimensions,(matrixClass.Size*squareDimensions)+squareDimensions,((len(matrix)-2)*squareDimensions)+squareDimensions,fill="red")

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
