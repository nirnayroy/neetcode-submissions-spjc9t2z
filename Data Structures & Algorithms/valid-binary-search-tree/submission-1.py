# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def is_valid(node, lb, ub):
            if not node.left and not node.right:
                return lb < node.val < ub
            elif not node.left and node.right:
                return lb < node.val < ub and is_valid(node.right, node.val, ub)
            elif node.left and not node.right:
                return  lb < node.val < ub and is_valid(node.left, lb, node.val)
            else:
                return is_valid(node.right, node.val, ub) and is_valid(node.left, lb, node.val) and lb < node.val < ub
            
        return is_valid(root, float('-inf'), float('inf'))