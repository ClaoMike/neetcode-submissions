class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        from collections import defaultdict
        found = defaultdict(int)
        found[0] += 1

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        for i in range(len(prefix)):
            
            if prefix[i] - k in found:
                count += found[prefix[i] - k]

            found[prefix[i]] += 1
        
        return count