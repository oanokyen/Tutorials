from karel.stanfordkarel import *

"""
Karel should paint the whole world, any color you want. 
As an extension, have karel randomly paint each corner.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while left_is_clear():
        paint_row()
        get_back()
        move_up()
    paint_row()
    

def move_up():
    if left_is_clear():
        turn_left()
        move()
        turn_right()
    
def get_back():
    #pre condition : karel facing east at the last cell
    #post condition: karel facing east at the first cell
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def paint_row():
    #pre condition: karel is facing east at the first cell
    #post condition: karel is facing east at the last cell
    while front_is_clear():
        paint_cell()
        move()
    paint_cell()
    # this function is supplemented by get_back function 


def turn_around():
    for i in range(2):
        turn_left()
        
def turn_right():
    for i in range(3):
        turn_left()
        
def paint_cell():
    """Choose between green or blue in each cell"""
    #pre con: karel at cell
    #post con: karel paints and moves to new cell
    if random():
        paint_corner('blue')
    else:
        paint_corner('green')
    
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
