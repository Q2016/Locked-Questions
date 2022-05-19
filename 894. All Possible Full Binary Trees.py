Question:
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
Solution: Recursion
    
Let FBT(N) be the list of all possible full binary trees with N nodes.
Every full binary tree T with 3 or more nodes, has 2 children at its root. Each of those children left and right are themselves full binary trees.
Thus, for N≥3, we can formulate the recursion: FBT(N)= [All trees with left child from FBT(x) and right child from FBT(N−1−x), for all x].
Also, by a simple counting argument, there are no full binary trees with a positive, even number of nodes.
Finally, we should cache previous results of the function FBT so that we don't have to recalculate them in our recursion.    

class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in xrange(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]

    
    
Complexity Analysis

Time Complexity: O(2^N)
Space Complexity: O(2^N)    
