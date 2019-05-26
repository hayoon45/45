#파이썬 10장
#1번
from tkinter import*
window=Tk()
l1 = Label(window, text="간단한 GUI 프로그램!")
button1 = Button(window, text="환영합니다.")
button2 = Button(window, text="종료")
l1.pack()
button1.pack()
button2.pack()
window.mainloop()

#2번
from tkinter import*
window=Tk()
sum=100
def process1():
    global sum
    sum= sum + float(e1.get())
    l2 = Label(window, text=sum)
    l2.grid(row=0, column=2)
def process2():
    global sum
    sum = sum - float(e1.get())
    l2 = Label(window, text=sum)
    l2.grid(row=0, column=2)
def process3():
    global sum
    sum = 100
    l2 = Label(window, text=sum)
    l2.grid(row=0, column=2)

l1 = Label(window, text="현재 합계:")
l2 = Label(window, text=sum)
l1.grid(row=0, column=0)
l2.grid(row=0, column=2)

e1 = Entry(window)
e1.grid(row=1, column=0, columnspan=3)

b1 = Button(window, text="더하기(+)", command=process1)
b2 = Button(window, text="빼기(-)", command=process2)
b3 = Button(window, text="초기화", command=process3)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)

window.mainloop()

#4번
from tkinter import*
window=Tk()

def process():
    result = float(e1.get()) * 2.54
    l4 = Label(window, text="%s 센티미터"%result)
    l4.grid(row=2, column=1)


l1 = Label(window, text="인치를 센티미터로 변환하는 프로그램:")
l1.grid(row=0, column=0, columnspan=2)
l2 = Label(window, text="인치를 입력하시오:")
l2.grid(row=1, column=0)

e1 = Entry(window)
e1.grid(row=1, column=1)
l3 = Label(window, text="변환결과:")
l4 = Label(window, text="")
l3.grid(row=2, column=0)
l4.grid(row=2, column=1)

b1 = Button(window, text="변환!", command=process)
b1.grid(row=3, column=1)

window.mainloop()