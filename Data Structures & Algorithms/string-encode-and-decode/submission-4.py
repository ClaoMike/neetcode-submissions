class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        print(s)

        result = []
        i = 0
        while i < len(s):
            length = []
            while '0' <= s[i] <= '9':
                length.append(s[i])
                i += 1
            length = "".join(length)
            
            length = int(length)
            print(length)

            word = []
            
            i += 1
            print(i)
            # print(i)
            for j in range(i, i + length):
                word.append(s[j])
            # print("".join(word))
            result.append("".join(word))
            i += length
        
        return result