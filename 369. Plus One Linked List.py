Question:
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

Example: Input: 1->2->3, Output: 1->2->4


Solution:
    
    def plusOne(self, head):

        lst = []
        cur = head 

        while cur:
        	lst.append(cur)
        	cur = cur.next

        carry = 1
        for i in range(len(lst)-1,-1,-1):
        	lst[i].val += carry
        	if lst[i].val < 10:
        		carry = 0
        		break
        	else:
        		lst[i].val -= 10

        if carry == 1:
        	node = ListNode(1)
        	node.next = head
        	return node
        else:
        	return head 
