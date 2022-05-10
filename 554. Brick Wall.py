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
    
For the picture of the problem, look at the leetcode.    
Number of Bricks Crossed by Line = Number of Rows in Wall - Frequency of Most Occuring Edge
    
    
    
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) 
    {
        unordered_map<int, int> edge_frequency;     //HashMap to store the number of common edges among the rows

        int max_frequency = 0;         //Variable to store the frequency of most occuring edge
        
        for(int row=0; row<wall.size(); row++)        //Iterating through each row
        {
            int edge_postion = 0;       //Variable to store different edge postion
            
            for(int brick_no=0; brick_no< wall[row].size() -1; brick_no++)    //Iterating through each brick inside a row
            { 
                int current_brick_length = wall[row][brick_no];  //Length of the current brick
                
                edge_postion = edge_postion + current_brick_length ;  //Next Edge Position = Previous Edge Position + Current Brick's Length
                
                edge_frequency[edge_postion]++;  //Incrementing the Frequency of just calculated Edge Postion
                
                max_frequency = max(edge_frequency[edge_postion],max_frequency);  //Comparing the "Frequency of just calculated Edge Postion" with "Max Frequency seen till now" & storing whichever is greater.
            }
        }
        return wall.size() - max_frequency; // returning (Number of Bricks Crossed by Line) i.e. (Number of Rows in Wall - Frequency of Most Occuring Edge) 
    }
};

    
    
Time Complexity : O(N * M),
where N = hieght of the wall OR number of rows in wall
where M = approx width of each row OR approx number of bricks in each row
where N * M = Total number of bricks in the wall


Space Complexity : O(M),
where M = Approx number of bricks in each row    
