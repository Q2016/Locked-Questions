Question:
Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as 
(x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the 
coordinates of the top-right corner of the rectangle.
Return True if the circle and rectangle are overlapped otherwise return False.	











Solution:---

https://leetcode.com/problems/circle-and-rectangle-overlapping/discuss/563351/Python-O(1)-simple-geometry

All relative positions of the intersecting shapes could be decomposed into 3 disjoint groups:
-a corner of a rectangle is inside the circle
-one of the edges of the rectangle crosses the circle
-the circle is completely inside the rectangle
Identifing that a given configuration belongs to one of these cases signifies that the shapes intersect.
Though to make our code simpler we will not go for the disjointness of the cases and allow our separate 
conditions to trigger on some of the same cases, obviously that doesn't sacrifice the corectness of the end result. 
For example x1<=x_c<=x2 and y1<=y_c<=y2 doesn't only search for the circle inside the rectangle, it could also catch 
certain cases of the corner inside of the rectangle or an edge crossing the circle, but what is important for us that 
is does its job of the cathing the former thing. The same applies to the second bullet point.


    def checkOverlap(self, r, x_c, y_c, x1, y1, x2, y2):
        corners = [(x1,y1), (x2,y1), (x2,y2), (x1, y2)]
        for (x, y) in corners:
            if (x_c - x)**2 + (y_c - y)**2 <= r**2:
                return True

        for x in [x1, x2]:
            if x_c-r <= x <= x_c+r and y1<=y_c<=y2:
                return True
        for y in [y1, y2]:
            if y_c-r <= y <= y_c+r and x1<=x_c<=x2:
                return True
				
        if x1<=x_c<=x2 and y1<=y_c<=y2:
            return True
        return False            
