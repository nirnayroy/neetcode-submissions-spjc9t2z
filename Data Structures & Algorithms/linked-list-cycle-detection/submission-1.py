# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def has_cycle(node, visited):
            if not node:
                return False
            elif node in visited:
                return True
            visited.add(node)
            if has_cycle(node.next, visited):
                return True
            else:
                return False
        
        visited = set()
        return has_cycle(head, visited)
            