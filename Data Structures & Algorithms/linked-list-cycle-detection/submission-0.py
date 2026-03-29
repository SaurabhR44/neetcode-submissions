# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        detection_set = set()
        curr = head
        while curr:
            if curr in detection_set:
                return True
            detection_set.add(curr)
            curr = curr.next
        return False