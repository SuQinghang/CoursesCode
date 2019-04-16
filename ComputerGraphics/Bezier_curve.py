#Bezier曲线绘制
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

current_x = 0
current_y = 0
pre_x = 0
pre_y=0
#将点v加入vList
def InsertVtovList(v):
    length = len(vList)
    for i in range(length):
        if vList[i].x>v.x:
            vList.insert(i,v)
            return
        if vList[i].x==v.x:
            return 
    vList.append(v)

#显示vList中的点
def showvList():
    print('--------------------------')
    for v in vList:
        print('({x},{y})'.format(x=v.x,y=v.y))
    print('--------------------------')

#删除vList与v近似的点
def RemoveV(v):
    for s in vList:
        if math.sqrt((s.x-v.x)**2+(s.y-v.y)**2)<2:
            vList.remove(s)
            return 

#n个顶点的参数方程
#vList按照顶点x坐标递增顺序排列
def ParamaterFunction(t):
    n = len(vList)
    new_v = Vertex(0,0)
    for i in range(n):
        new_v.x+=comb(n-1,i)*vList[i].x*((1-t)**(n-1-i))*(t**i)
        new_v.y+=comb(n-1,i)*vList[i].y*((1-t)**(n-1-i))*(t**i)
    return new_v

def drawPoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.,.0,.0)
    glPointSize(4)
    glBegin(GL_POINTS)
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
    for t in np.arange(0,1.1,.1):
        v = ParamaterFunction(t)
        print('draw_v: ({x},{y})'.format(x=v.x,y=v.y))
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
            pre_y = y
            #将该点加入vList
            InsertVtovList(Vertex(x,500-y))
            drawPoints()
            showvList()
        elif state==GLUT_UP:
            if len(vList)>1:
                drawCurve()
    #鼠标右键删除点
    elif button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
        flag = 0
        print('right click:({0},{1})'.format(x,y))
        y=500-y
        for i in range(len(vList)):
            if vList[i].x>x+2:
                break
            if(math.sqrt((vList[i].x-x)**2+(vList[i].y-y)**2)<2):
                vList.pop(i)
                flag=1
                break
        if flag==1:
            drawCurve()

#鼠标滑动事件
def MouseMotion(x,y):
    global pre_x,pre_y,current_x,current_y
    RemoveV(Vertex(pre_x,pre_y))
    current_x = x
    current_y = 500-y
    InsertVtovList(Vertex(current_x,current_y))
    pre_x,pre_y = current_x,current_y
    drawCurve()
    

#display函数
def display():
    print()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(500,500)
    glutCreateWindow('Bezier_curve')
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0.0,500.0,0.0,500.0)
    glutMouseFunc(OnMouse)
    glutMotionFunc(MouseMotion)
    glutDisplayFunc(display)
    glutMainLoop()
