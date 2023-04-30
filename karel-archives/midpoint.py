### fails authentication although it seems to be working fine with 2x2/5x5/6x6 worlds

from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    add_corners()

def add_corners():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    pick_beeper()
    move()
    if no_beepers_present():
        put_beeper()
        move()
        while no_beepers_present():
            move()
        turn_around()
        pick_beeper()
        move()
        if no_beepers_present():
            put_beeper()
            move()
            while no_beepers_present():
                paint_corner('green')
                move()
            if beepers_present():
                pick_beeper()
                turn_around()
            while no_beepers_present():
                move()
            pick_beeper()
            turn_around()
            move()
            put_beeper()
            paint_corner(' ')
            move()
            while corner_color_is('green'):
                paint_corner(' ')
                move()
            turn_around()
            while no_beepers_present():
                move()
            turn_around()
    else:
        while front_is_clear():
            move()
        turn_around()
    

    
    
def turn_around():
    turn_left()
    turn_left()
if __name__ == '__main__':
    main()
