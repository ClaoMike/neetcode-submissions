from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = []
        order = []
        queue = deque()

        for i in range(numCourses):
            graph[i] = set()
            indegree.append(0)
        
        for a, b in prerequisites:
            graph[b].add(a)
            indegree[a] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            
            order.append(node)

            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(order) != numCourses:
            return []

        return order