Given a binary tree, return thevertical ordertraversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input:
[3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: 
[3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input:
[3,9,8,4,0,1,7,null,null,null,2,5]
 (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2


Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
FB: Complexity!

Thoughts

Use map <col, list<val>> to record the col and list value pair. Use BFS to expand the tree to add entry

# Time:  O(n)
# Space: O(n)

# BFS + hash solution.



class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(root,0)]

        for node, col in queue:
            if node:
                cols[col].append(node.val)
                queue += (node.left, col - 1), (node.right, col + 1)

        return [cols[col] for col in sorted(cols)]
