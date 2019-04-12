#1번
for i in range(2, 101, 2):
    print(i)
#2번
#while문의~~

#4번
user = int(input("3*9= "))
while user!=3*9:
    user = int(input("3*9는 "))
print("맞았습니다.")

#5번
user = 1
sum = 0
while user !=0:
    user = int(input("정수를 입력하시오(끝내려면 0 입력): "))
    sum = sum + user
print("합은 %s입니다." %sum)

#6번
import random
for i in [0, 1, 2]:
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    print("첫번째 주사위 = %s 두번째 주사위 = %s"%(r1, r2))

#7번
import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(6):
    t.forward(100)
    t.forward(-30)
    t.left(60)
    t.forward(30)
    t.forward(-30)
    t.right(120)
    t.forward(30)
    t.forward(-30)
    t.up()
    t.goto(0,0)
    t.down()

#10번
import turtle
t=turtle.Turtle()
t.shape("turtle")
for i in range(5):
    t.forward(200)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)

#12번
import math
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red", "yellow")

for x in range(0, 360):
    t.goto(x, 200*math.sin(x*3.14/180))
turtle.exitonclick()


