from .internal import AsyncEngine, CardinalDirection

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


def restart():
    pass


def change_direction(direction: CardinalDirection):
    engine.change_direction(direction)


def adjust_difficulty():
    pass


def adjust_gameboard_size():
    pass


def get_score():
    return engine.get_score()


def get_high_score():
    pass


def get_state():
    pass
