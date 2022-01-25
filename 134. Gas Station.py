Question:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to 
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
the circuit once in the clockwise direction.

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.


Solution: ---
    
https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!    

Brute Force:
    
        int n = gas.length;
        for(int i = 0; i < n; i++){
            int totalFuel = 0;
            int stopCount = 0, j = i;
            while(stopCount < n){
                totalFuel += gas[j % n] - cost[j % n];
                if(totalFuel < 0) break; // whenever we reach -ve
                stopCount++;
                j++;
            if(stopCount == n && totalFuel >= 0) return i; // cover all the stops & our fuel left is 0 or more than that
        return -1;

Time Complexity O(N^2)
Space Complexity O(1)
 
                
Optimized: If we run out of fuel say at some ith gas station. All the gas station between ith and starting point are bad starting point as well.
So, this means we can start trying at next gas station on the i + 1 station. So, hopefully now you understand how this O(N) solution will takes place.                
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start

    

Time Complexity O(N)
Space Complexity O(1)
