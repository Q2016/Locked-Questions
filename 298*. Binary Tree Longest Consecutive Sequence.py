Question:
Given a binary tree, find the length of the longest consecutive sequence path. The path refers to any sequence of nodes 
from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to 
be from parent to child (cannot be the reverse). Note that consecutive means that, value of the nodes must be consecutive 
numbers like 1<2<3<4<5.... this is different from nodes being connected.
For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3. 
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.











Pre-order makes sense beacuse output is sorted

https://www.youtube.com/watch?v=oSYGjIq6ZM4

Solution: Pre-order
         
    def longestConsecutive(self, root):
         findLongestConsecutiveSequence(root, 0, 0, max)
         return max
      
    def findConsecutiveSequence(root, count, target, max):
         if root==None:
            return
         elif root.val==target:
            count++
         else:
            count=1
            
         max=math.max(max, count)
         findConsecutiveSequence(root.left, count, root.val+1, max)
         findConsecutiveSequence(root.right, count, root.val+1, max)
         
         
         
Complexity:         
         
time  O(n)   
space O(n)         

