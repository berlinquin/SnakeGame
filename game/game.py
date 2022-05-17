from .internal import AsyncEngine, CardinalDirection, Difficulty, BoardSize

# Expose this API to manage the state of the snake game

# instance of the Engine class to drive the game
engine = None


# Start a game of snake in another thread
def start():
    global engine
    engine = AsyncEngine()
    # Start the thread, calling engine.run()
    engine.start()
    # Start the game
    engine.start_game()


# Pause the game
def pause():
    engine.pause()


# Implement this as "resume", continuing an existing game,
# instead of starting a new game.
# (Assuming that's the intent as the opposite of "pause")
def restart():
    engine.restart()


# Change the direction of the snake
def change_direction(direction: CardinalDirection):
    engine.change_direction(direction)


# Adjust the difficulty of the game
def adjust_difficulty(difficulty: Difficulty):
    engine.adjust_difficulty(difficulty)


# Adjust the size of the game board
def adjust_gameboard_size(board_size: BoardSize):
    engine.adjust_gameboard_size(board_size)


# Return the score of the current game
def get_score():
    return engine.get_score()


# Return the high score across multiple games
def get_high_score():
    return engine.get_high_score()


# Return a string representation of the board
def get_state():
    return str(engine)
