#https://docs.python.org/ko/3/library/functions.html#print
#for문 이용해서 리스트 합 산출
sum = 0
for i in [1, 2, 3, 4, 5]:
    sum = sum + i
print(sum)

#range 함수 조절
for i in range(1, 6, 1):
    print(i, end=" ")

#for문 이용해서 터틀로 원 6개 겹쳐그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(6):
    t.circle(100)
    t.left(60)
turtle.exitonclick()

#for문 이용 n각형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
n = int(turtle.textinput("", "몇각형을 원하시나요? (숫자만 입력)"))
for i in range(n):
    t.forward(100)
    t.left(360/n)

#while문 이용예
key = "xodidWkd1Wkd"
user = ""   #데이터 초기화 단계
while user != key:
    user = input("암호를 입력하시오: ")
    #while문을 벗어날 수 있는 데이터 업데이트 단계가 필요하다.
print("로그인 성공")

#while문을 이용해 1~10까지 수 더하기
i = 1
sum = 0
while i<11:
    sum = sum + i
    i += 1
print(sum)

#while문을 이용해 1부터 사용자에게 입력받은 숫자까지의 합
i = 1
sum = 0
n = int(input("1부터 몇까지의 합을 구하고 싶습니까? (숫자만 입력) "))
while i<n+1:
    sum = sum + i
    i += 1
print("1부터", n, "까지의 합은", sum)

#while문 이용해 사각형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
i = 1                   #초기값 설정
while i<=4:            #조건 설정
    t.forward(100)
    t.left(90)
    i += 1             #조건 업데이트
turtle.exitonclick()   #클릭할 때까지 터틀창이 유지되도록 하는 것. 그냥 편의를 위함.

#while문을 이용해 사용자로부터 단을 입력받아 구구단 출력하기
dan = int(input("원하는 단은: "))
i = 1
while i<=9:
    result = dan*i
    print("%s * %s = %s"%(dan, i, result))
    i += 1

#while문으로 별 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

i = 1
while i<=5:
    t.forward(200)
    t.right(144)
    i += 1
turtle.exitonclick()

#for문을 이용한 별 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(5):
    t.forward(200)
    t.right(144)
turtle.exitonclick()

#while문으로 스파이럴 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

turtle.bgcolor("black")
t.speed(0)
t.width(3)
colors = ["aqua", "gray", "pink", "yellow", "orange", "white"]

length = 10
while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5