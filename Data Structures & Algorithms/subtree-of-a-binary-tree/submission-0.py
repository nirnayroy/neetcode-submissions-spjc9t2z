# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        function that returns true if it finds that a subtree in a tree is equal to
        a given root

        subproblem1: find if two trees are equal
        subproblem2: given the function to find if two trees are equal 
        return true if a subtree is found to be equal to the subroot
        '''

        # subproblem1:
        def is_equal(tree1, tree2):
            '''
            1
            2 3
            4 5 _ _
            6 
            '''
            if tree1 is None and tree2 is None:
                return True
            elif tree1 and tree2 and tree1.val == tree2.val:
                return is_equal(tree1.left, tree2.left) and is_equal(tree1.right, tree2.right)
            else:
                return False

        if subRoot is None:
            return True
        if root is None:
            return False
        
        if is_equal(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        