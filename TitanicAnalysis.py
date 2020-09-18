#!/usr/bin/env python
# coding: utf-8

# In[15]:


## Implementation of Titanic Data Set Case Study

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Loading the Dataset
full_data = pd.read_csv('/Users/arinjoy/Projects/DataScience/titanic.csv')
#print(full_data.head())

#Survived: Outcome of survival (0=No; 1=Yes)
#Pclass: 1 = upper, 2 = middle, 3  = lower
#Name: Name of the passenger
#Sex: Sex of the passegner
#Age: Age of the passenger
#SibSp: Number of Siblings and spouses of the passenger on aboard
#Parch: Number of parents and childrens of the passengers aboard
#Ticket: Ticket number of the passenger
#Fare: Fare paid by the passenger
#Cabin: Cabin number of the passenger (Some entries are having NAN)
#Embarked: Port of boarding the passenger (C = cherbourg, Q = Queenstown, S = Southampton)

# Store the Survived Column in another Field
outcomes = full_data['Survived']

# Drop the Survived column from Data Set
data =  full_data.drop('Survived', axis = 1)
#print(data.head())


## Creating our Data Science Model and then will implement
# Out of the first 5 passengers, if we predict that all of them survived, what will be our accuracy is

# create a Function to check the truth and prediction
def accuracy_score(truth, pred):
    # "Return the accuracy socre for input truth and predictions"
    
    # We need to Ensure that the number of predictons matches the number of outcomes
    if len(truth) == len(pred):
        ## Caluclate and return the accuracy as a percent
        ## {:.2f}.format((truth == pred).mean()*100)
        ## : represents format specification
        ## "2f" represents 2 decimal places
        
        return "Predictions have an accuracy of {:.2f}.".format((truth==pred).mean()*100)
    else:
        return "Number of Predictions does not match the number of outcomes"
    
# Test our accuracy_score function
# pd.Series() Creates a Series
# np.ones(5, dtype=int) it will create a 5X1 array of ones
predictions = pd.Series(np.ones(5, dtype=int))

# Call accuracy_score function and passing the arguments outcomes[:5] and predictions
# Since we predicting only 5X1 array, we can only compare with the first 5 rows
#print(accuracy_score(outcomes[:5], predictions))


## Making Predictions: If we are to make a prediction about any passenger aboard TITANIC whom we know nothing about, ten the 
# best prediction we could make would be that they did not survive. This is because we can assume that a majority of the 
# passsengers (more than 50%) did not survive the ship sinking. 
# Let us create a function predictions_0 below to always predict that a passenger did not survive

def predictions_0(data):
    # "Model with no features. Always predicts a passenger did not survive"
    predictions = [] 
    
    # for index, row in data.iteerrows()
    for index, passenger in data.iterrows():
        # Predict the survival of 'passenger'
        predictions.append(0)
        
        # return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_0(data)
#print(predictions.head())



#########################################  Predictions to be Done using Upper Model  #######################################

# 1. Using Titanic Data, how accurate would a Prediction be that none of the passengers survived ?
# print(accuracy_score(outcomes,predictions))

def predictions_1(data):
    # Model with one feature 
    # Predicting a passenger survived if they are female
    
    predictions = []
    for index,passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            predictions.append(0)

    return pd.Series(predictions)
predictions = predictions_1(data)
# print(predictions)
# Lets take a case where we need to take a look whether the feature 'Sex' has indication of survival rates: Predict the number 
# of males and females survived and not survived
####### LOGIC FOR Implementation of above Case then outcomes and predictions will changed



# 2. How accurate would a prediction be that all females passengers survived and the remaining passengers did not survive
# print(accuracy_score(outcomes,predictions)): # the result of accuracy_score will change becuase of upper case
def predictions_2(data):
    # Model with one feature 
    # Predicting a passenger survived if they are female
    
    predictions = []
    for index,passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
#         elif (passenger['Sex'] == 'male') & (passenger['Age'] < 10):
        elif passenger['Age'] < 10:
            predictions.append(1)
        else:
            predictions.append(0)

    return pd.Series(predictions)
predictions = predictions_2(data)
# print(predictions)



# 3. How accurate would a prediction be that all females passengers and all male passeengers younger than 10 survived ?
# print(accuracy_score(outcomes,predictions)): # the result of accuracy_score will change becuase of upper case
# def predictions_3(data):
#     # Model with multiple features
#     predictions = []
    
#     for index, passenger in data.iterrows():
#         if passenger['Sex'] == 'female' or passenger['Sex'] == 'male':
#             if passenger['Age'] < 10:
#                 predictions.append(1)
#             else:
#                 predictions.append(0)
                
#         elif passenger['Sex'] == 'male':
#             if passenger['Age'] < 10:
#                 predictions_male.append(1)
#             else:
#                 predictions_male.append(0)
                
#             return pd.Series(predictions)

# predictions = predictions_3(data)
# print(predictions)


def predictions_3(data):
    #model with multiple features
    predictions_male = [] 
    predictions_female = [] 
    
    # for index, row in data.iteerrows()
    for index, passenger in data.iterrows():
        # Predict the survival of 'passenger' on the basis of sex
        if (passenger['Sex']=='female'):
            if (passenger['Age']<10):
                predictions_female.append(1)
                predictions_male.append(0)
            else:
                predictions_female.append(0)
                predictions_male.append(0)
        elif (passenger['Sex']=='male'): 
            if (passenger['Age']<10):
                predictions_male.append(1)
                predictions_female.append(0)
            else:
                predictions_male.append(0)
                predictions_female.append(0)
        else:
            predictions3.append(0)
    # return our predictions
    return pd.Series(predictions_female)


predictions3 = predictions_3(data)
print(predictions3)
print(accuracy_score(outcomes,predictions3))
                


# In[ ]:




