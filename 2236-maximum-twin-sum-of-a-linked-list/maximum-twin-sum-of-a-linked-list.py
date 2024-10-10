# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first_half = []
        slow, fast = head, head

        while fast and fast.next:
            first_half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        second_half = []
        while slow:
            second_half.append(slow.val)
            slow = slow.next
        
        max_sum = 0
        for i in range(0, len(first_half)):
            curr_sum = first_half[i] + second_half[-(i+1)]
            max_sum = max(max_sum, curr_sum)

        return max_sum

        