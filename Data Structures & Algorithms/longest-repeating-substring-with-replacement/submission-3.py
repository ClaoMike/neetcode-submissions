class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        right = left = max_freq = length = best_length = 0
        occurences = defaultdict(int)

        # window is expanded to one cell now
        while right < len(s):
            # treat current expansion
            occurences[s[right]] += 1
            max_freq = max(max_freq, occurences[s[right]])

            # if window is valid
            if right - left + 1 - max_freq <= k:
                # calculate its length and save it if it is better then the previous
                length = right - left + 1
                
                if best_length < length:
                    best_length = length

            # if window is valid
            else:
                # slide window at previous length instead
                occurences[s[left]] -= 1
                left += 1
            
            # expand window
            right += 1

        return best_length