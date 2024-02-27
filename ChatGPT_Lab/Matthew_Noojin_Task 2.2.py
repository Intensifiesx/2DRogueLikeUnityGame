#!/usr/bin/env python

# Matthew Noojin
# CS422, Prof Kang
# 03/22/23

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from prettytable import PrettyTable

# Create a table to store cross-validation results
kFoldTable = PrettyTable()
kFoldTable.field_names = ['Fold','cylinders', 'displacement', 'horsepower', 'weight', 
         'acceleration', 'model year', 'origin', 'RMSE (HW)', 'RMSE']

# Define the categories/columns in the dataset
cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
         'acceleration', 'model year', 'origin', 'car name']

# Read data from file and drop unnecessary columns
data = pd.read_fwf('auto-mpg.data', names=cols)
data = data.drop(columns='car name')

# Set the number of folds for cross-validation
k = 10

# Initialize KFold object for splitting data
kf = KFold(n_splits=k, shuffle=True)

# Extract features (X) and target variable (Y)
X = data.iloc[:, 1:8].values
Y = data.iloc[:, 0].values

# Convert data to numpy arrays
X = np.asarray(X)
Y = np.asarray(Y)

# Remove rows containing '?' values
indxRemove = []
for j in range(len(X)):
    val = X[j,2]
    if val == '?':
        indxRemove.append(j)
for l in range(len(indxRemove)):
    X = np.delete(X, indxRemove[l] - l, 0)
    Y = np.delete(Y, indxRemove[l] - l, 0)

# Convert data to float
X = X.astype(float)
Y = Y.astype(float)

# Linear Regression with 10-fold Cross-Validation
# This loop generates folds with a test and train set, 
# performs linear regression, predicts mpg, and finds the RMSE
for i, (train_index, test_index) in enumerate(kf.split(X)):
    
    # Split data into train and test sets for features (X) and target (Y)
    X_train , X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    # Normalize features using StandardScaler
    X_train, X_test = normalize.fit_transform(X_train), normalize.fit_transform(X_test)

    # Add bias term by adding a column of ones to X_train and X_test
    X_train = np.hstack((np.ones((X_train.shape[0], 1)), X_train))
    X_test = np.hstack((np.ones((X_test.shape[0], 1)), X_test))

    # Compute coefficients using the normal equation method
    coefficients = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ Y_train

    # Predict target variable using the test set
    predict = X_test @ coefficients

    # Calculate Root Mean Square Error (RMSE)
    rmse1 = np.sqrt(np.sum((Y_test - predict) ** 2) / len(Y_test))
    rmse2 = np.sqrt(np.mean((Y_test - predict) ** 2))

    # Add results for each fold to the table
    kFoldTable.add_row(['Fold ' + str(i + 1), "{0:.4f}".format(coefficients[1]), 
                        "{0:.4f}".format(coefficients[2]), "{0:.4f}".format(coefficients[3]), 
                        "{0:.4f}".format(coefficients[4]), "{0:.4f}".format(coefficients[5]), 
                        "{0:.4f}".format(coefficients[6]), "{0:.4f}".format(coefficients[7]), 
                        "{0:.4f}".format(rmse1), "{0:.4f}".format(rmse2)])

# Print the table with cross-validation results
print(kFoldTable)


    

