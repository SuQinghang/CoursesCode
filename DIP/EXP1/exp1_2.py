# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:58:35 2019

@author: SU
"""

#利用Alpha通道合成
import cv2
import numpy as np
img = cv2.imread('a.png',-1)
background = cv2.imread('background.png')
background = cv2.resize(background,(426,300))

A = np.zeros((img.shape[0],img.shape[1]),dtype = img.dtype)


A = img[:,:,3]
a = A/255.0
result = np.zeros((img.shape[0],img.shape[1],3),dtype = img.dtype)

result[:,:,0] = img[:,:,0]*a+(1-a)*background[:,:,0]
result[:,:,1] = img[:,:,1]*a+(1-a)*background[:,:,1]
result[:,:,2] = img[:,:,2]*a+(1-a)*background[:,:,2]

cv2.imshow('result',result)
cv2.waitKey()
cv2.destroyAllWindows()