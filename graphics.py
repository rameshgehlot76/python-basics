# 🌀Spiral Fractal Pattern (Turtle Graphics) 
import turtle

t = turtle.Turtle()
t.speed(0)
t.color("cyan")
turtle.bgcolor("black")

for i in range(200):
    t.forward(i * 2)
    t.left(59)

turtle.done()
