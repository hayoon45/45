#두근두근 파이썬 4장 연습문제 풀이
#1번 문제
print('나는'+str(12)+'개의 사과를 먹었다.')

#2번 문제
#출력 결과
#applegrape
#appleappleapple

#3번 문제
s = input("문자열을 입력하시오: ")
result = s[0:2] + s[-2:]
print(result)

#4번 문제
s = input("문자열을 입력하시오: ")
result = s + "하는 중"
print(result)

#5번 문제
s = input("기호를 입력하시오: ")
t = input("중간에 삽입할 문자열을 입력하시오: ")
print(s[0]+t+s[1])

#6번 문제
list=[]
x = input("첫번째 수를 입력하시오: ")
list.append(x)
x = input("두번째 수를 입력하시오: ")
list.append(x)
x = input("세번째 수를 입력하시오: ")
list.append(x)
x = input("네번째 수를 입력하시오: ")
list.append(x)
list_sum = int(list[0]) + int(list[1]) + int(list[2]) + int(list[3])
print("리스트 =", list)
print("리스트 숫자들의 합 =", list_sum)

#7번 문제
import turtle
t = turtle.Turtle()
t.shape("turtle")
color_list = []
color = turtle.textinput("", "색상#1을 입력하시오: ")
color_list.append(color)
color = turtle.textinput("", "색상#2을 입력하시오: ")
color_list.append(color)
color = turtle.textinput("", "색상#3을 입력하시오: ")
color_list.append(color)
t.fillcolor(color_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(100, 0)
t.down()
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(200, 0)
t.down()
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()

#8번 문제
import turtle
t = turtle.Turtle()
t.shape("turtle")
list1 = []
num = turtle.textinput("", "x1: ")
list1.append(num)
num = turtle.textinput("", "y1: ")
list1.append(num)
num = turtle.textinput("", "x2: ")
list1.append(num)
num = turtle.textinput("", "y2: ")
list1.append(num)
num = turtle.textinput("", "x3: ")
list1.append(num)
num = turtle.textinput("", "y3: ")
list1.append(num)
t.up()
t.goto(int(list1[0]), int(list1[1]))
t.down()
t.goto(int(list1[2]), int(list1[3]))
t.goto(int(list1[4]), int(list1[5]))
turtle.exitonclick()