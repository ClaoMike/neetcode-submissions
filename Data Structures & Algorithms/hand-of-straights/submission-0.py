from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)

        for i in range(1001):
            if i in c.keys():
                
                groups = c[i]
                c[i] = 0
                del c[i]
                print(f"there are {groups} of {i}'s")
                for j in range(i+1, i + groupSize):
                    if j not in c.keys():
                        return False
                    
                    if c[j] < groups:
                        return False

                    print(f"there are {c[j]} of {j}'s")

                    c[j] -= groups

                    if c[j] == 0:
                        del c[j]

                print()
                print(c)
                print()

        return True