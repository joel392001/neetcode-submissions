# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    #     [2,4,6,8]
    #          s
    #                      f             f
    #              s
    # [0, 1, 2, 3, 4, 5, 6]
    # 0 - 6 - 1 - 5 - 2 - 4

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        node = slow
        # reverse second half  
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        first = head
        last = prev
        while last.next:
            first_next = first.next
            last_next = last.next

            first.next = last
            last.next = first_next

            first = first_next
            last = last_next