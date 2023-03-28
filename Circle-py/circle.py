# import depencies 
from math import sqrt
import matplotlib.pyplot as plt


class Circle:
  '''Create a circle with coordinate of center and radius. Center as coordinates of center in the form of (x,y). Radius as int'''
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius

    # set x,y attributes from center inputs
    self.x, self.y = center

  def draw(self):
    '''A method to draw circle initialized'''
    figure, axes = plt.subplots() 
    cc = plt.Circle(self.center, self.radius,alpha=0.6 ) 
    
    #set axes range
    plt.xlim(0, (self.x+self.radius)+10)
    plt.ylim(0, (self.y+self.radius) + 10)

    # plot origin
    plt.scatter(self.x,self.y,marker='o',c='r')
    axes.set_aspect(1)
    axes.add_artist( cc ) 
    plt.title( ("Circle with center of {} and radius of {}".format(self.center,self.radius)) ) 
    plt.show()



def point_in_circle(Circle, x):
  '''Check if point in circle. Circle = instance of Circle(), x = x,y cordinates on graph '''
  add_to_plot(Circle,x)   # plot the coordinating to be verified
  distance_f_rad = sqrt((x[0] - Circle.x)**2 + (x[1]-Circle.y)**2) #distance between 2 points
  if distance_f_rad <= Circle.radius:
    return 'True - Point within/on boundaries of circle'
  else:
    return 'False - Point out of Circle'

    

def add_to_plot(Circle,x):
  '''Plots the coordinates of x on the circle for better visual interpretaion '''
  figure, axes = plt.subplots() 
  cc = plt.Circle(Circle.center, Circle.radius,alpha=0.6 ) 
    
    #set axes range
  plt.xlim(0, (Circle.x+Circle.radius)+10)
  plt.ylim(0, (Circle.y+Circle.radius) + 10)

    # plot origin
  plt.scatter(Circle.x,Circle.y,marker='o',c='r')
  plt.title( ("Circle with center of {} and radius of {}".format(Circle.center,Circle.radius)) )
    
  # plot circle     
  axes.set_aspect(1)
  axes.add_artist( cc )

  # add point
  plt.scatter(x[0],x[1],marker='x', c='r')
  plt.show()
