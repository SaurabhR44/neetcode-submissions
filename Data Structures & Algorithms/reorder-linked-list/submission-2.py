# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Edge Case when empty List
        if not head:
            return 
        
        #Find the midpoint (second half)
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the second half
        second = slow.next
        slow.next = prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #Merge both the halves based on the order given
        first,second = head,prev
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        


