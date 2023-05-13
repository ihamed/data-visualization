import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import parallel_coordinates

#read used columns
df = pd.read_csv (r'project_data.csv', usecols=[6,9,11,13,14,15])

#draw pie chart for occupation



#print(df['occupation'].value_counts())

#query = df[['occupation', 'class', 'sex']].groupby(['occupation', 'class']).count()
query = df[['capital-loss', 'class']].groupby(['capital-loss', 'class']).size().reset_index(name='counts')
#print(query)

labels = query['capital-loss'].unique()
class1 = query.loc[(query['class'] == 1)]['counts'].tolist()
class2 = query.loc[(query['class'] == 0)]['counts'].tolist()
#result = pd.DataFrame(columns=['income', 'c1', 'c2'])
#result = [[]]
#print(query)
#parallel_coordinates(query[[ 'capital-loss','counts', 'class']][2:], 'class')
#plt.gca().legend_.remove()








fig, ax = plt.subplots(2, figsize=(10, 6))
ax[0].scatter(df.loc[(df['class'] == 1)]['capital-loss'], df.loc[(df['class'] == 1)]['income'])
ax[0].set_xlabel("Income >50k vs Capital Loss")
ax[0].set_ylabel("Income")

ax[1].scatter(df.loc[(df['class'] == 0)]['capital-loss'], df.loc[(df['class'] == 0)]['income'])
ax[1].set_xlabel("Income <=50k vs Capital Loss")
ax[1].set_ylabel("Income")

plt.show()
#plt.show()


#print(df[(df['class'] == 0) & (df['occupation'] != 0)].count())

#plt.pie(df['occupation'].value_counts(), labels=df['occupation'].unique(), shadow=False, autopct='%1.2f%%')
#plt.axis('equal')
#plt.show()
#print(df['class'])
