class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphabetic(c):
            return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'

        left = 0
        right = len(s) -1

        while left < right:
            if not isAlphabetic(s[left]):
                left += 1
                continue
            
            if not isAlphabetic(s[right]):
                right -= 1
                continue

                print(s[left])
                print(s[right])

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    