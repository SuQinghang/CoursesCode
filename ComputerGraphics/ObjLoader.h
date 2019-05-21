#pragma once
#include<GL\glut.h>
#include <vector>
#include<string>
using namespace std;
class ObjLoader {
public:
	ObjLoader(string filename);//构造函数
	void Draw();//绘制函数
private:
	vector<vector<GLfloat> >vSets;//顶点坐标
	vector<vector<GLint> >fSets;//面的三个顶点序列
};