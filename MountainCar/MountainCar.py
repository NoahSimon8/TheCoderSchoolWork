import gym
from MountainCar.Faster.GeneticAlgorithemFast import*
from MountainCar.Faster.GeneToNetwork import*



def mutation(new,rate):
    for n, j in enumerate(new):
        if uniform(0, 1) <= rate:
            new[n] = uniform(-1, 1)
    return new


#old version
# def reward(gene):
#     n=network(gene)
#     score=0
#     ob = env.reset()
#     for i in range(2000):
#         ob=np.array([ob])
#         ob, reward, done,info=env.step(np.argmax(n.predict(ob)))
#         if done==True:
#             break
#         score-=1
#     return score

#Fast Version
def reward(gene):
    rewards=[]
    for i in gene:
        n=network(i,2,6,3)
        ob = env.reset()
        fastest=ob[1]
        farthest=ob[0]
        for i in range(200):
            ob=np.array([ob])
            ob, reward, done,info=env.step(np.argmax(n.predict(ob)))

            if abs(ob[1])>fastest:
                fastest=abs(ob[1])
            if ob[0]>farthest:
                farthest=ob[0]
            if done==True:
                break

        rewards.append(-(fastest+(farthest/20)))
    return rewards

env=gym.make("MountainCar-v0")
g=Algorithem(30,35,reward,mutation)
genes, best, topscore=g.generation()
for i in range(300):
    genes, best, topscore=g.generation(genes,best,0.005)
    if i%50==0:
        print(i, "Top Score: "+str(topscore))
    if i%101==0:
        ob = env.reset()
        n = network(genes[best], 2, 6, 3)
        for i in range(200):
            ob = np.array([ob])
            env.render()
            ob, reward, done, info = env.step(np.argmax(n.predict(ob)))
            if reward == True:
                break
        env.close()
print("Top Score: "+str(topscore), "Composition: ", genes[best])





n=network(genes[best],2,6,3)
ob = env.reset()
while True:
    ob=np.array([ob])
    env.render()
    ob, reward, done,info=env.step(np.argmax(n.predict(ob)))
    if reward==True:
        break


# print(ob.size,reward, info)

env.close()