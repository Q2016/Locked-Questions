
// for binary search look at: 
//[Python/ Clear explanation] Powerful Ultimate Binary Search Template. Solved many problems.

class Solution {
public:
    
    bool feasible(int capacity, vector<int>& weights, int D){
        int days = 1;
        int total = 0;
        for (auto weight: weights){
            total += weight;
            if (total > capacity){  // too heavy, wait for the next day
                total = weight;
                days += 1;
                if (days > D){  // cannot ship within D days
                    return false;
                }
            }
        }
        return true;
    }
    
    
    int shipWithinDays(vector<int>& weights, int D) {
        
        int left=0; 
        for(auto w:weights){// max
            if (w>left) left=w;
        }
        //cout<<left;
        
        int right = std::accumulate(weights.begin(), weights.end(), 0);
        //cout<<right;
        
        while (left < right){
            int mid = left + (right - left) / 2;
            if (feasible(mid, weights, D)){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return left;
    }
    
};

/*
Explanation
Given the number of bags,
return the minimum capacity of each bag,
so that we can put items one by one into all bags.

We binary search the final result.
The left bound is max(A),
The right bound is sum(A).


More Good Binary Search Problems
Here are some similar binary search problems.
Also find more explanations.
Good luck and have fun.

Minimum Number of Days to Make m Bouquets
Find the Smallest Divisor Given a Threshold
Divide Chocolate
Capacity To Ship Packages In N Days
Koko Eating Bananas
Minimize Max Distance to Gas Station
Split Array Largest Sum
*/
