class Solution {
public:
    bool feasible(int days, vector<int>& bloomDay, int m, int k){
        int bonquets=0; 
        int flowers = 0;
        
        for (auto bloom : bloomDay){
            if (bloom > days){
                flowers = 0;
            }else{
                bonquets += (flowers + 1) / k;
                flowers = (flowers + 1) % k;
            }
        }
        return bonquets >= m;
    }
        
                    
    int minDays(vector<int>& bloomDay, int m, int k) {
        
        if (bloomDay.size() < m * k) return -1;
        
        int left= 1; 
        int right =*std::max_element(bloomDay.begin(), bloomDay.end());
        while (left < right){
            int mid = left + (right - left) / 2;
            if (feasible(mid, bloomDay, m, k)){
                right = mid;
                }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
