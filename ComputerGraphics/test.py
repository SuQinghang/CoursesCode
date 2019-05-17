import numpy as np 
from BSplineCurve import *
import matplotlib.pyplot as plt
def curve(vList, N, k, param, knot):
    '''
    Calculate B-spline curve.
    :param P: Control points
    :param N: the number of control points
    :param k: degree
    :param param: parameters
    :param knot: knot vector
    :return: data point on the b-spline curve
    '''
    Nik = np.zeros((len(param), N))

    for i in range(len(param)):
        for j in range(N):
            Nik[i][j] = basisFunc(param[i],j,k+1,knot)
    Nik[len(param)-1][N - 1] = 1
    #print(Nik)
    # D = np.dot(Nik, P)
    D = []
    P = []
    for p in vList:
        P.append([p.x,p.y])
    P = np.array(P)
    print(np.shape(P))
    print(np.shape(Nik))
    print('----------------------')
    D  = np.dot(Nik,P).tolist()
    X = []
    Y = []
    for d in D:
        X.append(d[0])
        Y.append(d[1])
    #print(X)
    #plt.plot(X,Y)
    P = P.tolist()
    PX = []
    PY = []
    for p in P:
        PX.append(p[0])
        PY.append(p[1])
    plt.plot(PX,PY)
    plt.plot(X,Y)
    plt.show()
    
    # for i in range(len(P)):
    #     D.append(np.dot(Nik, P).tolist())
    # # print(D)
    # return D

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


v = Vertex(20,20)
vList.append(v)
v = Vertex(30,100)
vList.append(v)
v = Vertex(40,30)
vList.append(v)
v = Vertex(50,40)
vList.append(v)
v = Vertex(50,40)
vList.append(v)
v = Vertex(60,20)
vList.append(v)
v = Vertex(70,50)
vList.append(v)
v = Vertex(80,90)
vList.append(v)
n = len(vList)-1
print('n:',n)
k = 4#曲线阶数
knot = np.linspace(1,n+k+1,n+k+1)#节点向量
print(knot)
start = knot[k-1]
end = knot[n+1]
print(start,end)
T = np.linspace(start,end,500)#数据点
print(T)
print(np.where(8>=knot)[0][-1])
X = []
Y = []
for t in T[:-1]:
    #寻找t所在的区间
    j = np.where(t>=knot)[0][-1]
    #j = np.where(knot==index)[0][0]
    print(j)
    x,y = deBoor(vList,j,k-1,k,t,knot)
    #print('({0},{1})'.format(x,y))
    X.append(x)
    Y.append(y)
print(X)
VX = []
VY = []
for v in vList:
    VX.append(v.x)
    VY.append(v.y)
plt.plot(VX,VY)
plt.plot(X,Y)
plt.show()