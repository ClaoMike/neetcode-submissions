from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result, stack = [], ["JFK"]
        graph = defaultdict(list)

        for source, destination in tickets:
            graph[source].append(destination)

        for source, destinations in graph.items():
            destinations.sort(reverse=True)

        while stack:
            stack.append(graph[stack[-1]].pop()) if graph[stack[-1]] else result.append(stack.pop())

        result.reverse()

        return result