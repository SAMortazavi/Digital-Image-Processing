import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np



img_8=cv.imread('spineXray.tif',0)
img_16=cv.imread('chest.tif',cv.IMREAD_ANYDEPTH)
print(f'dimension of 8 bit image is: {img_8.shape} and 16 bie: {img_16.shape}');
print(f'type of 8 : {type(img_8[1,1])} and 16:  {type(img_16[1,1])}')
#2 
def performCLAHE(img):
    img1=img.copy()
    clahe=cv.createCLAHE(clipLimit=40.0, tileGridSize=(3,3))
    CLAHE_IMG=clahe.apply(img1)
    return CLAHE_IMG
#3
def transform(img,bit_depth):
    img2=img.copy()
    if type(img2[1,1])==np.uint8:
        equalized_img=cv.equalizeHist(img2)
        
    elif type(img2[1,1])==np.uint16:
        row,col=img2.shape
        equalized_img=np.zeros([row,col])
        equalized_img=cv.normalize(img2,equalized_img, 0, 65535,cv.NORM_MINMAX)
    return equalized_img


img8_Clahe=performCLAHE(img_8)
img16_Clahe=performCLAHE(img_16)


img8_equalized=transform(img_8,2)
img16_equalized=transform(img_16,2)





img8_count,img8_bins=np.histogram(img_8,bins=64)
img8clahe_count,img8clahe_bins=np.histogram(img8_Clahe,bins=64)


img8eq_count,img8eq_bins=np.histogram(img8_equalized,bins=64)
img16_count,img16_bins=np.histogram(img_16,bins=65536)


img16clahe_count,img16clahe_bins=np.histogram(img16_Clahe,bins=65536)
img16eq_count,img16eq_bins=np.histogram(img16_equalized,bins=65536)


cdf8=np.cumsum((img8_count/sum(img8_count)))
cdf8clahe=np.cumsum((img8clahe_count/sum(img8clahe_count)))


cdf8eq=np.cumsum((img8eq_count/sum(img8eq_count)))
cdf16=np.cumsum((img16_count/sum(img16_count)))


cdf16clahe=np.cumsum((img16clahe_count/sum(img16clahe_count)))
cdf16eq=np.cumsum((img16eq_count/sum(img16eq_count)))

plt.figure("img8")
plt.subplot(3,3,1)
plt.imshow(img_8,'gray')
plt.subplot(3,3,2)
plt.imshow(img8_Clahe,'gray')
plt.subplot(3,3,3)
plt.imshow(img8_equalized,'gray')

plt.subplot(3,3,4)
img8_hist=plt.hist(img_8,rwidth=4)
plt.subplot(3,3,5)
img8_Clahe_hist=plt.hist(img8_Clahe,rwidth=4)
plt.subplot(3,3,6)
img8_equalized_hist=plt.hist(img8_equalized,rwidth=4)

plt.subplot(3,3,7)
plt.plot(img8_bins[1:],cdf8)
plt.subplot(3,3,8)
plt.plot(img8clahe_bins[1:],cdf8clahe)
plt.subplot(3,3,9)
plt.plot(img8eq_bins[1:],cdf8eq)
#------------------------------------------------------------------
plt.figure("img16")
plt.subplot(3,3,1)
plt.imshow(img_16,'gray')
plt.subplot(3,3,2)
plt.imshow(img16_Clahe,'gray')
plt.subplot(3,3,3)
plt.imshow(img16_equalized,'gray')

plt.subplot(3,3,4)
img8_hist=plt.hist(img_16,rwidth=1024)
plt.subplot(3,3,5)
img8_Clahe_hist=plt.hist(img16_Clahe,rwidth=1024)
plt.subplot(3,3,6)
img8_equalized_hist=plt.hist(img16_equalized,rwidth=1024)

plt.subplot(3,3,7)
plt.plot(img16_bins[1:],cdf16)
plt.subplot(3,3,8)
plt.plot(img16clahe_bins[1:],cdf16clahe)
plt.subplot(3,3,9)
plt.plot(img16eq_bins[1:],cdf16eq)

plt.show()