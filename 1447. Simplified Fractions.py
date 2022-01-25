Question:
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that 
the denominator is less-than-or-equal-to n. The fractions can be in any order.

Example 1:
Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".    


Solution: gcd
    
https://leetcode.com/problems/simplified-fractions/discuss/635260/Python3-Easy-GCD


Writing GCD Ourselves
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x    
        
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res

or:    
    
    
Using Python math library
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
