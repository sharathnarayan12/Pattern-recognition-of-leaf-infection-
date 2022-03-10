import cv2
import numpy as np
from matplotlib import pyplot as plt
img =cv2.imread('test3.jpg', cv2.IMREAD_COLOR)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(img[:,:,1], 120, 255, cv2.THRESH_BINARY) 
ret,thresh2=cv2.threshold(imgray,190,255,cv2.THRESH_BINARY_INV)
ret,thresh=cv2.threshold(imgray,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img[:,:,1],120,255,cv2.THRESH_MASK) # input image  with the corresponding thresholding 
white_pix = np.sum(thresh2 == 255)
black_pix = np.sum(thresh1 == 0)
#n=thresh1.shape[0]*thresh1[1]
v=black_pix+white_pix
a=(black_pix/white_pix)*100
print(a)
b=100-a
print(b)
print("total number of pixel :", v)
print("infected area is",a,"%")
print(' rest :', white_pix)
print(' infected pixels:', black_pix)
titles = ['Original Image','image gray','Binary Threshold','binary inv','mask','binaryin2']
images = [img, imgray, thresh1,thresh2,thresh3,thresh]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()