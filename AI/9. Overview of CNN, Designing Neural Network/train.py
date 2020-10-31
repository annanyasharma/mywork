#Create first network with Keras
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy

# load pima indians dataset
dataset = numpy.loadtxt('pima-indians-diabetes.csv', delimiter=",")
#dataset = pd.read_csv('pima-indians-diabetes.csv')

#    split into input (X ie dependent variables) and output (Y ie independent variables) variables
X = dataset[:,0:8]   #0-8 columns are dependent variables - remember 8th column is not included
Y = dataset[:,8]     #8 column is independent variable
print(X)

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu')) # 12 neurons
model.add(Dense(8, activation='relu')) # 500 neurons
model.add(Dense(1, activation='sigmoid')) # 1 output neuron
model.summary()

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=5, batch_size=10) # 150 epoch, 10 batch size,

_, accuracy = model.evaluate(X,Y)
print('Accuracy: %.2f' % (accuracy*100))

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")
