from heapq import *
from collections import defaultdict, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        schedule = []
        c = Counter(tasks)
        h = defaultdict(int, c)

        heap = [(-count, task) for task, count in c.items()]
        heapify(heap)

        i = 0
        while heap:
            count, task = heappop(heap)
            count = -count

            while count > 0:
                position = (h[task] - count) * (n + 1) + i
                count -= 1
                
                if len(schedule) <= position:
                    for _ in range(1 + position - len(schedule)):
                        schedule.append("")
                schedule[position] = task
        
            i += 1

        return max(len(tasks), len(schedule))