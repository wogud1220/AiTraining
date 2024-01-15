import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

#상품 생성
interest = {
    0: "만화",#10대 남성
    1: "화장품",#10대 여성
    2: "게임",#20대 남성
    3: "의류",#20대 여성
    4: "건강식품",#30대 남성
    5: "애완동물",#30대 여성
    6: "자전거",#40대 남성
    7: "골프",#40대 여성
    8: "낚시",#50대 남성
    9: "시험 응시자"#50대 여성
}


# 작은 합성 데이터 집합을 만듭니다.
data = {
    "age": [10, 10, 20, 20, 30, 30, 40, 40, 50, 50],
    "gender": [0,1,0,1,0,1,0,1,0,1],
    "category": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}

# 입력 특성과 레이블을 

features = np.array([data["age"], data["gender"]]).T
#label = [0 1 2 3 4 ````]
labels = np.array(data["category"])

#모델 생성, 정의
model = Sequential()
model.add(Dense(20, activation='relu', input_shape=(2,)))
model.add(Dense(len(interest), activation='softmax'))

# 모델을 컴파일합니다.
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델을 훈련합니다.
model.fit(features, labels, batch_size=1,epochs=2000, verbose=1)
while 1:
# 사용자 입력을 받습니다.
    age = int(input("나이를 입력하세요 (10~50): "))
    gender = int(input("성별을 입력하세요 (남, 여): "))

# 신경망을 사용하여 사용자 입력에 대한 예측을 수행합니다.
    input_data = np.array([[age, gender]])
    prediction = model.predict(input_data)

# 예측된 카테고리 인덱스를 가져옵니다.
    predicted_category_index = np.argmax(prediction[0])

# 인덱스를 해당하는 카테고리로 매핑합니다.
    predicted_category = interest[predicted_category_index]

    if gender==0:
        genderOutput='남성'
    else:
        genderOutput='여성'
# 결과를 출력합니다.
    print(age,'대',genderOutput,'이 관심있는 상품 카테고리는', predicted_category)