"""
File: snake_game-full.py
-------------------
For my final project, I will attempt to make a version of the classic Atari game of Snake. 
It was famously shipped on the original Apple II computers as well as Nokia phones.
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
        
        # move snake
        
        canvas.move(snake[-1], x_change, y_change) # only move snake head in that direction        time.sleep(0.10)
        #reversed_snake = snake[::-1]
        for i in range(len(snake[:])):
            if i+1<len(snake[:]):
                #time.sleep(snake_speed/2)
                canvas.moveto(snake[i], canvas.get_left_x(snake[i+1]),canvas.get_top_y(snake[i+1]))
        
            #    print(reversed_snake[i], "get left: ",canvas.get_left_x(reversed_snake[i]), "front left:",canvas.get_left_x(reversed_snake[i-1])  )
        #    print((snake[:-1])[i])
            #reversed_snake[i]
        #time.sleep(0.6)
        #canvas.moveto(snake[-2], canvas.get_left_x(snake[-1]),canvas.get_top_y(snake[-1]))
        #time.sleep(0.10)
        #coords = canvas.coords(snake[0])
        #print(coords)
        
        #time.sleep(0.6)
        #canvas.moveto(snake[-3], canvas.get_left_x(snake[-2]),canvas.get_top_y(snake[-2]))
        #canvas.moveto(snake[-4], canvas.get_left_x(snake[-3])-20,canvas.get_top_y(snake[-3]))
        
        #for i in snake[::-1]: # other snake parts just follow snake head
        #    time.sleep(DELAY*5)
            
            # get snake head position
            #snake_head_x =  canvas.get_left_x(snake[-1])
            #snake_head_y = canvas.get_top_y(snake[-1])
            
            #canvas.move(i,x_change, y_change )
            #canvas.moveto(i, snake_head_x,snake_head_y) 
        
        
        x_loc = canvas.get_left_x(snake[-1])
        y_loc = canvas.get_top_y(snake[-1])
        
        #conditions to end game
        #1 out of bounds
        if (x_loc<0) or (x_loc>=CANVAS_WIDTH) or (y_loc<0) or (y_loc>= CANVAS_HEIGHT):
            print("GAME OVER")
            break
        #2 snake bite itself
        objs = canvas.find_overlapping(x_loc, y_loc, x_loc+SIZE, y_loc+SIZE)
        if x_loc!=canvas.get_left_x(snake_food) and y_loc!=canvas.get_top_y(snake_food):
            if len(objs)>2:
                print("GAME OVER")
                break
        
        # when snake eats food
        if x_loc==canvas.get_left_x(snake_food) and y_loc==canvas.get_top_y(snake_food):            
            score+=10
            snake_rect=[]
            #for i in range(len(snake)):
            #    coords = canvas.coords(snake[i])
            #    snake_rect.append(coords)
            for old_snake in snake:
                coords = canvas.coords(old_snake)
                snake_rect.append(coords)
                #canvas.delete(old_snake)
            snake_rect.append([x_loc,y_loc])
            move_food(canvas, snake_food, snake_rect)
            
            for old_snake in snake:
                canvas.delete(old_snake)
            snake = player(canvas, snake_rect,SIZE)
            snake_speed -=snake_speed/20
        print(snake_rect)
        
        # print scores
        text_obj = canvas.create_text(1, 387,text=f"{score} points")
        
        # delay
        time.sleep(snake_speed)
        print(snake_speed," s")
        
        
        # Delete old scores text
        canvas.delete(text_obj)
        
    # show result
    result = f"Your Score is : {str(score)}"
    canvas.create_text((CANVAS_WIDTH/2)-30, CANVAS_HEIGHT/2, 'GAME OVER', color='red')
    canvas.create_text((CANVAS_WIDTH/2)-40, (CANVAS_HEIGHT/2)+14, result, color='black')


def player(canvas, snake_rect,y_SIZE):
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
    random_list = [i for i in range(0,380,20)]
    food_x = random.choice(random_list)
    food_y = random.choice(random_list)
    canvas.moveto(food, food_x, food_y)

    
if __name__ == '__main__':
    main()
