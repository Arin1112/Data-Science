#!/usr/bin/env python
# coding: utf-8

# In[14]:


## Identifying the Customer segment of spending money annually

# Import the libraries necssary for this 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipython.display import display # Allows the use of display() for Data Frames

from ipython.display import display, Markdown

def render(md):
    return display(Markdown(md))

def make_chaos(df, sample_size, columns, fn):
    # Keep chaos the same randomly
    some = df.sample(sample_size, random_state=sample_size)
    for col in columns:
        some[col] = some[col].apply(fn)
    # Update the original DataFrame
    df.update(some)
    
    
# Load the wholesale customers dataset
try:
    data = pd.read_csv("/Users/arinjoy/Projects/DataScience/customers.csv")
    data.drop(['Region','Channel'], axis = 1, inplace=True)
    print("Wholesale Customers Dataset has {} samples with {} features each".format(*data.shape))
except:
    print("DataSet Could not be loaded. is the dataset missing ?")
    

    
## Data Exploration Part
stats = data.describe()
stats

##  Implementation : Selecting Samples
# using data.loc to filter pandas Dataframe
data.loc[[100,200,300],:]
data.columns


# Fresh Filter
fresh_q1 = 3127.750000
display(data.loc[data.Fresh < fresh_q1, :].head())

# Frozen Filter
frozen_q1 = 742.250000
display(data.loc[data.Frozen < frozen_q1, :].head())

# Frozen
frozen_q3 = 3554.250000
display(data.loc[data.Frozen > frozen_q3, :].head(7))

# Hence we will be choosing:
# 1. 43: Very Low "Fresh" and Very High "Grocery"
# 2. 12: Very Low "Frozen" and Very High "Fresh"
# 3. 39: Very High "Frozen" and Very Low "Detergents_Paper"

# We will select 3 Indices of our choice i.e 43,12,39
indices = [43,12,39]

# Create a DataFrame of the chosen Samples
samples = pd.DataFrame(data.loc[indices], columns = data.columns).reset_index(drop=True)
print("chosen Samples of Wholesale Customers Dataset")
display(samples)

# Importing Library for Data Visualization
import seaborn as sns

# Get the Means
mean_data = data.describe().loc['mean',:]

# append means to the samples data
samples_bar = samples.append(mean_data)

# Construct Indices
samples_bar.index = indices + ['mean']

# PLot bar Plot
# samples_bar.plot(kind='bar', figsize=(14,8))


## Compare the Sample percentiles

# First calculate the percentile ranks of the whole dataset
percentiles = data.rank(pct=True)

# Then round it up and multiply by 100
percentiles = 100 * percentiles.round(decimals=3)

# Select the Indices we chose from the percentiles DataFrame
percentiles = percentiles.iloc[indices]

# Now, create the heat map using the seaborn library
sns.heatmap(percentiles, vmin=1, vmax=99, annot=True)


# In[ ]:




