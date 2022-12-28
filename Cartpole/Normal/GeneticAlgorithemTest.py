from Normal.GeneticAlgorithem import*
from time import time
gensize=1000
popsize=1000
x=np.linspace(1,10,gensize)
y=np.sin(x)



def reward(gene):
    return sum(abs(y - gene))

def mutation(new,rate):
    for n, j in enumerate(new):
        if uniform(0, 1) <= rate:
            new[n] = uniform(-1, 1)
    return new
alg=Algorithem(gensize,popsize,reward,mutation)

best,gen=alg.generation()

for i in range(10000):
    start=time()
    gen, best=alg.generation(gen,best,0.0005)
    print(round(time()-start,3))
    # print(alg.reward(gen[best]))