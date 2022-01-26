Question:
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


Solution:
    https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/add-two-numbers.py


    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)
        return dummy.next

    
    
# Time:  O(n)
# Space: O(1)

