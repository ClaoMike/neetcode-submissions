"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def printLinkedList(node):
            dummy = node
            while dummy:
                if dummy.random:
                    print(f"{dummy.val}(r: {dummy.random.val}) -> ", end="")
                else:
                    print(f"{dummy.val}(r: None) -> ", end="")
                dummy = dummy.next
            print()

        if head is None:
            return None

        h = {}

        dummy = head
        while dummy:
            h[dummy] = Node(x=dummy.val)
            dummy = dummy.next

        # print(h)

        sentinel = Node(x=-101)
        last = sentinel
        dummy = head
        while dummy:
            last.next = h[dummy]
            last.next.random = None if dummy.random is None else h[dummy.random]
            last = last.next
            dummy = dummy.next

        # printLinkedList(sentinel.next)

        return sentinel.next