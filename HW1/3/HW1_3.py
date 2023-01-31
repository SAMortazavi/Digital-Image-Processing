import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import cv2
from math import cos, sin
transformed_pic=cv.imread('transformed.png')
#--------------------------------------------------
real_pic=transformed_pic[0:370,0:256]
real_resized_pic=cv2.resize(real_pic,(512,512), interpolation=cv2.INTER_CUBIC)
# plt.imshow(real_resized_pic)
# plt.show()
# #--------------------------------------------------
zeropad_pic=np.zeros((1024,1024,3)).astype('uint8')
zeropad_pic[256:768,256:768]=real_resized_pic
# plt.imshow(zeropad_pic,'gray')
# plt.show()
#----------------------------------------------------
tranlate_matrix=np.float32(([1,0,250],[0,1,100]))
translated_pic=cv2.warpAffine(zeropad_pic,tranlate_matrix,(1024,1024))
plt.imshow(translated_pic,'gray')
plt.show()
#----------------------------------------------------
shear_matrix=np.float32([[1, 0, 0],[-0.3, 1  , 0],[0, 0  , 1]])
sheared_pic = cv2.warpPerspective(zeropad_pic,shear_matrix,(1024,1024))
# plt.imshow(sheared_pic,'gray')
# plt.show()
#----------------------------------------------------
rotate_matrix=cv2.getRotationMatrix2D((0,0), 20, 1.0)
rotated_pic=cv2.warpAffine(zeropad_pic, rotate_matrix, (1024, 1024))
plt.imshow(rotated_pic,'gray')
plt.show()