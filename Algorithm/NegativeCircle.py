'''
在有向图中寻找一个负圈
'''

from Graph import *
from DisjointSet import *
def FindNegativeCircle(G):
    '''
    有向图G
    返回一个负圈
    '''
    V = G.V
    E = G.Adjlist
    #---------------------------------------------
    #采用寻找圈方法
    Ds = DisjointSet(V)
    for u in E.keys():
        curList = E[u]
        curNode = curList.head
        while curNode!=0:
            v = curNode.data
            parentU = Ds.find(u)
            parentV = Ds.find(v)
            if parentU == parentV:
                #生成环,找v->u的所有路径的权重
                findPath(v,u,V,E,curNode.weight)
            else:
                #在不同的树中，这条边不会产生环
                Ds.union(parentU,parentV)
            curNode = curNode.next

def findPath(begin,end,V,E,w):
    '''
    寻找以V为顶点集,E为邻接链表的图中，从begin->end的所有路径
    w为end->begin的路径权重
    '''
    #标记某个点是否被访问过
    Mark = {}
    for v in V:
        Mark[v] = 0
    Mark[begin]=1
    stack = []
    stack.append(begin)
    while len(stack)!=0:
        flag = 0
        u = stack[-1]
        curList = E[u]
        curNode = curList.head
        while curNode!=0:
            v = curNode.data
            if Mark[v]==0:
                stack.append(v)
                Mark[v] = 1
                #发现终点
                if v==end:
                    #判断stack中表示的路径权重是否为负
                    if isNegativeCircle(begin,end,w,E,stack):
                        print('发现一条从{0}到{1}的负圈{2}'.format(begin,end,stack))
                    stack.pop(-1)
                    Mark[v]=0
                    curNode = curNode.next
                    continue
                flag=1
                break
            curNode = curNode.next
        if flag==1:
            continue
        else:
            stack.pop(-1)


def isNegativeCircle(begin,end,w,E,Path):
    '''
    begin,end为图中两顶点
    w为end->begin边的权重
    E为图的邻接链表
    Path为从begin->end的路径，不包含end->begin
    '''
    SumWeight = w
    for i in range(len(Path)-1):
        SumWeight+=E[Path[i]].find(Path[i+1]).weight
    if SumWeight<0:
        return True
    else:
        return False


if __name__ == "__main__":
    V = [1,2,3,4,5]
    # edges = [['A','B',1],['B','C',4],['C','D',2],
    #         ['D','E',3],['D','F',7],['E','C',-6],['F','A',-3]]
    # edges = [['A','B',1],['B','C',2],['B','D',3],['C','A',-2],
    #             ['D','E',3],['E','B',-7],['E','C',-6]]
    edges = [[1,2,3],[1,3,8],[1,5,-4],[2,1,-2],[2,4,1],[2,5,7],[3,2,4],
            [4,1,2],[4,3,-5],[5,4,6]]
    G = Graph(V,edges=edges,kind='direct')
    G.show()
    # findPath('C','E',G.V,G.Adjlist,1)
    FindNegativeCircle(G)