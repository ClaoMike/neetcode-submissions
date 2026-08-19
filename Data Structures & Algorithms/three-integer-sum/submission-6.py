class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fr = []
        i = 0
        nums.sort()

        print(nums)
        
        while i < len(nums)-2:
            left = i+1
            right = len(nums)-1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    r = [nums[i], nums[left], nums[right]]
                    fr.append(r)

                    while right > 0 and nums[right-1] == nums[right]:
                        right -= 1
                    right -= 1
                
                elif nums[i] + nums[left] + nums[right] > 0:
                    while right > 0 and nums[right-1] == nums[right]:
                        right -= 1
                    right -= 1
                else:
                    while left < len(nums) and nums[left+1] == nums[left]:
                        left += 1
                    left += 1

            while i < len(nums)-2 and nums[i+1] == nums[i]:
                i += 1
            i += 1

        return fr