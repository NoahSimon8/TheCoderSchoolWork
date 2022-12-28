# from Depth_First_Search.Maze_Maker import GUI
from random import*
class MakeMatrix:
    def __init__(self):
        self.Size=5
        self.AmountWalls=0
        self.matrix=None
        self.ListWalls=None

    def getSize(self,value):
        self.Size=value

    def getAmountWalls(self,value):
        self.AmountWalls=value

    def Matrix(self):
        self.matrix=[[]for i in range(self.Size+2)]
        for i in range(self.Size+1):
            for r in range(self.Size+2):
                if i==0:
                    self.matrix[i].append(0)
                elif r==0 or r==self.Size+1:
                    self.matrix[i].append(0)
                else:
                    self.matrix[i].append(r+((i-1)*self.Size))
        for i in range(self.Size+2):
            self.matrix[-1].append(0)
        return self.matrix

    def Walls(self):
        self.ListWalls=[]
        for i in range(self.AmountWalls):
            while True:
                while True:
                    while True:
                        row=randint(0,self.Size+1)
                        if row!=0 and row!=self.Size+1:
                            break
                    while True:
                        pos=randint(0,self.Size+1)
                        if pos!=0 and pos!=self.Size+1:
                            break
                    if row!=1 and pos!=self.Size or row!=self.Size and pos!=1:
                        break
                if [row,pos] not in self.ListWalls:
                    break
            self.ListWalls.append([row,pos])

            self.matrix[row][pos]=0
        return self.matrix
