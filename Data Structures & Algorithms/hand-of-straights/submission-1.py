from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)

        for i in range(1001):
            if i in c.keys():
                for j in range(i+1, i + groupSize):
                    if j not in c.keys():
                        return False
                    
                    if c[j] < c[i]:
                        return False

                    c[j] -= c[i]

                    if c[j] == 0:
                        del c[j]
                
                del c[i]

                if not c:
                    break

        return True