Question:
You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point [0, 0], and you are given a destination point 
target = [xtarget, ytarget] that you are trying to get to. There are several ghosts on the map with their starting positions given as a 2D 
array ghosts, where ghosts[i] = [xi, yi] represents the starting position of the ith ghost. All inputs are integral coordinates.
Each turn, you and all the ghosts may independently choose to either move 1 unit in any of the four cardinal directions: north, east, south, or west, 
or stay still. All actions happen simultaneously. You escape if and only if you can reach the target before any ghost reaches you. If you reach any 
square (including the target) at the same time as a ghost, it does not count as an escape.
Return true if it is possible to escape regardless of how the ghosts move, otherwise return false.

Example 1:
Input: ghosts = [[1,0],[0,3]], target = [0,1]
Output: true
Explanation: You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.    
    
    
Solution:
The best tactic for any ghost is to reach the target before pacman and block the exit.

Note that we do not require that any ghost reaches pacman (which will never happen on an infinite grid for a single ghost and be much harder to determine for multiple ghosts).
We only require that pacman can or cannot reach the target with optimal ghost strategy.
If any ghost has the same or lower distance to the target, then it can get there first and wait. Pacman cannot reach the target, although he would not necessarily be killed by a ghost.
If pacman is closer to the target than any ghost, he goes there along the most direct path.

Since we are working on a 2D grid, distances are measured as Manhattan distance.

    def escapeGhosts(self, ghosts, target):
        target_dist = abs(target[0]) + abs(target[1])
        
        for r, c in ghosts:
            ghost_target = abs(target[0] - r) + abs(target[1] - c)
            if ghost_target <= target_dist:
                return False
            
        return True
