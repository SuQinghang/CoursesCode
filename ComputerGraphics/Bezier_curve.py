#Bezier曲线绘制
#鼠标左键点击选择顶点，右键点击已有顶点可删除，拖动已有顶点改变顶点位置
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from scipy.special import comb
import math

class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y

vList = []
#鼠标拖动坐标的标记
current_x = 0
current_y = 0
pre_x = 0
pre_y=0

#显示vList中的点
def showvList():
    print('--------------------------')
    for v in vList:
        print('({x},{y})'.format(x=v.x,y=v.y))
    print('--------------------------')
#判断是否存在某个点
def isExist(v):
    for s in vList:
        if math.sqrt((s.x-v.x)**2+(s.y-v.y)**2)<20:
            return s
    return None


#n个顶点的参数方程
#vList按照顶点x坐标递增顺序排列
def ParamaterFunction(t):
    n = len(vList)
    new_v = Vertex(0,0)
    for i in range(n):
        new_v.x+=comb(n-1,i)*vList[i].x*((1-t)**(n-1-i))*(t**i)
        new_v.y+=comb(n-1,i)*vList[i].y*((1-t)**(n-1-i))*(t**i)
    return new_v
#显示顶点和限制多边形
def drawPoints():
    glClear(GL_COLOR_BUFFER_BIT)
    #点
    glColor3f(1.,.0,.0)
    glPointSize(4)
    glBegin(GL_POINTS)
    for v in vList:
        glVertex2f(v.x,v.y)
    glEnd()
    glFlush()
    #多边形
    glColor3f(1.,0.,0.)
    glBegin(GL_LINE_STRIP)
    for v in vList:
        glVertex2f(v.x,v.y)
    glEnd()
    glFlush()
#绘制曲线
def drawCurve():
    glClear(GL_COLOR_BUFFER_BIT)
    drawPoints()
    glColor3f(.0,1.,.0)
    glBegin(GL_LINE_STRIP)
    for t in np.arange(0,1.1,.01):
        v = ParamaterFunction(t)
        glVertex2f(v.x,v.y)
    glEnd()
    glFlush()

#鼠标点击事件
def OnMouse(button,state,x,y):
    #鼠标左键选点
    if button==GLUT_LEFT_BUTTON:
        if state==GLUT_DOWN:
            global pre_x,pre_y
            pre_x = x
            pre_y = 500-y
            #将该点加入vList
            v = isExist(Vertex(x,500-y))
            if v == None:
                vList.append(Vertex(x,500-y))
            #显示加入后的vList
            #showvList()
            drawPoints()
        elif state==GLUT_UP:
            if len(vList)>1:
                drawCurve()
    #鼠标右键删除点
    elif button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
        flag = 0
        v = isExist(Vertex(x,500-y))
        #如果当前点在vList中,v是他的近似点，删除v
        if v !=None:
            vList.remove(v)
            flag=1
        if flag==1:
            drawCurve()

#鼠标滑动事件
def MouseMotion(x,y):
    global pre_x,pre_y,current_x,current_y
    current_x = x
    current_y = 500-y
    currentV = Vertex(current_x,current_y)
    v = isExist(Vertex(pre_x,pre_y))
    if v !=None:
        index = vList.index(v)
        vList[index] = currentV
        #vList.remove(v)

    #如果该点在vList中，将近似点变色
    # if isExist(currentV) == None:
    #     vList.append(currentV)
    pre_x,pre_y = current_x,current_y
    drawCurve()
    

#display函数
def display():
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0.0,500.0,0.0,500.0)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(500,500)
    glutCreateWindow('Bezier_curve')
    glutMouseFunc(OnMouse)
    glutMotionFunc(MouseMotion)
    glutDisplayFunc(display)
    glutMainLoop()
