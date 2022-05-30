Problem:
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex.


For each consecutive pair of edges of the polygon (each triplet of points), compute the z-component of 
the cross product of the vectors defined by the edges pointing towards the points in increasing order. 
Take the cross product of these vectors:

The polygon is convex if the z-components of the cross products are either all positive or all negative. 
Otherwise the polygon is nonconvex.

Example 1:
[[0,0],[0,1],[1,1],[1,0]], Answer: True


    
    
    
    
    
    
    
    
    
    
    
Solution: (A cross B=axby-aybx so not sure about the formula below)
    
Get the cross product of the sequential input edge a, b  then:
if tmp == 0, a -> b 180° on the same line;
elif tmp > 0, a -> b clockwise;
else tmp < 0, a -> anticlockwise;
    
class Solution(object):
    def isConvex(self, points):

        n = len(points)
        zcrossproduct = None

        for i in range(-2, n-2):
            x = [ points[i][0], points[i+1][0], points[i+2][0] ]
            y = [ points[i][1], points[i+1][1], points[i+2][1] ]

            dx1 = x[1] - x[0]
            dy1 = y[1] - y[0]

            dx2 = x[2] - x[1]
            dy2 = y[2] - y[1]

            if not zcrossproduct:
                zcrossproduct = dx1 * dy2 - dy1 * dx2
            elif ( dx1 * dy2 - dy1 * dx2 ) * zcrossproduct < 0:
                return False
        return True
