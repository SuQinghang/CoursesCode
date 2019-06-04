from Graph import *
import copy
def f(u,s,V,E):
    '''
    返回从u出发，恰好经过V中所有点一次回到s的最佳路线长度
    '''
    #print('求{0}到顶点集V{1}的最短路径'.format(u,V))
    curList = E[u]
    if len(V)==0:
        #由u直接到达s
        node = Node(s)
        node = Node(u,0,node)
        return curList.find(s).weight,node
    else:
        weights = []
        count = 0
        nodeList = []
        for v in V:
            #print('当前u:{0},V:{1}:'.format(u,V))
            tempV = copy.deepcopy(V)

            if(curList.find(v)):
                count+=1
                tempV.remove(v)
                w,node = f(v,s,tempV,E)
                nodeList.append(node)
                weights.append(curList.find(v).weight+w)
            else:
                weights.append(float('inf'))
                nodeList.append(None)

        #找最小权重
        minweight = min(weights)
        index = weights.index(minweight)
        node = Node(u,0,nodeList[index])
        return minweight,node
        
def TSP(G):
    V = G.V
    E = G.Adjlist
    s = V[0]
    Path = []
    Path.append(s)
    V.remove(s)
    w,node = f(s,s,V,E)
    print(w)
    while node!=0:
        print(node.data)
        node = node.next



if __name__ == "__main__":
    #构造有向加权完全图
    V = [1,2,3,4,5]
    edges = [[1,2,1],[2,1,2],[2,3,9],[3,2,10],[2,4,5],[4,2,7],[1,4,6],[4,1,2],
                [1,5,9],[5,1,7],[1,3,4],[3,1,4],[2,5,11],[5,2,6],[3,4,4],[4,3,2],
                [3,5,4],[5,3,5],[4,5,8],[5,4,1]]
    #有向加权完全图相当于无向加权完全图
    G = Graph(V,edges,None,kind='direct')
    G.show()
    TSP(G)