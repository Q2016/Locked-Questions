Question:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses 
in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into 
on the same night. Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1], Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.  
                  3
               /    \
              2      3
               \      \
                 3      1  
        
        
        
        
        
        
  
        
Solution: DFS
  https://www.youtube.com/watch?v=nHR8ytpzz7c
  
class Solution:
  def rob(self, root):
    
    # return pair: [withRoot, withoutRoot]
    def dfs(root):
        if not root:
            return [0,0]

        leftPair=dfs(root.left)
        rightPair=dfs(root.right)

        withRoot=root.val+leftPair[1]+rightPair[1]
        withoutRoot=max(leftPair)+max(rightPair)

        return [withRoot, withoutRoot]
    
    return max(dfs(root))
  
  
Time complexity O(n)
