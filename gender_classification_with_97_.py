# -*- coding: utf-8 -*-
"""Gender Classification with 97%.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hEHYEBDsNbRu8e9iWLo-Vnz0BxEkKzTa
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#visualisation
from matplotlib import pyplot as plt
import seaborn as sns

import os
for dirname, _, filenames in os.walk('gender_classification_v7.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#Import data
data = pd.read_csv('gender_classification_v7.csv')

male = data[data.gender == "Male"]
female = data[data.gender == "Female"]

#Exploratory Data Analysis (EDA)
data.info()

data.head()

labels = data.gender.value_counts().index
color = ['red','blue']
explode = [0,0]
sizes = data.gender.value_counts().values


plt.figure(figsize=(5,5))
plt.pie(sizes, explode=explode, labels=labels, colors=color, autopct="%1.1f%%")
plt.title(label="Gender Distribution", color="red",fontsize=17)
plt.show()

#males and females ratio is %50 %50.

sns.scatterplot(data=data,x="forehead_width_cm",y="forehead_height_cm",hue="gender")
plt.show()

male2=male.drop(["forehead_width_cm","forehead_height_cm","gender"],axis=1)
df_meltedmale = male2.melt(var_name='collumn')
female2=female.drop(["forehead_width_cm","forehead_height_cm","gender"],axis=1)
df_meltedfemale = female2.melt(var_name='collumn')

g = sns.FacetGrid(df_meltedmale, col='collumn',)
g.map(plt.hist, 'value')
g.fig.suptitle("male collumn histograms",color="red")
plt.show()
h = sns.FacetGrid(df_meltedfemale, col='collumn',)
h.map(plt.hist, 'value')
h.fig.suptitle("female collumn histograms",color="red")
plt.show()

male3=male.iloc[:,[1,2]]
df_meltedmale1 = male3.melt(var_name='collumn')
female3=female.iloc[:,[1,2]]
df_meltedfemale1 = female3.melt(var_name='collumn')

g = sns.FacetGrid(df_meltedmale1, col='collumn',)
g.map(plt.hist, 'value')
g.fig.suptitle("male collumn histograms",color="red")
plt.show()
h = sns.FacetGrid(df_meltedfemale1, col='collumn',)
h.map(plt.hist, 'value')
h.fig.suptitle("female collumn histograms",color="red")
plt.show()

sns.heatmap(male.corr(numeric_only=True),annot=True,linewidths=3,)
plt.title("male correlation table",color="Blue")
plt.show()

sns.heatmap(female.corr(numeric_only=True),annot=True,linewidths=3,)
plt.title("male correlation table",color="Red")
plt.show()

sns.heatmap(data.corr(numeric_only=True),annot=True,linewidths=3,)
plt.title("all data correlation table",color="Red")
plt.show()

#Creating Classification Models
data.gender = [1 if i=="Male" else 0 for i in data.gender]

data.head()

x = data.drop(["gender"],axis=1)
y = data["gender"]

#Train Test Split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)

#Logistic Regression
#Accuracy: %96.40
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

print("Logistic Regression score: {}".format(lr.score(x_test, y_test)))

from sklearn.metrics import confusion_matrix

cf = confusion_matrix(y_test, y_pred)

print(cf)

from matplotlib import pyplot as plt
import seaborn  as sns

sns.heatmap(cf, annot = True, linewidths=3, fmt="0.0f")
plt.xlabel("y_pred")
plt.ylabel("y_test")
plt.show()

#KNN algorithm
#Accuracy: %97.00

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 3) # n_neighbors = k
knn.fit(x_train,y_train)
prediction = knn.predict(x_test)
print(" {} nn score: {} ".format(3,knn.score(x_test,y_test)))

score_list = []
for each in range(1,50):
    knn2 = KNeighborsClassifier(n_neighbors = each)
    knn2.fit(x_train,y_train)
    score_list.append(knn2.score(x_test,y_test))

plt.plot(range(1,50),score_list)
plt.xlabel("k values")
plt.ylabel("accuracy")
plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn16 = KNeighborsClassifier(n_neighbors = 16) # n_neighbors = k
knn16.fit(x_train,y_train)
prediction = knn16.predict(x_test)
print(" {} nn score: {} ".format(16,knn16.score(x_test,y_test)))

cf = confusion_matrix(y_test, prediction)

print(cf)

from matplotlib import pyplot as plt
import seaborn  as sns

sns.heatmap(cf, annot = True, linewidths=3, fmt="0.0f")
plt.xlabel("prediction")
plt.ylabel("y_test")
plt.show()

#Naive Bayes
#Accuracy: %96.53

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
nb.fit(x_train,y_train)

y_pred = nb.predict(x_test)

print("Naive Bayes score: {}".format(nb.score(x_test, y_test)))

cf = confusion_matrix(y_test, y_pred)

print(cf)

from matplotlib import pyplot as plt
import seaborn  as sns

sns.heatmap(cf, annot = True, linewidths=3, fmt="0.0f")
plt.xlabel("y_pred")
plt.ylabel("y_test")
plt.show()

#SVM Algorithm
#Accuracy: %96.93
from sklearn.svm import SVC

svm = SVC(random_state=1)
svm.fit(x_train,y_train)

print("SVM Algorithm score: {}".format(svm.score(x_test, y_test)))

y_pred = svm.predict(x_test)

cf = confusion_matrix(y_test, y_pred)

print(cf)

from matplotlib import pyplot as plt
import seaborn  as sns

sns.heatmap(cf, annot = True, linewidths=3, fmt="0.0f")
plt.xlabel("y_pred")
plt.ylabel("y_test")
plt.show()

#Decision Tree Classification
#Accuracy: %95.73
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)

print("Decision Tree Classification score: {}".format(dt.score(x_test, y_test)))

y_pred = dt.predict(x_test)

cf = confusion_matrix(y_test, y_pred)

print(cf)

from matplotlib import pyplot as plt
import seaborn  as sns

sns.heatmap(cf, annot = True, linewidths=3, fmt="0.0f")
plt.xlabel("y_pred")
plt.ylabel("y_test")
plt.show()

#Random Forest Classification
#Accuracy: %96.26
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=68, random_state=42)
rf.fit(x_train, y_train)
print("Random Forest Classification score: {}".format(rf.score(x_test, y_test)))

y_pred = rf.predict(x_test)

score_list = []
for each in range(1,80):
    rf = RandomForestClassifier(n_estimators=each, random_state=42)
    rf.fit(x_train, y_train)
    score_list.append(rf.score(x_test, y_test))

plt.plot(range(1,80),score_list)
plt.xlabel("n_estimators values")
plt.ylabel("accuracy")
plt.show()

cf = confusion_matrix(y_test, y_pred)

print(cf)

from matplotlib import pyplot as plt
import seaborn  as sns

sns.heatmap(cf, annot = True, linewidths=3, fmt="0.0f")
plt.xlabel("y_pred")
plt.ylabel("y_test")
plt.show()

#%97 accuracy at best with KNN(k=16) algorithm.