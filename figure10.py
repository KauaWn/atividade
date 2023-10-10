import turtle
import random
kaks = turtle.Turtle()
color = ("violet", "blue", "green", "red")

def hepta():
   for _ in range(9):
     kaks.forward(25)
     kaks.right(40)

def pular(f):
   kaks.up()
   kaks.forward(f)
   kaks.down()
for _ in range(3):
   kaks.color(random.choice(color))
   hepta()
   pular(50)