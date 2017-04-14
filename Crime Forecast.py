import pygame
from Settings import *
from Coordinates import *

class CrimeVisual:
	# Initialize Pygame & Create Window
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.load_data()

	# Starting Data
	def load_data(self):
		pass

	# Restarts The Game
	def new(self):
		self.run()

	# CrimeVisual Loop
	def run(self):		
		self.playing = True
		while self.playing:
			# Keep Loop Running At The Right Speed
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	# CrimeVisual Loop - Update
	def update(self):
		coordinates()
		printBoard(grid)

	# CrimeVisual Loop - Event
	def events(self):
		for event in pygame.event.get():
			# Checks For Closing Window
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

	# CrimeVisual Loop - Draw
	def draw(self):
		self.screen.fill(BLACK)
		for row in range(332):
			for column in range(391):
				color = WHITE
				if grid[row][column] > 0:
					color = RED
				pygame.draw.rect(self.screen, color, [((CELL_MARGIN + CELL_WIDTH)*column),((CELL_MARGIN + CELL_HEIGHT)*row), CELL_WIDTH, CELL_HEIGHT], AMOUNT)

		# Alway Do The Flip Last (after drawing everything)
		pygame.display.flip()

g = CrimeVisual()
while g.running:
	g.new()
pygame.quit()
