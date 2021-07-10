"""
	Modified Conway's game of life to generate maps
	Initial author: IceCereal (https://github.com/IceCereal/The-Game-Of-Life)
"""

# IMPORTS
import random

# HEIGHT & WIDTH OF THE GRID
HEIGHT = 100
WIDTH = 100

# OTHER PARAMS
MAP_COUNT = 100 # NUMBER OF CONWAY'S GAME OF LIFE SIMULATIONS THAT NEED TO BE ADDED
EPOCHS = 100    # NUMBER OF GENERATIONS

# GRID AND IT'S CORRESPONDING EQUIVALENCY VALUES
grid = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
netVals = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
heights = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

# RANGE FOR EACH CELL
lowerBound = 2
upperBound = 3

# MAIN LOOP
def updateGrid():
	# VERSION = 2.5

	# EASY VALS:
	maxColumn = WIDTH - 1
	maxRow = HEIGHT - 1

	# 4 Corners
	netVals[0][0] = grid[0][1] + grid[1][1] + grid[1][0]
	netVals[0][maxColumn] = grid[0][maxColumn-1] + grid[1][maxColumn-1] + grid[1][maxColumn]
	netVals[maxRow][maxColumn] = grid[maxRow][maxColumn-1] + grid[maxRow-1][maxColumn-1] + grid[maxRow-1][maxColumn]
	netVals[maxRow][0] = grid[maxRow][1] + grid[maxRow-1][1] + grid[maxRow-1][0]

	# Edges
	for column in range(1, maxColumn):
		netVals[0][column] = grid[0][column-1] + grid[1][column-1] + grid[1][column] + grid[1][column+1] + grid[0][column+1]
		netVals[maxRow][column] = grid[maxRow][column-1] + grid[maxRow-1][column-1] + grid[maxRow-1][column] + grid[maxRow-1][column+1] + grid[maxRow][column+1]

	for row in range(1, maxRow):
		netVals[row][0] = grid[row-1][0] + grid[row-1][1] + grid[row][1] + grid[row+1][1] + grid[row+1][0]
		netVals[row][maxColumn] = grid[row-1][maxColumn] + grid[row-1][maxColumn-1] + grid[row][maxColumn-1] + grid[row+1][maxColumn-1] + grid[row+1][maxColumn]

	# Everything in the middle
	for row in range(1, maxRow):
		for column in range(1, maxColumn):
			netVals[row][column] = grid[row-1][column-1] + grid[row-1][column] + grid[row-1][column+1] + grid[row][column+1] + grid[row+1][column+1] + grid[row+1][column] + grid[row+1][column-1] + grid[row][column-1]

	# EVALUATION METRIC
	for row in range(0, maxRow+1):
		for column in range(0, maxColumn+1):
			state = grid[row][column]

			if (state):
				if netVals[row][column] < lowerBound:
					grid[row][column] = 0

				if netVals[row][column] > upperBound:
					grid[row][column] = 0

			else:
				if (netVals[row][column] == upperBound):
					grid[row][column] = 1



# NUMBER OF RANDOM START POINTS ON THE GRID
startLocations = 400

# FUNCTION TO RETURN THE HEIGHT VALUES FOR THE MAP
def generateMaps():

	# NUMBER OF CONWAY'S GAME OF LIFE SIMULATIONS THAT NEED TO BE ADDED
	for _ in range(MAP_COUNT):

		# GENERATING THE RANDOM START POINTS
		for i in range(startLocations):
			random.seed()
			valueWidth = random.randint(0, WIDTH-1)
			random.seed()
			valueHeight = random.randint(0, HEIGHT-1)
			grid[valueHeight][valueWidth] = 1

		# RUNNING THE EPOCHS
		for i in range(EPOCHS + 1):
			updateGrid()

		# ADDING THE FINAL GENERATION
		for row in range(0, HEIGHT):
			for column in range(0, WIDTH):
				heights[row][column] += grid[row][column]

	return heights