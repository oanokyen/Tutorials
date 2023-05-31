from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CROSS_HEIGHT = 60
CROSS_WIDTH = 15

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    georgia_flag(canvas)
    

def georgia_flag(canvas):
    #draw entire georgia flag 
    draw_small_cross(canvas)
    #draw_box(canvas,CANVAS_WIDTH/4,CANVAS_HEIGHT/4,CROSS_HEIGHT,'black' )
    draw_cross(canvas,CANVAS_WIDTH/2,CANVAS_HEIGHT/2,CANVAS_HEIGHT,CANVAS_WIDTH/10, 'red' )

def draw_small_cross(canvas):
    ''' draw all crosses (or a plus) on canvas in all 4 quadrants'''  
    # bottom left quadrant
    draw_cross(canvas,CANVAS_WIDTH/4,CANVAS_HEIGHT*0.75,CROSS_HEIGHT,CROSS_WIDTH, 'red' )
    
    #bottm right quadrant
    draw_cross(canvas,CANVAS_WIDTH*0.75,CANVAS_HEIGHT*0.75,CROSS_HEIGHT,CROSS_WIDTH, 'red' )
    
    # top right quadrant
    draw_cross(canvas,CANVAS_WIDTH*0.75,CANVAS_HEIGHT/4,CROSS_HEIGHT,CROSS_WIDTH, 'red' )
    
    #top left quadrant
    draw_cross(canvas,CANVAS_WIDTH/4,CANVAS_HEIGHT/4,CROSS_HEIGHT,CROSS_WIDTH, 'red' )
    
    
def draw_box(canvas, center_x, center_y,height, color):
    '''Draw a square with black outlines that enclose a cross/plus
    '''
    x1= center_x - height/2
    x2= x1+ height
    y1= center_y-height/2
    y2= y1+ height
    # top line
    canvas.create_line(x1, y1, x2, y1, color)
    
    #left line
    canvas.create_line(x1, y1, x1, y2, color)

    # down line
    canvas.create_line(x1, y2, x2, y2, color)
    
    #right line
    canvas.create_line(x2, y1, x2, y2, color)


def draw_cross(canvas, center_x, center_y,height,width, color):
    ''' draw a cross (or a plus) on canvas by inputting center coordinates, height and width 
    ''' 
    left_x = center_x - height/2
    right_x= left_x + height
    top_y = center_y - width/2
    bottom_y = top_y + width
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, color)
        
    top_y = center_y - height/2
    bottom_y= top_y + height
    left_x = center_x - width/2
    right_x = left_x + width
    
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, color)
if __name__ == '__main__':
    main()
