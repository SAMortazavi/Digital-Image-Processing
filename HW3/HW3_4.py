import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
def correlation(f, w, kernel_size):
    out = np.zeros(np.shape(f))
    f = np.pad(f,1)
    for i in range(f.shape[0]-kernel_size+1):
        for j in range(f.shape[1]-kernel_size+1):
            out[i, j] = np.sum(f[i:i+kernel_size, j:j+kernel_size]*w)
    return out
def img_filter(image, filter_name, kernel_size=3):

    if filter_name == 'Mean':
        
        filter_matrix = np.ones((kernel_size,kernel_size))/kernel_size**2 
        out = correlation(image, filter_matrix, kernel_size)

    elif filter_name == 'Median':
        
        out = np.zeros(np.shape(image),dtype = 'int16')
        image = np.pad(image,1)
        for i in range(image.shape[0]-kernel_size+1):
            for j in range(image.shape[1]-kernel_size+1):
                out[i, j] = np.median(image[i:i+kernel_size, j:j+kernel_size])  

    elif filter_name == 'Sobel_x':
        
        filter_matrix = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]) 
        out = correlation(image, filter_matrix, kernel_size )    

    elif filter_name == 'Sobel_y':
        
        filter_matrix = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) 
        out = correlation(image, filter_matrix, kernel_size )   

    elif filter_name == 'Laplacian':
        
        filter_matrix = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]) 
        out = correlation(image, filter_matrix, kernel_size )                        
    return out
noisy_img=cv.imread('Noisy_Spine.png',0)
#a
median_filtered=img_filter(noisy_img,'Median',5)
median_filtered2=median_filtered.copy()
#b
mean_median_filtered=img_filter(median_filtered2,'Mean')
mean_median_filtered2=mean_median_filtered.copy()
laplacian_filtered_image=img_filter(mean_median_filtered2,'Laplacian')
sharped_image=mean_median_filtered-0.1*laplacian_filtered_image
(row,col)=sharped_image.shape
for i in range(row):
    for j in range(col):
        if sharped_image[i,j]>255:
            sharped_image[i,j]=255
        elif sharped_image[i,j]<0:
            sharped_image[i,j]=0
sharped_image=sharped_image.astype('uint8')
plt.figure()
plt.subplot(2,2,1)
plt.imshow(noisy_img,'gray')
plt.title('orginal')
plt.subplot(2,2,2)
plt.imshow(median_filtered,'gray')
plt.title('median filtered')
plt.subplot(2,2,3)
plt.imshow(mean_median_filtered,'gray')
plt.title('mean median')
plt.subplot(2,2,4)
plt.imshow(sharped_image,'gray')
plt.title('sharped')

#h
mean_filtered=img_filter(noisy_img,'Mean')
mean_filtered2=mean_filtered.copy()
median_mean_filtered=img_filter(mean_filtered2,'Median',5)
median_mean_filtered2=median_mean_filtered.copy()
laplacian_filtered_image2=img_filter(median_mean_filtered2,'Laplacian')
sharped_image2=median_mean_filtered-laplacian_filtered_image2
for i in range(row):
    for j in range(col):
        if sharped_image2[i,j]>255:
            sharped_image2[i,j]=255
        elif sharped_image2[i,j]<0:
            sharped_image2[i,j]=0
sharped_image2=sharped_image2.astype('uint8')
plt.figure()
plt.subplot(2,2,1)
plt.imshow(noisy_img,'gray')
plt.title('orginal')
plt.subplot(2,2,2)
plt.imshow(mean_filtered,'gray')
plt.title('mean filtered')
plt.subplot(2,2,3)
plt.imshow(median_mean_filtered,'gray')
plt.title('mean median')
plt.subplot(2,2,4)
plt.imshow(sharped_image2,'gray')
plt.title('sharped')
plt.show()
