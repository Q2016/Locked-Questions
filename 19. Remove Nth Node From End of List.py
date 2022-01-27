Question:
# Given a linked list, remove the nth node from the end of list and return its head.

Example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Solution:

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        
        for i in xrange(n):
            fast = fast.next
            
        while fast.next:
            slow, fast = slow.next, fast.next
            
        slow.next = slow.next.next
        
        return dummy.next

# Time:  O(n)
# Space: O(1)    
