#利用DFS(Breadth-First Search)解决无权图单源最短路问题
#Problem：
#   input:graph G=(V,E)
#         source vertex s
#   output:shortest path 
#           distance
#TODO：使用三个数组Clist,Dlist,Plist存放顶点的三个属性

import math

#图
class Graph(object):
    def __init__(self,V,Adjlist):
        self.V = V
        self.Adjlist = Adjlist    

#递归DFS
#White 0 Gray 1 Black 2
def DFS(graph):
    Vlist = graph.V
    Clist = {}
    Dlist = {}
    Flist = {}
    Plist = {}
    BackEdge = {}
    for v in Vlist:
        Clist[v]=0
        Dlist[v]=0
        Flist[v]=0
        Plist[v]=None
    time = 0
    for v in Clist.keys():
        if Clist[v]==0:
            DFS_visit(v,Clist,Dlist,Flist,Plist,graph.Adjlist,BackEdge,time)
    return BackEdge
def DFS_visit(u,Clist,Dlist,Flist,Plist,Adjlist,BackEdge,time):
    time = time+1
    Dlist[u] = time
    Clist[u] = 1
    curList = Adjlist[u]
    for v in curList:
        if Clist[v]==0:
            Plist[v]=u
            time = DFS_visit(v,Clist,Dlist,Flist,Plist,Adjlist,BackEdge,time)
        elif Clist[v]==1:
            curList.remove(v)
            if u in BackEdge:
                BackEdge[u].append(v)
            else:
                BackEdge[u] = [v]
    Clist[u] = 2
    time = time+1
    Flist[u] = time
    return time

if __name__=='__main__':
    #初始化图
    V = [1,2,3,4,5]
    Adjlist = {}
    Adjlist[1] = [2,4]
    Adjlist[2] = [3]
    Adjlist[3] = [1,4]
    Adjlist[4] = [5]
    Adjlist[5] = [1]

    graph = Graph(V,Adjlist)
    
    DFS(graph)
    for key in graph.Adjlist.keys():
        print('{0}:{1}'.format(key,graph.Adjlist[key]))
