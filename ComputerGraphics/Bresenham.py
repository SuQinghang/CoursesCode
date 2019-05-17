#Bresenhamline算法实现及优化 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.patches as patches
#0<k<1
#************************************************************
def Bresenhamline(x0,y0,x1,y1,ax):
    dx = x1-x0
    dy = y1-y0
    k = dy/dx
    e = -0.5
    x=x0
    y=y0
    while(x<=x1):    
        ax.add_patch(patches.Rectangle((x,y),1,1,color='red'))
        x=x+1 
        e=e+k
        if(e>=0):
            y=y+1
            e=e-1
#****************************************************************
#优化
#****************************************************************
def IntegerBresenhamline(x0,y0,x1,y1,ax):
    dx = x1-x0
    dy = y1-y0
    e = -dx
    x = x0
    y = y0
    while(x<=x1):
        ax.add_patch(patches.Rectangle((x,y),1,1))
        x = x+1
        e = e+2*dy
        if(e>=0):
            y = y+1
            e = e-dx
#*************************************************************
#网格
x = np.arange(0,50,1)
y = np.arange(0,50,1)
fig = plt.figure()
ax = fig.gca()
ax.set_xticks(x)
ax.set_yticks(y)
ax.grid()
#像素填充
Bresenhamline(0,0,45,30,ax)
IntegerBresenhamline(0,0,45,30,ax)
#绘制原函数
y = 30/45 * x
plt.plot(x,y,color='g')

plt.show()