#두근두근 파이썬 5장 연습문제 풀이
#1번 문제
#출력 결과
#20살 이상

#2번 문제
#조건을 age >= 30 and age <=50이라고 설정한다.

#3번 문제
temp = int(input("현재 온도를 입력하시오: "))
if temp>=25 :
    print("반바지를 입으세요")
else :
    print("긴바지를 입으세요")

#4번 문제
score = int(input("성적을 입력하시오: "))
if score >= 90:
    print("A학점 입니다.")
elif score >= 80:
    print("B학점 입니다.")
elif score >= 70:
    print("C학점 입니다.")
elif score >= 60:
    print("D학점 입니다.")
else :
    print("F학점 입니다.")

#5번 문제
import random
x = random.randint(1, 100)
y = random.randint(1, 100)
correct = x - y
user = int(input(str(x)+"-"+str(y)+"= "))
if user == correct:
    print("맞았습니다.")
else :
    print("틀렸습니다.")

#6번 문제
user = input("정수를 입력하시오: ")
if user % 2 == 0 and user % 3 == 0:
    print("2와 3으로 나누어 떨어집니다.")
else :
    print("2와 3으로 나누어 떨어지지 않습니다.")

#7번 문제
import random
x = random.randint(0, 9)
y = random.randint(0, 9)
solution = str(x) + str(y)
user = int(input("복권번호를 입력하시오(0에서 99사이): "))
print("당첨번호는 %s입니다." % solution)
if user == int(solution):
    print("상금은 100만원입니다.")
elif user//10 == x or user//10 == y or user%10 == x or user%10 ==y:
    print("상금은 50만원입니다.")
else :
    print("상금은 없습니다.")

#8번 문제
import turtle
t = turtle.Turtle()
t.shape("turtle")
x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))
t.up()
t.goto(x1, y1-r1)
t.down()
t.circle(r1)
t.up()
t.goto(x2, y2-r2)
t.down()
t.circle(r2)
distance = ((x1-x2)**2+(y1-y2)**2)**0.5
if distance <= r1-r2 :
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
else :
    t.write("두번째 원이 첫번째 원의 내부에 있지 않습니다.")
turtle.exitonclick()