class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0, nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        prefix.append(0)

        for i in range(1, len(prefix)-1):
            if prefix[i-1] == prefix[-2] - prefix[i]:
                return i-1

        return -1