"""@miracneorid
#Simple Triangle program
#this program will ask for your name, height and base,to name your triangle and set it's boundaries
"""
#importation of module
import turtle

#activating module for uses
my_turtle = turtle.Turtle()

#this will change the color of the turtle from default(black) to user requested
my_turtle.pencolor("light blue")

#this will increas the speed of turtle(0 parameter will set the speed to max)
my_turtle.speed(0)

name = input("Enter your name: ")

height = int(input("Enter the height of the triangle: "))
base = int(input("Enter the base of the triangle: "))
angle = int(input("Enter the angle of the triangle(120): "))

def triangle():
    area = (1/2)*base*height
    perimeter = height+base+height

    print(name,'details of your triangle are as followed: ')
    print("   Height of Triangle =",height,)
    print("   Base of Triangle =",base,)
    print("   Area of Triangle =",area,)
    print("   Perimeter of Triangle =",perimeter)
    print()

def repeation():
    my_turtle.left(angle)
    my_turtle.forward(height)
    my_turtle.left(angle)
    my_turtle.forward(height)
    my_turtle.left(angle)
    my_turtle.forward(height)

for i in range(height - 1):
    height = height - 1
    base = base - 0.25
    triangle()
    repeation()
