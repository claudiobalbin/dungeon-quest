import os
import time
import keyboard

print("Teste")
# time.sleep(5)
os.system("clear")

player_x = 0

# print("Loading game...")
# time.sleep(2)
# key_name = ""
player = "@"
print(player)

def print_panel():
    """
    Prints the panel of the game
    """
    print("#########################################")
    print("#                              # health #")
    print("#                              #        #")
    print("#                              #        #")
    print("#                              #        #")
    print("#                              #        #")
    print("#                              #        #")
    print("#                              #        #")
    print("#                              #        #")
    print("#########################################")
    pass

# print_panel()

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        player_new = player

        if keyboard.is_pressed('q') or keyboard.is_pressed('esc'):  # if key 'q' is pressed 
            print('Exiting...')
            break  # finishing the loop
        elif keyboard.is_pressed('right') and len(player) < 40:
            player_new = " " + player
        elif keyboard.is_pressed('left') and len(player) > 1:
            player_new = player[1:]

        if (player != player_new):
            os.system("clear")
            player = player_new
            print(player)      

    except:
        print("Error detected, exiting the game.")
        break  # if user pressed a key other than the given key the loop will break
