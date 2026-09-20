class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        allowed_operations = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in allowed_operations:
                stack.append(token)
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    result = int(operand1 / operand2)
                
                stack.append(str(result))
        
        return int(stack[0])