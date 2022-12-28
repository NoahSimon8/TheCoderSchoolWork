import numpy as np
from random import*
from multiprocessing import Pool



class Algorithem:
    def __init__(self,GenerationSize,PopSize,reward,mutation):
        self.gensize=GenerationSize
        self.popsize=PopSize
        self.genes=[]
        self.rewards=[]
        self.reward=reward
        self.mutation=mutation

    def generation(self,prev=None,best=None,mut=0):
        if prev==None:
            self.genes=[]
            self.rewards=[]
            for i in range(self.popsize):
                self.genes.append(np.random.rand(self.gensize)*2-1)

                self.rewards.append(self.reward(self.genes[i]))
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
                for n in range(len(prev[best])):
                    if n>=num:
                        new.append(b[n])
                    else:
                        new.append(a[n])
                #mutation
                new=self.mutation(new,mut)

                self.genes.append(new)

                self.rewards.append(self.reward(self.genes[i]))

            self.genes[np.argmax(self.rewards)]=prev[best] #eletism?
            newbest=np.argmin(self.rewards)
        topscore=max(self.rewards)
        return self.genes,  newbest, topscore

