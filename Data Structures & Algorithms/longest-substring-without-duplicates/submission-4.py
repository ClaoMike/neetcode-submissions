class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = length_of_longest_substring = length = 0
        visited = set()

        while right < len(s):
            length += 1

            if s[right] not in visited:
                visited.add(s[right])

            else:
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                    length -= 1

                left += 1
                length -= 1

            if length > length_of_longest_substring:
                length_of_longest_substring = length

            right += 1

        return length_of_longest_substring