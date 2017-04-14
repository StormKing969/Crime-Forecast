from Settings import *
import csv

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(332):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(391):
        grid[row].append(0)  # Append a cell

def coordinates():
	count = 0
	with open('Data.csv', 'r') as file:
		readerFile = csv.reader(file)
		for row in readerFile:
			xcoordinate = eval((row[1]))
			ycoordinate = eval((row[2]))
			
			top = 733940
			left = 7603950
		
			x = int((top - ycoordinate) / 250)
			y = int((xcoordinate - left) / 250)

			try: 
				grid[x][y] +=  1
			except IndexError:
				count += 1  
				
def printBoard(A):
    resultFile = open('Result.txt', 'w')
    for row in grid:
    	for col in row:
    		resultFile.write(str(col))
    	resultFile.write('\n')
    resultFile.close()