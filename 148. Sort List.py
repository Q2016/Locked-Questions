Question:
Given the head of a linked list, return the list after sorting it in ascending order.
















Solution: Merge Sort
 
-Recursively split the original list into two halves. The split continues until there is only one node in the linked list (Divide phase). 
To split the list into two halves, we find the middle of the linked list using the Fast and Slow pointer approach as mentioned in Find Middle Of 
Linked List.
-Recursively sort each sublist and combine it into a single sorted list. (Merge Phase). This is similar to the problem Merge two sorted linked lists
The process continues until we get the original list in sorted order.

    def sortList(self, head):
        if head == None or head.next == None:
            return head
        
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
        
        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow) #middle
        
        return self.mergeTwoLists(sorted_l1, sorted_l2)
           
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        
        cur = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.next
            else:
                cur.next, cur, l2 = l2, l2, l2.next
                
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
            
        return dummy.
    
# Time:  O(nlogn)
# Space: O(logn) for stack call


