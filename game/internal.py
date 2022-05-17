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
        self.snake = Snake(snake_origin, None, 1, CardinalDirection.NORTH)

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
            self.snake.length += 1
            grow = True
        elif c == 'X':
            # Game over
            pass
        # Handle the initial case where snake has only one segment
        if self.snake.tail is None:
            # Update the board with the new location of the snake's head
            self.board.set(next_head, 'X')
            if grow:
                self.snake.tail = self.snake.head
            else:
                # Clear location of the current head
                self.board.set(self.snake.head, '_')
            # Update snake
            self.snake.head = next_head
        else:
            # Update the board with the new location of the snake's head
            self.board.set(next_head, 'X')
            if grow:
                pass
            else:
                # Clear location of the current head
                self.board.set(self.snake.tail, '_')
                # Need to update tail...
            # Update snake
            self.snake.head = next_head

