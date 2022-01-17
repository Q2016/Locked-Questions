
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
Using Python math library
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
