import pygame
import csv
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 2
HEIGHT = 1.7

 
# This sets the margin between each cell
MARGIN = 0.5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(332):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(391):
        grid[row].append(0)  # Append a cell
 
# Setting the cell values. 
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
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [950, 731]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Visual Representation")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            quit()

    coordinates()
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(332):
        for column in range(391):
            color = WHITE
            if grid[row][column] >= 1:
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
 
    # Limit to 30 frames per second
    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
quit()