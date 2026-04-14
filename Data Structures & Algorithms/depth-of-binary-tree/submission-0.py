# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def get_depth(node):
            if not node.left and not node.right:
                return 1
            elif not node.left:
                return get_depth(node.right) + 1
            elif not node.right:
                return get_depth(node.left) + 1
            else:
                return max(get_depth(node.right), get_depth(node.left)) + 1
        if not root:
            return 0
        else:
            return get_depth(root)
        
        