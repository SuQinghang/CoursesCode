from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np 
import math
from Bezier_curve import showvList
#顶点
class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
#鼠标拖动坐标的标记
current_x = 0
current_y = 0
pre_x = 0
pre_y=0
vList = []
mode = 0
#判断是否存在某个点
def isExist(v):
    for s in vList:
        if math.sqrt((s.x-v.x)**2+(s.y-v.y)**2)<20:
            return s
    return None
#显示顶点及限制多边形
def drawPoints():
	glClear(GL_COLOR_BUFFER_BIT)
	#顶点
	glColor3f(1.0,0.0,0.0)
	glPointSize(4)
	glBegin(GL_POINTS)
	for v in vList:
		glVertex2f(v.x,v.y)
	glEnd()
	glFlush()
	#边
	glColor3f(0.0,1.0,0.0)
	glBegin(GL_LINE_STRIP)
	for v in vList:
		glVertex2f(v.x,v.y)
	glEnd()
	glFlush()


#deboor算法求k次B样条基函数
#u为一个节点，i为节点号，k为阶数，knot为节点向量
def basisFunc(u,i,k,knot):
	Nik_u = 0
	if k==1:
		if u>=knot[i] and u<knot[i+1]:
			return 1.0
		else:
			return 0.0	
	else:
		length1 = knot[i+k-1]-knot[i]
		length2 = knot[i+k]-knot[i+1]
		if not length1 and not length2:
			Nik_u = 0
		elif not length1:
			Nik_u = (knot[i+k]-u)/length2 * basisFunc(u,i+1,k-1,knot)
		elif not length2:
			Nik_u = (u-knot[i])/length1 * basisFunc(u,i,k-1,knot)
		else:
			Nik_u = ((u-knot[i])/length1 * basisFunc(u,i,k-1,knot)+
						(knot[i+k]-u)/length2 * basisFunc(u,i+1,k-1,knot))
		return Nik_u

#设置节点向量
#n+1个控制顶点，k阶
def knot_vector(k, n):
	m = n+k
	knot = np.linspace(0,1,m+1)
	for i in range(0,k):
		knot[i]=0
	for i in range(m-(k-1),m+1):
		knot[i]=1
	return knot
#递归绘制B样条曲线
def NormalBSpline():
	n = len(vList)-1#顶点数目
	k = 4#曲线阶数
	T = np.linspace(0,1,500)
	knot = knot_vector(k,n)
	#print('knot:',knot)
	Nik = np.zeros((len(T),n+1))
	for i in range(len(T)):
		for j in range(n+1):
			Nik[i][j] = basisFunc(T[i],j,k,knot)
	P = []
	for v in vList:
		P.append([v.x,v.y])
	P = np.array(P)
	D = np.dot(Nik,P).tolist()
	#return D
	#绘制求出的曲线上的点
	drawPoints()
	glColor3f(0.0,0.0,1.0)
	glPointSize(1)
	glBegin(GL_POINTS)
	for d in D:
		glVertex2f(d[0],d[1])
	glEnd()
	glFlush()

#除法
def div(a,b):
	'''
	a:被除数
	b:除数
	'''
	if a==0 or b==0:
		return 0
	else:
		return a/b
#deBoor递推
def deBoor(P,i,r,k,u,U):
    '''
    P:控制节点
    i:区间起点
    r:降阶阶数
    k:曲线阶数
    u:节点
    U:节点向量
    '''
    if r==0:
        return P[i].x,P[i].y
    else:
        x1,y1 = deBoor(P,i,r-1,k,u,U)
        x2,y2 = deBoor(P,i-1,r-1,k,u,U)
        return div(u-U[i],U[i+k-r]-U[i])*x1+div(U[i+k-r]-u,U[i+k-r]-U[i])*x2,\
                    div(u-U[i],U[i+k-r]-U[i])*y1+div(U[i+k-r]-u,U[i+k-r]-U[i])*y2
#deBoor绘制B样条曲线
def deboorCurve():
	n = len(vList)-1#顶点数目
	k = 4#曲线阶数
	knot = np.linspace(1,n+k+1,n+k+1)
	start = knot[k-1]
	end = knot[n+1]
	T = np.linspace(start,end,500)
	D = []
	for t in T[:-1]:	
		j = np.where(t>=knot)[0][-1]
		x,y = deBoor(vList,j,k-1,k,t,knot)
		#print('({0},{1})'.format(x,y))
		D.append([x,y])
	drawPoints()
	glColor3f(0.0,0.0,1.0)
	glPointSize(1)
	glBegin(GL_LINE_STRIP)
	for d in D:
		glVertex2f(d[0],d[1])
	glEnd()
	glFlush()

#鼠标左键点击选点
def OnMouse(button,state,x,y):
	if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
		global pre_x,pre_y
		pre_x = x
		pre_y = 500-y
		#将该点加入vList
		v = isExist(Vertex(x,500-y))
		if v==None:
			vList.append(Vertex(x,500-y))
		drawPoints()
	elif button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
		flag = 0
		v = isExist(Vertex(x,500-y))
		if v!=None:
			vList.remove(v)
			flag = 1
		if flag==1:
			drawPoints()

#键盘事件
def OnKeyboard(key,x,y):
	global mode
	if key==b'a' and len(vList)>=4:
		mode = 1
		NormalBSpline()
	if key==b'b' and len(vList)>=4:
		mode = 2
		deboorCurve()

#鼠标滑动事件
def MouseMotion(x,y):
	global pre_x,pre_y,current_x,current_y,mode
	current_x = x
	current_y = 500-y
	currentV = Vertex(current_x,current_y)
	v = isExist(Vertex(pre_x,pre_y))
	if v!=None:
		index = vList.index(v)
		vList[index] = currentV
	pre_x,pre_y = current_x,current_y
	if mode==1:
		NormalBSpline()
	elif mode==2:
		deboorCurve()
	else:
		drawPoints()

#显示
def display():
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0.,500.0,0.0,500.0)

if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(500,500)
	glutCreateWindow('BSpline')

	glutDisplayFunc(display)
	glutMouseFunc(OnMouse)
	glutKeyboardFunc(OnKeyboard)
	glutMotionFunc(MouseMotion)

	glutMainLoop()