from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20
pos_list = [i for i in range(CANVAS_HEIGHT-19)]

def main():
    print('Random Circles')
    draw_all_circles()
    
    
def draw_all_circles():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_CIRCLES):
        left_x   = random.choice(pos_list)
        top_y    = random.choice(pos_list)
        right_x  = left_x + CIRCLE_SIZE
        bottom_y =  top_y + CIRCLE_SIZE
        canvas.create_oval(left_x, top_y, right_x, bottom_y, random_color() )

    
def draw_one_circle():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    left_x   = random.choice(pos_list)
    top_y    = random.choice(pos_list)
    right_x  = left_x + CIRCLE_SIZE
    bottom_y =  top_y + CIRCLE_SIZE
    canvas.create_oval(left_x, top_y, right_x, bottom_y, random_color() )

    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()
