from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQ_SIZE= CANVAS_HEIGHT/8

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    
    for i,x_cord in enumerate(range(0,400,50)): # x_cord = break square length into 8 and return each x1 cordinate
        if is_odd(i+1) == True: # divide the length into 8 and run different codes for odd and even squares
            for i,y_cord in enumerate(range(0,400,50)): # start at the first row for odd x_cord
                if is_odd(i+1) == True:
                    draw_square(canvas, x_cord, y_cord, SQ_SIZE)
        else: #start at the second row for even x_cord
            for i,y_cord in enumerate(range(0,400,50)):
                if is_odd(i+1) == False:
                    draw_square(canvas, x_cord, y_cord, SQ_SIZE)
                    
                    
def draw_square(canvas, x1, y1, SQ_SIZE):
    '''Build a square using the cordinates of 
    the top left corner of the square'''
    left_x = x1
    top_y = y1
    right_x = left_x + SQ_SIZE
    bottom_y = top_y + SQ_SIZE
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y)
    
def is_odd(value):
    # return True if value is odd and False if even
    remainder = value % 2
    return remainder == 1

if __name__ == '__main__':
    main()
