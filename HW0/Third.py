import numpy as np
from matplotlib import pyplot as pp
from math import floor
def unit_circle_vectorized(r):
    A = np.arange(-r,r+1)**2
    dists = np.sqrt(A[:,None] + A)
    return 255*((dists-r)<((0.5)**(r+1))).astype('uint8')
print(unit_circle_vectorized(5))    
print(type(unit_circle_vectorized(7)))
#__________________________________________________________________
#3b
stdnumber=9833063
def noise_circle(Arr):
    (row,col)=np.shape(Arr)
    for i in range(row):
        for j in range(col):
            if Arr[i][j]==0:
                Arr[i][j]+=np.random.uniform(0,48)
                Arr[i][j]=floor(Arr[i][j])
            else:
                Arr[i][j]-=np.random.uniform(0,48)
                Arr[i][j]=floor(Arr[i][j])
    return Arr
print(noise_circle(unit_circle_vectorized(5)))
#_____________________________________________________________________
# 3c
pp.figure('HW0-Image-9833063')
pp.subplot(1,2,1)
pp.title('Real Array')
pp.imshow(unit_circle_vectorized(5),'gray')
pp.axis(False)
pp.subplot(1,2,2)
pp.title('Noisy Array amplitude=48 ')
pp.imshow(noise_circle(unit_circle_vectorized(5)),'gray')
pp.axis(False)
pp.savefig('HW0-Image-9833063-3.png')
pp.show()