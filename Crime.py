import csv

grid = []
for row in range(331):
    grid.append([])
    for column in range(390):
        grid[row].append(0)  

def printBoard(A):
    resultFile = open('Result.txt', 'w')
    for row in grid:
    	for col in row:
    		resultFile.write(str(col))
    	resultFile.write('\n')
    resultFile.close()


def coordinates():	
	count = 0
	with open('Data.csv', 'r') as file:
		readerFile = csv.reader(file)
		for row in readerFile:
			x = eval((row[1]))
			y = eval((row[2]))
			
			top = 733940
			left = 7603950
		
			i = int((top - y) / 250)
			j = int((x - left) / 250)

			try: 
				grid[i][j] +=  1
			except IndexError:
				count += 1   

coordinates()
printBoard(grid)