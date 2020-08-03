import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
from numpy.lib import stride_tricks

img=cv2.imread('D:\CV\Tutorials\\hand.jpeg',0)

img=cv2.GaussianBlur(img,(7,7),1)

def conv(img,kernel):
    kernel = np.flipud(np.fliplr(kernel))
    kernel=[[kernel]]
    img=np.float32(img)
    c=[]
    ksize=len(kernel[0][0])
    shape=(img.shape[0] - ksize + 1, img.shape[1] - ksize + 1, ksize, ksize)
    stride=img.strides
    patches = stride_tricks.as_strided(img, shape=shape, strides=2*stride)
    l=(patches*kernel)
    m=np.sum(l,axis=3)
    res=np.sum(m,axis=2)

    return res

def sobel(a, typ):
    sx = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]], dtype='float32')

    sy = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]], dtype='float32')

    scx = np.array([[3, 0, -3],
                    [10, 0, -10],
                    [3, 0, -3]], dtype='float32')

    scy = np.array([[3, 10, 3],
                    [0, 0, 0],
                    [-3, -10, -3]], dtype='float32')
    sx = np.divide(sx,4)
    sy = np.divide(sy,4)
    scx = np.divide(scx, 16)
    scy = np.divide(scy, 16)

    cx = conv(a, sx)
    cy = conv(a, sy)

    if typ == 'x':
        return (cx)
    else:
        return (cy)

def grad(a):

    resx = sobel(a, 'x')
    resy = sobel(a, 'y')


    resx=np.divide(resx,1)
    resy = np.divide(resy,1)


    mag=np.divide(np.hypot(resx,resy),1)

    x=np.copy(resx)
    x[(x==0)]=1
    gradient_angle = np.empty(mag.shape)
    gradient_angle=np.rad2deg(np.arctan2(resy,resx))
    gradient_angle[(gradient_angle==(-0.0))]+=0.0

    gradient_angle[(gradient_angle<0)]+=180
    a=mag,gradient_angle
    return a
def nms(b,a):


    #horizontal
    a[(a<=(22.5)) | (a>=(180-22.5))]=0

    #diagonal1
    a[(a>(22.5)) & (a<=(45+22.5))]=45
    #vertical
    a[(a>90-22.5) & (a<=90+22.5)]=90
    #diagonal2
    a[(a>(135-22.5)) & (a<=(135+22.5))]=135
    sh=a.shape
    for x in range (sh[1]):
        for y in range(sh[0]):

            #x1,y1 and x2,y2 are neighbour pixels
            if(a[y,x]==0):
                x1, y1 = x + 1, y
                x2, y2 = x - 1, y
            elif(a[y,x]==90):
                x1, y1 = x, y - 1
                x2, y2 = x, y + 1
            elif(a[y,x]==45):
                x1, y1=x + 1, y + 1
                x2, y2=x - 1, y - 1
            elif (a[y,x] == 135):
                x1, y1=x + 1, y - 1
                x2, y2=x - 1, y + 1
            if (sh[0]>y1>=0)and(sh[1]>x1>=0):
                if (b[y,x]<b[y1,x1]):
                    b[y,x]=0
                    continue
            if (sh[0]>y2>=0) and (sh[1]>y1>=0):
                if (b[y,x] < b[y2,x2]):
                    b[y,x] = 0

    cv2.imwrite("non-maxima_suppressed.bmp", b)
    return b
def Canny(thin,min,max):

    #Non Maximum Suppression
    #Hysterisis Threshholding
    R1=np.zeros_like(thin)
    R2=np.zeros_like(thin)
    R3=np.zeros_like(thin)

    R1=np.copy(thin)
    R1[R1<max]=0


    R3=np.copy(thin)
    R3[R3<min]=0

    R2=np.copy(thin)
    R2[(R2<min)|(R2>=max)]=0


    sh=thin.shape

    for i in range(0,sh[0]-1):
        for j in range(0,sh[1]-1):
            if (i!=0 and j!=0):
                if(thin[i,j]==R2[i,j] and R2[i,j]!=0):

                    l1=[thin[i-1,j-1], thin[i-1,j], thin[i-1,j+1], thin[i,j-1], thin[i,j+1], thin[i+1,j-1], thin[i+1,j],thin[i+1,j+1]]
                    l2=[R1[i-1,j-1],R1[i-1,j],R1[i-1,j+1],R1[i,j-1],R1[i,j+1],R1[i+1,j-1] ,R1[i-1,j-1],R1[i+1,j+1]]
                    kk=np.intersect1d(l1,l2)
                    if(len(kk>0)):
                        R1[i,j]=R2[i,j]
                    else:
                        R2[i,j]=0

    R1 = R1.astype('uint8')
    R1[R1!=0]=255
    a=R1


    return a


l=grad(img)

a=nms(l[0],l[1])
c=Canny(a,20,50)
cv2.imshow('Canny',c)
k=cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()










