import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#read used columns
df = pd.read_csv (r'project_data.csv', usecols=[6,9,11,13,14,15])

#draw pie chart for occupation



#print(df['occupation'].value_counts())

query = df[['occupation', 'class', 'sex']].groupby(['occupation', 'class']).count()
query = df[['occupation', 'class']].groupby(['occupation', 'class']).size().reset_index(name='counts')
#print(df[['occupation', 'class']].groupby(['occupation', 'class']).size().reset_index(name='counts'))

labels = query['occupation'].unique()
class1 = query.loc[(query['class'] == 1)]['counts'].tolist()
class2 = query.loc[(query['class'] == 0)]['counts'].tolist()

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
print(class2)
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, class1, width, label='>50K')
rects2 = ax.bar(x + width/2, class2, width, label='<=50K')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count')
ax.set_title('Count By Occupation')
ax.set_xticks(x)
plt.xticks(rotation=60)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()



#print(df[(df['class'] == 0) & (df['occupation'] != 0)].count())

#plt.pie(df['occupation'].value_counts(), labels=df['occupation'].unique(), shadow=False, autopct='%1.2f%%')
#plt.axis('equal')
#plt.show()
#print(df['class'])
