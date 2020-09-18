#!/usr/bin/env python
# coding: utf-8

# In[8]:


##  Building a Student Intervention System: Data Science Classification and Regression

# Step1: Import the libraries and load the data
import numpy as np
import pandas as pd
from time import time
from sklearn.metrics import f1_score

# Read Student Data
student_data = pd.read_csv('/Users/arinjoy/Projects/DataScience/student-data.csv')
print("Student Data Read Successfully")
# print(student_data.head())

# Convert DataSet into DataFrame
student_data.shape

# Check the type of Data in Pandas as DataFrame
print(type(student_data))


# Step2: Implementation: Data Exploration
# Lets begin by investigating the dataset to determine how many students we have information on, and learn about the graduation
# rate among these students

# a. Total Number of Students
# b. The total number of features for each student
# c. The number of students who have passed
# d. The number of students who have failed
# e. The graduation rate of the class in percentage(%)

# a.
n_students = student_data.shape[0]

# b.
n_features = student_data.shape[1] - 1

# c.
passed = student_data.loc[student_data.passed == 'yes', 'passed']
n_passed = passed.shape[0]

# d.
failed = student_data.loc[student_data.passed == 'no', 'passed']
n_failed = failed.shape[0]

# e.
total = float(n_passed + n_failed)
grad_rate = float (n_passed * 100 / total)


# Print the Results
print("Total number of students: {}".format(n_students))
print("Number of Features: {}".format(n_features))
print("Total number of students who passed: {}".format(n_passed))
print("Total number of students who failed: {}".format(n_failed))
print("Graduation rate of the class: {:.2f}".format(grad_rate))


# Need to Identify Features and Target Columns
# student_data.columns
# student_data.columns[-1]
student_data.columns[:-1]

feature_cols = list(student_data.columns[:-1])

# Extract Target Column
target_col = student_data.columns[-1]

# Show the list of columns
print("Feature columns:\n{}".format(feature_cols))
print("\nTarget column:{}".format(target_col))

## Seperate the Data into feature data and target data (X_all and y_all, respectively)
X_all = student_data[feature_cols]
y_all = student_data[target_col]

# show the feature information by printing the first five rows
print("\nFeature Values:")
print(X_all.head())


# In[ ]:




