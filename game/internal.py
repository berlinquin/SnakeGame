from enum import Enum, auto
from dataclasses import dataclass
from time import sleep
from collections import deque


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
    # segments is a list of Points, giving each segment of the snake
    segments: deque
    # orientation gives the direction the snake is facing
    orientation: CardinalDirection

    def __len__(self):
        return len(self.segments)

    # Define head and tail attributes on Snake
    def __getattr__(self, item):
        if item == 'head' and len(self.segments) > 0:
            return self.segments[0]
        elif item == 'tail' and len(self.segments) > 0:
            return self.segments[-1]
        else:
            return None


class Board:
    def __init__(self, N: int):
        # N must be odd
        self.N = N
        self.board = [['_'] * self.N for i in range(self.N)]

    def __str__(self):
        out = ''
        for row in self.board:
            for c in row:
                out += c
            out += "\n"
        return out

    def get(self, p: Point):
        return self.board[p.x][p.y]

    def set(self, p: Point, c):
        self.board[p.x][p.y] = c


class Engine:
    def __init__(self):

        # Represent the board as a list of lists of chars
        self.board_dimensions = 7
        self.board = Board(self.board_dimensions)

        # The starting point for the snake
        snake_origin = Point(3, 3)
        # The snake object
        self.snake = Snake(deque([snake_origin]), CardinalDirection.NORTH)

        # Track which points are free using a set of points
        self.clear = set([Point(x, y) for x in range(7) for y in range(7)])
        self.clear.remove(snake_origin)

        self.board.set(self.snake.head, 'X')

        # food is a random point that is clear
        # self.food = self.clear.pop()
        self.food = Point(0, 3)
        self.board.set(self.food, 'F')

    def start(self):
        game_over = False
        while not game_over:
            self.advance()
            print(self.board)
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
        elif self.snake.orientation == CardinalDirection.WEST:
            pass
        c = self.board.get(next_head)
        grow = False
        if c == 'F':
            # Grow the snake
            grow = True
        elif c == 'X':
            # Game over
            pass
        # Handle the initial case where snake has only one segment
        if grow:
            # DONT pop the old tail
            # Add the next head to the front of the list
            self.snake.segments.appendleft(next_head)
            # Update the board
            self.board.set(next_head, 'X')
        else:
            # Pop the old tail off the list of segments
            old_tail = self.snake.segments.pop()
            # Add the next head to the front of the list
            self.snake.segments.appendleft(next_head)
            # Update the board
            self.board.set(old_tail, '_')
            self.board.set(next_head, 'X')

