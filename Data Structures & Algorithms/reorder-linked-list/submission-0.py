# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp = head
        fp = head.next

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        cur = sp.next
        prev = sp.next = None 
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
            
                        