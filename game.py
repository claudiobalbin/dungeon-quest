import pandas as pd
import numpy as np
import curses

def render_screen(window):
    """Render the screen considering background, itens and player"""
    global back_arr

    if back_arr.size == 0:
        back_arr = np.loadtxt("maps/0101.txt", delimiter=",")

    try:
        for y in range(0, back_arr.shape[0]):
            for x in range(0, back_arr.shape[1]):
                if player_x == x and player_y == y:
                    window.addstr(y, x, translate_char(2), curses.color_pair(4))
                else:
                    window.addstr(y, x, translate_char(back_arr[y,x]))
                pass
            pass
        pass
    except Exception as ex:
        # print('Msg de Erro: ' + str(ex))
        # TODO: running the game from vscode generates an exception in line 18,
        # so this try/except is to workaround it for now
        pass

    #menus
    window.addstr(1, 21, "q:exit")
    window.addstr(3, 21, "arrows")
    window.addstr(4, 22, "move")
    window.refresh()


def translate_char(x):
    """Receves a number and return the corresponding character for map rendering"""
    global char_df
    
    if char_df.empty:
        char_df = pd.read_csv('char_dictionary.csv' ,sep=';')
    char = char_df.loc[char_df['number'] == x].values[0,1]
    if '\\' in char:
        char = bytes(char, 'utf-8').decode("unicode-escape")
    return char


# constants
player_x = 1
player_y = 1
WIDTH = 20
HEIGHT = 12
char_df = pd.DataFrame()
back_arr = np.array([])

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