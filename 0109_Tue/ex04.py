#학생 성적 관리 프로그램
# 1. 입력 2. 출력 3. 종료
# > 1
# 이름: ###
# 나이: ##
# 국어: ##
# 수학: ##
# 영어: ##
#1. 입력 2. 출력 3. 종료
# > 2
# 1. 전체 학생 출력 2. 개별 학생 출력 3. 뒤로
# > 1
# 전체 학생의 이름 나이 국영수 평균이 출력
# 1. 전체 학생 출력 2. 개별 학생 출력 3. 뒤로
# > 2

# 출력할 학생의 이름을 입력해주세요
# 김철수

# 김철수 학생의 그간 입력된 정보를 토대로
#3 국어, 영어 수학 점수가 그래프로 출력


# 1. 전체 학생 출력 2. 개별학생 출력 3. 뒤로
# > 3
# 1. 입력 2. 출력 3. 종료
# > 3
# 사용해주셔서 감사합니다.

# 유의점: 똑같은 이름이면 무조건 동일 학생으로 판단
# 그래프 출력시 처음에는 평균 점수가 토대로 되고
# 심화 문제를 풀고 싶다면 한 그래프에 국ㄱ영수 평균이 출력
import matplotlib.pyplot as mp
import numpy as np

name=[]
age=[]
korean=[]
english=[]
math=[]
incnt=[]



x=[]
y=[]

def grades(len):
     for i in range(len):
        print(name[i])
        print('나이',age[i])
        print('국어',korean[i])
        print('영어',english[i])
        print('수학',math[i])
        print('세 과목의 평균:',(korean[i]+english[i]+math[i])/3,'\n')
    
b=0
subjects=[]
def graph(cnt):
    x_vals = np.arange(1, len(cnt) + 1)

    for subject in ['Korean', 'English', 'Math']:

        scores_for_subject = []
        for index in cnt:
            if subject == 'Korean':
                scores_for_subject.append(korean[index])
            elif subject == 'English':
                scores_for_subject.append(english[index])
            elif subject == 'Math':
                scores_for_subject.append(math[index])

        mp.plot(x_vals, scores_for_subject)
    avg_vals = [(korean[ind] + english[ind] + math[ind]) / 3 for ind in cnt]
    mp.plot(x_vals, avg_vals)
    mp.show()

a=0

while True:
    num = int(input('1.입력2.출력3.종료'))
    if num==1: 
        nameInput=input('이름: ')
        name.append(nameInput)
        ageInput=int(input('나이: '))
        age.append(ageInput)
        # 각 성적 입력
        koreanInput=int(input('국어: '))
        korean.append(koreanInput)
        englishInput=int(input('영어: '))
        english.append(englishInput)
        mathInput= int(input('수학: '))
        math.append(mathInput)
        print('\n\n')
    elif num ==2 :
        print('1. 전체 학생 출력 2. 개별 학생 출력 3. 뒤로')
        num2=int(input())
        if num2==1:
            grades(len(name))
        elif num2==2:
               studentName=input('출력할 학생의 이름을 입력하세요.')
               for i, n in enumerate(name):
                   if n == studentName:
                       incnt.append(i)
               graph(incnt)
               print('김철수는',len(incnt),'번 입력되었습니다.')
        elif num2 ==3:
            break
    elif num==3:
        break

print('사용해주셔서 감사합니다.')
                

