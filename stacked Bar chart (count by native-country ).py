import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#read used columns
df = pd.read_csv (r'project_data.csv', usecols=[6,9,11,13,14,15])

#draw pie chart for occupation


query = df[['native-country', 'class']].groupby(['native-country', 'class']).size().reset_index(name='counts')
#query.dropna()
query2 = df[['native-country']].groupby(['native-country']).size().reset_index(name='counts')
print(query.loc[(query['native-country'] == 'Holand-Netherlands')])
# 1 => 1 : 26
start = 0
end = 27
labels = query['native-country'].unique()
class1 = query.loc[(query['class'] == 1)]
class2 = query.loc[(query['class'] == 0)]['counts'].tolist()

print(class1)

query2['class2'] = class2 / query2['counts']
query2['class1'] = 1 - query2['class2']
print (query2)
query.plot(
  x = 'native-country', 
  kind = 'barh', 
  stacked = True, 
  title = 'Percentage Stacked Bar Graph', 
  mark_right = True)


df_total = query['counts']
df_rel = query[query.columns[1:]].div(df_total, 0)*100
#print(df_rel)
for n in df_rel:
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n], 
                                         df[n], df_rel[n])):
        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', 
                 va = 'center', ha = 'center')
