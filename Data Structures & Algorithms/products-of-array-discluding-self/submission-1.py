class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix_left = [1]
        prefix_right = [1]

        for i in range(1, len(nums)):
            prefix_left.append(prefix_left[i-1] * nums[i-1])
        
        for i in reversed(range(1, len(nums))):
            prefix_right.append(prefix_right[-1] * nums[i])
        prefix_right = list(reversed(prefix_right))

        for i in range(len(nums)):
            output.append( prefix_left[i] * prefix_right[i] )
        
        return output