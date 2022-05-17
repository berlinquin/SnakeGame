from .internal import AsyncEngine, CardinalDirection, Difficulty

# Expose this API to manage the state of the snake game

# instance of the Engine class to drive the game
engine = None


def start():
    print("start")
    global engine
    engine = AsyncEngine()
    # Start the thread, calling engine.run()
    engine.start()
    # Start the game
    engine.start_game()


def pause():
    engine.pause()


# Implement this as "resume", continuing an existing game,
# instead of starting a new game.
# (Assuming that's the intent as the opposite of "pause")
def restart():
    engine.restart()


def change_direction(direction: CardinalDirection):
    engine.change_direction(direction)


def adjust_difficulty(difficulty: Difficulty):
    pass


def adjust_gameboard_size():
    pass


def get_score():
    return engine.get_score()


def get_high_score():
    return engine.get_high_score()


def get_state():
    pass
