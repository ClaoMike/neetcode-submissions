from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)

        for source, destinations in graph.items():
            destinations.sort()
            destinations.reverse()
            graph[source] = destinations

        result, stack = [], []
        stack.append("JFK")

        while stack:
            airport = stack[-1]
            if graph[airport]:
                stack.append(graph[airport].pop())
            else:
                result.append(stack.pop())

        result.reverse()

        return result