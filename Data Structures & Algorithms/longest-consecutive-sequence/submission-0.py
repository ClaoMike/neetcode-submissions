class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import Counter

        longest = 0
        c = Counter(nums)

        for key in c.keys():
            if key - 1 not in c:
                sequenceable = key
                curr = 1
                c[sequenceable] = 0
                # c.pop(sequenceable)

                while sequenceable + 1 in c and c[sequenceable+1] != 0:
                    curr += 1
                    sequenceable += 1
                    # c.pop(sequenceable)

                if curr > longest:
                    longest = curr

        return longest