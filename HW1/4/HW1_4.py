from filecmp import cmp
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import cv2

background=cv2.imread('background-LE.bmp',0)
fullscale=cv2.imread('fullscale-LE.bmp',0)
object_pic=cv2.imread('object-LE.bmp',0)
avg_back=[]
avg_full=[]
for i in range(320):
    avg_back.append(np.average(background[i,:]))
    avg_full.append(np.average(fullscale[i,:]))
avg_back=np.array(avg_back)
avg_full=np.array(avg_full)
#----------------------------------------------------
normalize_pic=np.zeros(([320,413]))
for i in range(320):
    normalize_pic[i,:]=(object_pic[i,:]-avg_back[i])*(255/(avg_full[i]-avg_back[i]))
plt.subplot(1,2,1)
plt.imshow(normalize_pic,'gray')
plt.subplot(1,2,2)
plt.imshow(object_pic,'gray')
plt.show()
