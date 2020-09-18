## Implementation of City Homes and GDP Data Set Case Study

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Loading the Dataset
city_data = pd.read_csv('/Users/arinjoy/Projects/DataScience/City_Zhvi_AllHomes.csv')
print("CITY DATA")
print(city_data.head())

gdp_data = pd.read_excel('/Users/arinjoy/Projects/DataScience/gdplev.xls')
print("GDP DATA")
print(gdp_data.head())
