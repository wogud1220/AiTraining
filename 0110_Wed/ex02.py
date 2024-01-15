#케라스 시퀀스 모델 로딩
from keras.models import Sequential
#케라스 레이어 로딩
from keras.layers import Dense

# x_train: -100 ~ 100까지의 정수 값
import numpy as np
#x_prepare=np.arange(-10, 10, 1)
#y_prepare=2*x_train+1
#print(y_prepare)


x_train = np.arange(-100, 101, 1)
print(x_train)

y_train = 2*x_train+1

#훈련 정확성을 위해서 셔플해줌
index = np.arange(x_train.shape[0])
np.random.shuffle(index)
x_train = x_train[index]
y_train = y_train[index]

#1차원 배열은 학습시킬 수 없음, 2차원으로 만들어야함
#x_train = x_train.reshape(-1,1)#왼쪽행의 갯수, 열의 갯수 = 한줄로 길게 만들겠다.
#print(x_train)


#Sequential Model 생성
model = Sequential()
#생성된 모델에 덴스 레이어 추가
model.add(Dense(units=1, input_shape=(1,)))

#모델 준비, 손실 mse = 평균 구해서 표준오차 벗어난 애 제끼는
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

#배치 사이즈= 한번에 1개씩 훈련, 얼마나 잘라서 할까, 너무 크면 훈련을 잘 안 함, 너무 자잘하면 간단한 것도 훈련양이 많아짐
model.fit(x_train, y_train,epochs=80, batch_size=1)


# 훈련 결과를 테스트하기 위해서 1~10까지의 정수가 들어간
# 배열을 준비
x_test = np.arange(1,11,1)
y_test = 2*x_train +1
print(model.predict(x_test))
print(y_test)