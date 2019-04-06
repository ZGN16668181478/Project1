import turtle

# 长方形，正方形，五角星，多边形，五环
# 运动命令
# 其他命令

# 长方形
turtle.speed(6)
turtle.begin_fill()
turtle.fillcolor('red')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
turtle.hideturtle()
turtle.showturtle()
turtle.down()
# 正六边形
turtle.goto(100,0)
turtle.right(35)
turtle.begin_fill()
turtle.fillcolor('blue')
turtle.circle(70,steps=6)
turtle.end_fill()
turtle.up()
turtle.hideturtle()

# 正五角星
turtle.showturtle()
turtle.goto(200,120)
turtle.down()
turtle.begin_fill()
turtle.fillcolor('yellow')
turtle.pencolor('green')
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.right(160)
turtle.forward(100)
turtle.end_fill()
turtle.hideturtle()



turtle.showturtle()
turtle.down()
turtle.goto(-100,0)
def addPlus(a):
    return int(a(a+2))
for x in range(10):
    y = x**2-18*x+81
    turtle.goto(-x,-y)
turtle.pencolor('purple')
turtle.up()
turtle.goto(9,0)
turtle.down()
for x in range(30):
    y = x**2-18*x+81
    turtle.goto(x,-y)
turtle.done()