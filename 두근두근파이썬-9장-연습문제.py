#1번
list = []
sum = 0
for i in range(5):
    score = int(input("정수를 입력하시오 : "))
    list.append(score)
    sum = sum + score
print("평균 = %s" %(sum/5))

#2번
import random
counters = [0, 0, 0, 0, 0, 0]
for i in range(1000):
    value = random.randint(0, 5)
    counters[value] = counters[value] + 1
print("주사위가 1인 경우는 %s" %counters[0])
print("주사위가 2인 경우는 %s" %counters[1])
print("주사위가 3인 경우는 %s" %counters[2])
print("주사위가 4인 경우는 %s" %counters[3])
print("주사위가 5인 경우는 %s" %counters[4])
print("주사위가 6인 경우는 %s" %counters[5])

#3번
contacts = {}
while True:
    name = input("(입력모드)이름을 입력하시오: ")
    if not name:
        break;
    tel = input("전화번호를 입력하시오: ")
    contacts[name] = tel
while True:
    search = input("(검색모드)이름을 입력하시오: ")
    print("%s 의 전화번호는 %s 입니다."%(search, contacts[search]))
    if not search:
        break;

#7번
domains = {"kr": "대한민국", "sk": "슬로바키아", "no": "노르웨이", "us": "미국", "jp": "일본", "hu": "헝가리", "de": "독일"}
for k, v in domains.items():
    print(k, ":", v)

#8번
problems = {"파이썬": "최근에 가장 떠오르는 프로그래밍 언어",
            "변수": "데이터를 저장하는 메모리 공간",
            "함수": "작업을 수행하는 문장들의 집합에 이름을 붙인 것",
            "리스트": "서로 관련이 없는 항목들의 모임"}
for word in problems.keys():
    print("다음은 어떤 단어에 대한 설명일까요?")
    print(problems[word])
    print("(1)파이썬 (2)함수 (3)리스트 (4)변수")
    answer = input("정답(문자만 입력할 것): ")
    if answer == word:
        print("정답입니다!")
    else:
        print("정답이 아닙니다.")