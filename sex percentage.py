import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#read used columns
df = pd.read_csv (r'project_data.csv', usecols=[6,9,11,13,14,15])

#draw pie chart for sex


query = df[['sex', 'class']].groupby(['sex', 'class']).size().reset_index(name='counts')
query.dropna()
query2 = df[['sex']].groupby(['sex']).size().reset_index(name='counts')
#print(query)
# 1 => 1 : 26
start = 0
end = 27
labels = query['sex'].unique()
class1 = query.loc[(query['class'] == 1)]['counts'].tolist()
class2 = query.loc[(query['class'] == 0)]['counts'].tolist()

#for index, row in query.iterrows():
 #   print(row)

query2['class2'] = np.ceil((class2 / query2['counts']) *100)
query2['class1'] = (100 - query2['class2'])
print (query2)


x = np.arange(len(query2['sex']))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, query2['class1'], width, label='>50K')
rects2 = ax.bar(x + width/2, query2['class2'], width, label='<=50K')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage %')
ax.set_title('Class Percentage of sex')
ax.set_xticks(x)
plt.xticks(rotation=90)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()



#print(df[(df['class'] == 0) & (df['sex'] != 0)].count())

#plt.pie(df['sex'].value_counts(), labels=df['sex'].unique(), shadow=False, autopct='%1.2f%%')
#plt.axis('equal')
#plt.show()
#print(df['class'])
