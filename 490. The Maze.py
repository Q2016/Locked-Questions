Question:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left 
or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of 
the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1
Input 1: a maze represented by a 2D array, Input 2: start coordinate (rowStart, colStart) = (0, 4), Input 3: destination coordinate (rowDest, colDest) = (4, 4)
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
    
        
Solution:  Bellman ford  
https://medium.com/tech-life-fun/leet-code-490-the-maze-graphical-explained-python3-solution-b4369bbf4050    
 https://www.youtube.com/watch?v=e_75Z90j0IM
    
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        visited = []
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]    
        dest = (destination[0],destination[1])
        
        def rollFrom(pos):
            newStops = []
            for d in dirs:
                newX = pos[0]
                newY = pos[1]
                while(True): #rolling
                    possibleNewX = newX + d[0] 
                    possibleNewY = newY + d[1]                     
                    
                    if (possibleNewX >= 0 and possibleNewX < len(maze) ) and \
                        (possibleNewY >= 0 and possibleNewY < len(maze[0])) and \
                        (maze[possibleNewX][possibleNewY] != 1):
                        
                        newX = possibleNewX
                        newY = possibleNewY
                        continue
                    else:
                        break
                newStop = (newX, newY)
                if newStop == dest:
                    return True
                newStops.append(newStop)
                
            visited.append(pos)
                
            for newStop in newStops:            
                if newStop not in visited:
                    if rollFrom(newStop):
                        return True                
            return False
            
        startPos = (start[0], start[1])        
        return rollFrom(startPos)    

    
Time & Space Complexity
Assuming the maze is M*N, actually I need to touch nearly every cell (except walls), 
the time spent is directly related to the scale of M*N. Therefore, the time complexity is O(M*N).
I use a visited list to store all stop positions the algorithm will run into. Also, since 
I use recursive calls of rollFrom(), each time execution stack will used when a call is invoked. 
Actually both are related since normally a stop will lead to 4 rollFrom() so space complexity is 
directly related to the number of stops. In a M*N maze, the stop number is also directly scaling 
along with the size, so space complexity is also O(M*N).     
