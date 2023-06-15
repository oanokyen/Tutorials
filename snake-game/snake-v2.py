"""
File: snake_game-full.py
-------------------
For my final project, I will attempt to make a version of the classic Atari game of Snake. 
It was famously shipped on the original Apple II computers as well as Nokia phones.

Functionalities include:
1. Snake increases after eating food
2. Snake speeds up after each food taking
3. Score is incremented
4. Game ends when snake hits itself  
"""

#load dependencies

from graphics import Canvas
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
DELAY=0.1
SIZE = 20

#initial snake 
X_INITIAL=0
Y_INITIAL=0

def main():
    
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    #create snake
    snake_rect =[[X_INITIAL,Y_INITIAL]]
    snake = player(canvas, snake_rect,SIZE)
    

    # create the snake food rectangle
    snake_food = food(canvas, SIZE)
    
    # default direction
    key="ArrowRight"
    
    # change direction
    X_CHANGE =0
    Y_CHANGE =0
    
    # start score
    SCORE = 0
    
    # increasing speed
    SNAKE_SPEED = DELAY
    
    # direction loop
    while True:
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            print('left arrow pressed!')
            X_CHANGE = -SIZE
            Y_CHANGE = 0
        if key == 'ArrowRight':
            print('right arrow pressed!')
            X_CHANGE = SIZE
            Y_CHANGE = 0
        if key == 'ArrowUp':
            print('up arrow pressed!')
            X_CHANGE = 0
            Y_CHANGE = -SIZE
        if key == 'ArrowDown':
            print('down arrow pressed!')
            X_CHANGE = 0
            Y_CHANGE = SIZE
        
        #move snake around
        canvas.move(snake[-1], X_CHANGE, Y_CHANGE) # only move snake head in that direction
        
        #move snake tail where the head goes
        for i in range(len(snake[:])):
            if i+1<len(snake[:]):
                canvas.moveto(snake[i], canvas.get_left_x(snake[i+1]),canvas.get_top_y(snake[i+1]))
        
        
        # get snake head coordinates
        x_loc = canvas.get_left_x(snake[-1])
        y_loc = canvas.get_top_y(snake[-1])
        
        #conditions to end game
        #1 out of bounds
        if (x_loc<0) or (x_loc>=CANVAS_WIDTH) or (y_loc<0) or (y_loc>= CANVAS_HEIGHT):
            #print("GAME OVER")
            break
        
        #2 snake bite itself
        objs = canvas.find_overlapping(x_loc, y_loc, x_loc+SIZE, y_loc+SIZE)
        if (x_loc!=canvas.get_left_x(snake_food) and y_loc!=canvas.get_top_y(snake_food)):
            # when snake is not eating and multiple shapes collide
            if len(objs)>2:
                #print("GAME OVER")
                break
        
        # when snake eats food
        if (x_loc ==canvas.get_left_x(snake_food)) and (y_loc==canvas.get_top_y(snake_food)):            
            SCORE+=1
            
            # get new snake_rect shape coordinate
            snake_rect=[]
            for old_snake in snake:
                coords = canvas.coords(old_snake)
                snake_rect.append(coords)
                #canvas.delete(old_snake)
            snake_rect.append([x_loc,y_loc])
            
            
            move_food(canvas, snake_food, snake_rect)
            
            #refresh snake 
            for old_snake in snake:
                canvas.delete(old_snake)
            
            snake = player(canvas, snake_rect,SIZE)
            
            # increment snake speed
            SNAKE_SPEED -=SNAKE_SPEED/20
            SCORE*=1.1 # speed score multiplier
        #print(snake_rect)
        
        # print scores
        score_obj = canvas.create_text(1, 387,text=f"{round(SCORE)} points")
        
        # delay
        time.sleep(SNAKE_SPEED)
        #print(SNAKE_SPEED," s")
        
        
        # Delete old scores text
        canvas.delete(score_obj)
        
    # show result
    result = "Your Score is : " + str(round(SCORE))
    canvas.create_text((CANVAS_WIDTH/2)-80, (CANVAS_HEIGHT/2)-20, 'GAME OVER', font='Lato', font_size = 30, color='red')
    canvas.create_text((CANVAS_WIDTH/2)-40, (CANVAS_HEIGHT/2)+14, result, color='black')


def player(canvas, snake_rect,y_SIZE):
    '''Create snake on the canvas. snake_rect is a list of shapes.
    Snake head is the ssmae colour as the snake food.
    '''
    snake_length=[]
    for i in snake_rect:
        if i==snake_rect[-1]:
            colour = "red"
        else:
            colour="blue"
        left_x = i[0]
        top_y = i[1]
        right_x = left_x + SIZE
        bottom_y = top_y + y_SIZE
        snake_length.append(canvas.create_rectangle(left_x, top_y, right_x, bottom_y, colour))
    return snake_length
    
# create snake food    
def food(canvas, SIZE):
    '''Create the snake food on the canvas
    '''
    left_x = 360
    top_y = 360
    right_x = left_x + SIZE
    bottom_y = top_y + SIZE
    return canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "red")
    
    
# Move the food to a new location
def move_food(canvas, food, snake_rect):
    ''' Move snake food to another random position 
    '''
    random_list = [i for i in range(0,380,20)]
    food_x = random.choice(random_list)
    food_y = random.choice(random_list)
    canvas.moveto(food, food_x, food_y)

    
if __name__ == '__main__':
    main()
