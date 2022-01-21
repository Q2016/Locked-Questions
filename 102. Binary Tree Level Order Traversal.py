Question:
Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).

 

Example 1:
    3
  /   \
9     20
    /   \
   15    7
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]    

Solution: --

level is a list of the nodes in the current level. Keep appending a list of the 
values of these nodes to ans and then updating level with all the nodes in the next 
level (kids) until it reaches an empty level. Python's list comprehension makes it 
easier to deal with many conditions in a concise manner.


Solution 1, (6 lines)

def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf]
    return ans

Solution 2, (5 lines), same idea but use only one list comprehension in while loop to get the next level
def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])            
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans

Solution 3 (10 lines), just an expansion of solution 1&2 for better understanding.
def levelOrder(self, root):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
