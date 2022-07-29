Question:
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning 
and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, 
or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".    






Decision tree, but how do we know we get the shortest? we apply BFS, some tircks with mod for adding 1+9%10 works but counter clockwise
1-9%Null so what we do is 1-9+10%2

Solution: 
    https://www.youtube.com/watch?v=Pzg3bCDY87w
        
class Solution:
    def openLock(self, deadends, target):
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res=[]
            for i in range(4):
                digit=str((int(lock[i])+1)% 10)
                lock=lock[:i]+digit+lock[i+1:]
                
        q=deque()
        q.append(["0000",0]) # [lock, turns]
        visit=set(deadends)
        while q:
            lock, turns=q.popleft()
            if lock==target:
                return turns
            for child in cildren(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns+1])
        return -1
    
    
    
    
    
    
    BFS
By using BFS, we can generate all possible of locks, initialize with "0000".
For each step, we can generates neighbors of current lock state (by turning clockwise or 
counter-clockwise of 4 circular wheels) and go to its neighbors if neighbor is not in our deadends.
If we meet the target then the current steps is minimum number of turns to open the target lock.


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
                curr = q.popleft()   #  Never realized that pop(0) takes O(N) in Python!!!!
                if curr == target:
                    return steps
                for nei in neighbors(curr):
                    if nei in deadSet: continue
                    deadSet.add(nei)  # Marked as visited
                    q.append(nei)
            steps += 1

        return -1

    
    
Complexity
worst possible casse we have to visit all the combinations so in n=4 we have O(10000) 
Space will ve also O(10000) for the visited variable
