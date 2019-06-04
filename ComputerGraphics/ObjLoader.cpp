#include "ObjLoader.h"
#include <fstream>
#include <iostream>
using namespace std;
ObjLoader::ObjLoader(string filename) {
	string line;
	fstream f;
	f.open(filename, ios::in);
	if (!f.is_open()) {
		cout << "File can't Open" << endl;
	}
	while (!f.eof()) {
		getline(f, line);//读取obj文件中的一行，作为字符串
		vector<string>paramaters;
		string tailMark = " ";
		string ans = "";

		line = line.append(tailMark);
		for (int i = 0; i < line.length(); i++) {
			char ch = line[i];
			if (ch != ' ') {
				ans += ch;
			}else {
				paramaters.push_back(ans);
				ans = "";
			}
		}
		if (paramaters.size() != 4) {
			cout << "The Size is not correct!" << endl;
		}
		else {
			if (paramaters[0] == "v") {
				//顶点
				vector<GLfloat>Point;
				for (int i = 1; i < 4; i++) {
					GLfloat xyz = atof(paramaters[i].c_str());
					cout << "XYZ:" << xyz << endl;
					Point.push_back(xyz);
				}
				vSets.push_back(Point);
			}
			else if (paramaters[0] == "f") {
				vector<GLint>vIndexSets;
				for (int i = 1; i < 4; i++) {
					string x = paramaters[i];
					string ans = "";
					for (int j = 0; j < x.length(); j++) {
						char ch = x[j];
						if (ch != '/') {//不关注'/'
							ans += ch;
						}
						else {
							break;
						}
					}
					GLint index = atof(ans.c_str());
					index = index--;//顶点在vset中从0开始
					vIndexSets.push_back(index);
				}
				fSets.push_back(vIndexSets);
			}
		}
	}
		f.close();
}
void ObjLoader::Draw(){
	glBegin(GL_TRIANGLES);
	for (int i = 0; i < fSets.size(); i++) {
		GLfloat VN[3];//法向量
		GLfloat SV1[3];
		GLfloat SV2[3];
		GLfloat SV3[3];

		if (fSets[i].size() != 3) {
			cout << "The face" << i << "'s size is not correct" << endl;
		}
		else {
			//三个顶点的索引
			GLint firstVertexIndex = fSets[i][0];
			GLint secondVertexIndex = fSets[i][1];
			GLint thirdVertexIndex = fSets[i][2];
			//补充三个顶点的坐标
			SV1[0] = vSets[firstVertexIndex][0];
			SV1[1] = vSets[firstVertexIndex][1];
			SV1[2] = vSets[firstVertexIndex][2];

			SV2[0] = vSets[secondVertexIndex][0];
			SV2[1] = vSets[secondVertexIndex][1];
			SV2[2] = vSets[secondVertexIndex][2];

			SV3[0] = vSets[thirdVertexIndex][0];
			SV3[1] = vSets[thirdVertexIndex][1];
			SV3[2] = vSets[thirdVertexIndex][2];
			//求三角面片法向量
			GLfloat vec1[3], vec2[3], vec3[3];
			//向量一
			vec1[0] = SV1[0] - SV2[0];
			vec1[1] = SV1[1] - SV2[1];
			vec1[2] = SV1[2] - SV2[2];
			//向量二
			vec2[0] = SV1[0] - SV3[0];
			vec2[1] = SV1[1] - SV3[1];
			vec2[2] = SV1[2] - SV3[2];
			//叉乘
			vec3[0] = vec1[1] * vec2[2] - vec1[2] * vec2[1];
			vec3[1] = vec2[0] * vec1[2] - vec2[2] * vec1[0];
			vec3[2] = vec2[1] * vec1[0] - vec2[0] * vec1[1];
			GLfloat D = sqrt(pow(vec3[0], 2) + pow(vec3[1], 2) + pow(vec3[2], 2));

			VN[0] = vec3[0] / D;
			VN[1] = vec3[1] / D;
			VN[2] = vec3[2] / D;

			glNormal3f(VN[0], VN[1], VN[2]);//绘制法向量

			glVertex3f(SV1[0], SV1[1], SV1[2]);
			glVertex3f(SV2[0], SV2[1], SV2[2]);
			glVertex3f(SV3[0], SV3[1], SV3[2]);
  
		}
	}
	glEnd();
}