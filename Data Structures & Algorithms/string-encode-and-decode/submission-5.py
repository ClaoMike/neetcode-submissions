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
            word = []
            length = []

            while '0' <= s[i] <= '9':
                length.append(s[i])
                i += 1
            length = int("".join(length))
            
            i += 1
  
            for j in range(i, i + length):
                word.append(s[j])
       
            result.append("".join(word))
            i += length
        
        return result