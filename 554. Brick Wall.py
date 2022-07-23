Question:
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed.
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

Example:
Input:      Output: 2
[[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]]








Solution: Hashmap
    https://www.youtube.com/watch?v=Kkmv2h48ekw
    
    
For the picture of the problem, look at the leetcode.    
Number of Bricks Crossed by Line = Number of Rows in Wall - Frequency of Most Occuring Edge
    
class Solution:
    def leastBricks(self, wall):
        countGap={0:0}
        
        for r in wall:
            total=0
            for b in r[:-1]:
                total +=b
                countGap[total]=1+countGap.get(total,0)
                
        return len(wall)-countGap
    

    
    
Time Complexity : O(N * M),
where N = hieght of the wall OR number of rows in wall
where M = approx width of each row OR approx number of bricks in each row
where N * M = Total number of bricks in the wall


Space Complexity : O(M),
where M = Approx number of bricks in each row    
