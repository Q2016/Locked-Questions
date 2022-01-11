Problem:
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1: Given points = [[1,1],[-1,1]], return true.

Example 2: Given points = [[1,1],[-1,-1]], return false.

Follow up: Could you do better than O(n2)?

Hint:

Find the smallest and largest x-value for all points. If there is a line then it 
should be at y = (minX + maxX) / 2. For each point, make sure that it has a reflected point in the opposite side.

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        pointSet = set()
        maxNum = -sys.maxint
        minNum = sys.maxint
        for x, y in points:
            maxNum = max(maxNum, x)
            minNum = min(minNum, x)
            pointSet.add((x, y))
        sumNum = maxNum + minNum
        for x, y in points:
            tempTuple = (sumNum - x, y)
            if tempTuple not in pointSet:
                return False
        return True
