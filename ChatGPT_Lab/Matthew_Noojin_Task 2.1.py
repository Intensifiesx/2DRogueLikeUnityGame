from sklearn.neighbors import NearestNeighbors
import pandas as pd

# Number of nearest neighbors we are checking
K = 9

# Read train into pandas DataFrame
trainingData = pd.read_csv("MNIST_training.csv")

# Read test into pandas DataFrame
testData = pd.read_csv("MNIST_test.csv")

# Number of correctly classified values
correctClassified = 0

# Extract features and labels
X_train = trainingData.drop(columns='label')
y_train = trainingData['label']
X_test = testData.drop(columns='label')
y_test = testData['label']

# Fit Nearest Neighbors model
nbrs = NearestNeighbors(n_neighbors=K, algorithm='auto').fit(X_train)

# Find K nearest neighbors for each test instance
distances, indices = nbrs.kneighbors(X_test)

# Iterate through MNIST test data
for i in range(len(X_test)):

    # The correct label in our current iteration
    groundTruth = y_test.iloc[i]

    # Get labels of nearest neighbors
    neighbor_labels = y_train.iloc[indices[i]]

    # Count the occurrences of each label
    c = Counter(neighbor_labels)

    # Get the most common label as the predicted label
    predictedLabel = c.most_common(1)[0][0]

    # If our prediction is right we keep note and output it
    if predictedLabel == groundTruth:
        print("\nCorrectly predicted: ", groundTruth)
        correctClassified += 1
    # Else if it is wrong we show what we got and the real answer
    else:
        print("\nIncorrect prediction: ", predictedLabel)
        print("Ground Truth: ", groundTruth)

# Calculate and print our accuracy
accuracy = (correctClassified / len(X_test)) * 100
print("Accuracy: ", accuracy, "%")



        
        

    