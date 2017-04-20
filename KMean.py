from Coordinates import *
import csv
import random
import math

relevant = []
groupcluster1 = []
groupcluster2 = []

def KMean():
	# Open the file
	with open('Data.csv', 'r') as file:
		readerFile = csv.reader(file)
		for row in readerFile:
			xcoordinate = eval((row[1]))
			ycoordinate = eval((row[2]))

			x = int((top - ycoordinate) / 250)
			y = int((xcoordinate - left) / 250)

			# Put the need data in a list
			relevant.append((x, y))

		# Use the random function to get 2 random clusters
		centroid1 = random.choice(relevant)
		centroid2 = random.choice(relevant)

		print("Old Cluster1: ", centroid1)
		print("Old Cluster2: ", centroid2)

	# Constants used in the while loop
	loop = False
	iterations = 0
	OldCentroid1 = None
	OldCentroid2 = None
	MaxIteration = 200

	# Loop to start and end the shiftinng of cluster points
	while not loop:
		iterations += 1
		OldCentroid1 = centroid1
		OldCentroid2 = centroid2

		# Use the distance formula to determine which coordinate is closer to which cluster 
		for x in relevant:
			distance1 = math.sqrt((x[0]-centroid1[0])**2 + (x[1]-centroid1[1])**2)
			distance2 = math.sqrt((x[0]-centroid2[0])**2 + (x[1]-centroid2[1])**2)

			# If statement used to put those coordinates in their appropriate cluster group
			if distance1 > distance2:
				groupcluster2.append((x[0], x[1]))
			else:
				groupcluster1.append((x[0], x[1]))

		# Calculating the mean of the first cluster group
		xsum = 0
		ysum = 0
		for y in groupcluster1:
			xsum += y[0]
			ysum += y[1]

		xmean = int(xsum / len(groupcluster1))
		ymean = int(ysum / len(groupcluster1))

		centroid1 = (xmean, ymean)

		# Calculating the mean of the second cluster group
		sumx = 0
		sumy = 0
		for y in groupcluster2:
			sumx += y[0]
			sumy += y[1]

		meanx = int(sumx / len(groupcluster2))
		meany = int(sumy / len(groupcluster2))

		centroid2 = (meanx, meany)

		if iterations >= MaxIteration:
			loop = True	

	print("Final Cluster1: ", centroid1)
	print("Final Cluster2: ", centroid2)
	print("Number of iterations: ", iterations)

KMean()