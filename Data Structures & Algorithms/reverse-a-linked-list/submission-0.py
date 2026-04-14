# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = None
        tmp = head.next

        while tmp:
            head.next = res
            res = head
            head = tmp
            tmp = head.next
        head.next = res
        return head