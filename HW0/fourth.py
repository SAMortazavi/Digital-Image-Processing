import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
#4a
chest_im=cv.imread('ChestXray.tif')
cv.imshow('Display window',chest_im)
print(np.shape(chest_im))
chest_im_gray=cv.cvtColor(chest_im,cv.COLOR_BGR2GRAY)
cv.imshow('Display window',chest_im_gray)
print(np.shape(chest_im_gray))
#______________________________________________________________________________
#4b
print(chest_im.dtype)
print(chest_im_gray.dtype)
#_______________________________________________________________________________
#4c
print(chest_im_gray.size)
print(chest_im.size)
#_______________________________________________________________________________
#4d
crop_img=chest_im_gray[80:, 100:500]
cv.imshow("cropped", crop_img)
#_______________________________________________________________________________
#4e
mirror=chest_im_gray[80:, 500:100:-1]
cv.imshow("mirror", mirror)
#4H
plt.figure("HW0-9833063")
plt.subplot(1,3,1)
plt.title('Gray Image')
plt.imshow(chest_im_gray,'gray')
plt.axis(False)
plt.subplot(1,3,2)
plt.title('Cropped Image')
plt.imshow(crop_img,'gray')
plt.axis(False)
plt.subplot(1,3,3)
plt.title('Mirrored Image')
plt.imshow(mirror,'gray')
plt.axis(False)
plt.savefig('HW0-9833063-4.png')
plt.show()
cv.waitKey(0)