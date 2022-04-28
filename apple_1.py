#   a123_apple_1.py
import turtle as trtl
import time
import random as r

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple): #draw apple and then draw A over the apple afterwards
  active_apple.shape(apple_image)
  wn.tracer(False)
  active_apple.up()
  active_apple.sety(active_apple.ycor()-30)
  active_apple.color("white")
  active_apple.write("A", align="center", font=("Arial", 40, "bold"))
  active_apple.sety(active_apple.ycor()+30)
  wn.tracer(True)
  wn.update()

def drop_apple(): #drops apple to y 
  apple.up()
  apple.clear() #clears letter A
  apple.sety(-120) #moves apple to grounds
  time.sleep(0.5)
  apple.hideturtle()
  apple.sety(r.randint(-40,100))
  apple.setx(r.randint(-100,100))
  apple.showturtle()


#-----function calls-----
wn.bgpic("background.gif")
draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.mainloop()

'''import turtle as trtl
import random as r
wn = trtl.Turtle()
a_letter = "A"
letters = ["A", "B", "C", "D", "E", "F", "G"]

def draw_apple(active_apple):
  wn.tracer(False)
  active_apple.setx(r.randint(-100, 100))
  active_apple.sety(r.randint(-50, 100))
  a_letter = letters[r.randint(0,6)]
  wn.onkeypress(drop_apple, a_letter)
  active_apple.sety(active_apple.ycor()-30)
  active_apple.color("white")
  active_apple.write("A", align="center")
  active_apple.sety(active_apple.ycor()+30)
  active_apple.showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple():
  apple.up()
  apple.clear()
  apple.sety(-110)
  apple.hideturtle()
  draw_apple(apple)

def typeA():
  if a_letter == 'A':
    drop_apple()

wn.listen()
draw_apple(apple)
#wn.onkeypress(drop_apple, "a")'''