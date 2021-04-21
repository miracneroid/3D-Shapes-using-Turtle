"""@miracneorid
#Simple Reactangle program
#this program will ask for your name, length and breadth,to name your reactangle and set it's boundaries
"""
#importation of module
import turtle

#activating module for uses
my_turtle = turtle.Turtle()

#this will change the color of the turtle from default(black) to user requested
my_turtle.pencolor("maroon")

#this will increas the speed of turtle(0 parameter will set the speed to max)
my_turtle.speed(0)

name = input("Enter your name: ")
length = int(input("Enter the length of the reactangle: "))
breadth = int(input("Enter the breadth of the reactangle: "))
angle = int(input("Enter the angle of the reactangle(90): "))

def reactangle():
    area = length*breadth
    perimeter = 2*(length+breadth)

    print(name,'details of your reactangle are as followed: ')
    print("   Length of Reactangle =",length,)
    print("   Breadth of Reactangle =",breadth,)
    print("   Area of Reactangle =",area,)
    print("   Perimeter of Reactangle =",perimeter)
    print()

def repeation():
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(breadth)


for i in range(length - 1):
    length = length - 1
    breadth = breadth - 0.25
    reactangle()
    repeation()
