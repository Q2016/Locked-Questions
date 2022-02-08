Question:
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Solution:
The idea is to calculate all the distance between each two points, and sort them. In this way, we get 4 edges and 2 diagonals of the square in order. 
If the 4 edges equal to each other, that means it should be equilateral parallelogram. Finally, we check whether the 2 diagonals equal to 
each other so as to check if it's a square.

    def validSquare(self, p1, p2, p3, p4):
        if p1==p2==p3==p4:
            return False
        
        def dist(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        
        ls=[dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)]
        ls.sort()
        if ls[0]==ls[1]==ls[2]==ls[3]:
            if ls[4]==ls[5]:
                return True
        return False
