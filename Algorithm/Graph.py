#节点
class Node(object):
    def __init__(self,vertex,w=1,p=0):
        self.data = vertex
        self.weight = w
        self.next = p
#链表
class Linklist(object):
    def __init__(self):
        self.head=0
    def initList(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p=p.next
    def pushback(self,node):
        if self.head==0:
            self.head = node
        else:
            current = self.head
            nextNode = current.next
            while nextNode!=0:
                current = nextNode
                nextNode = current.next
            current.next = node
    def find(self,v):
        if self.head==0:
            return None
        else:
            curNode = self.head
            nextNode = curNode.next
            while True:
                if curNode.data==v:
                    return curNode
                else:
                    curNode = nextNode
                    if curNode==0:
                        break
                    else:
                        nextNode = curNode.next
            return None
    def remove(self,v):
        if self.head==0:
            return 
        else:
            if self.head.data==v:
                removeNode = self.head
                nextNode = self.head.next
                self.head = nextNode
                del removeNode
                return 
            else:
                current  = self.head
                nextNode = current.next
                while nextNode!=0:
                    if nextNode.data==v:
                        removeNode = nextNode
                        current.next = nextNode.next
                        del removeNode
                        return
                    current = nextNode
                    nextNode = current.next
    def show(self):
        node = self.head
        while not node ==0:
            print(node.data,node.weight,end=', ')
            node = node.next
        print()

#图
class Graph(object):
    def __init__(self,V,edges,Adjlist=None,kind='direct'):
        '''
        V=[v1,v2,v3,...,vk]为图的顶点集
        edges = [[v1,v2,w1],[v1,v3,w2]...]为图的边集
        Adjlist 为邻接链表
        kind为创建图的类型，默认为无向图
        '''
        self.V = V
        self.kind=kind
        if Adjlist != None:
            self.Adjlist=Adjlist
        else:
            self.Adjlist = {}
            #初始化邻接链表
            for v in V:
                self.Adjlist[v] = Linklist()
            #将边加入邻接链表
            for e in edges:
                node = Node(e[1],e[2])
                self.Adjlist[e[0]].pushback(node)
                if kind == 'nodirect':
                    node = Node(e[0],e[2])
                    self.Adjlist[e[1]].pushback(node)
    def show(self):
        print('顶点:',self.V)
        print('邻接链表：')
        for v in self.V:
            print('{0}:'.format(v),end=' ')
            curList = self.Adjlist[v]
            curNode = curList.head
            while curNode!=0:
                print('({0},{1})'.format(curNode.data,curNode.weight),end=' ')
                curNode = curNode.next
            print()