# -*- coding: utf-8 -*-


'''
图像缩放 双线性插值
'''

import cv2
import numpy as np
import math

'''
计算一个像素点的某个通道的色值
'''
def f(inputIMG,i,j,u,v):
    height,width = inputIMG.shape
    if i==0 or j==0 or i== height-1 or j==width-1 :
        return inputIMG[i][j]
    else:
        return  (1-u)*(1-v)*inputIMG[i][j]+(1-v)*u*inputIMG[i][j+1]+v*(1-u)*inputIMG[i+1][j]+u*v*inputIMG[i+1][j+1]


'''
图像缩放
inputIMG为输入图像，sx为图片的高缩放倍数，sy为宽缩放倍数
'''
def Scale(inputIMG,sx,sy):
    height,width,channel =inputIMG.shape
    output_width = int(width*sy)
    output_height = int(height*sx)
    outputIMG = np.zeros((output_height,output_width,channel),dtype = inputIMG.dtype)
    for dstX in range(output_height):
        for dstY in range(output_width):
            srcX = dstX/sx
            srcY = dstY/sy
            i = math.floor(srcX)
            j = math.floor(srcY)
            u = srcX - i
            v = srcY - j
            outputIMG[dstX][dstY][0] = f(inputIMG[:,:,0],i,j,u,v)
            outputIMG[dstX][dstY][1] = f(inputIMG[:,:,1],i,j,u,v)
            outputIMG[dstX][dstY][2] = f(inputIMG[:,:,2],i,j,u,v)
    return outputIMG

'''
图像变形
'''
    
def Map(inputIMG):
    #中心归一化
    height,width,channel = inputIMG.shape
    outputIMG = np.zeros((height,width,channel),dtype = inputIMG.dtype)
    for x in range(height):
        for y in range(width):
            tmpX = (x-0.5*height)/(0.5*height)
            tmpY = (y-0.5*width)/(0.5*width)
            r = math.sqrt(tmpX**2+tmpY**2)
            theta = (1-r)**2
            if  r>=1:
                inputX,inputY = tmpX, tmpY
            else:
                inputX,inputY = math.cos(theta)*tmpX-math.sin(theta)*tmpY, math.sin(theta)*tmpX+math.cos(theta)*tmpY
            inputX,inputY = int((inputX+1)*0.5*height),int((inputY+1)*0.5*width)
            outputIMG[x][y][0] = inputIMG[inputX][inputY][0]
            outputIMG[x][y][1] = inputIMG[inputX][inputY][1]
            outputIMG[x][y][2] = inputIMG[inputX][inputY][2]
    return outputIMG
             
if __name__ == '__main__':
    img = cv2.imread('a.jpg')
    output = Scale(img,1.3,0.7)
#    output = Map(img)
    cv2.imshow('output',output)
    cv2.imwrite('1.3_0.7.jpg',output)
    cv2.waitKey()
    cv2.destroyAllWindows()