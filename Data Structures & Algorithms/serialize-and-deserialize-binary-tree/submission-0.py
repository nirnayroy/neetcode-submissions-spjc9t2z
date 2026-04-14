# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        def dfs(node):
            if not node:
                data.append('N')
                return
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split(',')
        self.i = 0

        def build_tree():
            if data_list[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(data_list[self.i]))
            self.i += 1
            if self.i == len(data_list):
                return node
            node.left = build_tree()
            node.right = build_tree()
            
            return node

        return build_tree()

            

        

            

