class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import defaultdict
        
        frequency = defaultdict(int)
        permutation = defaultdict(int)
        for c in s1:
            permutation[c] += 1

        left = 0
        right = len(s1)-1

        for i in range(len(s1)-1):
            if s2[i] in permutation:
               frequency[s2[i]] += 1

        while right < len(s2):
            print(s2[left:right])
            print(s2[right])
            if s2[right] in permutation:
                frequency[s2[right]] += 1
                print(frequency)

                if frequency == permutation:
                    return True
            
            if s2[left] in permutation:
                frequency[s2[left]] -= 1
            print(frequency)
            left += 1
            right += 1

                    
        return False