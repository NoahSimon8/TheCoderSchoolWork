import gym
from Cartpole.Cartpole.OldAlg.GeneticAlgorithemFast import*
from Cartpole.Cartpole.OldAlg.GeneToNetwork import*

def mutation(new,rate):
    for n, j in enumerate(new):
        if uniform(0, 1) <= rate:
            new[n] = uniform(-1, 1)
    return new
#Normal version
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
        n=network(i,4,4,2)
        score=0
        ob = env.reset()
        for i in range(2000):
            ob=np.array([ob])
            # print(np.argmax(n.predict(ob))+2)
            # ob, reward, done,info=env.step(np.argmax(n.predict(ob))+2)
            ob, reward, done,info=env.step(np.argmax(n.predict(ob)))

            if done==True:
                break
            score-=1
        rewards.append(score)
    return rewards



env=gym.make("CartPole-v1")
g=Algorithem(24,10,reward,mutation)
genes, best, topscore=g.generation()
for i in range(1500):
    genes, best, topscore=g.generation(genes,best,0.001)
    if i%500==0:
        print(i, "Top Score: "+str(topscore))
print("Top Score: "+str(topscore), "Composition: ", genes[best])





n=network(genes[best],4,4,2)
ob = env.reset()
while True:
    ob=np.array([ob])
    env.render()
    ob, reward, done,info=env.step(np.argmax(n.predict(ob)))
    if done==True:
        break


# print(ob.size,reward, info)

env.close()