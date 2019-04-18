#1번
def draw_snowman(x, y):
    t.penup()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.up()
    t.goto(x, y-11)
    t.down()
    t.left(20)
    t.forward(40)
    t.forward(-40)
    t.left(130)
    t.forward(40)
    t.forward(-40)
    t.right(150)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.up()
    t.goto(x, y-44)
    t.down()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.color('black', 'white')
s.bgcolor('skyblue')

for i in range(3):
    draw_snowman(i*100, 0)
#2번
def draw_hexa():
    for i in range(6):
        t.fd(100)
        t.rt(60)

import turtle
t = turtle.Turtle()

for i in range(6):
    t.fd(100)
    t.lt(60)
    draw_hexa()
#3번
def fx(x):
    y = (x*x)+1
    return y

import turtle
t = turtle.Turtle()

t.forward(300)
t.goto(0, 0)
t.left(90)
t.forward(300)
t.goto(0, 0)
t.right(90)
for i in range(0, 150):
    y = fx(i)*0.1
    t.goto(i, y)
#4번
def draw_line():
    t.forward(100)
    t.backward(100)

import turtle
t = turtle.Turtle()
for i in range(12):
    draw_line()
    t.left(360/12)
#5번
def song(name):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear %s"%name)
    print("Happy Birthday to you!")

user = input("이름이 무엇인가요? ")
song(user)
#6번
def math():
    x = int(input("첫 번째 정수: "))
    y = int(input("두 번째 정수: "))
    print("정수 %s + %s의 합은?"%(x, y))
    print(x+y)

math()
#7번
def circleArea(r):
    global PI
    PI = 3.14
    return PI*(r**2)
def circleCircumference(r):
    return 2*PI*r
r = int(input("반지름은? "))
print("반지름이 %s인 원의 면적: %s"%(r, circleArea(r)))
print("반지름이 %s인 원의 둘레: %s"%(r, circleCircumference(r)))
#8번
def sum(a, b):
    print("(%s + %s) = %s"%(a, b, a+b))
def minus(a, b):
    print("(%s - %s) = %s"%(a, b, a-b))
def multiply(a, b):
    print("(%s * %s) = %s"%(a, b, a*b))
def division(a, b):
    print("(%s / %s) = %s"%(a, b, a/b))

n1 = int(input("첫 번쨰 정수: "))
n2 = int(input("두 번쨰 정수: "))
sum(n1, n2)
minus(n1, n2)
multiply(n1, n2)
division(n1, n2)