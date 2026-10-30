# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_value = head
        previous_value = None

        while current_value:
            temp = current_value.next
            current_value.next = previous_value
            previous_value = current_value
            current_value = temp
        return previous_value