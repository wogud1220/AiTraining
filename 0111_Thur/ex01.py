import tensorflow as tf
import keras
import numpy as np


#손글씨 이미지 데이터 전처리 과정
mist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mist.load_data()

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255

print(x_test)

#categorical() = 결과값이 몇가지로나오는지 분류할때 사용, 10가지 0~9
y_train = tf.keras.utils.to_categorical(y_train,10)
y_test = tf.keras.utils.to_categorical(y_test,10)

#모델 생성
model = keras.models.Sequential()
#1차원으로 변환
model.add(keras.layers.Flatten(input_shape=(28,28)))

#이미지 분류할때 사용할 뇌의 뉴런의 개수 128개로 잡음
model.add(keras.layers.Dense(128, activation='relu'))

#분류를 위해서 사용하는 활성화 함수와 개수
#128 덴스에서 입력이 들어오고 처리한걸 아래 덴스에서 처리
#해당 값을 분류화 시켜야된다. softmax 사용. 
model.add(keras.layers.Dense(10, activation='softmax'))

#컴파일      SGD = 최적화   accuracy=정확도를 기준으로, 분류할 것이다.     
model.compile(optimizer='SGD', loss = 'categorical_crossentropy', metrics=['accuracy'])
#model.compile(optimizer='adam', loss='mse',                       metrics=['accuracy'])
#훈련 시키기 validation = 검증할때 데이터를 잘라서 20프로는 검증 80프로는 훈련, 내가 훈련한 것이 맞게 되었는지
model.fit(x_train, y_train, batch_size = 64, epochs = 400, verbose=1, validation_split=0.2)

test_loss, test_acc = model.evaluate(x_test, y_test)
print("정확도: ", test_acc)