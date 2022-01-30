Question:
Given a binary tree, return thevertical ordertraversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7], Output: [[9],[3,15],[20],[7]]
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 


Solution: BFS + hash solution.

    def verticalOrder(self, root):

        cols = collections.defaultdict(list)
        queue = [(root,0)]

        for node, col in queue:
            if node:
                cols[col].append(node.val)
                queue += (node.left, col - 1), (node.right, col + 1)
        return [cols[col] for col in sorted(cols)]
   
   
# Time:  O(n)
# Space: O(n)   
