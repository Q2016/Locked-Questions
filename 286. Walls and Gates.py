You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle. 0 - A gate. INF - Infinity means an empty room. We use the 
value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is 
less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is 
impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  
  
  Methodology
This question can be solved by Depth First Search.

To find the neareast distance to the gate of each empty cell, we can start from the gate 
and use dfs to walk through each reachable cell. This will also give the distance for the 
current cell to the current gate. If there is another gate, we will use the dfs again to walk 
through each empty cell again and if the current cell’s distance is more close to the current gate, 
then we update the distance for the current cell.


def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        row = len(rooms)
        col = len(rooms[0])
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(x,y,dis):
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and rooms[nx][ny]>rooms[x][y]:
                    rooms[nx][ny]=dis+1
                    dfs(nx,ny,dis+1)
        
        for x in range(row):
            for y in range(col):
                if rooms[x][y] == 0:
                    dfs(x,y,0)
                    

We iterate each cell will cost O(m*n) where m*n is the size of the 2D list. 
Each cell will also iterate four directions O(m*n*4). In total O(4*m*n)
