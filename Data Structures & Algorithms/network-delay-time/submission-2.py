from collections import defaultdict, deque
from heapq import *
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        timess, dist = defaultdict(int), defaultdict(int)
        pq = []

        for i in range(1, n+1):
            graph[i] = set()

        for time in times:
            x, y, t = time
            graph[x].add(y)
            timess[(x, y)] = t

        times = timess
        
        for node in graph.keys():
            dist[node] = math.inf
        dist[k] = 0

        heappush(pq, (0, k) )
        while pq:
            distance, node = heappop(pq)

            if distance > dist[node]:
                continue

            for neighbour in graph[node]:
                new_dist = distance + times[(node, neighbour)]
                
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    heappush(pq, (new_dist, neighbour))
        
        total = max(dist.values())
        if total == math.inf:
            return -1
        
        return total