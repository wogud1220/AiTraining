import matplotlib.pyplot as mp
import numpy as np
import pandas as pd
class Student():
    def __init__(self):
        self.name = ' '
        self.age=0
        self.kor=[]
        self.eng=[]
        self.math=[]

    def calcAvg(self): #가장 최신의 평균
        index = len(self.kor)-1
        average=(int(self.kor[index])+int(self.eng[index])+int(self.math[index]))/3
        return average
    def totalAvg(self):
        average=[]
        size = len(self.kor)
        for i in range(0,size):
            temp =0
            temp += int(self.kor[i])
            temp += int(self.eng[i])
            temp += int(self.math[i])
            average.append(temp/3)
        return average
    




def prepareDataFrame(studentArray):
    keys = studentArray.keys()
    dataframe={}
    korArray=[]
    engArray=[]
    mathArray=[]
    averageArray=[]
    for k in keys:
        v = studentArray[k]
        lastIndex = len(v.kor) - 1
        korArray.append(int(v.kor[lastIndex]))
        engArray.append(int(v.eng[lastIndex]))
        mathArray.append(int(v.math[lastIndex]))
        averageArray.append(v.calcAvg())
    dataframe['name'] = keys
    dataframe['국어'] = korArray
    dataframe['영어'] = engArray
    dataframe['수학'] = mathArray
    dataframe['평균'] = averageArray

    return dataframe


studentArray={}
while True:
    temp=int(input('1.입력 2. 출력 3. 종료'))
    if (temp == 3):
        break
    elif temp == 1 :
        s=Student()
        s.name = input('이름을 입력')
        s.age = input('나이를 입력')
        kor = int(input('국어 점수'))
        eng = int(input('영어 점수'))
        math = int(input('수학 점수'))

        if (s.name in studentArray.keys()): #중복이라면
            studentArray[s.name].kor.append(kor)
            studentArray[s.name].eng.append(eng)
            studentArray[s.name].math.append(math)
        else:
            s.kor.append(kor)
            s.eng.append(eng)
            s.math.append(math)
            studentArray[s.name]=s
    elif(temp ==2):
        while True:
            temp = int(input('1. 전체 출력 2. 개별 출력 3. 뒤로'))

            if (temp == 3):
                break
            elif temp == 1:
                dataframe = pd.DataFrame(prepareDataFrame(studentArray))
                print(dataframe)
            elif temp ==2:
                name = input('이름을 입력해주세요')
                if name in studentArray.keys(): #중복된 이름이면
                    length=len(studentArray[name].kor)
                x=[]
                for i in range(1,length+1):#김철수 2번 입력하면 x[]에 1,2 들어감
                    x.append(int(i))
                mp.plot(x,studentArray[name].kor, label = 'korean')
                mp.plot(x,studentArray[name].eng,label='english')
                mp.plot(x,studentArray[name].math,label='math')
                mp.plot(x,studentArray[name].totalAvg(),label='Average')


                mp.legend()
                mp.show()