Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

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

My solution:
   
class Solution:
    # your task is to complete this function
    # function should print the top view of the binary tree
    # Note: You aren't required to print a new line after every test case
    
    sequence=[]
    def longestConsecutive(self, root):
        # Code here
        
        if root.left==None and root.right==None:
            return sequence 
        value_pre=root.data
        if root.right==value_pre+1:
            self.sequence.append(value_pre)
            return longestConsecutive(root.right)
        if root.left==value_pre+1:
            self.sequence.append(value_pre)
            return longestConsecutive(root.left)
         

         
 https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/binary-tree-longest-consecutive-sequence-ii.py        
 class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longestConsecutiveHelper(root):
            if not root:
                return 0, 0
            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)
            cur_inc_len, cur_dec_len = 1, 1
            if root.left:
                if root.left.val == root.val + 1:
                    cur_inc_len = max(cur_inc_len, left_len[0] + 1)
                elif root.left.val == root.val - 1:
                    cur_dec_len = max(cur_dec_len, left_len[1] + 1)
            if root.right:
                if root.right.val == root.val + 1:
                    cur_inc_len = max(cur_inc_len, right_len[0] + 1)
                elif root.right.val == root.val - 1:
                    cur_dec_len = max(cur_dec_len, right_len[1] + 1)
            self.max_len = max(self.max_len, cur_dec_len + cur_inc_len - 1)
            return cur_inc_len, cur_dec_len

        self.max_len = 0
        longestConsecutiveHelper(root)
        return self.max_len
