Intuition

Take |x[i] - x[j]| + |y[i] - y[j]| as Manhattan distance of two points.
x is the coordinate of points on the x-axis,
y is the coordinate of points on the y-axis.


Explanation 1: Math
Assume i < j, there are four possible expression:
|x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]|) + (y[i] - y[j]) = (x[i] + y[i]|) - (x[j] + y[j])
|x[i] - x[j]| + |y[i] - y[j]| = (x[i] - x[j]|) - (y[i] - y[j]) = (x[i] - y[i]|) - (x[j] - y[j])
|x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]|) + (y[i] - y[j]) = (-x[i] + y[i]|) - (-x[j] + y[j])
|x[i] - x[j]| + |y[i] - y[j]| = -(x[i] - x[j]|) - (y[i] - y[j]) = (-x[i] - y[i]|) - (-x[j] - y[j])

So we can see, the expression
|x[i] - x[j]| + |y[i] - y[j]| + |i - j| = f(j) - f(i)

where f(i) = p * x[i] + q * y[i] + i
with p = 1 or -1, q = 1 or -1


Explanation 2: Graph
For 3 points on the plane, we always have |AO| - |BO| <= |AB|.
When AO and BO are in the same direction, we have ||AO| - |BO|| = |AB|.

We take 4 points for point O, left-top, left-bottom, right-top and right-bottom.
Each time, for each point B, and find the smallest A point to O,
the Manhattan distance |AB| >= |AO| - |BO|.


Complexity
Time O(N) for 4 passes
Space O(1)



Python:

    def maxAbsValExpr(self, x, y):
        res, n = 0, len(x)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            smallest = p * x[0] + q * y[0] + 0
            for i in xrange(n):
                cur = p * x[i] + q * y[i] + i
                res = max(res, cur - smallest)
                smallest = min(smallest, cur)
        return res
