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
