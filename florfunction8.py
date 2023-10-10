import turtle
import random
colors = ('blue','yellow','gray','purple','red','violet','cyan','black','green')
kaks = turtle.Turtle()


def flor():
    for i in range(6):
        kaks.color(random.choice(colors))
        for u in range(8):
            kaks.forward(20)
            kaks.right(30)
        kaks.right(60)

for up in range(3):
    flor()
    kaks.penup()
    kaks.right(120)
    kaks.forward(150)
    kaks.pendown()