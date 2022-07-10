Question:
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply 
available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.
If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or 
both buckets by the end. Operations allowed: Fill any of the jugs with water. Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
 
Example 1:
Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example     
Example 2:
Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false
Example 3:
Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true

 
 
 
 
 
 
 
 
 
 
Solution: BFS
 
we have 6 different states we can attain :-
1.Fill jug 1.
2.Fill jug 2.
3.Empty Jug 1.
4.Empty jug 2
5.pour from jug2 to jug1
6.pour from jug1 to jug2.
Use this 6 states on each node and add those nodes in queue which we havent already had.
Here (0,0) is a little deviated from its right place. Please bear it.
                     (0,0)
                      / \
                  (3,0)   (0,5)
                   / \       |
              (3,5)  (0,3)   (3,2)
               |       |       |
              ()     (3,3)   (0,2) 
                       |       |
                     (1,5)   (2,0)
                               |
                             (2,5)
                               |
                             (3,4) <---the answer



We can store these unique combinations in a Set and use a queue for BFS but a little better option would be to
Store unique total instead of just storing unique combinations in HashSet. Rest is just BFS.



    def canMeasureWater(self, jug1, jug2, target):

        if jug1 > jug2: # jug1 smaller than jug2 always
            temp = jug1;
            jug1 = jug2;
            jug2 = temp;
            
        if z > x + y:
            return False;
        
        # set the initial state will empty jars;
        queue = [(0, 0)];
        visited = set((0, 0));
        while len(queue) > 0:
            a, b = queue.pop(0);
            if a + b == target:
                return True;
            
            states = set()
            
            states.add((jug1, b)) # fill jar x;
            states.add((a, jug2)) # fill jar y;
            states.add((0, b)) # empty jar x;
            states.add((a, 0)) # empty jar y;
            states.add((min(jug1, b + a), 0 if b < jug1 - a else b - (jug1 - a))) # pour jar y to x;
            states.add((0 if a + b < jug2 else a - (jug2 - b), min(b + a, jug2))) # pour jar x to y;

            for state in states:
                if state in visited:
                    continue;
                queue.append(state)
                visited.add(state);
                
        return False;
       
Time complexity of BFS is O(x + y) which can be treated as linear (Because there are only 2x + 2y possible states.).        
       
