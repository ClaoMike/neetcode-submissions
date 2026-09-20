class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for c in s:

            if c in h.keys():
                stack.append(c)
            else:
                top = stack[-1] if stack else None

                if top is None:
                    return False
                
                if c == h[top]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
            
        return True