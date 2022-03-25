Question:
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. 
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected. 
The length of a clear path is the number of visited cells of this path.	


Solution: Optimized BFS (we can think about in terms of a tree with edges having weights) 

	
	
Example[[0,0,0,1,0,0,1,0],
	[0,0,0,0,0,0,0,0],
	[1,0,0,1,1,0,1,0],
	[0,1,1,1,0,0,0,0],
	[0,0,0,0,0,1,1,1],
	[1,0,1,0,0,0,0,0],
	[1,1,0,0,0,1,0,0],
	[0,0,0,0,0,1,0,0]]

Breadth-first search

Good link with animation of BFS: https://www.youtube.com/watch?v=oDqjPvD54Ss

from collections import deque

def breadth_first_search(grid):
    N = len(grid)

    def is_clear(cell):
        return grid[cell[0]][cell[1]] == 0

    def get_neighbours(cell):
        (i, j) = cell
        return (
            (i + a, j + b)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            if a != 0 or b != 0 # boundaries
            if 0 <= i + a < N # boundaries
            if 0 <= j + b < N # boundaries
            if is_clear( (i + a, j + b) ) # places we can step into
        )

    start = (0, 0) # initial point
    goal = (N - 1, N - 1) # destination

    queue = deque()                # define a queue
    if is_clear(start):
        queue.append(start)
    visited = set()                # keep track of seen or visited
    path_len = {start: 1}          # main part tailored inside BFS

    while queue: # queue of which node it should visit first
        cell = queue.popleft()
        if cell in visited:
            continue
        if cell == goal:
            return path_len[cell]
        visited.add(cell)
        for neighbour in get_neighbours(cell):
            if neighbour not in path_len:
                path_len[neighbour] = path_len[cell] + 1  # main part tailored inside BFS # keeping track of path length
            queue.append(neighbour)

    return -1
