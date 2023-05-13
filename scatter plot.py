import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import parallel_coordinates

#read used columns
df = pd.read_csv (r'project_data.csv', usecols=[6,9,11,13,14,15])



query = df[['capital-loss', 'class']].groupby(['capital-loss', 'class']).size().reset_index(name='counts')


labels = query['capital-loss'].unique()
class1 = query.loc[(query['class'] == 1)]['counts'].tolist()
class2 = query.loc[(query['class'] == 0)]['counts'].tolist()

plt.grid(True, linewidth=0.4, color='#ff0000', linestyle='-')
plt.scatter(df['income'],df['capital-loss'])
plt.title("Capital-loss vs Income")
plt.xlabel("Income")
plt.ylabel("Capital-loss")
plt.show()


