# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIndex = 0
        h = {}
        for i in range(len(inorder)):
            h[inorder[i]] = i

        def createNode(l, r):
            if l >= r:
                return None

            nonlocal preorderIndex
            
            value = preorder[preorderIndex] # get the value for the current node
            preorderIndex += 1 # move pointer to next node's value
            
            node = TreeNode(val=value) # create the node
            # i = inorder.index(value)
            i = h[value]
            
            node.left = createNode(l, i)
            node.right = createNode(i+1, r)

            return node

        return createNode(0, len(inorder))