Question:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up,down,left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. Given the ball's start 
position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is 
defined by the number of empty spacestraveled by the ball from the start position (excluded) to the destination (included). 
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders 
of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1:
Input 1: a maze represented by a 2D array, Input 2: start coordinate (rowStart, colStart) = (0, 4)     0 0 1 0 0
Input 3: destination coordinate (rowDest, colDest) = (4, 4), Output: 12                                0 0 0 0 0
                                                                                                       0 0 0 1 0
                                                                                                       1 1 0 1 1
                                                                                                       0 0 0 0 0
Solution:  Bellman ford

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        q = collections.deque()
        q.append((start[0],start[1]))
        distances = [[float('inf')]*n for _ in range(m)]
        distances[start[0]][start[1]] = 0
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
         
        while q:
            curr_pos = q.popleft()
            
            for d in dirs:
                x = curr_pos[0]+d[0]
                y = curr_pos[1]+d[1]
                
                step = 1
                while 0<=x<m and 0<=y<n and maze[x][y]==0:
                    x = x+d[0]
                    y = y+d[1]
                    step += 1
                
                if distances[x-d[0]][y-d[1]]>distances[curr_pos[0]][curr_pos[1]]+step-1:
                    q.append((x-d[0],y-d[1]))
                    distances[x-d[0]][y-d[1]]=distances[curr_pos[0]][curr_pos[1]]+step-1
        
        return distances[destination[0]][destination[1]] if distances[destination[0]][destination[1]]!=float('inf') else -1
  
 

Backtracing

DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def shortestDistance(self, maze, start, destination):

        if not maze: return False
        rows = len(maze)
        cols = len(maze[0])
        # min heap: the distance value has to be the first element
        heap = [(0, start[0], start[1])]
        visited = set()
        
        while heap:
            dist, x, y = heapq.heappop(heap)
            # check if visited
            if (x, y) in visited: continue
            visited.add((x, y))
            # check if arrived
            if x == destination[0] and y == destination[1]: return dist
            for d_x, d_y in DIRECTION:
                nxt_x, nxt_y = x + d_x, y + d_y
                cur_dist = dist
                while 0 <= nxt_x < rows and 0 <= nxt_y < cols and \
                    maze[nxt_x][nxt_y] == 0:
                    nxt_x += d_x
                    nxt_y += d_y
                    cur_dist += 1
                # x and y locates @ a wall when exiting the above while loop, so we need to backtrack 1 position
                nxt_x -= d_x
                nxt_y -= d_y

                # Check if the new starting position has been visited
                if maze[nxt_x][nxt_y] not in visited: 
                    heapq.heappush(heap, (cur_dist, nxt_x, nxt_y))
        
        return -1



      
      
   
      
 
