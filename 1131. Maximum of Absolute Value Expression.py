Question:
Given two arrays of integers with equal lengths, return the maximum value of:
|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|    



Solution: ---


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



Complexity
Time O(N) for 4 passes
Space O(1)



Python:

    def maxAbsValExpr(self, x, y):
        result, n = 0, len(x)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            smallest = p * x[0] + q * y[0] + 0
            for i in xrange(n):
                cur = p * x[i] + q * y[i] + i
                result = max(result, cur - smallest) # what we are after
                smallest = min(smallest, cur) # we find the smallest because  f(i)-f(j) :max of first & min of second term
        return res
