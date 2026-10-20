from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_as_tuples = []
        for x, y in points:
            points_as_tuples.append( (x, y) )
        points = points_as_tuples

        def getManhattanDistance(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])

        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append( ( points[i], points[j], getManhattanDistance(points[i], points[j]) ) )

        edges.sort(key=lambda e: e[2])

        parents = defaultdict(tuple)
        size = defaultdict(int)
        for point in points:
            parents[point] = point
            size[point] = 1

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])

            return parents[x]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:

                if size[root_v] > size[root_u]:
                    root_u, root_v = root_v, root_u

                parents[root_v] = root_u
                size[root_u] += size[root_v]

        mst = []
        for u, v, w in edges:
            if find(u) != find(v):
                mst.append(w)
                union(u, v)
                if len(mst) == len(points)-1:
                    break

        return sum(mst)