//
// Created by subuntu on 19-4-16.
//

#include <GL/glut.h>
#include <vector>
#include <math.h>
#include <iostream>
using namespace std;


class Vertex{
public:
    float x;
    float y;
};

vector<Vertex> vlist;
//阶乘
int factorial(int n){
    if (n<=1){
        return 1;
    }else{
        return n*factorial(n-1);
    }
}
//求C(i,n)
int C(int i,int n){
    return factorial(n)/(factorial(i)*factorial(n-i));
}
//显示vlist
void showvlist(){
    cout<<"-------------------------------------"<<endl;
    for(int i=0;i<vlist.size();i++){
        cout<<"("<<vlist[i].x<<","<<vlist[i].y<<")"<<endl;
    }
    cout<<"-------------------------------------"<<endl;
}

//将一个顶点加入到vlist中
void InsertVtoList(Vertex v){
    int len = vlist.size();
    if(len==0){
        vlist.push_back(v);
        return;
    }else{
        for(int i=0;i<len;i++){
            if(vlist[i].x>v.x){
                vlist.insert(vlist.begin()+i,v);
                return;
            }
            if(vlist[i].x==v.x){
                return;
            }
        }
        vlist.push_back(v);
    }
}
//n个顶点的参数方程
//vlist必须是按照x递增顺序排列
Vertex ParamaterFunction(float t){
    int n = vlist.size();
    Vertex v;
    v.x=0;
    v.y=0;
    for(int i=0;i<n;i++){
        v.x+=C(i,n)*vlist[i].x*pow(1-t,n-i)*pow(t,i);
        v.y+=C(i,n)*vlist[i].y*pow(1-t,n-i)*pow(t,i);
    }
    return v;
}
//绘制曲线
void drawCurve(){
    glColor3f(0.0,1.0,0.0);
    glBegin(GL_LINE_STRIP);
    for(float t=0.1;t<1;t+=0.1){
        Vertex v;
        v = ParamaterFunction(t);
        glVertex2f(v.x,v.y);
    }
    glEnd();
    glFlush();
}
//鼠标左键点击窗口选点显示
//鼠标右键点击某个点则将该点在vlist中删除
void OnClick(int button,int state,int x,int y){
    if(button==GLUT_LEFT_BUTTON){
        if(state==GLUT_DOWN){
            //显示点
            glColor3f(1.0,0.0,0.0);
            glPointSize(4.0);
            glBegin(GL_POINTS);
            glVertex2f(x,400-y);
            glEnd();
            glFlush();
            cout<<"left click:("<<x<<","<<y<<")"<<endl;
            //把点加入到vlist
            Vertex v;
            v.x = x;
            v.y = y;
            InsertVtoList(v);
            showvlist();
            drawCurve();
        }
    }
    else if(button==GLUT_RIGHT_BUTTON){
        if(state==GLUT_DOWN){
            cout<<"right click:("<<x<<","<<y<<")"<<endl;
            int flag=0;//0表示未做更改
            for(int i=0;i<vlist.size();i++){
                if(vlist[i].x>x+2){
                    break;
                }
                if(sqrt((pow(vlist[i].x-x,2))+pow(vlist[i].y-y,2))<2){
                    vlist.erase(vlist.begin()+i);
                    flag=1;
                    break;
                }
            }
            if(flag==1){
                cout<<"refresh"<<endl;
                glClearColor(0.0,0.0,0.0,1.0);
                glClear(GL_COLOR_BUFFER_BIT);
                glColor3f(1.0,0.0,0.0);
                glPointSize(4.0);
                glBegin(GL_POINTS);
                for(int i=0;i<vlist.size();i++){
                    glVertex2f(vlist[i].x,400-vlist[i].y);
                }
                glEnd();
                glFlush();

            }
        }
    }
}
void init() {
    glClearColor(0.0, 0.0, 0.0,1.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluOrtho2D(0, 400, 0, 400);
}

void display(void){

}
int main(int argc,char **argv){
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_DEPTH|GLUT_SINGLE|GLUT_RGBA);

    glutInitWindowPosition(100,100);
    glutInitWindowSize(400,400);
    glutCreateWindow("BezierCurve");
    init();
    glutDisplayFunc(display);
    glutMouseFunc(OnClick);
    glutMainLoop();
    return 0;
}
