Question:
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. 
This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may 
have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.
Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. 
Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.
Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.	

Example:
Input: head = [1,2,null,3]
Output: [1,3,2]
	
prev  next   ------>   prev  next     
     1                     2
   child     <------     child
     |
     |>
prev  next
     3
  child

Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

prev  next   ------> prev  next ------>  prev  next     
     1                   3                   2
   child     <------   child   <------     child







Solution:

For picture: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/	
	
Basic idea is straight forward:
Start form the head , move one step each time to the next node. When meet with a node with child, say node p, follow its child 
chain to the end and connect the tail node with p.next, by doing this we merged the child chain back to the main thread. 
Return to p and proceed until find next node with child. Repeat until reach null


    def flatten(self, head) :
        if Not head 
	    return head
	# Pointer
        p = head; 
        while p :
            # CASE 1: if no child, proceed 
            if (Not p.child) :
                p = p.next
                continue
            
            # CASE 2: got child, find the tail of the child and link it to p.next 
            temp = p.child
            # Find the tail of the child
            while temp.next : 
                temp = temp.next
            # Connect tail with p.next, if it is not null
            temp.next = p.next  
            if p.next:  
		p.next.prev = temp
            # Connect p with p.child, and remove p.child
            p.next = p.child 
            p.child.prev = p
            p.child = None
        
        return head
    

