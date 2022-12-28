import numpy as np
from random import*
from multiprocessing import Pool
from time import time


class Algorithem:
    def __init__(self,Gensize,Popsize,reward,mutation):
        self.gensize=Gensize
        self.popsize=Popsize
        self.genes=[]
        self.rewards=[]
        self.reward=reward
        self.mutation=mutation

    def generation(self,prev=None,best=None,mut=0):
        start = time()

        # print(__name__)
        if prev==None:
            self.genes=[]
            self.rewards=[]
            for i in range(self.popsize):
                self.genes.append(np.random.rand(self.gensize)*2-1)

                self.rewards=self.reward(self.genes[i])
            newbest=np.argmin(self.rewards)
        else:
            self.genes=[]
            self.rewards=[]
            for i in range(self.popsize):
                new=[]
                num=np.random.randint(0,len(prev[0])-1)
                other=best
                while other==best:
                    other=randint(0,len(prev)-1)
                a=prev[best]
                b=prev[other]
                # print(num)
                for n in range(len(prev[best])):
                    if n>=num:
                        new.append(b[n])
                    else:
                        new.append(a[n])
                #mutation
                new=self.mutation(new,mut)

                self.genes.append(new)
            start=time()
            p=Pool(1)
            # if __name__=="__main__":
            self.rewards=p.map(self.reward,self.genes)
            end=time()

            print(round(end-start,3))
            # self.rewards=self.reward(self.genes)
            self.genes[np.argmax(self.rewards)]=prev[best] #eletism?
            newbest=np.argmin(self.rewards)
        end = time()
        # print("time",end - start)
        return newbest, self.genes

