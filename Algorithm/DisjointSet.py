#并查集
class DisjointSet():
    id = {}
    def __init__(self,V):
        for v in V:
            self.id[v]=v
    def find(self,v):
        parent = self.id[v]
        while parent!=self.id[parent]:
            parent = self.id[parent]
        return parent
    def union(self,parent1,parent2):
        self.id[parent2] = self.id[parent1]
    def show(self):
        print(self.id)