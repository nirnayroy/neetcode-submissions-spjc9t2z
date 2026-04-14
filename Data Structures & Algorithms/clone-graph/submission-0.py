"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = Node(node.val, [])
        original2clone = {}
        original2clone[node] = clone
        queue = deque([node])
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in original2clone:

                    original2clone[neighbor] = Node(val = neighbor.val, neighbors = [])
                    queue.append(neighbor)
                original2clone[cur_node].neighbors.append(original2clone[neighbor])

        return clone