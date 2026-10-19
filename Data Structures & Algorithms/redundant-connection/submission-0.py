class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent, size = [], []

        for a, b in edges:
            while a > len(parent)-1:
                parent.append(0)
                size.append(1)

            while b > len(parent)-1:
                parent.append(0)
                size.append(1)
        
        for a, b in edges:
            parent[a] = a
            parent[b] = b

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return [x, y]
            
            if size[root_y] > size[root_x]:
                root_x, root_y = root_y, root_x

            parent[root_y] = root_x
            size[root_x] += size[root_y]
            return None

        for a, b in edges:
            r = union(a, b)
            if r:
                return r