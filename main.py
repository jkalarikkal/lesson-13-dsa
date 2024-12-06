from collections import defaultdict as dd


class Graph:
    def __init__(self):
        self.graph = dd(list)

    def addEdge(self, u ,v):
        self.graph[u].append(v)

    def DFS12(self,v, visited):

        visited.add(v)
        print(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS12(neighbour, visited)

    def DFS(self, v):

        visited = set()
        self.DFS12(v, visited)


g = Graph()
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(0,1)

print("here is DFSSSSS - from v2")

g.DFS(2)