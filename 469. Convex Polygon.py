Problem:
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex.

Example 1:
[[0,0],[0,1],[1,1],[1,0]], Answer: True


    
    
    
    
    
    
    
    
    
    
    
Solution: (A cross B=axby-aybx so not sure about the formula below)
    
Get the cross product of the sequential input edge a, b as tmp= (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1]), then:
if tmp == 0, a -> b 180° on the same line;
elif tmp > 0, a -> b clockwise;
else tmp < 0, a -> anticlockwise;
Update instead of just maintaining the sequential cross product result, any of the two cross product shouldn't multiplies to minus:
    
    def isConvex(self, points):
        last, tmp = 0, 0
        for i in xrange(2, len(points) + 3):
            
            p0=points[(i - 2) % len(points)] 
            p1=points[i % len(points)]
            p2 =points[(i - 1) % len(points)]
            
            tmp = (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
            if tmp:
                if last * tmp < 0:
                    return False
                last = tmp
        return True
