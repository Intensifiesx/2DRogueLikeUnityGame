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
from keras.utils import to_categorical
from sklearn.model_selection import KFold, train_test_split

# Read in data into pandas
data = pd.read_csv('MNIST_HW4.csv')

# Place our data into our labels and images vars
labels = data.iloc[:, 0].values.astype('int32')
images = data.iloc[:, 1:].values.astype('float32') / 255
# Reshape the image 
images = images.reshape(-1, 28, 28, 1)
labels = to_categorical(labels)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(images, labels)

# Neural network model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 5-fold cross-validation
kf = KFold(n_splits=5, shuffle=False)
scores = []

for train_index, test_index in kf.split(X_train):
    X_train_cv, X_test_cv = X_train[train_index], X_train[test_index]
    y_train_cv, y_test_cv = y_train[train_index], y_train[test_index]

    model.fit(X_train_cv, y_train_cv, epochs=5, batch_size=128, verbose=1)
    scores.append(model.evaluate(X_test_cv, y_test_cv, verbose=0)[1])

# Print accuracy for each fold
for i, score in enumerate(scores):
    print('Fold', i + 1, 'Accuracy:', score * 100)

# Print overall accuracy
print('Mean Accuracy: ', np.mean(scores) * 100)
