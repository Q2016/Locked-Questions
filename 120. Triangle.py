# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        
        cur = triangle[0] + [float("inf")]
        for i in xrange(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0])
            for j in xrange(1, i + 1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
            cur = next + [float("inf")]
            
        return reduce(min, cur)
