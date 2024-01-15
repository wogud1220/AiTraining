#케라스 중 가장 간단한 모델인 시퀀셜 모델을 로딩한다.
from keras.models import Sequential

#내부 신경망을 구성할 레이어들을 로딩한다.
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

#케라스 시퀀셜 모델 사용
model = Sequential()

#입력되는 데이터를 규정하는 코드
#3차원 배열을 받아들일 것이고, 각 입력값은 [100][1]배열이다. 즉 [1000][100][1]이 됨.
#activation = Conv1D를 실행시킬때 어떤 함수를 쓸 거냐, 주로 relu 사용
#입력이 끝난 후에는 해당 배열의 차수를 1개 줄인다.
#즉3차원에서 2차원 배열이됨.
model.add(Conv1D(32, 3, activation='relu', input_shape=(100, 1))) 

#위에서 입력된 데이터를 필터링한다.
model.add(MaxPooling1D(2))

#필터링된 데이터를 최종적으로 1차원화(평탄화) 시킴.
model.add(Flatten())

#Dense Layer는 입력 뉴런과 출력 뉴런이 연결된 밀집 모델이다.
#훌련된 데이터를 입력 뉴런에 넣어 출력 뉴런에 보내어 처리한다.
#하지만 우리가 이 과정은 뇌의 깊은 영역에서 행해지듯
#자세한 과정은 알 수 없기 때문에 '숨겨진 레이어' or 'hidden layer'라고 함.
model.add(Dense(1, activation='sigmoid'))

#위에 설정 값들을 토대로 모델을 생성"
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


import numpy as np
#모델한테 학습시킬 데이터 x_train, y_train 준비
x_train = np.random.randn(1000, 100, 1) #크기가 1인 배열이 100개 모여잇는 배열이 1000개 모여있는 3차원 배열 =[1000][100][1]
print("x_train: \n", np.shape(x_train), "----\n")
y_train = np.random.randint(2, size=(1000, 1))
#print("y_train: \n", y_train, "----\n")


#epochs=훈련 횟수 100번째 훈련하니깐 80퍼,
#500번째에서 정확도 100퍼 나옴 이후엔 의미 없음
#loss = 그래프가 모든 점을 포함하면 좋지만 못할수도있음, 거기서 가장 말이 안되는 애들을 제껴라, 손실
'''
model.fit(x_train,y_train, epochs=50, batch_size=32)
x_predict=np.random.randn(10, 100, 1)
y_predict=model.predict(x_predict)
results = model.evaluate(x_predict, y_predict)
print('\n\n results:\n\n', results)'''

#이 값들은 우리 모델이 xpredict가 들어갈때 예상한 결과값들을 모아둔 것.
#print(model.predict(x_predict))
