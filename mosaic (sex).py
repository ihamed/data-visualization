import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.mosaicplot import mosaic

#read used columns
df = pd.read_csv (r'project_data.csv', usecols=[6,9,11,13,14,15])

#draw pie chart for occupation


query = df[['sex', 'class']].groupby(['sex', 'class']).size().reset_index(name='counts')
#print(query)

labels = query['sex'].unique()
class1 = query.loc[(query['class'] == 1)]['counts'].tolist()
class2 = query.loc[(query['class'] == 0)]['counts'].tolist()


mosaic(df, ['sex','income'], title='Income by Sex Feature')
plt.show()


#print(df[(df['class'] == 0) & (df['occupation'] != 0)].count())

#plt.pie(df['occupation'].value_counts(), labels=df['occupation'].unique(), shadow=False, autopct='%1.2f%%')
#plt.axis('equal')
#plt.show()
#print(df['class'])
