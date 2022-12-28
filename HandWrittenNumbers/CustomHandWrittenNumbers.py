import numpy as np
import math
import mnist as m
import matplotlib.pyplot as plt


def sigmoid(x):
    return  1/(1+math.e**-x)

def errorformula(expected,correct):

    total2 = 0
    for num in range(len(expected)):
        total=0
        total+=(expected[num]-correct[num])**2
        for i in total:
            total2+=i

    return total2/(len(correct)*len(correct[0]))


def predict(x,w1,w2):
    # hiden layer
    x=np.array([x])
    z1 = x.dot(w1)  # input from layer 1
    a1 = sigmoid(z1)  # output of layer 2

    # Output layer
    z2 = a1.dot(w2)  # input of out layer
    a2 = sigmoid(z2)  # output of out layer

    return a2


# Back propagation of error
def back_prop(x, y, w1, w2, alpha,timer):
    z1 = x.dot(w1)  # input from layer 1
    a1 = sigmoid(z1)  # output of layer 2
    # Output layer
    z2 = a1.dot(w2)  # input of out layer
    a2 = sigmoid(z2)  # output of out layer

    d2 = (a2 - y)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(),
                     (np.multiply(a1, 1 - a1)))

    # Gradient for w1 and w2
    w1_adj = x.transpose().dot(d1)
    w2_adj = a1.transpose().dot(d2)

    # Updating parameters
    w1 = w1 - (alpha * (w1_adj))
    w2 = w2 - (alpha * (w2_adj))

    if timer%1000==0:
        er=errorformula(a2,y)
        print(er)
        errors.append(er)
    return (w1, w2)

insize=784
midsize=20
outsize=10

W1=np.random.rand(insize,midsize)
W2=np.random.rand(midsize,outsize)

images = m.train_images()
train_labels = m.train_labels()



inputs=[]
for i in images:
    inputs.append(i.reshape(1,784)[0]/255)

inputs=np.array(inputs)
outputs=[]
for i in train_labels:
    blank=[0 for i in range(10)]
    blank[i]=1
    outputs.append(blank)

outputs=np.array(outputs)
errors=[]
for i in range(10000):
    selected=np.random.randint(0,59000)
    inbatch=[]
    outbatch = []

    for n in range(1000):
        inbatch.append(inputs[selected+n])
        outbatch.append(outputs[selected + n])

    inbatch=np.array(inbatch)
    outbatch = np.array(outbatch)

    W1,W2=back_prop(inbatch,outbatch,W1,W2,0.00001,i)

print(np.argmax(predict(inputs[1],W1,W2)))
print(predict(inputs[1],W1,W2))

# sigin=np.random.rand(1,25)*5
# sig=sigmoid(sigin)
# plt.scatter(sigin.flatten(),sig.flatten())
plt.imshow(images[1])
plt.title(np.argmax(predict(inputs[1],W1,W2)))
plt.show()
