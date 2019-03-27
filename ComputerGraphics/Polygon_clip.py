from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from enum import Enum
class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
#边界类型
class Boundary(Enum):
    Left = 1
    Right = 2
    Top = 3
    Bottom = 4
#判断顶点与边界的关系
#待判断顶点p,边界b,边界低点minP,边界高点maxP
def Inside(p,b,minP,maxP):
    if b is Boundary.Left:
        if(p.x < minP.x):
            return False
    elif b is Boundary.Right:
        if(p.x > maxP.x):
            return False
    elif b is Boundary.Top:
        if(p.y > maxP.y):
            return False
    elif b is Boundary.Bottom:
        if(p.y < minP.y):
            return False
    return True
#直线段SP和窗口边界求交，返回交点
#端点s,p,边界b,边界低点minP,边界高点maxP
def Intersect(s,p,b,minP,maxP):
    k=0
    if s.x != p.x:
        k = (p.y-s.y)/(p.x-s.x)
    if b is Boundary.Left:
        x = minP.x
        y = p.y+(x-p.x)*k
    elif b is Boundary.Right:
        x = maxP.x
        y = p.y+(x-p.x)*k
    elif b is Boundary.Top:
        y = maxP.y
        if s.x!=p.x:
            x = p.x+(y-p.y)/k
        else:
            x = p.x
    elif b is Boundary.Bottom:
        y = minP.y
        if s.x!=p.x:
            x = p.x+(y-p.y)/k
        else:
            x = p.x
    return Vertex(x,y)

#利用边界对每条边进行裁剪
def edgeClip(b,minP,maxP,InvertexArray):
    new_Out = []
    current = -1
    next = 0
    while(current<len(InvertexArray)-1):
        S = InvertexArray[current]
        P = InvertexArray[next]
        if(Inside(S,b,minP,maxP) and Inside(P,b,minP,maxP)):
            new_Out.append(P)
        elif(Inside(S,b,minP,maxP) and (not Inside(P,b,minP,maxP))):
            v = Intersect(S,P,b,minP,maxP)
            new_Out.append(v)
        elif((not Inside(S,b,minP,maxP)) and Inside(P,b,minP,maxP)):
            v =Intersect(S,P,b,minP,maxP)
            new_Out.append(v)
            new_Out.append(P)
        current = next
        next +=1
    return new_Out

#多边形裁剪
def display():
    #绘制边界
    minP = Vertex(-50,0)
    maxP = Vertex(50,100)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(minP.x,minP.y)
    glVertex2f(maxP.x,minP.y)
    glVertex2f(maxP.x,maxP.y)
    glVertex2f(minP.x,maxP.y)
    glEnd()
    #绘制多边形
    polygon = [Vertex(-100,-50),Vertex(0,150),Vertex(20,50)]
    glLineWidth(2.0)
    glBegin(GL_LINE_LOOP)
    for v in polygon:
        glVertex2f(v.x,v.y)
    glEnd()
    glFlush()
    VertexArray = polygon
    #边界裁剪
    for b in Boundary:
        VertexArray = edgeClip(b,minP,maxP,VertexArray)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    for v in VertexArray:
        glVertex2f(v.x,v.y)
    glEnd()
    glFlush()


if(__name__ == "__main__"):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(800,800)
    glutCreateWindow('Sutherland_HClip')
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400.0,400.0,-300.0,300.0)
    glutDisplayFunc(display)
    glutMainLoop()