class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        traveller = nums[0]

        while True:
            t = traveller
            traveller = nums[traveller]
            nums[t] = -1
            if traveller == -1:
                return t