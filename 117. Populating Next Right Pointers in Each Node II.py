Question:

Given a binary tree Populate each next pointer to point to its next right node. 
        
Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
Solution: similar to 116  but now in constant space
        
If you have solved [https://leetcode.com/problems/populating-next-right-pointers-in-each-node/] 
this question this is exactly same as this one except for one change.

I spend some time for this problem, because my solution for problem 116 is quite different and can not be applied here.

The main idea is to go level by level and use already existing .next connections: if you will not do it, problem will be quite painful. 
So, idea is the following:
We will keep two nodes: node and curr: first one is for parent level and curr for next level.
We check if we have node.left and if we have, we create connection curr.next = node.left and also move our curr to the right, 
so it always will be the rightest visited node in level.
In similar way we check if we have node.right and do the same for it.
When we finished with node, we move it to right: node = node.next.
Finally, we need to go to the next level: we update node = dummy.next.
Note, that in this place we will have some extra connections from dummy variables to left side of our tree, 
but there is no way testing system can detect it, because it is one-way connections. 
If you want to be completely honest, you need to add just one more line dummy.next = None after the line node = dummy.next.

Complexity: time complexity is O(n): we visit each node of our tree only once. Space complexity is O(1)

class Solution:
    def connect(self, root):
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next
               
        return root
