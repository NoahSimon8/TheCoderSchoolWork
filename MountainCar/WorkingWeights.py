import gym
from MountainCar.Faster.GeneToNetwork import *
env=gym.make("MountainCar-v0")


one=  [0.8683598349024371, 0.6444961929769468, -0.8038317417105414, 0.8333704216472808, -0.8108639162054259, -0.3410125166088851, 0.5881435603705696, -0.9242404310811809, 0.7190105017285762, 0.4675135413313789, 0.8771016744305848, 0.21372409207042065, -0.5863750920374953, -0.7703696344317514, 0.44588769381514104, 0.6337702226313973, -0.8787433875213928, -0.861382416874588, -0.5710263738785488, 0.7073860079317877, 0.331581300028966, 0.40875127360190877, 0.2620217897788275, 0.5499321042510512, 0.033762800896967926, 0.45554990477806534, -0.08161109111703246, 0.9536860199781958, -0.4508124664307307, 0.3677275268537967]
two=[0.49489250743630064, 0.9001382964390772, -0.9556330648476421, -0.43408950472715735, 0.49129020501356124, 0.44358078840904236, 0.20795608296213697, 0.911458804066287, -0.8537669185702068, 0.8701499984911276, -0.9747720260138357, 0.480757833615981, 0.5352648488057801, 0.6361684234412177, 0.7102271882865809, 0.5066833880820021, 0.051906310675586154, 0.7462139444695692, -0.4198421042387881, 0.07473504257922414, -0.8373036995150045, -0.3928930557526622, -0.9590153657441736, 0.5430495675813156, 0.7725686283927464, 0.7710152484767583, -0.46371942200202887, -0.07079686641222072, -0.6826407603118563, 0.1811145132010572]

n=network(two,2,6,3)
ob = env.reset()
count=0
while True:
    count+=1
    ob=np.array([ob])
    env.render()
    ob, reward, done,info=env.step(np.argmax(n.predict(ob)))
    if done==True:
        break


# print(ob.size,reward, info)

env.close()