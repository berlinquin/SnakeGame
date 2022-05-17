import threading
from enum import Enum, auto
from dataclasses import dataclass
from time import sleep
from collections import deque
from pathlib import Path


# Three difficulty levels the game can be played at.
# These values control the speed of play.
class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


# The number of seconds between frames for the different
# levels of difficulty
sleep_intervals = {
    Difficulty.EASY: 3,
    Difficulty.MEDIUM: 2,
    Difficulty.HARD: 1
}


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


class AsyncEngine(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.engine_lock = threading.Lock()

        # Represent the board as a list of lists of chars
        self.board_dimensions = 7
        self.board = Board(self.board_dimensions)

        # Start in medium difficulty
        self.difficulty = Difficulty.MEDIUM

        # The starting point for the snake
        snake_origin = Point(3, 3)
        # The snake object
        self.snake = Snake(deque([snake_origin]), CardinalDirection.NORTH)

        # Track which points are free using a set of points
        self.clear = set([Point(x, y) for x in range(7) for y in range(7)])
        self.clear.remove(snake_origin)

        self.board.set(self.snake.head, 'X')

        # food is a random point that is clear
        self.food = self.clear.pop()
        self.board.set(self.food, 'F')

        # True if running, False if paused
        self.running = False
        # True if a game is in progress, False if game has ended
        self.game_over = False

    # The main game loop
    def run(self):
        while not self.game_over:
            with self.engine_lock:
                if self.running:
                    self.advance()
                    print(self)
            # Sleep for the number of seconds at the given difficulty level
            sleep(sleep_intervals[self.difficulty])
        score = self.get_score()
        high_score = self.get_high_score()
        if score > high_score:
            print("New high score: {}".format(score))
            self.set_high_score(score)
        print("Game over!")

    def start_game(self):
        with self.engine_lock:
            self.running = True

    def pause(self):
        with self.engine_lock:
            self.running = False

    def restart(self):
        with self.engine_lock:
            self.running = True

    def get_score(self):
        with self.engine_lock:
            return len(self.snake)

    def get_high_score(self):
        with self.engine_lock:
            file_path = Path('high_score.txt')
            # If the high score file does not exist, return 0
            if not file_path.exists():
                return 0
            # If file can be opened, return the first line of the file converted to an int
            with open(file_path, 'r') as f:
                return int(f.readline())

    def set_high_score(self, high_score: int):
        with self.engine_lock:
            # Convert high_score to a string and write to the file
            with open('high_score.txt', 'w') as f:
                f.write(str(high_score))

    def change_direction(self, direction: CardinalDirection):
        vertical_axis = {CardinalDirection.NORTH, CardinalDirection.SOUTH}
        horizontal_axis = {CardinalDirection.EAST, CardinalDirection.WEST}
        with self.engine_lock:
            # Only change direction if changing to a different axis
            opposite_axes = (direction in vertical_axis and self.snake.orientation in horizontal_axis) \
                            or (direction in horizontal_axis and self.snake.orientation in vertical_axis)
            if opposite_axes:
                self.snake.orientation = direction

    def adjust_difficulty(self, difficulty: Difficulty):
        with self.engine_lock:
            self.difficulty = difficulty

    # Move the snake one square
    # Requires engine_lock to already have been acquired!
    def advance(self):
        next_head = None
        if self.snake.orientation == CardinalDirection.NORTH:
            next_x = (self.snake.head.x - 1) % self.board_dimensions
            next_head = Point(next_x, self.snake.head.y)
        elif self.snake.orientation == CardinalDirection.SOUTH:
            next_x = (self.snake.head.x + 1) % self.board_dimensions
            next_head = Point(next_x, self.snake.head.y)
        elif self.snake.orientation == CardinalDirection.EAST:
            next_y = (self.snake.head.y + 1) % self.board_dimensions
            next_head = Point(self.snake.head.x, next_y)
        elif self.snake.orientation == CardinalDirection.WEST:
            next_y = (self.snake.head.y - 1) % self.board_dimensions
            next_head = Point(self.snake.head.x, next_y)
        grow = False
        c = self.board.get(next_head)
        if c == 'F':
            # Grow the snake
            grow = True
        elif c == 'X':
            # Game over
            self.game_over = True
        # Only clear the tail if the snake did not grow
        if not grow:
            # Pop the old tail off the list of segments
            old_tail = self.snake.segments.pop()
            # Update the board
            self.board.set(old_tail, '_')
            # This point is now clear
            self.clear.add(old_tail)
        # Add the next head to the front of the list
        self.snake.segments.appendleft(next_head)
        self.board.set(next_head, 'X')
        # Remove next_head from clear if present
        if next_head in self.clear:
            self.clear.remove(next_head)
        # If the food was consumed, put a new food somewhere on the board
        if grow:
            self.food = self.clear.pop()
            self.board.set(self.food, 'F')

    def __str__(self):
        return str(self.board)
