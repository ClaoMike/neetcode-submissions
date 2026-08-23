class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        prefix_0 = []
        prefix_1 = []

        if s[0] == "0":
            prefix_0.append(1)
            prefix_1.append(0)
        else:
            prefix_0.append(0)
            prefix_1.append(1)

        for i in range(1, len(s)):
            if s[i] == "0":
                prefix_0.append(1 + prefix_0[-1])
                prefix_1.append(prefix_1[-1])
            else:
                prefix_0.append(prefix_0[-1])
                prefix_1.append(1 + prefix_1[-1])

        print(prefix_0)
        print(prefix_1)

        for i in range(len(s)-1):
            score = prefix_0[i] + prefix_1[-1] - prefix_1[i]
            print(score)

            if score > max_score:
                max_score = score

        return max_score