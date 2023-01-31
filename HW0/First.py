#1a
import random
import numpy as np
Random_Numbers=[]
for i in range(80):
    Random_Numbers.append(round(random.uniform(-5000,5000),2))
Random_array=np.array(Random_Numbers)
# print((Random_array))
#________________________________________________________________
#1.b
# print(type(Random_array))
# print(Random_array.dtype)
#1c
Random_array=np.round(Random_array)
# print(Random_array)
#1d
Random_array=np.array(Random_Numbers,dtype='int16')
# print(Random_array)
# 1.e
Random_array=(Random_array+5000)/39.21
Random_array=Random_array.astype('int16')
# print(Random_array)
#1.f
Random_array=Random_array.reshape(10,8)
# print(Random_array)
# 1.g
Random_array=Random_array.astype('int8')
print(Random_array)