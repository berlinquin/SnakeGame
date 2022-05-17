from enum import Enum, auto
from dataclasses import dataclass
from time import sleep


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
    orientation: CardinalDirection


class Engine:
    def __init__(self):
        # The dimensions of the board.
        # Must be NxN, where N is odd.
        self.board_dimensions = 7

        # Represent the board as a list of lists of chars
        self.board = [['_'] * 7 for i in range(7)]

        # The starting point for the snake
        snake_origin = Point(3, 3)
        # The snake object
        self.snake = Snake(snake_origin, None, 1, CardinalDirection.NORTH)

        # Track which points are free using a set of points
        self.clear = set([Point(x, y) for x in range(7) for y in range(7)])
        self.clear.remove(snake_origin)

        self.board[self.snake.head.x][self.snake.head.y] = 'X'

        # food is a random point that is clear
        self.food = self.clear.pop()
        self.board[self.food.x][self.food.y] = 'F'

    def start(self):
        game_over = False
        while not game_over:
            self.advance()
            self.print_board()
            sleep(2)

    # Move the snake one square
    def advance(self):
        next_head = None
        if self.snake.orientation == CardinalDirection.NORTH:
            next_x = (self.snake.head.x - 1) % self.board_dimensions
            next_head = Point(next_x, self.snake.head.y)
        elif self.snake.orientation == CardinalDirection.SOUTH:
            next_x = (self.snake.head.x + 1) % self.board_dimensions
            next_head = Point(next_x, self.snake.head.y)
        elif self.snake.orientation == CardinalDirection.EAST:
            pass
        # if self.board[next_head.x][next_head.y] == '':
        # if self.snake.tail is None:
        #     self.board[next_head.x][next_head.y]

    # Print board to screen
    def print_board(self):
        for row in self.board:
            for c in row:
                print(c, end='')
            print()

