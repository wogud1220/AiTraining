import numpy as np
import matplotlib.pyplot as mp


x=[]
y=[]

for i in range (1,101):
    x.append(i)
    y.append(i*i)


arr_x= np.array(x)
arr_y = np.array(y)

mp.plot(arr_x, arr_y)
mp.show()