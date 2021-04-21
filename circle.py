"""@miracneorid
#Simple Circle program out of squares
#this program will ask for your name and radius,to name your circle and set it's radius respectively
"""
#importation of module
import turtle

#activating module for uses
my_turtle = turtle.Turtle()

#this will increas the speed of turtle(0 parameter will set the speed to max)
my_turtle.speed(0)

name = input("Enter your name: ")
radius = int(input("Please enter radius of cicle:"))
number_of_circle = int(input("Please enter the number of circles required:"))

radius1 = radius - 25
radius2 = radius1 - 24

number_of_circle = number_of_circle*36

def circle(radius):
    angle = 90
    area = (22/7)*radius**2
    circumfarence = 2*(22/7)*radius
    print(name,"area of your circle =",area)
    print(name,"circumfarence of your Cicrle =",circumfarence)
    print()

    for i in range(4):
        my_turtle.forward(radius)
        my_turtle.right(angle)

def output():
    for orange in range(number_of_circle):
        my_turtle.pencolor("orange")
        circle(radius)
        my_turtle.right(11)
        
    for black in range(number_of_circle):
        my_turtle.pencolor("black")
        circle(radius1)
        my_turtle.right(11)

    for green in range(number_of_circle):
        my_turtle.pencolor("green")
        circle(radius2)
        my_turtle.right(11)

output()
