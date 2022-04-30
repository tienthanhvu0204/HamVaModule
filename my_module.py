import turtle
import math
# turtle.hideturtle ()
turtle.speed (10)
def rectangle (a, b, color):
    _doc_ = """vẽ hình chữ nhật cạnh a, b, tô màu color"""
    turtle.color (color)
    turtle.pencolor ("black")
    turtle.begin_fill ()
    for i in range (2):
        turtle.fd (a)
        turtle.lt (90)
        turtle.fd (b)
        turtle.lt (90)
    turtle.end_fill ()
    
def regpol (n, x):
    __doc__ = "vẽ hình đa giác đều n cạnh chiều dài x" 
    for i in range (n):
      turtle.fd (x)
      turtle.lt (360/n)

def drawCircle (r):
  __doc__ = "vẽ hình bán kính r, tâm tại điểm đang đứng"
  turtle.penup ()
  turtle.fd (r)
  turtle.lt (90)
  turtle.pendown ()
  turtle.circle (r)
  turtle.rt (90)
  turtle.penup ()
  turtle.bk (r)
  turtle.pendown ()

def areaCircle (r):
  return r * r * math.pi



def greeting(name):
  turtle.write ("Hello, " + name, )



