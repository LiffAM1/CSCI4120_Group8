import pandas as pd
import random
import math
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn import metrics


def readDataset(url):
    df = pd.read_csv(url, header=None)
    array = df.to_numpy()
    return array

def splitDataset(dataset, split):
    array = np.array(dataset)
    random.shuffle(array)
    training_len = int(len(array) * split)
    trainingSet = array[:training_len]
    testSet = array[training_len:]
    return trainingSet, testSet

def getPredictionSkLearn(trainingSet, testSet, k, attributes):
    model = KNeighborsClassifier(n_neighbors=k)
    trainingData = np.array(trainingSet)
    trainingX = trainingData[:,0:attributes]
    trainingY = trainingData[:,attributes]
    model.fit(trainingX,trainingY)

    testData = np.array(testSet)
    testX = testData[:,0:attributes]
    testY = testData[:,attributes]
    predictions = model.predict(testX)
    accuracy = metrics.accuracy_score(testY, predictions)
    return predictions, accuracy

def main():
    # Load dataset
    url = 'https://raw.githubusercontent.com/ruiwu1990/CSCI_4120/master/KNN/iris.data'
    dataset = readDataset(url)
    accuracies = {}
    # Get predictions for the full range 10 times
    for r in range(5):
        trainingSet, testSet = splitDataset(dataset,0.66)
        for k in range(1,21):
            predictions, accuracy = getPredictionSkLearn(trainingSet,testSet,k,4)
            if k not in accuracies.keys():
                accuracies[k] = []
            accuracies[k].append(accuracy)
    # Compute average accuracies for each K value
    averageAccuracies = {}
    for a in accuracies.keys():
        averageAccuracies[a] = sum(accuracies[a])/len(accuracies[a])

    # Plot K vs Average Accuracy
    x = averageAccuracies.keys()
    y = averageAccuracies.values()
    plt.plot(x,y)
    xint = range(min(x), math.ceil(max(x)) + 1)
    plt.xticks(xint)
    plt.title('K Neighbors vs Average Accuracy')
    plt.xlabel('K Neighbors (count)')
    plt.ylabel('Average Accuracy (decimal)')
    plt.show()

main()
