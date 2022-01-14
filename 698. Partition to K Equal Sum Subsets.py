# Time:  O(n * s), s is the sum of nums
# Space: O(s)

# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.
#
# Note:
# Both the array size and each of the array element will not exceed 100.
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False

        dp = [False] * (s/2 + 1)
        dp[0] = True
        for num in nums:
            for i in xrange(1, len(dp)):
                if num <= i:
                    dp[i] = dp[i] or dp[i - num]
        return dp[-1]
        
        
 other solution:
 
 
 /*Approach 1: Naive Backtracking
Intuition

Our goal is to break the given array into k subsets of equal sums.
Firstly, we will check if the array sum can be evenly divided into k parts by ensuring that totalArraySum % k is equal to 0.

Now, if the array sum can be evenly divided into k parts, as previously mentioned, we will try to build those k subsets using backtracking.

We will keep a currentSum variable denoting the sum of the current subset. One by one, try to include 
each element from the array that has not already been picked and then make a recursive call to pick the next element.
To keep track of already picked elements we will use a vector (taken) to denote if the element at the 
ith index has already been picked or not.
When we pick the ith element, we will set taken[i] equal to true. Then after we try all combinations, 
we will backtrack and discard the picked element by setting taken[i] equal to false so that it can be picked in a future recursive call.

If we reach the condition currentSum is greater than targetSum, then we cannot reach the target by adding 
more elements to the subset, so there is no need to proceed further; we can just backtrack from here.
If we reach the condition, currentSum equals targetSum, that means we made one subset with the target sum. So 
now we can increment a count variable that counts how many subsets with a sum equal to the target we have made from our array.
When count becomes k, that means we have made k equal sum subsets of our array; hence we can return true.
Finally, when count becomes k - 1, that means we have k equal sum subsets in our array because the totalArraySum 
is divisible by k and the sum of k - 1 subsets will be (k - 1) * targetSum, hence the last subset-sum must also equal 
targetSum. So we can stop at condition count == k - 1 to save some time by skipping a few redundant recursive calls.
*/



class Solution {
public:
    bool backtrack(vector<int>& arr, int count, int currSum, int k, int targetSum, vector<bool>& taken) {
        int n = arr.size();
      
        // We made k - 1 subsets with target sum and last subset will also have target sum.
        if (count == k - 1) { 
            return true;
        }
        
        // Current subset sum exceeds target sum, no need to proceed further.
        if (currSum > targetSum) { 

            return false;
        }
      
        // When current subset sum reaches target sum then one subset is made.
        // Increment count and reset current subset sum to 0.
        if (currSum == targetSum) {
            return backtrack(arr, count + 1, 0, k, targetSum, taken);
        }
        
        // Try not picked elements to make some combinations.
        for (int j = 0; j < n; ++j) {
            if (!taken[j]) {
                // Include this element in current subset.
                taken[j] = true;
                
                // If using current jth element in this subset leads to make all valid subsets.
                if (backtrack(arr, count, currSum + arr[j], k, targetSum, taken)) {
                    return true;
                }
                
                // Backtrack step.
                taken[j] = false;
            }
        }
        // We were not able to make a valid combination after picking each element from the array,
        // hence we can't make k subsets.
        return false;
    }
  
    bool canPartitionKSubsets(vector<int>& arr, int k) {
        int totalArraySum = 0;
        int n = arr.size();
        
        for (int i = 0; i < n; ++i) {
             totalArraySum += arr[i];
        }
      
        // If total sum not divisible by k, we can't make subsets.
        if (totalArraySum % k != 0) { 
            return false;
        }
      
        int targetSum = totalArraySum / k;
        vector<bool> taken(n, false);
      
        return backtrack(arr, 0, 0, k, targetSum, taken);
    }
};
