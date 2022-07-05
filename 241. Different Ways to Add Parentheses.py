Question:
Given a string expression of numbers and operators, return all possible results from computing 
all the different possible ways to group numbers and operators. 

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10	











Solution: DFS 
    
we solved 22. using Backtracking    

class Solution(object):
    def diffWaysToCompute(self, input):
        m = {}
        return self.dfs(input, m)
        
    def dfs(self, input, m):
        if input in m:
            return m[input]
        if input.isdigit():
            m[input] = int(input)
            return [int(input)]
        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[input] = ret
        return ret
