#!/usr/bin/env python

# Matthew Noojin
# CS422, Prof Kang
# 02/24/23

# Import required libraries
import pandas as pd
from scipy.spatial.distance import euclidean
from collections import Counter
import operator

# Define a class of pairs to put into a list
# This has the distance from test to training
# and the label associated with the training value
class distancePair:
    def __init__(self, distance, label):
        self.distance = distance
        self.label = label

# Number of nearest neighbors we are checking
K = 9

# Read train into panda
trainingData = pd.read_csv("MNIST_training.csv")

# Read test into panda
testData = pd.read_csv("MNIST_test.csv")

# Number of correctly classified values 
correctClassified = 0

# Iterate through MNIST test data
for i in range(testData.shape[0]):

    # Define our lists
    distList = []
    tempList = []
    c = Counter()

    # The correct lable in our current iteration
    groundTruth = testData.loc[i,'label']

    # Check our test against each training row
    for j in range(trainingData.shape[0]):
        # Find euclidean distance for current vector row
        distance = euclidean(testData.iloc[i].drop(columns='label'), trainingData.iloc[j].drop(columns='label'))
        # Append to our list pair
        distList.append(distancePair(distance, trainingData.loc[j, 'label']))
        
    # Sort the distance from least to greatest
    # This also keeps labels paired to the distance with the distance
    distList.sort(key=operator.attrgetter('distance'))

    # Make a temp list with first K labels from sorted distList
    for m in range(K):
        tempList.append(distList[m].label)

    # Place temp into a Counter object
    c.update(tempList)

    # Get simple majority from Counter list
    predictedLabel = c.most_common()[0][0]

    # If our prediction is right we keep note and output it
    if predictedLabel == groundTruth:
        print("\nCorrectly predicted: ", groundTruth)
        correctClassified += 1
    # Else if it is wrong we show what we got and the real answer
    else:
        print("\nIncorrect prediction: ", predictedLabel)
        print("Ground Truth: ", groundTruth)

    # Clear the lists
    distList.clear
    tempList.clear
    c.clear
    
# Print our accuracy 
print("Accuracy: ", (correctClassified / testData.shape[0]) * 100, "%")


        
        

    