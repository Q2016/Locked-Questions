Question:
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.
Follow up: Could you do better than O(n^2)?

Example 1: Given points = [[1,1],[-1,1]], return true.


Solution:
Find the smallest and largest x-value for all points. If there is a line then it 
should be at y = (minX + maxX) / 2. For each point, make sure that it has a reflected point in the opposite side.


    def isReflected(self, points):

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
