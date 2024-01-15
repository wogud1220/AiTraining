import numpy as np
import pandas as pd

sample = {'name':'조재영', '직업':'강사', '나이':34, '나이':24}
print(sample['나이'])
print(sample.keys())
print(sample.values())


sample = {'name':['소나타','그랜져','모닝','페라리'],
          'year':[2000, 2023, 2024, 2001],
          'price':[1000,2000,4000,8000]}

print(sample['name'][2],'\n\n')

dataframe = pd.DataFrame(sample, index=sample['price'])
print(dataframe)



csv_df = pd.read_csv('AI/data1.csv') # /Users/yoonjaehyeong/Desktop/Git/Python/AI/data1.csv 해도 됨
print(csv_df[['country', 'population']]) # 해당 열만 뽑아내라
print(csv_df.iloc[10:]) # 10번줄부터 다 뽑아내라