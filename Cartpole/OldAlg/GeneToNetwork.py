import numpy as np


class network():
    def __init__(self,gene,insize,midsize,endsize):
        self.gene=gene
        self.insize=insize
        self.midsize=midsize
        self.endsize=endsize
        self.w1=[]
        self.w2=[]
        self.create()

    def create(self):

        for i,n in enumerate(self.gene):
            if i<self.insize*self.midsize:
                self.w1.append(n)
            else:
                self.w2.append(n)
        self.w1=np.array(self.w1)
        self.w2=np.array(self.w2)
        self.w1=self.w1.reshape(self.insize,self.midsize)
        self.w2=self.w2.reshape(self.midsize,self.endsize)


    def predict(self,inputs):
        inputs=np.array(inputs)
        mid=inputs.dot(self.w1)
        mid=self.sigmoid(mid)
        end=mid.dot(self.w2)
        end=self.sigmoid(end)
        return end



    def sigmoid(self,x):
        return 1/(1+np.exp(-x))


