from .internal import Engine

# Expose this API to manage the state of the snake game

# instance of the Engine class to drive the game
engine = None


def start():
    print("start")
    global engine
    engine = Engine()
    engine.start()


def pause():
    pass


def restart():
    pass


def adjust_difficulty():
    pass


def adjust_gameboard_size():
    pass


def get_score():
    pass


def get_high_score():
    pass


def get_state():
    pass
