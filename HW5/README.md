# CSCI 4120 - Group 8 - Homework 5 
**Group Members:** 
Abigail Holloway, hollowayab21@students.ecu.edu
Nicholas Everette, everetten17@students.ecu.edu

This README file will walk you through how to run our Homework 5 Jupyter notebook, which runs a Random Forest Classification exercise and tunes hyperparameters.

## Dependencies

The following dependencies and packages are required to be installed on the host machine in order to run the script:
 - Python (>= 3.5)
 - Jupyter
 - Juptyer Notebooks
 - yellowbrick
 - seaborn
 - pandas
 - random
 - math
 - numpy
 - sklearn
 - matplotlib

## Walkthrough

1. Use Git command line or a Git UI to clone the repo (https://github.com/LiffAM1/CSCI4120_Group8.git)
2. In a terminal, cd to the directory where you cloned the repo to.
3. Run the command 'jupyter notebook' to start jupyter. Click on the HW5_RandomForest.ipynb file to open it.
4. Run the notebook by pressing 'Run'.

## Results
We selected the 20 features with the highest importance to build our model against. See the below graph for the features we picked alongside their importance.

![image](https://user-images.githubusercontent.com/22064340/139353475-f289e0ab-eab8-4c01-a34d-f3d426752ca4.png)

For the hyperparameters, we got the following values using GridSearchCV to find the best combinations of values:
{'bootstrap': True, 'max_depth': 4, 'min_samples_split': 2, 'n_estimators': 20}

Finally, for the results, we scored the training data against the target and the test data against the target, and got the following values for accuracy:
- Accuracy score, training dataset: 0.9671361502347418
- Accuracy score, test dataset: 0.9370629370629371
- Average, training dataset: 0.048356807511737085
- Average, test dataset: 0.04685314685314686

As you can see, the model was slightly overfit as it performed better on the training data, but the accuracy on the test data was still pretty good.
