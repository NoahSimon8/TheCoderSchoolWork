
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

train,test=tf.keras.datasets.mnist.load_data(path='mnist.npz')

model=keras.Sequential([
                        keras.layers.Dense(25,activation="sigmoid",input_shape=(784,)),
                        # keras.layers.Dropout(0.1,),
                        keras.layers.Dense(25,activation="sigmoid"),
                        keras.layers.Dense(10,activation="softmax")])

model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
print(model.summary())
images = train[0]
train_labels = train[1]


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

testimages = test[0]
testlabels= test[1]
testoutputs=[]
for i in testlabels:
    blank=[0 for i in range(10)]
    blank[i]=1
    testoutputs.append(blank)
testoutputs=np.array(testoutputs)

testinputs=[]
for i in testimages:
    testinputs.append(i.reshape(1,784)[0]/255)
testinputs=np.array(testinputs)

hist=model.fit(inputs,outputs,epochs=35,batch_size=100,validation_data=(testinputs,testoutputs))


plt.plot(hist.history["loss"],label="Training Loss")
plt.plot(hist.history["val_loss"],label="Testing Loss")
plt.legend()
plt.show()
while True:
    var=int(input("Enter a number <60000: "))
    plt.imshow(testimages[var])
    plt.title("Guess: "+str(np.argmax(model.predict(np.array([testinputs[var]]))))+"   Answer: "+str(testlabels[var]))
    plt.show()

