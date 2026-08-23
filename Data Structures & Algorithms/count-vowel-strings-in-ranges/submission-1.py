class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')

        ans = []
        prefix = [1] if words[0][0] in vowels and words[0][-1] in vowels else [0]

        for i in range(1, len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        for query in queries:
            left, right = query
            current = 1 if words[left][0] in vowels and words[left][-1] in vowels else 0
            ans.append(prefix[right] - prefix[left] + current)

        return ans