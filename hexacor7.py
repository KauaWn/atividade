import turtle
import random
kaks = turtle.Turtle()
colors = ('red','yellow','blue','green','purple','gray','black','pink')
for u in range(6):
 for i in range(6):
        kaks.color(random.choice(colors))
        kaks.forward(50)
        kaks.right(60)
 kaks.right(60)