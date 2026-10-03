# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
            
        tree_as_array = []
        tree_as_array.append(str(root.val))

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                tree_as_array.append(str(node.left.val))
            else:
                tree_as_array.append("#")

            if node.right:
                queue.append(node.right)
                tree_as_array.append(str(node.right.val))
            else:
                tree_as_array.append("#")
        
        while tree_as_array and tree_as_array[-1] == "#":
            tree_as_array.pop()

        return ".".join(tree_as_array)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = data.split(".")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if idx < len(tokens):
                if tokens[idx] != "#":
                    node.left = TreeNode(int(tokens[idx]))
                    queue.append(node.left)
                idx += 1
            if idx < len(tokens):
                if tokens[idx] != "#":
                    node.right = TreeNode(int(tokens[idx]))
                    queue.append(node.right)
                idx += 1
        return root





