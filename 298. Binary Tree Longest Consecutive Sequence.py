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
         
https://www.geeksforgeeks.org/longest-consecutive-sequence-binary-tree/         
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# Utility method to return length of
# longest consecutive sequence of tree
def longestConsecutiveUtil(root, curLength,
                           expected, res):
    if (root == None):
        return
 
    # if root data has one more than its
    # parent then increase current length
    if (root.data == expected):
        curLength += 1
    else:
        curLength = 1
 
    # update the maximum by current length
    res[0] = max(res[0], curLength)
 
    # recursively call left and right subtree
    # with expected value 1 more than root data
    longestConsecutiveUtil(root.left, curLength,
                           root.data + 1, res)
    longestConsecutiveUtil(root.right, curLength,
                           root.data + 1, res)
 
# method returns length of longest consecutive
# sequence rooted at node root
def longestConsecutive(root):
    if (root == None):
        return 0
 
    res = [0]
 
    # call utility method with current length 0
    longestConsecutiveUtil(root, 0, root.data, res)
 
    return res[0]
