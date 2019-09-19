# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:20:30 2019

@author: SU
"""
import imageio
import cv2
import os
'''
读取png，jpg，bmg格式图片
'''
#img= cv2.imread('b.jpg')
##cv2.imshow('a',img)
##cv2.waitKey()
##cv2.destroyAllWindows()

'''
利用opencv每隔两帧截取一张图片
'''
#times = 0
#frameQuency = 2
#GIF = cv2.VideoCapture('d.gif')
#while True:
#    times+=1
#    res,image =GIF.read()
#    if not res:
#        print('not res,not image')
#        break
#    if times % frameQuency==0:
#        cv2.imwrite('gif/'+str(times)+'.jpg',image)
#GIF.release
'''
将截取的图片合并成一副动图
'''
#num = 2
#imgs = os.listdir('gif/')
##图片排序
#imgs.sort(key = lambda x:int(x[:-4]))
#frames = []
#for name in imgs:
#    frames.append(imageio.imread('gif/'+name))
##保存为gif格式
#imageio.mimsave('cai.gif',frames,'GIF',duration = 0.1)
#******************************************************************************

