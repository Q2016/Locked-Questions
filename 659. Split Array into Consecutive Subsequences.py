Question:
You are given an integer array nums that is sorted in non-decreasing order. Determine if it is possible to split nums into one or 
more subsequences such that both of the following conditions are true: Each subsequence is a consecutive increasing sequence. 
All subsequences have a length of 3 or more. Return true if you can split nums according to the above conditions, or false otherwise. 

Example 1:
Input: nums = [1,2,3,3,4,5], Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3 and 3, 4, 5  








Solution: DP
  
class Solution {
public:
    bool isPossible(vector<int> &nums) {
        int n = nums.size();
        int start = 0;

        for (int i = 1; i < n; i++) {
            // Check possibility of a valid segment starting at index start and ending at index i - 1.
            if (nums[i] - nums[i - 1] > 1) {
                if (!isSegmentValid(nums, start, i - 1)) {
                    return false;
                }
                // Update the starting index of the next segment.
                start = i;
            }
        }
        // Check for the last segment
        return isSegmentValid(nums, start, n - 1);
    }
    
private:
    bool isSegmentValid(vector<int> &nums, int start, int end) {
        int noOfUniqueNumbers = nums[end] - nums[start] + 1;

        // Count frequency of each number in the current segment.
        vector<int> frequency(noOfUniqueNumbers);
        
        for (int i = start; i <= end; i++) {
            frequency[nums[i] - nums[start]]++;
        }
        // lengthOneSubsequences[i] holds count of subsequences of length 1 ending with index i
        vector<int> lengthOneSubsequences(noOfUniqueNumbers);

        // lengthTwoSubsequences[i] holds count of subsequences of length 2 ending with index i
        vector<int> lengthTwoSubsequences(noOfUniqueNumbers);

        // totalNoOfSubsequences[i] holds count of all subsequences ending with index i
        vector<int> totalNoOfSubsequences(noOfUniqueNumbers);

        lengthOneSubsequences[0] = totalNoOfSubsequences[0] = frequency[0];

        for (int i = 1; i < noOfUniqueNumbers; i++) {

            // If the frequency[i] is less than total number of subsequences ending with i - 1,
            // we do not have enough subsequences where we can put i.
            if (frequency[i] < lengthOneSubsequences[i - 1] + lengthTwoSubsequences[i - 1]) {
                return false;
            }
            
            //Total number of subsequences of length 2 can be obtained by adding i 
            //to subsequences of length 1 ending with i - 1.
            lengthTwoSubsequences[i] = lengthOneSubsequences[i - 1];
            
            // For the remaining i valued numbers we can either add them to an existing subsequence
            // or create a new one. We first try to add them to the existing subsequences ending 
            // with i - 1. If there are not enough of such subsequences, we start a new subsequence.
            // The existing subsequences ending with i - 1 is denoted by totalNoOfSubsequences[i - 1];
            lengthOneSubsequences[i] = max(0, frequency[i] - totalNoOfSubsequences[i - 1]);
            totalNoOfSubsequences[i] = frequency[i];
        }

        // If there is no remaining subsequence of length one or two, we can return true. 
        // Otherwise, return false.
        return lengthOneSubsequences[noOfUniqueNumbers - 1] == 0 && 
               lengthTwoSubsequences[noOfUniqueNumbers - 1] == 0;
    }
};  


Complexity Analysis

Time complexity: O(N)
At one glance, it might look that the isSegmentValid function takes O(N) time. However, if you look at the value of noOfUniqueNumbers, 
you will realize that the for loop in the isSegmentValid function iterates over each unique element in the nums array only once. 
For the given array of size N there can be at max N unique elements. Thus the overall time complexity is O(N).

Space complexity: O(N)
In the isSegmentValid function four arrays of size at max N is used. So the space complexity is O(N * 4) = O(N) in Big O notation.
