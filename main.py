import fileinput

from game.game import start, change_direction, CardinalDirection


if __name__ == '__main__':
    start()
    # Very basic driver.
    # At the prompt, type [wasd] and hit enter to move the snake.
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
        elif c == 'q':
            break
