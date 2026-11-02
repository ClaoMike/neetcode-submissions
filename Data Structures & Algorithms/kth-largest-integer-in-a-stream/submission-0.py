from heapq import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = [-x for x in nums]
        heapify(self.nums)

        self.k = k

    def add(self, val: int) -> int:
        heappush(self.nums, -val)

        result = None
        temporary = []
        i = 1
        while i < self.k:
            temporary.append(heappop(self.nums))
            i += 1
        
        result = -self.nums[0]

        while temporary:
            heappush(self.nums, temporary.pop())

        return result