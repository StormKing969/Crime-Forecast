import numpy as np
from Coordinates import *
import csv
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

relevant = []

with open('Data.csv', 'r') as file:
	readerFile = csv.reader(file)
	for row in readerFile:
		xcoordinate = eval((row[1]))
		ycoordinate = eval((row[2]))

		x = int((top - ycoordinate) / 250)
		y = int((xcoordinate - left) / 250)

		
		if (x <= 330 and x >= 0) and (y >= 0 and y <= 389):
			relevant.append([x, y])

X = np.array(relevant)

Kmeans = KMeans(n_clusters = 2)
Kmeans.fit(X)

centroids = Kmeans.cluster_centers_
labels = Kmeans.labels_

colors = ["g.", "c."]

for i in range(len(X)):
	plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 1)

plt.scatter(centroids[:, 0], centroids[:, 1], marker = "x", s = 150, linewidths = 5, zorder = 5)
plt.show()