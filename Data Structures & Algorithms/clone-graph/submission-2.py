"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque, defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        root = None
        h = {}
        seen = set()
        queue = deque()

        copy_node = Node(val=node.val)
        h[copy_node.val] = copy_node
        root = copy_node

        queue.append(node)
        seen.add(node)

        while queue:
            node = queue.popleft()
            copy_node = h[node.val]

            for neighbor in node.neighbors:

                if neighbor.val not in h.keys():
                    h[neighbor.val] = Node(val=neighbor.val)

                copy_node.neighbors.append(h[neighbor.val])

                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return root