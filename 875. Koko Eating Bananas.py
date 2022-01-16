class Solution {
public:
        
    bool feasible(int speed, vector<int>& piles, int h) {
        // return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower        
        int sum=0;
        for (auto pile:piles){
            sum+=(pile - 1) / speed + 1;
        }
        return sum <= h;  // faster
    }
    
    int minEatingSpeed(vector<int>& piles, int h) {    
        int left=1; 
        int right =  *std::max_element(piles.begin(), piles.end());
        while (left < right){
            int mid = left  + (right - left) / 2;
            if (feasible(mid, piles, h)){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left; 
    }
};


Python

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
