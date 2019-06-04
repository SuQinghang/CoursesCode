'''
局部替换方法求解最小生成树
MST = []
for e in G.E:
    if MST.E+e不形成环:
        MST = MST+e
    else:
        MST = MST+e-e'
'''
import queue
import pysnooper
from Graph import Node,Linklist,Graph
from DisjointSet import DisjointSet

class edge():
    def __init__(self,u,v,weight):
        '''
        u,v为边的两个断点
        weight为边的权重
        '''
        self.u = u
        self.v = v
        self.w = weight

#寻找begin和end之间权重最大的边
def getMaxWeightEdge(V,E,begin,end):
    Plist = BFS(V,E,begin)
    child = end
    parent = Plist[child]
    MaxWeightEdge = edge(parent,child,E[parent].find(child).weight)
    while True:
        child=parent
        parent = Plist[child]
        if parent==None:
            return MaxWeightEdge
        node = E[parent].find(child)
        if node.weight>MaxWeightEdge.w:
            MaxWeightEdge = edge(parent,child,node.weight)
#用BFS找
def BFS(V,E,begin):
    Clist = {}
    Plist = {}
    for v in V:
        Clist[v]=0
        Plist[v]=None
    Clist[begin]=1
    #BFS
    q = queue.Queue()
    q.put(begin)
    while(not q.empty()):
        #print('while')
        u = q.get()
        #u的邻接链表
        curList = E[u]
        curNode = curList.head
        while curNode!=0:
            v = curNode.data
            if Clist[v]==0:
                Clist[v]=1
                Plist[v]=u
                q.put(v)
            curNode = curNode.next
    Clist[u]=2
    return Plist
#局部替换算法求最小生成树
def MST(G):
    '''
    图G
    '''
    V = G.V
    E = G.Adjlist

    MSTV = set()
    MSTE = {}
    Ds = DisjointSet(V)
    for v in V:
        MSTE[v]=Linklist()
    for u in MSTE.keys():
        curList = E[u]
        curNode = curList.head
        while(curNode!=0):
            v = curNode.data
            #使用并查集判断是否生成环
            #------------------------------------
            parentu = Ds.find(u)
            parentv = Ds.find(v)
            if parentu!=parentv:
                #不会生成环
                MSTV.add(u)
                MSTV.add(v)
                MSTE[u].pushback(Node(v,curNode.weight))
                MSTE[v].pushback(Node(u,curNode.weight))
                #合并两并查集
                Ds.union(parentu,parentv)
            else:
                #加入该边会生成环
                MaxWeightEdge = getMaxWeightEdge(MSTV,MSTE,u,v)
                if curNode.weight<MaxWeightEdge.w:
                    MSTE[MaxWeightEdge.u].remove(MaxWeightEdge.v)
                    MSTE[MaxWeightEdge.v].remove(MaxWeightEdge.u)
                    MSTE[u].pushback(Node(v,curNode.weight))
                    MSTE[v].pushback(Node(u,curNode.weight))
                    #合并
                    Ds.union(parentu,parentv)
            curNode = curNode.next

    return Graph(MSTV,None,MSTE,kind='nodirect')
                
if __name__ == '__main__':
    #main()
    V = ['A','B','C','D','E','F','G','H','I']
    # V = [1,2,3,4,5,6,7,8,9]
    edges = [["A", "B", 4], ["A", "H", 8],
             ["B", "C", 8], ["B", "H", 11],
             ["C", "D", 7], ["C", "F", 4],
             ["C", "I", 2], ["D", "E", 9],
             ["D", "F", 14], ["E", "F", 10],
             ["F", "G", 2], ["G", "H", 1],
             ["G", "I", 6], ["H", "I", 7]]
    Adjlist = {}
    for v in V:
        Adjlist[v] = Linklist()
    for e in edges:
        node = Node(e[1],e[2])
        Adjlist[e[0]].pushback(node)
        node = Node(e[0],e[2])
        Adjlist[e[1]].pushback(node)

    G = Graph(V,edges,kind='nodirect')
    G.show()
    print('---------------------')
    T = MST(G)
    T.show()
    