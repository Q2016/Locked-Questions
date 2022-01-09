Idea

By using BFS, we can generate all possible of locks, initialize with "0000".
For each step, we can generates neighbors of current lock state (by turning clockwise or 
counter-clockwise of 4 circular wheels) and go to its neighbors if neighbor is not in our deadends.
If we meet the target then the current steps is minimum number of turns to open the target lock.

Complexity

Time: O(N^2 * A^N + D), where N is number of dials (4 in our case), A is number of 
alphabet (10 in our case), D is size of deadends.
There are 10^4 possible combinations => O(A^N)
To get neighbors, for each combination, we are looping 4 times (which is N) and in each 
iteration, there are substring operations which costs O(N) => O(N^2)
Total O(D) to create the hashset
Space: O(A^N), in worst case equal to number of combinations.


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff + 10) % 10
                    yield code[:i] + str(y) + code[i + 1:]

        deadSet = set(deadends)
        if "0000" in deadSet: return -1
        q = deque(["0000"])
        steps = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for nei in neighbors(curr):
                    if nei in deadSet: continue
                    deadSet.add(nei)  # Marked as visited
                    q.append(nei)
            steps += 1

        return -1
