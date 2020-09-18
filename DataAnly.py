import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('Position_Salaries.csv')
sb.regplot(x="Level",y="Salary",data=df)
plt.show()