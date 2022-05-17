from enum import Enum, auto
from dataclasses import dataclass


# Three difficulty levels the game can be played at.
# These values control the speed of play.
class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


# Available directions for the snake to move
class CardinalDirection(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


# Need to model: snake, food, game board
@dataclass(frozen=True)
class Point:
    x: int
    y: int


# Represent the snake as two points, giving its head and tail
@dataclass
class Snake:
    head: Point
    tail: Point
    length: int


# The dimensions of the board.
# Must be NxN, where N is odd.
board_dimensions = (7, 7)

# Represent the board as a list of lists of chars
board = [['_'] * 7 for i in range(7)]

snake_origin = Point(3, 3)

# Track which points are free using a set of points
clear = set([Point(x, y) for x in range(7) for y in range(7)])
clear.remove(snake_origin)

snake = Snake(snake_origin, None, 1)
board[snake.head.x][snake.head.y] = 'X'

# food is a random point that is clear
food = clear.pop()
board[food.x][food.y] = 'F'


# Helper function to print board to screen
def print_board():
    for row in board:
        for c in row:
            print(c, end='')
        print()
