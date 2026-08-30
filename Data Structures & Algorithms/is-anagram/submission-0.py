class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        cs = Counter(s)
        ct = Counter(t)

        return ct == cs