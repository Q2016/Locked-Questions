Question:
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's 
left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. The island is partitioned into a grid of square 
cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring 
cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both 
the Pacific and Atlantic oceans.

Example 1:
Input: heights = [
	[1,2,2,3,$5],
Pacific	[3,2,3,$4,$4],  Atlantic
 Ocean	[2,4,$5,3,1],   Ocean
	[$6,$7,1,4,5],
	[$5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]], shown with '$' above	


Solution: DFS
https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1126938/Short-and-Easy-w-Explanation-and-diagrams-or-Simple-Graph-traversals-DFS-and-BFS
  
Naive approach takes O((mn)^2). We have to consider each cell and find if it is reachable to both the oceans which is not efficient. DFS solution:
We can classify cells based on their ocean reach: -None -Pacific -Atlantic -Both Pacific and Atlantic
Now, if we start from the cells connected to altantic ocean and visit all cells having height greater than current cell 
(water can only flow from a cell to another one with height equal or lower), we are able to reach some subset of cells (let's call them A).
Next, we start from the cells connected to pacific ocean and repeat the same process, we find another subset (let's call this one B).
The final answer we get will be the intersection of sets A and B (A ∩ B).
                                                                                                                                                                                                                        
    # denotes cells reachable starting from atlantic and pacific edged cells respectively
    # atlantic: bool vector intitalize with False
    # pacific: bool vector intitalize with False
    # ans: matrix int    
    
    def pacificAtlantic(mat) :
        if size(mat)==0: 
	    return ans
        m = size(mat) 
	n = size(mat[0])
	# perform dfs from all edge cells (ocean-connected cells)
        for i in range(m): 
		dfs(mat, pacific, i, 0) 
		dfs(mat, atlantic, i, n - 1)
        for i in range(m):  
		dfs(mat, pacific, 0, i) 
		dfs(mat, atlantic, m - 1, i)           
        return ans
    													      
    def dfs(mat, visited, i, j):        
        if (visited[i][j]):
		return
        visited[i][j] = True
	#if cell reachable from both the oceans, insert into final answer vector
        if (atlantic[i][j] and pacific[i][j]): 
		ans.append([i, j])    
	# dfs from current cell only if height of next cell is greater
	if(i + 1 <  m and mat[i + 1][j] >= mat[i][j]) dfs(mat, visited, i + 1, j)  #⬇️ 
        if(i - 1 >= 0 and mat[i - 1][j] >= mat[i][j]) dfs(mat, visited, i - 1, j)  #⬆️ 
        if(j + 1 <  n and mat[i][j + 1] >= mat[i][j]) dfs(mat, visited, i, j + 1)  #➡️
        if(j - 1 >= 0 and mat[i][j - 1] >= mat[i][j]) dfs(mat, visited, i, j - 1)  #⬅️

													      
													      
Time Complexity : O(M*N), in worst case, all cells are reachable to both oceans and would be visited twice. This case can occur when all elements are equal.
Space Complexity : O(M*N), to mark the atlantic and pacific visited cells.

