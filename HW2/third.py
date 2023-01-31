import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
img_org=cv.imread('spine.tif',0)
img=img_org.copy()
# transformattion PL and LCS
def transform(img,transformname,gama=1):
    img_MAX=img.max()
    img_MIN=img.min()
    if transformname=='PL':
        for i in range(512):
            for j in range(512):
                img[i,j]=img[i,j]**gama
    elif transformname=='LCS':
        for i in range(512):
            for j in range(512):
                img[i,j]=(255*(img[i,j]-img_MIN))/(img_MAX-img_MIN)
    return img
#2
img_LCS=transform(img,'LCS').astype('uint8')
img_LCS1=img_LCS.copy()
img_PL=transform(img,'PL',0.5).astype('uint8')
img_PL1=img_PL.copy()
img_LCS_PL=transform(img_LCS1,'PL',0.5).astype('uint8')
img_PL_LCS=transform(img_PL1,'LCS').astype('uint8')
# #3
plt.subplot(2,3,1)
plt.imshow(img_org,'gray')
plt.title('original')
plt.subplot(2,3,2)
plt.imshow(img_LCS,'gray')
plt.title('img_LCS')
plt.subplot(2,3,3)
plt.imshow(img_LCS_PL,'gray')
plt.title('img_LCS_PL')
plt.subplot(2,3,4)
plt.imshow(img_org,'gray')
plt.title('original')
plt.subplot(2,3,5)
plt.imshow(img_PL,'gray')
plt.title('img_PL')
plt.subplot(2,3,6)
plt.imshow(img_PL_LCS,'gray')
plt.title('img_PL_LCS')
plt.show()
