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






Lets' say we start from the origine, and explore points around, how different is seeing a '1' from a '0' in our treatment of points?

Solution: DFS
This is similar to 1020. Number of Enclaves, Flood Fill
   
Intuition
class Solution(object):
    def closedIsland(self, grid):
	
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, val):
            if 0<=i<m and 0<=j<n and grid[i][j]==0:
                grid[i][j] = val
                dfs(i, j+1, val)
                dfs(i+1, j, val)
                dfs(i-1, j, val)
                dfs(i, j-1, val)
        
        for i in xrange(m):
            for j in xrange(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0: # flood-fill islands on the boundary
                    dfs(i, j, 1)
                
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0: # what remains is the center of each island? 
                    dfs(i, j, 1)
                    res += 1 # we count the left over centers
                    
        return res


BFS:

https://www.youtube.com/watch?v=uwzCdK9M1PY

Class Solution:
	
     def ClosedIsland(self, grid):
	ans=0
	queue=[]
	m=len(grid)
	n=len(grid[0])
	
	directions=((-1,0),(1,0),(0,-1),(0,1))
	
	for i in range(m):
	   for j in range(n):
	      if grid[i][j]==0:
		queue.append((i,j))
		grid[i][j]=1
		isClosed=True
		
		while queue:
		   cur_i, cur_j=queue.pop()
		   
		   if cur_i in (0, m-1) or cur_j in (0, n-1):
		      isClosed=False
		   for d in directions:
		      new_i=i+d[0]
		      new_j=j+d[1]
			
		      if 0<=new_j< m and 0 <=new_j<n and grid[new_i][new_j]==0:
			queue.append(new_i, new_j)
			grid[new_i][new_j]=1
			
	     if isClosed:
		ans+=1
	return ans
			


200. NUMBER OF ISLANDS

Class Solution:
  def numIslands(self, grid):
      if not grid:
	return 0

      rows, cols =len(grid), len(grid[0])
      visited=set()
      islands=0
	
      def bfs(r,c):
	 q=collections.deque()
	 visit.add((r,c))
	 q.append((r,c))	
	 while q:
	    row, col =q.popleft()
	    directions=[[1,0],[-1,0],[0,1],[0,-1]]
	    for dr, dc in directions:
		r,c =row+dr, col+dc
		if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit):
		   q.append((r,c))
		   visit.add((r,c))

      for r in range(rows):
	 for c in range(cols):
	    if grid[r][c]=="1" and (r,c) not in visit: # if the position is not visited before
		bfs(r,c) # visit the layers around it
		islands+=1 # count unvisited '1's  as the number of islands
      return islands




Complexity:

DFS' time complexity is proportional to the total number of vertexes and edges of the graph visited. In that case, 
there are N*M vertexes and slightly less than 4*N*M edges, their sum is still O(N*M).

Why so: because we process each edge exactly once in each direction. Situation where recursive call is immediately terminated does not 
matter as time spent for that call can be accounted for on the call site; and there is at most once call for each directed edge, hence O(N*M).

BFS' time complexity is quite similar. Maximal length of the queue does not matter at all because at no point we 
examine it in a whole. Queue only gets "append" and "remove first" queries, which can be processed in constant time regardless of queue's size. 
If we need to check whether a vertex was already visited, we do so in constant time.

Worst-case space complexity for DFS is Theta(N*M): just take any "snake-wise" maze:

......
#####.
......
.#####
......
Here DFS will be forced to traverse the path in whole before it stops and starts freeing up the stack. However, in no situation 
there will be more than N*M+1 elements on the stack.

Worst-case space complexity for BFS is indeed not O(max(N, M)): it's Theta(N*M) even when we're considering simple grid.
