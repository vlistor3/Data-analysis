# Databricks notebook source
import sklearn
import pandas as pd
from sklearn.datasets import load_iris
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import random
import matplotlib.pyplot as plt
from numpy import array, average

# COMMAND ----------

Initial_amount = 100
Number_periods = 1000
Iterations = 10000
Gain = 0.5
Loose = -0.4

# COMMAND ----------

def game(x, i):
    j = 0
    money = list()
    time = list()
    while j < i:
        r = random.randint(0,1)
        if r == 0:
            x = (1 + Loose) * x
        else:
            x = (1 + Gain) * x
        money.append(x)
        time.append(j)
        j += 1
    return time, money, i



def plotting(Amount, Periods, i):
    j = 0
    List_money = list()
    List_time = list()
    
    while j < i:
        x = game(Amount, Periods)[0]
        y = game(Amount, Periods)[1]
        List_money.append(y)
        List_time.append(x)
        j += 1
    
    array_money = array(List_money)
    time_average = average(array_money, axis = 0)
    
    fig, ax = plt.subplots(figsize=(20,15))
    ax.set_yscale("log")
    ax.set_ylabel("Money")
    ax.set_xlabel("Time")
    
    j = 0
    while j < i:
        ax.plot(List_time[j], List_money[j])
        ax.plot(List_time[0], time_average, color='purple', linewidth = 5)
        j += 1
        
    print("The final average is ", time_average[len(time_average)-1])
    
        

# COMMAND ----------

plotting(Initial_amount, Number_periods, Iterations)

# COMMAND ----------

print(pow(1.05, Iterations) )

# COMMAND ----------

i = 0

List_money = list()
List_time = list()
while i < Iterations:
    x = game(Initial_amount, Number_periods)[0]
    y = game(Initial_amount, Number_periods)[1]
    List_money.append(y)
    List_time.append(x)
    i += 1
array_money = array(List_money)
column_average = average(array_money, axis=0)
print(column_average)

fig, ax = plt.subplots(figsize=(20, 15))
ax.set_yscale('log')
ax.set_xlabel("Time")
ax.set_ylabel("Money")
for x in range(Iterations):
    ax.plot(List_time[x], List_money[x])
    ax.plot(List_time[x], column_average, color='purple', linewidth=5)
    

# COMMAND ----------

plantes_iris = load_iris()
df_plantes_iris = pd.DataFrame(plantes_iris.data, columns=plantes_iris.feature_names)

# COMMAND ----------

sns.set(style="ticks", color_codes=True)
df_plantes_iris = sns.load_dataset("iris")
sns.pairplot(df_plantes_iris, hue="species")

# COMMAND ----------

df_plantes_iris
