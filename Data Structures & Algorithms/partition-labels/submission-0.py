from collections import defaultdict, Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s = list(s)
        h = defaultdict(int)
        result = []

        c = Counter(s)

        for i in range(len(s)):
            h[s[i]] = i

        to_be_unlocked = set()
        group_size = 0
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