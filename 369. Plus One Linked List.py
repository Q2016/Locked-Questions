Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:

Input:
1->2->3

Output:
1->2->4



class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
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
