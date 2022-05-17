import fileinput

from game.game import start, pause, change_direction, adjust_difficulty, get_state, CardinalDirection, Difficulty


if __name__ == '__main__':
    start()
    adjust_difficulty(Difficulty.MEDIUM)
    print("initial state:")
    print(get_state())
    # Very basic driver.
    # At the prompt, type [wasd] and hit enter to move the snake.
    # Type p and hit enter to pause.
    # Type q and hit enter to quit.
    for line in fileinput.input():
        c = line[0]
        if c == 'w':
            change_direction(CardinalDirection.NORTH)
        elif c == 'a':
            change_direction(CardinalDirection.WEST)
        elif c == 's':
            change_direction(CardinalDirection.SOUTH)
        elif c == 'd':
            change_direction(CardinalDirection.EAST)
        elif c == 'p':
            pause()
        elif c == 'q':
            break
