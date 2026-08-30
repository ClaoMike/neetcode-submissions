class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        h = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in h and i != h[target - nums[i]]:
                return [h[target - nums[i]], i]
            
            h[nums[i]] = i
