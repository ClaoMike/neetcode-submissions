from heapq import *
from collections import defaultdict, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

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

                # print(f"i: {i}")
                # print(f"position: {position}")
                # print(f"schedule: {schedule}")
                # print(f"we need {1 + position - len(schedule)} more spaces")
                
                if len(schedule) <= position:
                    for _ in range(1 + position - len(schedule)):
                        schedule.append("")
                schedule[position] = task

                # print(schedule)
        
            i += 1

        # return len(schedule)
        return max(len(tasks), len(schedule))