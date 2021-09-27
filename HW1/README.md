# CSCI 4120 - Group 8 - Homework 1
**Group Members:** 
Abigail Holloway, hollowayab21@students.ecu.edu
Nicholas Everette, everetten17@students.ecu.edu
Michael Trofimov, trofimovm19@students.ecu.edu

This README file will walk you through how to run our Homework 1 Python script, which runs KNN prediction on the provided Iris classification dataset.

## Dependencies

The following dependencies and packages are required to be installed on the host machine in order to run the script:
 - Python (>= 3.5)
 - pandas
 - random
 - math
 - numpy
 - sklearn
 - matplotlib

## Walkthrough

1. Use Git command line or a Git UI to clone the repo (https://github.com/LiffAM1/CSCI4120.git)
2. In a terminal, cd to the directory where you cloned the repo to.
3. Run the command `python main.py` in the directory base folder.
4. The script should run and a matplotlib window plotting the average accuracy over all the runs should appear (the plot should look similar to the plot displayed below).

## Results
Below is a chart plotting the results of the sklearn KNN prediction. Average accuracy is the average for each K value over all 5 runs.
(![KNN K vs Average Accuracy](https://user-images.githubusercontent.com/22064340/132771494-4f52269f-0caa-43fe-b22c-51e73a8e6b9e.png))

## Why K values have similar accuracys
In the graph, you can see that the most of the accuracys for different K values are fairly close, with 1-17 being only .01 different. Our group came to the consensus this could be due to the fact that there are noticable differences in the size of each flower. Each flower differed in size enough that it was noticable enough that just scrolling through the dataset and solely looking at the numbers we could tell when we were looking at a different flower. Since they were all so different there would have to be a large k value for the acuraccy to show a big difference. This is why there is only a .025 difference in the accuracys for all 20 K values.
