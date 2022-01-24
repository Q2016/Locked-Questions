Question:
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 
4-directionally connected group of 0s and a closed island is an island totally 
(all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],
	       [1,0,0,0,0,1,1,0],
	       [1,0,1,0,1,1,1,0],
	       [1,0,0,0,0,1,0,1],
	       [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).	


Solution: DFS
   
Intuition
The idea is simple. We want to perform a DFS on the matrix to find the connected component of 0s. 
Call a connnected component valid if none of its element lies on the border of the matrix. 
It is clear that we need to find all the valid connected component.
We consider a cell with value 1 as a blocked cell and a cell with value 0 an empty cell. 
We also need to maintain a visited matrix, but we can just modify the input matrix, 
setting each 0 to 1 after we have visited it.
Now, all that remains is to start a DFS from the first unvisited 0. This DFS call would cover 
all the elements of this connected component (As per the property of DFS). Now, we just need 
to keep track whether any element in this connected component touches the boundary of the matrix or not. 
If it does, this connected component becomes invalid. If none of the elements touch the boundary, 
it means that it is surrounded by1s on all the sides. Hence, we increment the counter for answer.
To check whether any element in the connected componenet is a terminal node, we can just maintain a 
boolean variable called terminal and set it to true whenver we see a terminal node during the DFS call. 
After the DFS, we only increment the counter if terminal is set to false.
How do we look out for terminal nodes? Note that if we hit a terminal node, we are also going to 
hit an out of bound neighbour. Hence, if we see an out of bounds index, we update the terminal to True


    int closedIsland(vector<vector<int>>& g) {
	//count the number
        int count = 0; 
        for(int i = 0;i < g.size();i++){
           for(int j = 0;j < g[0].size();j++){
                if(g[i][j] == 0){
                       count += dfs(g,i,j);
                }
           }
        }
        return count;
    }
    
    
    int dfs(vector<vector<int>>& g,int row,int col){
         if(row < 0 || row >= g.size() || col < 0 || col >= g[0].size()){
                 return 0;//if we meet the edge return 0;
         }
         if(g[row][col] == 1){
                 return 1;//if we meet 1 return 1;
         }
         g[row][col] = 1;
         int up = dfs(g,row-1,col);
         int down = dfs(g,row+1,col);
         int left = dfs(g,row,col-1);
         int right = dfs(g,row,col+1);
         return up & down & left & right;//any of the side meet the edge,is not a island;
    }





