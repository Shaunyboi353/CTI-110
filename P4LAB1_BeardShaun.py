# Shaun Beard

# 3/20/2025

# P4LAB1

# Learning turtle grapghics and loops

import turtle
win = turtle.Screen()
franklin = turtle.Turtle()

franklin.pensize(5)
franklin.pencolor('Blue')
franklin.shape('turtle')
win.bgcolor('white')

for tri in range(3):
    franklin.forward(100)
    franklin.left(120)



square_loop = 0

while square_loop <=3:
    franklin.forward(100)
    franklin.right(90)
    square_loop += 1



win.mainloop()