#include "pch.h"
#include "ObjLoader.h"
#include <iostream>
#include <GL\glut.h>

using namespace std;

//读取OBJ文件
//-------------------------------------
//obj文件路径
string filePath = "cube.obj";
ObjLoader objModel = ObjLoader(filePath);

//设置移动鼠标观察模型所需变量
static float c = 3.1415926 / 180.0f;
static float r = 1.0f;
static int degree = 90;
static int oldPosX = -1;
static int oldPosY = -1;

//安置光源
void setLightRes() {
	GLfloat lightPosition[] = { 0.0f,0.0f,1.0f,0.0f };
	glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);
	glEnable(GL_LIGHTING);//启用光源
	glEnable(GL_LIGHT0);//使用指定灯光
}
//初始化
void init() {
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
	glutCreateWindow("ObjLoader");
	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_SMOOTH);
	setLightRes();
	glEnable(GL_DEPTH_TEST);
}
//显示
void display() {
	glColor3f(1.0, 1.0, 1.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(0.0f, 0.0f, -5.0f);
	setLightRes();
	glPushMatrix();

	gluLookAt(r*cos(c*degree), 0, r*sin(c*degree), 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 1.0f);

	objModel.Draw();//绘制obj模型
	glPopMatrix();
	glutSwapBuffers();
}
void reshape(int width, int height) {
	glViewport(0, 0, width, height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(60.0f, (GLdouble)width / (GLdouble)height, 1.0f, 200.0f);
	glMatrixMode(GL_MODELVIEW);
}
//移动鼠标
void mouseMove(int button, int state, int x, int y) {
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
		oldPosX = x;
		oldPosY = y;
	}
}
//改变视角
void changeViewPoint(int x, int y) {
	int temp = x - oldPosX;
	degree += temp;
	oldPosX = x;
	oldPosY = y;
}
void myIdle() {
	glutPostRedisplay();
}

int main(int argc, char* argv[])
{
	glutInit(&argc, argv);
	init();
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMouseFunc(mouseMove);
	glutMotionFunc(changeViewPoint);
	glutIdleFunc(myIdle);
	glutMainLoop();

	return 0;
}
//--------------------------------------

