Question:
Numbers can be regarded as product of its factors. For example, 8 = 2 x 2 x 2; = 2 x 4. Write a function that takes an 
integer n and return all possible combinations of its factors.

Examples: 
input: 12
output:[[2, 6],[2, 2, 3],[3, 4]]  


class Solution(object):
    def __init__(self):
        self.factors = dict()

    def getFactors(self, n):

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
