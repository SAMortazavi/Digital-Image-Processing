import pydicom as dicom
from matplotlib import pyplot as plt
import numpy as np
import cv2
import math
pic1=dicom.dcmread('file1.dcm')
im_type=pic1.Modality
im_bite=pic1.BitsAllocated
im_loc=pic1[0x0180015].value
im_bite_stored=pic1[0x0280101].value
part1_list=[im_type,im_bite,im_bite_stored,im_loc]
print(f'type is, {part1_list[0]}, bite={part1_list[1]}, stored bit={part1_list[2]}, path={part1_list[3]}')
#------------------------------------------------------
data=pic1.pixel_array
down_x=np.array(([data[4*i,:] for i in range(128)]))
transposed=np.transpose(data)
down_y=np.transpose(np.array(([transposed[4*i,:] for i in range(128)])))
# plt.subplot(1,2,1)
# plt.title('Down_X')
# plt.imshow(down_x,'gray',vmin=0,vmax=511)
# plt.subplot(1,2,2)
# plt.title('Down_Y')
# plt.imshow(down_y,'gray',vmin=0,vmax=511)
# plt.show()
# # #------------------------------------------------------
down_x1=np.array([data[2*i,:] for i in range(256)])
down_xy=np.array([down_x1[:,2*i] for i in range(256)])
down_xy=np.array([down_xy[:,i] for i in range(256)])
# plt.imshow(down_xy,'gray',vmin=0,vmax=511)
# plt.show()
#-------------------------------------------------------
resize_NN=np.array(Image.fromarray(down_xy).resize((512,512), Image.NEAREST))
plt.imshow(resize_NN,'gray',vmin=0,vmax=511)
plt.title("Nearest neighbourhood")
# plt.show()
#-------------------------------------------------------
resize_BL=cv2.resize(down_xy, (512,512), interpolation=cv2.INTER_LINEAR)
# plt.imshow(resize_BL,'gray',vmin=0,vmax=511)
plt.title("inter linear")
# plt.show()
#--------------------------------------------------------
resize_BC=cv2.resize(down_xy,(512,512), interpolation=cv2.INTER_CUBIC)
plt.imshow(resize_BC,'gray',vmin=0,vmax=511)
plt.title("inter cubic")
plt.show()
#--------------------------------------------------------
resize_BC=resize_BC/16
cv2.imwrite('tiffile.tif', resize_BC)
cv2.imwrite('bmpfile.bmp', resize_BC)