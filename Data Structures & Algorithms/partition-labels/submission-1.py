from collections import defaultdict, Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        group_size = 0
        result = []
        to_be_unlocked = set()
        h = defaultdict(int)
        
        s = list(s)
        c = Counter(s)

        for i in range(len(s)):
            h[s[i]] = i
        
        for i in range(len(s)):
            if h[s[i]] == i:
                to_be_unlocked.discard(s[i])
                group_size += c[s[i]]

                if not to_be_unlocked:
                    result.append(group_size)
                    group_size = 0
                
            else:
                to_be_unlocked.add(s[i])

        return result