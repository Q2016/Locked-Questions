Question:
 https://leetcode.com/problems/unique-binary-search-trees/
    
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
Solution:   (hard, no idea, why complexity? N^3) 

The fastest solution has complexity of O(N) but too dificault to understand, below is the simple version but higher time (brute force)    

pick a root, then you have the left tree and right tree
    
    
Solution 1: Top down DP

class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def dfs(left, right):
            if left > right: return 1
            ans = 0
            for i in range(left, right + 1):
                ans += dfs(left, i-1) * dfs(i+1, right)
            return ans
        
        return dfs(1, n)
Complexity:

Time: O(N^3), where N <= 19
Space: O(N^2)    
