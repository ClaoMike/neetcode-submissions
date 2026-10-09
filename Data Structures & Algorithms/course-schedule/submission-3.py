from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        queue = deque()
        order, indegree = [], []

        for i in range(numCourses):
            graph[i] = set()
            indegree.append(0)

        for courseA, courseB in prerequisites:
            graph[courseA].add(courseB)
            indegree[courseB] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbour in graph[course]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(order) == numCourses:
            return True

        return False