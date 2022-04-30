import turtle
import math
# turtle.hideturtle ()
turtle.speed (10)
def rectangle (a, b, color):
    _doc_ = """vẽ hình chữ nhật cạnh a, b, tô màu color"""
    turtle.fillcolor (color)
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

def drawTriangle (a, b, color):
  __doc__ = "Vẽ tam giác cân, đáy a, chiều cao b"
  x = math.atan (2*b/a) * 180 / math.pi
  turtle.pencolor ("black")
  turtle.fillcolor (color)
  turtle.begin_fill ()
  turtle.lt (x)
  turtle.fd (math.sqrt (a*a/4 + b*b))
  turtle.rt (2*x)
  turtle.fd (math.sqrt (a*a/4 + b*b))
  turtle.lt (x)
  turtle.bk (a)
  turtle.end_fill ()

def drawHouse (a, b, c):
  __doc__ = "vẽ ngôi nhà chiều ngang a, chiều cao b, chiều cao mái ngói c"
  # vẽ nhà và cửa
  rectangle (a, b, "#808080")
  turtle.fd (a / 3)
  rectangle (a / 4, b * 2 / 3, "#0000CD")
  
  # đi đến điểm vẽ ống khói
  turtle.lt (90)
  turtle.penup ()
  turtle.fd (b + c/4)
  turtle.rt (90)
  turtle.fd (a/6)
  turtle.pendown ()
  
  rectangle (a/15, c*2/3, "#B22222")
  turtle.lt (90)
  turtle.penup ()
  turtle.fd (c *2/ 3 + 5)
  turtle.pendown ()
  turtle.fd (10)
  turtle.penup ()
  turtle.rt (90)
  turtle.fd (5)
  turtle.lt (90)
  turtle.pendown ()
  turtle.fd (8)
  turtle.bk (18)
  
  turtle.penup ()
  turtle.bk (11/12*c + 5)
  turtle.right (90)
  turtle.bk (a / 2 + 5)

  drawTriangle (2 * a / 3,  c, "#A52A2A")

def drawTrapezoid (a, b, c):
  __doc__ = "Vẽ hình thang 2 đáy a, b, chiều cao c"
  x = math.atan (c * 2 / (a-b)) * 180 / math.pi
  turtle.lt (x)
  turtle.fd (math.sqrt ((a*a + b*b - 2*a*b)/4 + c*c))
  turtle.rt (x)
  turtle.fd (b)
  turtle.rt (x)
  turtle.fd (math.sqrt ((a*a + b*b - 2*a*b)/4 + c*c))
  turtle.lt (x)
  turtle.bk (a)

def drawTree (a, b, c):
  __doc__ = "vẽ cây chiều cao a, chiều rộng gốc b, chiều rông tán c"
  # vẽ gốc
  turtle.fillcolor ("#8B4513")
  turtle.begin_fill ()
  drawTrapezoid (b, 2*b/3, a/3)
  turtle.end_fill ()
  # vẽ tán cây
  turtle.penup ()
  turtle.fd (b/2)
  turtle.lt (90)
  turtle.fd (a/3)
  turtle.rt (90)
  turtle.bk (c/2)
  turtle.pendown ()
  drawTriangle (c, a/3, "#006400")
  turtle.penup ()
  turtle.fd (c/2)
  turtle.lt (90)
  turtle.fd (a/3)
  turtle.rt (90)
  turtle.bk (c/3)
  turtle.pendown ()
  drawTriangle (c*2/3, a*2/9, "#008000")
  turtle.penup ()
  turtle.fd (c/2)
  turtle.lt (90)
  turtle.fd (a*2/9)
  turtle.rt (90)
  turtle.bk (c/3)
  turtle.pendown ()
  drawTriangle (c/3, a/9, "#228B22")
 





# drawHouse (200, 100, 50)
# turtle.bk (200)
# drawTree (150, 50, 90)
# turtle.hideturtle ()
# turtle.done ()

# def greeting(name):
#   turtle.write ("Hello, " + name, )


