import turtle
kaks = turtle.Turtle()
def formas():
    for _ in range(6):
        kaks.forward(25)
        kaks.left(60)

def pulo(f):
    kaks.up()
    kaks.forward(f)
    kaks.down()

for _ in range(6):
    for _ in range(2):
        for _ in range(4):
            formas()
            pulo(75) 
        pulo(-25)
        kaks.left(60)
        pulo(25)
        kaks.left(120)
    pulo(-25)
    kaks.right(60)
    pulo(50)
    kaks.left(60)

turtle.Terminator()
