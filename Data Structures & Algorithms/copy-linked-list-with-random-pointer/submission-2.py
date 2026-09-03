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
        if head is None:
            return None

        h = {}

        dummy = head
        while dummy:
            h[dummy] = Node(x=dummy.val)
            dummy = dummy.next

        sentinel = Node(x=-101)
        last = sentinel
        dummy = head
        while dummy:
            last.next = h[dummy]
            last.next.random = None if dummy.random is None else h[dummy.random]
            last = last.next
            dummy = dummy.next

        return sentinel.next