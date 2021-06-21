import turtle 

back_color="#9EC388"
crust_color="#ECA84F"
sauce_color="#AD0509"
cheese_color="#FBC70F"
pepperoni_location=[[-70,105],[-85,175],[-25,50],[-15,100],[-25,150],[-30,205],[15,50],[20,120],[20,200],[60,156],[71,215],[80,90],[95,150]]

screen=turtle.Screen()
screen.bgcolor(back_color)
screen.title("My Pizza")

my_turtle=turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle") 

def draw_circle(radius,line_color,fill_color):
  my_turtle.color(line_color)
  my_turtle.fillcolor(fill_color)
  my_turtle.begin_fill()
  my_turtle.circle(radius)
  my_turtle.end_fill()
  
def move_turtle(x,y):
  my_turtle.up()
  my_turtle.goto(x,y)
  my_turtle.down()
  
draw_circle(150,crust_color,crust_color)
move_turtle(0,25)
draw_circle(125,sauce_color,cheese_color)

for location in pepperoni_location:
  move_turtle(location[0],location[1])
  draw_circle(10,sauce_color,sauce_color)
  
move_turtle(0,150)
my_turtle.color(back_color)

for i in range(0,8):
  my_turtle.pendown()
  my_turtle.left(45)
  my_turtle.forward(150)
  my_turtle.penup()
  my_turtle.backward(150)

turtle.done() 
