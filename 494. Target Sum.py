Question:
You are given an integer array nums and an integer target. You want to build an expression out of nums by adding one of 
the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3, Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3    






Solution: Brute force- recursive
    
The brute force approach is based on recursion. We need to try to put both the + and - symbols at every location in the 
given numsnums array and find out the assignments which lead to the required result S.
For this, we make use of a recursive function calculate(nums, i, sum, S), which returns the assignments leading to the sum S, starting from the i^{th}
index onwards, provided the sum of elements up to the i^{th} element is sumsum. This function appends a + sign and a - sign both 
to the element at the current index and calls itself with the updated sumsum as sum + nums[i] and sum - nums[i] respectively along 
with the updated current index as i+1. Whenever we reach the end of the array, we compare the sum obtained with S. If they are equal, 
we increment the countcount value to be returned. Thus, the function call calculate(nums, 0, 0, S) returns the required number of assignments.

    count = 0;
    def findTargetSumWays(nums, S) :
        calculate(nums, 0, 0, S)
        return count
     
    def calculate(nums, i, sum, S) :
        if (i == len(nums)) :
            if (sum == S) :
                count++
        else :
            calculate(nums, i + 1, sum + nums[i], S)
            calculate(nums, i + 1, sum - nums[i], S)
        

Complexity Analysis
Time complexity: O(2^n)
Space complexity: O(n). The depth of the recursion tree can go up to n.    
    
Adding memoization:
    
public class Solution {
    int total;
    
    public int findTargetSumWays(int[] nums, int S) {
        total = Arrays.stream(nums).sum();
        
        int[][] memo = new int[nums.length][2 * total + 1];
        for (int[] row : memo) {
            Arrays.fill(row, Integer.MIN_VALUE);
        }
        return calculate(nums, 0, 0, S, memo);
    }
    
    public int calculate(int[] nums, int i, int sum, int S, int[][] memo) {
        if (i == nums.length) {
            if (sum == S) {
                return 1;
            } else {
                return 0;
            }
        } else {
            if (memo[i][sum + total] != Integer.MIN_VALUE) {
                return memo[i][sum + total];
            }
            int add = calculate(nums, i + 1, sum + nums[i], S, memo);
            int subtract = calculate(nums, i + 1, sum - nums[i], S, memo);
            memo[i][sum + total] = add + subtract;
            return memo[i][sum + total];
        }
    }
}    
        
Complexity Analysis:
Time complexity: O(t⋅n) 
Space complexity: O(t⋅n)
