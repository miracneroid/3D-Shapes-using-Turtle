"""@miracneorid
#Simple Square program
#this program will ask for your name, length and breadth,to name your square and set it's boundaries
"""
#importation of module
import turtle

#activating module for uses
my_turtle = turtle.Turtle()

#this will change the color of the turtle from default(black) to user requested
my_turtle.pencolor("cyan")

#this will increas the speed of turtle(0 parameter will set the speed to max)
my_turtle.speed(0)

name = input("Enter your name: ")

length = int(input("Enter the side of the square: "))
angle = int(input("Enter the angle of the square(90): "))

def Square():
    area = length**2
    perimeter = 2*(length+length)

    print(name,'details of your square are as followed: ')
    print("   Side of Square =",length,)
    print("   Area of Square =",area,)
    print("   Perimeter of Square =",perimeter)
    print()

def repeation():
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(length)


for i in range(length - 1):
    length = length - 1
    breadth = length - 1
    Square()
    repeation()