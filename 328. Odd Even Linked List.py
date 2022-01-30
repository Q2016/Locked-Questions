Question:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even 
indices, and return the reordered list. The first node is considered odd, and the second node is even, and so on. Note that the 
relative order inside both the even and odd groups should remain as it was in the input. You must solve the problem in O(1) 
extra space complexity and O(n) time complexity.    

Example 1:
Input: head = [1,2,3,4,5]    1--->2--->3--->4--->5
Output: [1,3,5,2,4]          1--->3--->5--->2--->4

    
    
Soluion:    
    
    def oddEvenList(self, head):

        if not head:
            return head
        
        odd = head # Both of them point at the first node of the target linked list
        even = head.next # doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even # We have to keep where the even-node list starts
        
        while even and even.next: # won't get in the loop at first if there's only one node in the linked list
            # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
            # AND, why these two, small discussion by myself as below
            odd.next = odd.next.next
            even.next = even.next.next
            # After these two ops, odd/even still points at its original place
            # Therefore, we move them to the next node repectively
            odd = odd.next
            even = even.next
        
        odd.next = eHead # the odd pointer currently points at the last node of the odd-node list
        
        return head # We keep the start of the odd-node list in the first of our code
      
      
