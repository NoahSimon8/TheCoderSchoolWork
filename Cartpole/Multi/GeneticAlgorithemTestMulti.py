from Multi.GeneticAlgorithemMulti import*

gensize=1000
popsize=1000
x=np.linspace(1,10,gensize)
y=np.sin(x)


def reward(genes):
    scored=[]
    scored.append(sum(abs(y - genes)))
    return scored

def mutation(new,rate):
    for n, j in enumerate(new):
        if uniform(0, 1) <= rate:
            new[n] = uniform(-1, 1)
    return new

if __name__ == "__main__":

    alg=Algorithem(gensize,popsize,reward,mutation)

    best,gen=alg.generation()

    for i in range(10000):
        best,gen=alg.generation(gen,best,0.0005)
            # print(alg.reward(gen[best]))