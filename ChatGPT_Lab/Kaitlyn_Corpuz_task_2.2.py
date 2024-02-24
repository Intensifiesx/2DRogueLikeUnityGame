import pandas as pd
import numpy as np

train_data = pd.read_csv('MNIST_training.csv', header=None, skiprows=1)
test_data = pd.read_csv('MNIST_test.csv', header=None, skiprows=1)

y_train = train_data.iloc[:, 0].values
X_train = train_data.iloc[:, 1:].values

y_test_groundtruth = test_data.iloc[:, 0].values
X_test = test_data.iloc[:, 1:].values

k = 5

predictions = []

for i in range(len(X_test)):
    distances = np.sum(np.square(X_train - X_test[i]), axis=1)
    nearest_neighbors_indices = np.argsort(distances)[:k]
    nearest_neighbors_labels = y_train[nearest_neighbors_indices]
    prediction = np.bincount(nearest_neighbors_labels).argmax()
    predictions.append(prediction)

correctly_classified = (predictions == y_test_groundtruth).sum()
incorrectly_classified = len(y_test_groundtruth) - correctly_classified
accuracy = correctly_classified / len(y_test_groundtruth)

print("Correctly classified: %d" % correctly_classified)
print("Incorrectly classified: %d" % incorrectly_classified)
print("Accuracy: %f" % accuracy)

# Documented Code
import pandas as pd
import numpy as np

# Read training and test data from CSV files
train_data = pd.read_csv('MNIST_training.csv', header=None, skiprows=1)
test_data = pd.read_csv('MNIST_test.csv', header=None, skiprows=1)

# Extract labels and features from training and test data
y_train = train_data.iloc[:, 0].values  # Labels of training data
X_train = train_data.iloc[:, 1:].values  # Features of training data

y_test_groundtruth = test_data.iloc[:, 0].values  # Ground truth labels of test data
X_test = test_data.iloc[:, 1:].values  # Features of test data

k = 5  # Number of nearest neighbors to consider

predictions = []  # List to store predictions for test data

# Loop over each data point in the test set
for i in range(len(X_test)):
    # Compute Euclidean distances between the current test point and all training points
    distances = np.sum(np.square(X_train - X_test[i]), axis=1)
    
    # Find the indices of the k nearest neighbors
    nearest_neighbors_indices = np.argsort(distances)[:k]
    
    # Get the labels of the k nearest neighbors
    nearest_neighbors_labels = y_train[nearest_neighbors_indices]
    
    # Predict the label for the current test point based on the most common label among nearest neighbors
    prediction = np.bincount(nearest_neighbors_labels).argmax()
    
    # Append the prediction to the list of predictions
    predictions.append(prediction)

# Calculate the number of correctly and incorrectly classified samples
correctly_classified = (predictions == y_test_groundtruth).sum()
incorrectly_classified = len(y_test_groundtruth) - correctly_classified

# Calculate the accuracy of the classifier
accuracy = correctly_classified / len(y_test_groundtruth)

# Print results
print("Correctly classified: %d" % correctly_classified)
print("Incorrectly classified: %d" % incorrectly_classified)
print("Accuracy: %f" % accuracy)

