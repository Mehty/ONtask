from random import randint

a=[]

for i in range(100):
	a.append([randint(20,50),randint(40,100), randint(1000,3000), [randint(0,100), randint(0,100)], randint(500,2000)])
	#print a

from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import pylab as pl
from sklearn import preprocessing

# each data point is of the form [age, weight, height, caloric intake, carbs, protein, fat, exercise calories to be burnt]
X = np.array([[1, 2, 3, 6, 7 , 8, 2, 4], [1, 4, 3, 5, 5, 3, 2 ,4], [1, 3, 3, 2, 3,3, 2,3],
               [4, 2, 4, 4,4, 4, 2, 6], [4, 4, 4, 4, 4, 4, 5,7], [4, 2, 56,2,2,2, 44,4],
               [10, 3, 2, 5,5,5, 2, 1], [10, 8, 8, 5,3, 2, 5,5], [11, 5, 2,2, 4, 2, 1,1]]) 

X_scaled = preprocessing.scale(X)

print X_scaled

if len(X) > 9:
	comm = len(X)/10
else:
	comm = 1

kmeans = KMeans(n_clusters=comm, random_state=0).fit(X_scaled) # comm is the number of communities

print kmeans.labels_

#print kmeans.predict([[0, 0, 0, 6,8 ,45], [4, 4, 0, 3, 409, 6], [7,7, 0, 48, 50, 2]])

#kmeans.cluster_centers_
