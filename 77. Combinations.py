Question:
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n. 
For example,
If n = 4 and k = 2, a solution is: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],]


Solution:DFS

This link is also interesting
https://leetcode.com/problems/combinations/discuss/27006/A-template-to-those-combination-problems

class Solution(object):
    def combine(self, n, k):

        result, combination = [], []
        i = 1
        while True:
            if len(combination) == k:
                result.append(combination[:])
            if len(combination) == k or \
               len(combination)+(n-i+1) < k:
                if not combination:
                    break
                i = combination.pop()+1
            else:
                combination.append(i)
                i += 1
        return result
    

class Solution2(object):
    def combine(self, n, k):

        def combineDFS(n, start, intermediate, k, result):
            if k == 0:
                result.append(intermediate[:])
                return
            for i in xrange(start, n):
                intermediate.append(i+1)
                combineDFS(n, i+1, intermediate, k-1, result)
                intermediate.pop()

        result = []
        combineDFS(n, 0, [], k, result)
        return result
    
    
    
Time:  O(k * C(n, k))
Space: O(k)    
