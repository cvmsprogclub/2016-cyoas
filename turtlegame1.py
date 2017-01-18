import turtle
import random
import math
import time
import winsound



maxTime = 60;#choose your amount of time
maxGoals = 4
maxBombs = 4
ballSpeed = 4;
#bomb speed is at the bottom

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

#Set up screen
turtle.setup(600,600)   
wn = turtle.Screen()
wn.title("HAVE A BALL!")
wn.bgcolor("lightblue")
wn.tracer(2)
# draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-250,-250)
mypen.pendown()
mypen.pensize(3)

for side in range(4):
   mypen.forward(500)
   mypen.left(90)
mypen.hideturtle()

# create player turtle

player = turtle.Turtle()
player.color("green")
player.shape("turtle")
player.penup()
player.speed(0)


#Create score variable
score=0
#creat goalSSS

goals = []
for count in range(maxGoals):
   goals.append(turtle.Turtle());
   goals[count].color("red")
   goals[count].shape("circle")
   goals[count].penup()
   goals[count].speed(0)
   goals[count].setposition(random.randint(-240,240),random.randint(-240,240) )
   
#create bombsSSS

bombs = []
for count in range(maxBombs):
   bombs.append(turtle.Turtle());
   bombs[count].color("black")
   bombs[count].shape("triangle")
   bombs[count].shapesize(1,1,1)
   bombs[count].penup()
   bombs[count].speed(0)
   bombs[count].setposition(random.randint(-240,240),random.randint(-240,240) )
   
# set speed variable

speed = 1
# define funtions
def turnleft():
   player.left(30)
   
def turnright():
   player.right(30)
   
def increasespeed() :
   global speed
   speed +=1
   
def decreasespeed() :
   global speed
   if speed > 0:
      speed -= 1

def boundaryBump(t1):
   if int(t1.xcor()) > 235 or int(t1.xcor()) < -235 :
      angleIncidence = t1.heading()
      t1.setheading(180 - angleIncidence)
   #Boundary Checking
   if int(t1.ycor()) > 235 or int(t1.ycor()) < -235 :
      angleIncidence = t1.heading()
      t1.setheading( 360 - angleIncidence)

def isCollision(t1,t2) :
   d = math.sqrt(math.pow(t1.ycor()-t2.ycor(),2)+math.pow(t1.xcor()-t2.xcor(),2))
   if d <15:
      return True;
   else:
      return False;

def leave():
   wn.bye()
   
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")
turtle.onkey(leave, "q")

timePen = turtle.Turtle()
timePen.penup()
timePen.setposition(100,260)
timePen.pendown()
timePen.pensize(3)
timePen.hideturtle();

start = time.time()
while True :
   player.forward(speed)

   boundaryBump(player)

   for ind in range(maxGoals): 
      boundaryBump(goals[ind])
      #Collision Checking
      if isCollision(goals[ind],player) :
         goals[ind].setposition(random.randint(-240, 240),random.randint(-240, 240))
         goals[ind].right(random.randint(0,360))
         score +=1
         player.shapesize(2,1.5,1.5)
         time.sleep(0.2)
         player.shapesize(1,1,1)
         # sraw score on screen
         mypen.undo()
         mypen.penup()
         mypen.hideturtle()
         mypen.setposition(-240,260)
         scorestring = "Score: %s" %score
         mypen.write(scorestring,False, align ="left", font=("Arial",14, "normal"))
      # move the goal
      goals[ind].forward(ballSpeed)


        
   

   for ind in range(maxBombs): 
      boundaryBump(bombs[ind])
        #Collision Checking
      if isCollision(bombs[ind],player) :
         bombs[ind].setposition(random.randint(-240, 240),random.randint(-240, 240))
         bombs[ind].right(random.randint(0,360))
         player.color("orange")
         time.sleep(0.15);
         player.color("green")
         player.setposition(random.randint(-240, 240),random.randint(-240, 240))
         player.right(random.randint(0,360))
         score -=1
         # Draw score on screen
         mypen.undo()
         mypen.penup()
         mypen.hideturtle()
         mypen.setposition(-240,260)
         scorestring = "Score: %s" %score
         mypen.write(scorestring,False, align ="left", font=("Arial",14, "normal"))
      # move the goal
      if score>0:
         bombs[ind].forward(score)




   now = int(time.time())
   timeRemaining = int(maxTime - ( now - start))
   timestring = "Time Left (s): %d" %timeRemaining
   timePen.undo()
   timePen.hideturtle();
   timePen.write(timestring,False, align ="left", font=("Arial",14, "normal"))
   if now - start > maxTime:
       time.sleep(5);
       leave()
