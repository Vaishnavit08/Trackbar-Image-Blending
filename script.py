#  Image Blending with Trackbars

import cv2
import numpy as np

img=cv2.imread('krishna.jpg' )
img=cv2.resize(img,(500,700))

img1=cv2.imread('radha.jpg')
img1=cv2.resize(img1,(500,700))

cv2.imshow('krishna',img)
cv2.imshow('radha',img1)

def blend(x):
    pass


# creating blank image
img3=np.zeros((400,400,3),np.uint8)
# creating track bar windows
cv2.namedWindow('win')

cv2.createTrackbar('alpha','win',1,100,blend)

# creating switch to invoke the trackbar
switch='0 : OFF\n1 : ON'

# creating trackbar for switch
cv2.createTrackbar(switch,'win',0,1,blend)

while True:
    s=cv2.getTrackbarPos(switch,'win')
    a=cv2.getTrackbarPos('alpha','win')

    n=float(a/100)
    print(n)

    if s==0:
        dst=img3[:]

    else:
        dst=cv2.addWeighted(img,1-n,img1,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)
    cv2.imshow('dst',dst)
    k=cv2.waitKey(1)
    if k==ord('v'):
        break


cv2.destroyAllWindows()

