class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent, size = [], []
        count = n

        for i in range(n):
            parent.append(i)
            size.append(1)

        def find(x):
            nonlocal parent
            
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            nonlocal parent, size, count

            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:

                if size[root_y] > size[root_x]:
                    root_x, root_y = root_y, root_x
            
                parent[root_y] = root_x
                size[root_x] += size[root_y]
                count -= 1

        for a, b in edges:
            union(a, b)

        return count