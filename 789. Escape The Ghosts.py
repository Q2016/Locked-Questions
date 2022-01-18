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
