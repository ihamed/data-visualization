import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#read used columns
df = pd.read_csv (r'project_data.csv', usecols=[6,9,11,13,14,15])

#draw pie chart for capital-loss


query = df[['capital-loss', 'class']].groupby(['capital-loss', 'class']).size().reset_index(name='counts')
query.dropna()
query2 = df[['capital-loss']].groupby(['capital-loss']).size().reset_index(name='counts')
#print(query)
# 1 => 1 : 26
start = 0
end = 27
labels = query['capital-loss'].unique()
class1 = query.loc[(query['class'] == 1)]['counts'].tolist()
class2 = query.loc[(query['class'] == 0)]['counts'].tolist()

c1 =[]
c2 =[]
flag = 0
for index, row in query.iterrows():
    if flag == 1:
        flag = 0
        continue
    if (index + 1 < len(query)):
        if(row['capital-loss'] == query['capital-loss'][index+1] ):
            class1_va1 = query.loc[(query['capital-loss'] == row['capital-loss']) & query['class'] == 1 ]['counts'].tolist()
            class2_va1 = query.loc[(query['capital-loss'] == row['capital-loss']) & query['class'] == 0 ]['counts'].tolist()
            count = query2.loc[( query2['capital-loss'] == row['capital-loss'])]['counts'].tolist()
            #print(class1_va1, count)
            c1.append( np.ceil(( class1_va1[0] / count[0] ) *100))
            c2.append(100- np.ceil(( class1_va1[0] / count[0] ) *100))
            flag = 1
        else:
            if (row['class'] == 1):
                c1.append(100)
                c2.append(0)
            else:
                c2.append(100)
                c1.append(0)
    elif(index == len(query)-1):
        if (row['class'] == 1):
            c1.append(100)
            c2.append(0)
        else:
            c2.append(100)
            c1.append(0)
print(len(c1))
query2['class1'] = c1
query2['class2'] = c2

print (query2)


x = np.arange(len(query2['capital-loss']))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, query2['class1'], width, label='>50K')
rects2 = ax.bar(x + width/2, query2['class2'], width, label='<=50K')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage %')
ax.set_title('Class Percentage of capital-loss')
ax.set_xticks(x)
plt.xticks(rotation=90)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()



#print(df[(df['class'] == 0) & (df['capital-loss'] != 0)].count())

#plt.pie(df['capital-loss'].value_counts(), labels=df['capital-loss'].unique(), shadow=False, autopct='%1.2f%%')
#plt.axis('equal')
#plt.show()
#print(df['class'])
