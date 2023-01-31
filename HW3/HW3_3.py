import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

#a

def correlation(f, w, kernel_size):
    out = np.zeros(np.shape(f))
    f = np.pad(f,1)
    for i in range(f.shape[0]-kernel_size+1):
        for j in range(f.shape[1]-kernel_size+1):
            out[i, j] = np.sum(f[i:i+kernel_size, j:j+kernel_size]*w)
    return out

def img_filter(img, filter_name, kernel_size=3):
    image=img.copy()
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
        
        filter_matrix = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]) 
        out = correlation(image, filter_matrix, kernel_size )                        
    return out
#b
MRI_IMG=cv.imread("MRI.png",0)
mean_filtered_img=img_filter(MRI_IMG,'Mean')
median_filtered_img=img_filter(MRI_IMG,'Median')
sobelx_filtered_img=img_filter(MRI_IMG,'Sobel_x')
sobely_filtered_img=img_filter(MRI_IMG,'Sobel_y')
laplacian_filtered_img=img_filter(MRI_IMG,'Laplacian')
plt.figure()
plt.subplot(3,2,1)
plt.imshow(MRI_IMG,'gray')
plt.title('orginal')
plt.subplot(3,2,2)
plt.imshow(mean_filtered_img,'gray')
plt.title('Mean filtered')
plt.subplot(3,2,3)
plt.imshow(median_filtered_img,'gray')
plt.title('Median filtered')
plt.subplot(3,2,4)
plt.imshow(sobelx_filtered_img,'gray')
plt.title('sobel x filtered')
plt.subplot(3,2,5)
plt.imshow(sobely_filtered_img,'gray')
plt.title('sobel y filtered')
plt.subplot(3,2,6)
plt.imshow(laplacian_filtered_img,'gray')
plt.title('laplacian filtered')
plt.show()
#c
mean5_filtered_img=img_filter(MRI_IMG,'Mean',5)
median5_filtered_img=img_filter(MRI_IMG,'Median',5)
plt.figure(figsize=(10,8))
plt.imshow(mean5_filtered_img,'gray')
plt.title('mean 5*5')
plt.show()
plt.figure()
plt.imshow(median5_filtered_img,'gray')
plt.title('median 5*5')
plt.show()
#d
def weighted_mean_filter(image):
        
    filter_matrix = np.array([[1,2,1],[2,5,2],[1,2,1]])/16
    out = correlation(image, filter_matrix, 3)
    return out
weighted_mean_filtered=weighted_mean_filter(MRI_IMG)
plt.figure(figsize=(10,8))
plt.subplot(1,2,1)
plt.imshow(weighted_mean_filtered,'gray')
plt.title('weighted mean')
plt.subplot(1,2,2)
plt.imshow(mean_filtered_img,'gray')
plt.title('Mean filtered')
plt.show()
