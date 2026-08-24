class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        print(prefix)

        from collections import defaultdict
        hm = defaultdict(int)
        hm[0] = 1

        for i in range(len(prefix)):
            remainder = prefix[i] % k
            if remainder in hm:
                count += hm[remainder]
            
            hm[remainder] += 1
        
        print(hm)

        return count