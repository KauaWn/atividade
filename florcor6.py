import turtle
import random
kaks = turtle.Turtle()
colors = ('red', 'green','violet','blue','yellow','purple','cyan','gray','black')

for i in range(12):
    for u in range(2):
        kaks.color(random.choice(colors))
        kaks.forward(60)
        kaks.right(30)
        kaks.forward(60)
        kaks.right(150)
    kaks.right(30)