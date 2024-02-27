#!/usr/bin/env python

# Matthew Noojin
# CS422, Prof Kang
# 03/22/23

# Import our libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from prettytable import PrettyTable

# Our final table
kFoldTable = PrettyTable()
kFoldTable.field_names = ['Fold','cylinders', 'displacement', 'horsepower', 'weight', 
         'acceleration', 'model year', 'origin', 'RMSE (HW)', 'RMSE']

# The names of each of our categories (This is just for pandas)
cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
         'acceleration', 'model year', 'origin', 'car name']

# Read from our .data file and drop the car name column
data = pd.read_fwf('auto-mpg.data', names=cols)
data = data.drop(columns='car name')

# The number of K-folds we will have
k = 10

# How we will normalize our features
normalize = StandardScaler()

# Initialize our KFold package
kf = KFold(n_splits = k, shuffle=True)

# Our variables
X = data.iloc[:, 1:8].values
Y = data.iloc[:, 0].values

# I'm converting this to a numpy, as I'm not sure if 
# setting it from the panda has it as a numpy already
X = np.asarray(X)
Y = np.asarray(Y)

# We need to drop rows that contain '?'
# There is probably a more efficient way to do this but I'm lazy :)
indxRemove = []
for j in range(len(X)):
    val = X[j,2]
    if val == '?':
        indxRemove.append(j)
# Remove rows where '?' was identified 
for l in range(len(indxRemove)):
    X = np.delete(X, indxRemove[l] - l, 0)
    Y = np.delete(Y, indxRemove[l] - l, 0)

# Make our values a float :)
X = X.astype(float)
Y = Y.astype(float)

# This loop will allow us to generate our folds with a 
# test and train set, and then we can predict mpg and find the RMSE
for i, (train_index, test_index) in enumerate(kf.split(X)):
    
    # Store our test and train sets for X and Y
    X_train , X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    # Normalize our features
    # I will use this comment to explain why I did not normalize Y
    # It just didn't give me very pretty data. I feel like I do not need
    # to normalize the Y sets since it makes the model predict too closely, 
    # hence it kind of overfits based on the data. 
    X_train, X_test = normalize.fit_transform(X_train), normalize.fit_transform(X_test)

    # Add column of ones to X_train and X_test
    X_train = np.hstack((np.ones((X_train.shape[0], 1)), X_train))
    X_test = np.hstack((np.ones((X_test.shape[0], 1)), X_test))

    # b = (X'X)^-1X'y, our coefficients
    coefficients = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ Y_train

    # Multiply our coefficients by our test set to get our prediction set Xib
    predict = X_test @ coefficients

    # RMSE = sqrt(sigma(yi - Xib)^2/N)
    rmse1 = np.sqrt(np.sum(Y_test - predict) ** 2)
    rmse2 = np.sqrt(np.mean(Y_test - predict) ** 2)

    # Add each of our rows into our table :)
    kFoldTable.add_row(['Fold ' + str(i + 1), "{0:.4f}".format(coefficients[1]), "{0:.4f}".format(coefficients[2]), 
                        "{0:.4f}".format(coefficients[3]), "{0:.4f}".format(coefficients[4]),
                        "{0:.4f}".format(coefficients[5]), "{0:.4f}".format(coefficients[6]),
                        "{0:.4f}".format(coefficients[7]), "{0:.4f}".format(rmse1), "{0:.4f}".format(rmse2)])

# Print the table
print(kFoldTable)


    

