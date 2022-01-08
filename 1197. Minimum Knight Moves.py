https://goodtecher.com/leetcode-1197-minimum-knight-moves/

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a 
cardinal direction, then one square in an orthogonal direction.
<image>
Return the minimum number of steps needed to move the knight to the square [x, y]. 




A Knight movement can be summarised as below in terms of coordinate increments considering a current position as x, y:
1. (x-1, y+2) ==> (-1, +2)
2. (x+1, y+2) ==> (+1, +2)
3. (x+2, y+1) ==> (+2, +1)
4. (x+2, y-1) ==> (+2, -1)
5. (x+1, y-2) ==> (+1, -2)
6. (x-1, y-2) ==> (-1, -2)
7. (x-2, y-1) ==> (-2, -1)
8. (x-2, y+1) ==> (-2, +1)
As we see at a given coordinate the Knight can move to 8 different positions. From there it can move next 
seven(1 will be the start position) places. The minimum number of steps can be found using BFS traversal.

Also since the initial position is at (0, 0) we can restrict the moves in the positive region or first 
quadrant. We can do so if we take the absolute value of the target coordinate. We can do so since we 
only need to find the minimum number of steps. Also, we keep track of visiting positions.

Code Implementation:

  
  def minKnightMoves(x, y):
    x , y = abs(x), abs(y)
    possible_moves = [
        (1, 2), (2, 1), (-1, 2), 
        (-2, 1), (-1, -2), (-2, -1), 
        (1, -2), (2, -1)
        ]
    
    que = collections.deque([[0, 0, 0]])
    visited = set()
    visited.add((0, 0))
    while que:
        qx, qy, d = que.popleft()
        if x == qx and y == qy:
            return d
        for dx, dy in possible_moves:
            nx, ny = qx + dx, qy + dy
            if (nx, ny) not in visited and nx >=-2 and ny>=-2:
                visited.add((nx, ny))
                que.append([nx, ny, d + 1])
                
                
Complexity Analysis:
Time complexity: O(max(x²,y²)). This is due to the fact that every place the Knight covers a radius of 2x or 2y. 
  The number of cells inside this circle is the max of x² or y².
Constant space: O(max(x²,y²)) at any level we store all nodes that can be reached from the previous level.
