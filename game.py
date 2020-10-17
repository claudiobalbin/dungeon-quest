import os
import time
import platform
from pynput.keyboard import Key, Listener
# from pynput import keyboard
from termcolor import colored

def clear_term():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

# def on_press(key):
#     print('{0} pressed'.format(
#         key))

def on_release(key):
    global player_x
    # print('{0} release'.format(
    #     key))
    if key == Key.esc:
        # Stop listener
        print('Exiting the game...')
        return False
    if key == Key.right and player_x < 20:
        player_x = player_x + 1
    if key == Key.left and player_x > 0:
        player_x = player_x - 1
    print(colored(player_x, 'green'))


player_x = 0

# Collect events until released
with Listener(
        # on_press=on_press,
        on_release=on_release, suppress=True) as listener:
    listener.join()

# ...or, in a non-blocking fashion:

# # print("Loading game...")
# # time.sleep(2)
# # key_name = ""
# player = "@"
# print(player)


# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         player_new = player

#         if keyboard.is_pressed('q') or keyboard.is_pressed('esc'):  # if key 'q' is pressed
#             print('Exiting...')
#             break  # finishing the loop
#         elif keyboard.is_pressed('right') and len(player) < 40:
#             player_new = " " + player
#         elif keyboard.is_pressed('left') and len(player) > 1:
#             player_new = player[1:]

#         if (player != player_new):
#             clear_term()
#             player = player_new
#             print(player)

#     except Exception as e:
#         print('Error detected, exiting the game: '+ str(e))
#         break  # if user pressed a key other than the given key the loop will break
