#!/usr/bin/env python

# Matthew Noojin
# CS422, Prof Kang
# 04/23/23

# Import packages
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.utils import to_categorical
from sklearn.model_selection import KFold, train_test_split, learning_curve
import matplotlib.pyplot as plt


# Read in data into pandas
data = pd.read_csv('MNIST_HW4.csv')

# Place our data into our labels and images vars
labels = data.iloc[:, 0].values.astype('int32')
images = data.iloc[:, 1:].values.astype('float32') / 255
# Reshape the image 
images = images.reshape(-1, 28, 28, 1)
labels = to_categorical(labels)

# Define KFold
kf = KFold(n_splits=5, shuffle=False)
scores = []

# Split our images and labels into test and train sets
X_train, X_test, y_train, y_test = train_test_split(images, labels)

# Neural network built based off VGG model
model = Sequential([
    layers.Conv2D(32, (3,3),activation='relu',input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.Flatten(),
    layers.Dense(2048,activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10,activation='softmax')
])
# Compile our model
model.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])

# 5-fold cv
for i, (train_index, test_index) in enumerate(kf.split(X_train)):
    
    X_train_cv, X_test_cv = X_train[train_index], X_train[test_index]
    y_train_cv, y_test_cv = y_train[train_index], y_train[test_index]

    model.fit(X_train_cv, y_train_cv,epochs=10,batch_size=100)

    scores.append(model.evaluate(X_test_cv,y_test_cv)[1])
# Scores for each fold
for i in range(len(scores)):
    print('Fold '+str(i+1),'Accuracy: ', scores[i] * 100)

# Accuracy
print('Accuracy: ', np.mean(scores) * 100)