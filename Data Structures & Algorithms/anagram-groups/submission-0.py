class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        h = defaultdict(list)

        for s in strs:
            h["".join(sorted(s))].append(s)

        return list(h.values())