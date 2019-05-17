#多边形泛滥填充算法
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import queue
import sys
class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Color:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

def isOldColor(v,oldColor):
    data = glReadPixels(v.x,v.y,1,1,GL_RGB,GL_FLOAT,outputType=None)
    color = [data[0][0][0],data[0][0][1],data[0][0][2]]
    if color[0]==oldColor.r and color[1]==oldColor.g and color[2]==oldColor.b:
        return True
    else:
        return False

def drawPixel(x,y,color):
    glBegin(GL_POINTS)
    glColor3f(color.r,color.b,color.b)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def floodfill(x,y,boundry,label,oldColor,newColor):
    # if isOldColor(Vertex(x,y),oldColor):
    #     glColor3f(newColor.r,newColor.g,newColor.b)
    #     glBegin(GL_POINTS)
    #     glVertex2f(x,y)
    #     glEnd()
    #     glFlush()
    #     floodfill(x+1,y,oldColor,newColor)
    #     floodfill(x-1,y,oldColor,newColor)
    #     floodfill(x,y+1,oldColor,newColor)
    #     floodfill(x,y-1,oldColor,newColor)

    q = queue.Queue()
    q.put(Vertex(x,y))
    drawPixel(x,y,newColor)

    while not q.empty():
        v = q.get(False)
        print('V:({0},{1})'.format(v.x,v.y))
        if isOldColor(Vertex(v.x,v.y+1),oldColor):
            q.put(Vertex(v.x,v.y+1))
            drawPixel(v.x,v.y+1,newColor)
        if isOldColor(Vertex(v.x,v.y-1),oldColor):
            q.put(Vertex(v.x,v.y-1))
            drawPixel(v.x,v.y-1,newColor)
        if isOldColor(Vertex(v.x-1,v.y),oldColor):
            q.put(Vertex(v.x-1,v.y))
            drawPixel(v.x-1,v.y,newColor)
        if isOldColor(Vertex(v.x+1,v.y),oldColor):
            q.put(Vertex(v.x+1,v.y))
            drawPixel(v.x+1,v.y,newColor)
    
def onMouse(button,state,x,y):
    oldColor = Color(1.,1.,1.)
    newColor = Color(1.,0.,0.)
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        floodfill(15,15,oldColor,newColor)

def display():
    p1 = Vertex(10,10)
    p2 = Vertex(20,10)
    p3 = Vertex(20,20)
    p4 = Vertex(10,20)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1.,0.,0.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(p1.x,p1.y)
    glVertex2f(p2.x,p2.y)
    glVertex2f(p3.x,p3.y)
    glVertex2f(p4.x,p4.y)
    glEnd()
    glFlush()

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(100,100)
    glutCreateWindow('FloodFill')
    glClearColor(1.,1.,1.,0.)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.,100.,0.,100.)
    glutDisplayFunc(display)
    glutMouseFunc(onMouse)
    glutMainLoop()