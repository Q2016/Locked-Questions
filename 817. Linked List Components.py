Question:
You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.
Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

Example 1:
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.


    
    
    
    
    
    
    
    
    
Solution: Two pointers


class Solution(object):
    def numComponents(self, head, G):

        p, prev, count, G = head, False, 0, set(G)
        while p:
            if p.val in G and not prev:
                count += 1
            prev, p = p.val in G, p.next;
        
        return count
