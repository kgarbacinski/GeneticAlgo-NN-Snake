from Vector import *

INPUT_NODES = 24
HIDDEN_NODES = 18
OUTPUT_NODES = 4
MUTATION_RATE = 0.01
PLAYABLE_AREA_WIDTH = 400
PLAYABLE_AREA_HEIGHT = 400
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# Vectors for input
LEFT_VECTOR = Vector(-10, 0)
RIGHT_VECTOR = Vector(10, 0)
UP_VECTOR = Vector(0, -10)
DOWN_VECTOR = Vector(0, 10)
LEFT_UP_VECTOR = Vector(-10, -10)
RIGHT_UP_VECTOR = Vector(10, -10)
RIGHT_DOWN_VECTOR = Vector(10, 10)
LEFT_DOWN_VECTOR = Vector(-10, 10)