# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = j = total_1 = total_2 = size_1 = size_2 = 0

        current_1 = l1
        current_2 = l2

        while current_1 is not None:
            size_1 += 1
            current_1 = current_1.next

        while current_2 is not None:
            size_2 += 1
            current_2 = current_2.next

        current_1 = l1
        current_2 = l2

        dup = 1
        while (size_1 != 0 and current_1 is not None):
            total_1 += current_1.val * dup
            dup *= 10
            size_1 -= 1
            current_1 = current_1.next

        dup = 1
        while (size_2 != 0 and current_2 is not None):
            total_2 += current_2.val * dup
            dup *= 10
            size_2 -= 1
            current_2 = current_2.next

        s = total_1 + total_2

        if s == 0:
            return ListNode(0)

        dummy = ListNode(0)
        tail = dummy
        while s > 0:
            tail.next = ListNode(s % 10)
            tail = tail.next
            s //= 10

        return dummy.next

        
        
        total_1 = current_1.val
        size_1 = size_1 - 1
        dup = 10 

        while(size_2 is not 0):
            total_2 += current_2.val * dup
            size_2 += size_2 - 1
            dup = dup * 10 
            current_2 = current_2.next
        
        return total_1 + total_2    




        