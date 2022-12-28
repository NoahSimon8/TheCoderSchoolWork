import gym
from MountainCar.Faster.GeneToNetwork import*
env=gym.make("CartPole-v1")


# ob = env.reset()  #6 numbers
# print(ob)
# for i in range(500):
#     ob, reward, done,info=env.step(0)   #0-2
# print(done)

ob = env.reset()
while True:
    ob=np.array([ob])
    env.render()
    ob, reward, done,info=env.step(0)
    if done==True:
        break