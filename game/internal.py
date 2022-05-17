from enum import Enum, auto


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


