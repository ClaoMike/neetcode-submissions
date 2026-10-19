from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check if graph is connected
        if len(edges) != n-1:
            return False

        # check if graph is acyclic
        class UnionFind:
            def __init__(self, n):
                self.parent = []
                self.size = []

                for i in range(n):
                    self.parent.append(i)
                    self.size.append(1)

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return False # already conencted

                if self.size[root_x] < self.size[root_y]:
                    root_x, root_y = root_y, root_x

                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]

                return True

        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        
        return True