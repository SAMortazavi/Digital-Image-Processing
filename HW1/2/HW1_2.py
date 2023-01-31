import pydicom as dicom
from matplotlib import pyplot as plt
import numpy as np
import cv2
img=[]
cap=cv2.VideoCapture('MRI-Head.avi')
while cap.isOpened():
    i=0
    ret, frame=cap.read()
    if not ret:
        print('end')
        break
    img.append(frame)
img=np.array(img)
average_frame=np.zeros(shape=(256,256))
for i in range(256):
    for j in range(256):
        average_frame[i,j]=np.average(img[:,i,j])
# plt.subplot(1,2,1)
# plt.title('Average')
# plt.imshow(average_frame,'gray')
# plt.subplot(1,2,2)
# plt.title('first frame')
# plt.imshow(img[0],'gray')
# plt.show()
#----------------------------------------------------------
mask1=np.load('mask1.npy')
mask2=np.load('mask2.npy')
filtered_mask1=mask1*average_frame
filtered_mask2=mask2*average_frame
all_filtered=filtered_mask1+filtered_mask2
plt.imshow(all_filtered,'gray')
plt.show()