import pandas as pd
import numpy as np
import curses

def render_screen(window):
    """Render the screen considering background, itens and player"""
    back = np.loadtxt("maps/0101.txt", delimiter=",")

    for y in range(0, back.shape[0]):
        for x in range(0, back.shape[1]):
            if player_x == x and player_y == y:
                window.addstr(y, x, translate_char(2), curses.color_pair(1))
            else:
                window.addstr(y, x, translate_char(back[y,x]))
            pass
        pass

    #menus
    window.addstr(1, 21, "q:exit")
    window.addstr(3, 21, "arrows")
    window.addstr(4, 22, "move")
    window.refresh()


def translate_char(x):
    """Receves a number and return the corresponding character for map rendering"""
    df = pd.read_csv('char_dictionary.csv' ,sep=';')
    char = df.loc[df['number'] == x].values[0,1]
    if '\\' in char:
        char = bytes(char, 'utf-8').decode("unicode-escape")
    return char


# constants
player_x = 1
player_y = 1
WIDTH = 20
HEIGHT = 12

def main(stdscr):
    global player_x
    global player_y

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, 1, -1)
    curses.init_pair(2, 2, -1)
    curses.init_pair(3, 3, -1)
    curses.init_pair(4, 4, -1)
    curses.curs_set(False)

    while True:
        render_screen(stdscr)
        c = stdscr.getch()
        if c == curses.KEY_RIGHT and player_x < WIDTH - 2:
            player_x = player_x + 1
        elif c == curses.KEY_LEFT and player_x > 1:
            player_x = player_x - 1
        elif c == curses.KEY_DOWN and player_y < HEIGHT - 2:
            player_y = player_y + 1
        elif c == curses.KEY_UP and player_y > 1:
            player_y = player_y - 1
        elif c == ord('c'):
            stdscr.clear()
        elif c == ord('q'):
            break  # Exit the while loop

curses.wrapper(main)