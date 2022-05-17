from .internal import print_board
# Expose this API to manage the state of the snake game

def start():
    print("start")
    game_over = False
    while not game_over:
        print_board()
        game_over = True


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
