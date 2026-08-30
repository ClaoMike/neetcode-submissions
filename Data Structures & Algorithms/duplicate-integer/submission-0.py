class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        
        c = Counter(nums)
        for value in c.values():
            if value > 1:
                return True
        
        return False