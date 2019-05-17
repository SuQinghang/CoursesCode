from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
from functools import cmp_to_key
#数据结构定义
#*********************************************************
#顶点
class Vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
#边界点
class Edge:
	def __init__(self,x=0,delta_x=0,maxy=0):
		self.x = x
		self.delta_x = delta_x 
		self.maxy = maxy
#*********************************************************
#数据定义
#顶点集
vList = []
#新边表
NET = {}
#*********************************************************

#显示选择的顶点
def drawPoints():
	glColor3f(1.0,0.0,0.0)
	glPointSize(4)
	glBegin(GL_POINTS)
	for v in vList:
		glVertex2f(v.x,v.y)
	glEnd()
	glFlush()
#显示多边形
def drawPolygon():
	glClearColor(1.0,1.0,1.0,0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	drawPoints()
	glColor3f(0.0,1.0,0.0)
	glBegin(GL_LINE_LOOP)
	for v in vList:
		glVertex2f(v.x,v.y)
	glEnd()
	glFlush()
#获得顶点中最小和最大纵坐标
def getMinMaxY(vList):
	miny = vList[0].y
	maxy = vList[0].y
	for v in vList[1:]:
		if miny>v.y:
			miny = v.y
		if maxy<v.y:
			maxy = v.y
	return miny,maxy
#对边进行排序
def func(edge1,edge2):
	if edge1.x<edge2.x:
		return -1
	elif edge1.x==edge2.x:
		return 0
	else:
		return 1
#为新边表和活性表分配空间
def allocNET(miny,maxy):
	for y in range(miny,maxy+1):
		NET[y] = []
#将edge插入到以head为头的链表中，插入排序
def Insert2NET(key,edge):
	l = NET[key]
	for i in range(len(l)):
		if l[i].x>edge.x:
			l.insert(i,edge)
	l.append(edge) 

#初始化新边表
def InitNET():
	num = len(vList)
	current = num-1
	nextNode = 0
	while nextNode<num:
		#忽略水平线
		if vList[current].y==vList[nextNode].y:
			current = nextNode
			nextNode += 1
			continue
		if vList[current].y>vList[nextNode].y:
			minY = vList[nextNode].y
			maxY = vList[current].y
			x = vList[nextNode].x
		else:
			minY = vList[current].y
			maxY = vList[nextNode].y
			x = vList[current].x
		delta_x = (float)((vList[current].x-vList[nextNode].x)/(vList[current].y-vList[nextNode].y))
		edge = Edge(x,delta_x,maxY)
		Insert2NET(minY,edge)
		current = nextNode
		nextNode+=1
#将NET[i]中的边节点插入排序插入到AET中
def Insert2AET(AET,edgeList):
	length1 = len(AET)
	length2 = len(edgeList)

	if length1==0:
		AET += edgeList
		return 
	elif length2==0:
		return
	else:
		source = 0
		insert = 0
		while(insert<length2):
			while(source<len(AET) and AET[source].x<edgeList[insert].x):
				source+=1
			AET.insert(source,edgeList[insert])
			source+=1
			insert+=1
	AET = sorted(AET,key = cmp_to_key(func))

#给扫描线涂色
def FillLine(AET,y):
	if len(AET)==0:
		return 
	i=0
	while i<len(AET):
		if y==AET[i].maxy:
			i=i+1
			continue
		x = int(AET[i].x+0.5)
		endx = int(AET[i+1].x+0.5)
		glColor3f(1.0,0.0,0.0)
		glBegin(GL_POINTS)
		while x<=endx:
			glVertex2i(x,y)
			x+=1
		glEnd()
		glFlush()
		i = i+2

#更新AET
def updateAET(AET,y):
	for e in AET:
		if e.maxy<=y:
			AET.remove(e)
		else:
			e.x +=e.delta_x
	#对AET重新排序
	AET = sorted(AET,key = cmp_to_key(func))
	# for e in AET:
	# 	print('y:',y,e.x,e.delta_x,e.maxy)

#扫描线填充
def scanFill():
	AET = []
	miny,maxy = getMinMaxY(vList)
	# print('miny:{0},maxy:{1}'.format(miny,maxy))
	allocNET(miny,maxy)
	InitNET()
	#查看NET
	# for key in NET.keys():
	# 	for e in NET[key]:
	# 		print(key,e.x,e.delta_x,e.maxy)
	for y in range(miny,maxy):
		Insert2AET(AET,NET[y])
		AET = sorted(AET,key = cmp_to_key(func))
		FillLine(AET,y)
		updateAET(AET,y+1)

		
#鼠标左键点击选点
def OnMouse(button,state,x,y):
	if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
		vList.append(Vertex(x,500-y))
		print('({0},{1})'.format(x,500-y))
		drawPoints()
#键盘事件
def OnKeyboard(key,x,y):
	if key==b' ':
		drawPolygon()
	elif key==b'f':
		print(key)
		scanFill()

def display():
	glClearColor(1.0,1.0,1.0,0.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluOrtho2D(0.,500.0,0.0,500.0)
	# v = Vertex(20,20)
	# vList.append(v)
	# v = Vertex(50,10)
	# vList.append(v)
	# v = Vertex(110,30)
	# vList.append(v)
	# v = Vertex(110,80)
	# vList.append(v)
	# v = Vertex(50,50)
	# vList.append(v)
	# v = Vertex(20,70)
	# vList.append(v)
	# drawPoints()
	# drawPolygon()
	# scanFill()

if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(500,500)
	glutCreateWindow('ScanFill')

	glutDisplayFunc(display)
	glutMouseFunc(OnMouse)
	glutKeyboardFunc(OnKeyboard)
	glutMainLoop()
