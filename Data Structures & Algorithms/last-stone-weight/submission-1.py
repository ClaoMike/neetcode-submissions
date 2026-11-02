from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            x = -heappop(stones)
            y = -heappop(stones)

            if x==y:
                continue

            heappush(stones, -abs(x-y))

        if not stones:
            return 0
            
        return -stones[0]