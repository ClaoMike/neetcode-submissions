from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [ (x**2 + y**2, [x, y]) for [x, y] in points]
        heapify(points)

        result = []
        while k > 0:
            _, point = heappop(points)
            result.append(point)
            k -= 1

        return result