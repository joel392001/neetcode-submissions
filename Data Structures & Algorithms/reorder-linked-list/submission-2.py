# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    #     [2,4,6,8]
    #          s
    #                     f             f
    #           s
    # [0, 1, 2, 3, 4, 5, 6]
    # 0 - 6 - 1 - 5 - 2 - 4

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        # reverse second half  
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first = head
        last = prev
        while last:
            first_next = first.next
            last_next = last.next

            first.next = last
            last.next = first_next

            first = first_next
            last = last_next