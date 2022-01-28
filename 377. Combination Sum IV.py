Question:
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations 
that add up to a positive integer target.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are: (1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 3), (2, 1, 1), (2, 2), (3, 1)
Therefore the output is 7.


Solution:  Backtracking or DP
I also solved other versions of this problem using backtracking. The backtracking method is Memory Limit Exceeded when our 
target goes very large, but if this problem requires you output the combinations, the backtracking method is very useful. 
(Only for positive number)

Backtracking:
    
        int combinationSum4(vector<int>& nums, int target) {
            vector<int> path;
            vector<vector<int>> res;
            find(nums,target,path,res);
            return res.size();//or you can change it to output the vector res.
        }

        void find(vector<int>& nums, int target, vector<int>& path, vector<vector<int>>& res){
            if (target == 0) { res.push_back(path); return;}
            else if (target < 0 ) return;
            for(int i = 0;i<nums.size();i++){
                path.push_back(nums[i]);
                find(nums, target - nums[i], path, res);
                path.pop_back();
            }
        }    

DP:    

    def combinationSum4(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()

        for i in xrange(1, target+1):
            for j in xrange(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
                else:
                    break
        return dp[target]
    
    
# Time:  O(nlon + n * t), t is the value of target.
# Space: O(t)
    
