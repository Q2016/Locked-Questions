Question:
Suppose you are at a party with n people and one celebrity. The definition of a celebrity is that all the other n - 1 people know 
him but he does not know any of them. You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a 
functionint findCelebrity(n), your function should minimize the number of calls to knows.


Solution:
One way to solve this problem is by taking each node, check if other nodes know this node, and 
check if this node does not know any other nodes. If yes, this is the required celebrity. 
Otherwise, continue checking the other nodes.

    def findCelebrity(self, n: int) -> int:
        def is_celeb(celeb):
            for other in range(n):
                if other == celeb:
                    continue
                if not knows(other, celeb) or knows(celeb, other):
                    return False
            return True
        for i in range(n):
            if is_celeb(i):
                return i
        return -1
        
Complexity analysis.
Time Complexity
We are visiting each node and comparing it with other nodes to check if it's a celebrity. Hence the time complexity is O(N²).
Space Complexity.
Since we are not using any extra data structure to store intermediate results, the space complexity is O(1).

Let us see if we can improve the time complexity.
In the earlier solution, we are taking each node, and we were checking if all the nodes know the current 
node and if the current node does not know the other nodes.
Let us try to split it into two parts. First, let us check if we can find a possible celebrity. We start 
with node “0”, we would check if all other nodes know this node and if this node does not know all other 
nodes. If at any point the above conditions turn False, we will consider a new candidate for the celebrity status.
Once we finish the loop, we will again run a loop to check if all node is aware of current candidate node 
and current candidate node is not aware of other nodes. If the above condition is False, we will return 
-1 else we will return the candidate.
Let us look into the code snippet.

    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(i, candidate) and not knows(candidate, i):
                continue
            else:
                candidate = i
        for j in range(candidate):
            if not knows(j, candidate) or knows(candidate, j):
                return -1
        return candidate
        
Complexity analysis.
Time Complexity
We are visiting each node and check if they are probable candidates. Once we get a probable 
candidate, we check if they are a celebrity. Hence the time complexity is O(N).
Space Complexity.
Since we are not using any extra data structure to store intermediate results, the space complexity is O(1).
