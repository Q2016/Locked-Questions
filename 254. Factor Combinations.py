Problem:
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
You may assume that n is always positive.
Factors should be greater than 1 and less than n.

Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
  [
    [2, 6],
    [2, 2, 3],
    [3, 4]
  ]  
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


class Solution(object):
    def __init__(self):
        self.factors = dict()

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return []
        elif n in self.factors:
            return self.factors[n]

        else:
            res = list()
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    residue = n // f
                    res.append([f, residue])
                    for l in self.getFactors(residue):
                        if l[0] >= f:
                            res.append([f] + l)
            return res
