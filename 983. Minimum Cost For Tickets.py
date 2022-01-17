There are other solutions as well in
https://leetcode.com/problems/minimum-cost-for-tickets/solution/


class Solution {
public:
 int sub(vector<int> &day, vector<int> &cost, int si)		// si denotes starting index
    {
        int n = day.size();
        if(si>=n)   return 0;
        
        int cost_day = cost[0] + sub(day , cost , si+1);
        
        int i;
        for(i = si ; i<n and day[i]<day[si]+7 ; i++);   //skip till ith day is curr_day+7 as we are buying week pass
        int cost_week = cost[1] + sub(day, cost, i);
        
        for(i = si ; i<n and day[i]<day[si]+30 ; i++);   //skip till ith day is curr_day+30 as we are buying month pass
        int cost_month = cost[2] + sub(day, cost, i);      
        
        return min({cost_day, cost_week , cost_month  });
    }
    
    int mincostTickets(vector<int>& days, vector<int>& costs) {        
        return sub(days,costs,0);
    }
};
