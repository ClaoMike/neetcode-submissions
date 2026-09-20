class MinStack:

    class Node:
        def __init__(self, value=None, minimum=None):
            self.value = value
            self.minimum = minimum

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        node = self.Node(value=val)

        top = self.stack[-1] if self.stack else None
        if top is None:
            node.minimum = node
        elif node.value <= top.minimum.value:
            node.minimum = node
        else:
            node.minimum = top.minimum

        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].minimum.value