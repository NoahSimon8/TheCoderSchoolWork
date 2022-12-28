
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

train,test=tf.keras.datasets.mnist.load_data(path='mnist.npz')

model=keras.Sequential([
    keras.layers.Conv2D(10,(4,4),activation="sigmoid",input_shape=(28,28,1,)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(10,(4,4),activation="sigmoid"),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    # keras.layers.Dense(25,activation="sigmoid"),
    # keras.layers.Dropout(0.1,),
    keras.layers.Dense(10,activation="sigmoid"),
    keras.layers.Dense(10,activation="softmax")])

model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
print(model.summary())
images = train[0]
train_labels = train[1]


inputs=[]
for i in images:
    inputs.append(i/255)

inputs=np.array(inputs).reshape((60000,28,28,1))

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
    testinputs.append(i/255)
testinputs=np.array(testinputs).reshape((len(testinputs),28,28,1))




hist=model.fit(inputs,outputs,epochs=30,batch_size=100,validation_data=(testinputs,testoutputs))
model.save("convolutionalnetwork")
out=[layer.output for layer in model.layers]
print(out[0])
print(testinputs[0].shape)
activation_model=keras.Model(inputs=model.input, outputs=out)
# print(model.predict(np.array([testinputs[0]])))
activations=activation_model.predict(np.array([testinputs[0]]))
print(activations[0].shape)
# for i in range(10):
#     plt.subplot(3,3,i)
# print(activations[0][0,:,:,0].shape)
for i in range(10):
    plt.subplot(3,10,i+1)
    plt.imshow(testimages[0])

for i in range(10):
    plt.subplot(3,10,i+11)
    plt.imshow(activations[0][0,:,:,i])

for i in range(10):
    plt.subplot(3,10,i+21)
    plt.imshow(activations[1][0,:,:,i])
plt.show()

#
# plt.plot(hist.history["loss"],label="Training Loss")
# plt.plot(hist.history["val_loss"],label="Testing Loss")
# plt.legend()
# plt.show()

# plt.imshow(testimages[var])
# plt.title(str(np.argmax(model.predict(np.array([testinputs[var]]))))+"   "+str(testlabels[var]))
# plt.show()

