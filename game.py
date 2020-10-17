import os
import time
import platform
from pynput.keyboard import Key, Listener
from termcolor import colored
import pandas as pd
import json
import numpy as np

def clear_term():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

# def on_press(key):
#     print('{0} pressed'.format(
#         key))

def render_screen():
    """Render the screen considering background, itens and player"""
    back = np.loadtxt("maps/0101.txt", delimiter=",")

    for y in range(0, back.shape[0]):
        for x in range(0, back.shape[1]):
            if player_x == x and player_y == y:
                print(translate_char(2), end = '')
            else:
                print(translate_char(back[y,x]), end ='')
            pass
        print()
        pass


def translate_char(x):
    """Receves a number and return the corresponding character for map rendering"""
    df = pd.read_csv('char_dictionary.csv' ,sep=';')
    char = df.loc[df['number'] == x].values[0,1]
    return char


def on_release(key):
    """Deals with the keystroke"""
    global player_x
    global player_y
    if key == Key.esc:
        # Stop listener
        print('Exiting the game...')
        return False
    if key == Key.right and player_x < 8:
        player_x = player_x + 1
    if key == Key.left and player_x > 1:
        player_x = player_x - 1
    if key == Key.down and player_y < 4:
        player_y = player_y + 1
    if key == Key.up and player_y > 1:
        player_y = player_y - 1
    clear_term()
    render_screen()
    # print(player_x)
    # print(colored(player_x, 'green'))


player_x = 1
player_y = 1

# Collect events until released
with Listener(
        # on_press=on_press,
        on_release=on_release, suppress=True) as listener:
    listener.join()
