import turtle as t
import random

print(
    "Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!"
)

t.penup()
t.left(90)
t.forward(250)
t.left(90)
t.forward(300)
t.pendown()

t.write("Drawing App!", font=("Arial", 16, "normal"))

t.penup()
t.left(90)
t.forward(50)
t.pendown()

t.write("To draw a shape, go to the Console tab and choose an option!",
        font=("Arial", 16, "normal"))

t.penup()
t.forward(150)
t.left(90)
t.forward(150)
t.pendown()


def star():
    # Star
    for i in range(0, 5):
        t.forward(110)
        t.left(216)


def square():
    # Square
    for i in range(0, 4):
        t.forward(100)
        t.left(90)


def hexagon():
    # Hexagon
    for i in range(0, 6):
        t.forward(100)
        t.right(60)


selection = input("1. Star\n2. Square\n3. Hexagon\nSelect a number: ")
if selection == "1":
    print("Excellent choice! Go to the result tab to see your creation.")
    star()
elif selection == "2":
    print("Excellent choice! Go to the result tab to see your creation.")
    square()
elif selection == "3":
    print("Excellent choice! Go to the result tab to see your creation.")
    hexagon()
