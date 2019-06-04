#利用DFS求一个连通无向图的各点，衔接点
#图G的衔接点：u
#u为根节点，且u有两个及以上子节点
#u为非根节点，u的后代没有到u的父亲的后向边

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
    Low = {}
    for v in Vlist:
        Clist[v]=0
        Dlist[v]=0
        Flist[v]=0
        Plist[v]=None
        Low[v]=0
    time = 0
    for v in Clist.keys():
        if Clist[v]==0:
            DFS_visit(v,Clist,Dlist,Plist,Low,graph.Adjlist,time)
    # print('D:',Dlist)
    # print('Low:',Low)
def DFS_visit(u,Clist,Dlist,Plist,Low,Adjlist,time):
    time = time+1
    Dlist[u] = time
    Clist[u] = 1
    Low[u] = time
    curList = Adjlist[u]
    children = 0
    for v in curList:
        #树边
        if Clist[v]==0:
            children+=1
            Plist[v]=u
            time = DFS_visit(v,Clist,Dlist,Plist,Low,Adjlist,time)
            Low[u] = min(Low[u],Low[v])
            # print('set {0}.low={1}'.format(u,Low[u]))
            #若u是根节点且子节点大于等于2
            if Plist[u]==None and children>=2:
                print('{} is a cut point!'.format(u))
            #u非根节点且子节点后向边
            if Plist[u]!=None and Low[v]>=Dlist[u]:
                print('{} is a cut point!'.format(u))
        else:
            if Plist[u]!=v:
                Low[u] = min(Low[u],Dlist[v])
                # print('set {0}.low={1}'.format(u,Low[u]))
    Clist[u] = 2
    return time

if __name__=='__main__':
    #初始化图
    # V = ['a','b','c','d','e','f','g','h','i','j','k','l']
    V = [0,1,2,3,4,5,6]
    Adjlist = {}
    Adjlist[0] = [1]
    Adjlist[1] = [0,2,3]
    Adjlist[2] = [1,3,4,6]
    Adjlist[3] = [1,2,4,5]
    Adjlist[4] = [2,3,5]
    Adjlist[5] = [3,4]
    Adjlist[6] = [2]
    # Adjlist['a'] = ['b']
    # Adjlist['b'] = ['c','j']
    # Adjlist['c'] = ['b','d']
    # Adjlist['d'] = ['c','e','i']
    # Adjlist['e'] = ['d','f','k']
    # Adjlist['f'] = ['e','g','h']
    # Adjlist['g'] = ['f','h']
    # Adjlist['h'] = ['f','g','i','j']
    # Adjlist['i'] = ['d','h']
    # Adjlist['j'] = ['b','h']
    # Adjlist['k'] = ['e','l']
    # Adjlist['l'] = ['k']

    graph = Graph(V,Adjlist)
    DFS(graph)
