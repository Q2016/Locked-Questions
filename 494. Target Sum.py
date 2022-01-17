class Solution {
public:
    
    int findTargetSumWays(vector<int>& nums, int target){
         int index = nums.size() - 1;
         int curr_sum = 0;
         return dp(nums, target, index, curr_sum);
    }
    
    int dp(vector<int>& nums, int target, int index, int curr_sum){
        // Base Cases
         if (index < 0 and curr_sum == target){
             return 1;
         }
         if (index < 0){
             return 0;
         }

        // Decisions
         int positive = dp(nums, target, index-1, curr_sum + nums[index]);
         int negative = dp(nums, target, index-1, curr_sum + -nums[index]);

         return positive + negative;
    }
};
