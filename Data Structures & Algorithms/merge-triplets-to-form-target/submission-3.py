from collections import deque

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target = (target[0], target[1], target[2])
        triplets = set([ (item[0], item[1], item[2]) for item in triplets])

        non_valids = []
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                non_valids.append(t)

        for non_valid in non_valids:
            triplets.discard(non_valid)

        if not triplets:
            return False

        triplets = deque(triplets)
        state = triplets.popleft()
        if state == target:
            return True

        while triplets:
            curr = triplets.popleft()
            state = (max(state[0], curr[0]), max(state[1], curr[1]), max(state[2], curr[2]))

            if state == target:
                return True

        return False