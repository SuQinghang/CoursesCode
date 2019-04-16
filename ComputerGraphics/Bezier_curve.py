#Bezier曲线绘制
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
#一次函数公式
def linear_curve(t,P0,P1):
    return (1-t)*P0.x+t*P1.x,(1-t)*P0.y+t*P1.y
#一次函数绘制
def display_linear_curve(P0,P1,color):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_LINE_STRIP)
    for t in np.arange(0,1.1,0.1):
        glVertex(linear_curve(t,P0,P1))
    glEnd()
    glFlush()
#二次函数公式
def quadratic_curve(t,P0,P1,P2):
    return (1-t)**2*P0.x+2*t*(1-t)*P1.x+t**2*P2.x,(1-t)**2*P0.y+2*t*(1-t)*P1.y+t**2*P2.y
#二次函数绘制
def display_qudratic_curve(P0,P1,P2,color):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_LINE_STRIP)  
    for t in np.arange(0,1.1,0.1):
        glVertex(quadratic_curve(t,P0,P1,P2))
    glEnd()
    glFlush()
#三次函数公式
def cubic_curve(t,P0,P1,P2,P3):
    return ((1-t)**3*P0.x+3*t*(1-t)**2*P1.x+3*t*t*(1-t)*P2.x+t**3*P3.x,
            (1-t)**3*P0.y+3*t*(1-t)**2*P1.y+3*t*t*(1-t)*P2.y+t**3*P3.y)
#三次曲线绘制
def display_cubic_curve(P0,P1,P2,P3,color):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_LINE_STRIP)  
    for t in np.arange(0,1.1,0.1):
        glVertex(cubic_curve(t,P0,P1,P2,P3))
    glEnd()
    glFlush()

#鼠标事件
def OnMouse(button,state,x,y):
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        glColor3f(1.,1.,1.)
        glBegin(GL_POINTS)
        glVertex2f(x,5.-y)
        glEnd()
        glFlush()

#display函数
def display():

    #绘制一次曲线
    P0 = Vertex(0.0,0.0)
    P1 = Vertex(5.0,5.0)
    display_linear_curve(P0,P1,[1.0,0.0,0.0])
    # #绘制二次曲线
    # P0 = Vertex(0.0,0.0)
    # P1 = Vertex(1.0,1.0)
    # P2 = Vertex(2.0,4.0)
    # display_qudratic_curve(P0,P1,P2,[0.0,.1,.0])
    # #绘制三次曲线
    # P0 = Vertex(0.0,0.0)
    # P1 = Vertex(1.0,1.0)
    # P2 = Vertex(3.0,2.0)
    # P3 = Vertex(4.0,5.0)
    # display_cubic_curve(P0,P1,P2,P3,[.0,.0,.1])



if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(5,5)
    glutCreateWindow('Bezier_curve')
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,5.0,0.0,5.0)
    glutMouseFunc(OnMouse)
    glutDisplayFunc(display)
    glutMainLoop()
