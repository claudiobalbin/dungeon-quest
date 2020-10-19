# import sys
# import time

# for i in range(10):
#     sys.stdout.write("\r{0}>".format("="*i))
#     sys.stdout.flush()
#     time.sleep(0.5)

# import time
# import curses

# def pbar(window):
#     for i in range(10):
#         window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
#         window.refresh()
#         time.sleep(0.5)

# curses.wrapper(pbar)

import curses

y = 0

def main(stdscr):
    global y
    while True:
        c = stdscr.getch()
        if c == ord('p'):
            # PrintDocument()
            stdscr.addstr(y,0,"Pretty text")
            stdscr.refresh()
            y = y + 1
        elif c == ord('c'):
            y = 0
            stdscr.clear()
        elif c == ord('q'):
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0

curses.wrapper(main)

