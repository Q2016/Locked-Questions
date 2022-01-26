Question:
Given the head of a linked list, return the list after sorting it in ascending order.



Solution:

    def sortList(self, head):
        if head == None or head.next == None:
            return head
        
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
        
        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)
        
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


