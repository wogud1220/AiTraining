import tensorflow as tf
import random
import numpy as np


x_test =[]
x_train = []
for i in range(1,10000):
    age = random.randint(10,50)
    gender = random.randint(0,1)
    if i< 9000:
        x_train.append((age, gender))
    else:
        x_test.append((age,gender))


#np배열로 변환
x_train = np.array(x_train)
x_test = np.array(x_test)

y_test = []
y_train = []

for x in x_train:
    if x[1] == 0: #남자일때 
        if x[0] // 10 ==1: #남자 10대면
            y_train.append(0)
        elif x[0]//10==2:
            y_train.append(2)
        elif x[0]//10==3:
            y_train.append(4)
        elif x[0]//10==4:
            y_train.append(6)
        elif x[0]//10==5:
            y_train.append(8)
    elif x[1] == 1: #여자일 때
        if x[0]//10==1:
            y_train.append(1)
        elif x[0]//10==2:
            y_train.append(3)
        elif x[0]//10==3:
            y_train.append(5)
        elif x[0]//10==4:
            y_train.append(7)
        elif x[0]//10==5:
            y_train.append(9)
            
#옮기기


#실수로 바꾸는 법
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model= Sequential()

#model.add(Flatten(input_shape=(2,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
model.fit(x_train, y_train, batch_size=80, epochs=100, verbose=1, validation_split =0.1)


x_test=x_train
y_test=y_train

test_loss, test_acc = model.evaluate(x_test, y_test)
print('정확성', test_acc)


user_age=input("나이 ")
user_gender=input("성별 (남자: 0, 여자: 1)")
user_data = [(int(user_age)//10, int(user_gender))]
user_data=np.array(user_data)
print(model.predict(user_data))