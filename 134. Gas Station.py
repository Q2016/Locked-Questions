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







Solution: Greedy
A more complicated version of this question:
    
Got a variation of the gas station problem with the following caveats
The car can go backwards
The solution is to return the maximum distance traveled, rather than simply a boolean    
    
    
    
    
    
class Solution 
{
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) 
    {
        # first of all we need to check whether we've sfficient fuel or not. 
        int total_cost=0,total_fuel=0,n=cost.size();
        for(int i=0;i<n;i++)
        {
            total_cost+=cost[i];
            total_fuel+=gas[i];
        }
        # If the total fuel is lesser than the cost then definitely we can't cover the whole cicular tour.
        if(total_fuel<total_cost)
        {
            return -1;
        }
        
        
        # If the total fuel is sufficient enough to cover the circular tour then definitely an answer exists
        int curr_fuel=0,start=0;  # start with zero fuel.
        for(int i=0;i<n;i++)
        {
            # If at any point our balance/ current fuel is negative that means we can't come to the i'th petrol pump 
            # from the previous pump beacuse our fuel won't allow us to cover such distance. 
            # So we'll make the i'th pump as the start point ans proceed. Simultaneously we'll make the current fuel 
            # to be 0 as we're starting freshly.
            if(curr_fuel<0)
            {
                start=i;
                curr_fuel=0;
            }
            # at any station we'll fill petrol and pay the cost to go to the next station . so current fuel would be the following.
            curr_fuel+=(gas[i]-cost[i]);
        }
        return start;
    }
};

    

Time Complexity O(N)
Space Complexity O(1)
