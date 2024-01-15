import random
'''
a=5
b=10
print(a+b)


#함수
def printVars(a,b):
    print("a+b =", a+b)
    print("a-b =", a-b)
    print("a*b =", a*b)
    print("a/b =", a/b)

printVars(a,b)


#제어문
if a<b:
    print("b가 더 큽니다.")
else:
    print("a가 더 큽니다.")


if a ==10:
    print("a는 10 입니다.")
elif a==20:
    print("a는 20입니다.")
elif a==5:
    print("a는 5입니다")
else:
    print('a는 그 외 숫자입니다.')


#iteration
for i in range(5,10):
    print("i의 현재 값", i)


height = int(input("트리의 높이를 입력하세요: "))

for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
'''



'''
computer=random.randint(1,100)

user=-1
score=0
while user!=computer:
    print(score+1,'번째 입력', '해주세요')
    print('숫자를 입력해주세요')
    user = int(input())
    score=score+1
    if user>computer:
        print('DOWN!!')
    elif user==computer:
        break
    else:
        print('UP!!!')
print(score,'번만에 맞혔습니다.')'''




'''
a='abcde'
print(a[0:len(a)])
print(a[4])

#얘는 안 됨
#a[3]='Z' 문자열 도중 교체 안됨
#print(a)

print(a.find('bc',0,4)) # 0부터 4까지 bc가 있냐 true 출력
print(a*4)


c=a[1:4] #문자열 슬라이스
print(c)


def makeStar(starLength):
    temp = "*" * starLength
    return temp

c=makeStar(10)
print(c)


cars= ['소나타','제니시스','포르쉐']
print(cars)
cars.append('모닝')#마지막에 이어붙이기
print(cars)

cars.insert(2,'그랜져')#원하는곳에 삽입
print(cars)

print(cars.index('제니시스'))#찾기 없으면 오류남 find는 없으면 -1반환

cars.sort()#정렬
print(cars)
'''

'''
#로또 생성기
lotto=random.sample(range(1,46),6)


lotto.sort()
print(lotto)

numbers=[]
while len(numbers)<6:
    temp=random.randint(1,45)
    if numbers.count(temp)==0: #중복되는 것이 없다면
        numbers.append(temp)#배열에 추가하기
    else:
        continue
numbers.sort()
print(numbers)

'''



print('무슨 붕어빵 주문?')
userChoice = input()
print('몇 개?')
userCnt=int(input())
print(f"{userChoice}를 {userCnt}개 만듭니다.")




class bread:
    def __init__(self):
        self.type=" "
        self.qnt = 0
        #print(self.type, "을",self.qnt,"개 만듭니다.")
    def make(self):
       print(self.type, "을",self.qnt,"개 만듭니다.")


a=bread()
a.type="초코 붕어빵"
a.qnt=3
a.make()

b=bread()
b.type="민트초코 붕어빵"
b.qnt=10
b.make()