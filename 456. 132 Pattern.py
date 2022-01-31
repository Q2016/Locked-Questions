Question:
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
such that i < j < k and nums[i] < nums[k] < nums[j]. Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.


Solution: 
https://leetcode.com/problems/132-pattern/discuss/94089/Java-solutions-from-O(n3)-to-O(n)-for-%22132%22-pattern-(updated-with-one-pass-slution)

I. Naive O(n^3) solution
The naive O(n^3) solution is a no-brainer --- simply check every (i, j, k) combination to see if there is any 132 pattern.

public boolean find132pattern(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            for (int k = j + 1; k < nums.length; k++) {
                if (nums[i] < nums[k] && nums[k] < nums[j]) return true;
            }
        }
    }
    return false;
}

II. Improved O(n^2) solution
To reduce the time complexity down to O(n^2), we need to do some observations. In the naive solution above, let's assume we have index j fixed, 
what should index i be so that it is most probable we will have a 132 pattern? 
The answer lies in the fact that once the first two numbers nums[i] and nums[j] are fixed, we are up to find the third number nums[k] which 
will be within the range (nums[i], nums[j]) (the two boundaries are exclusive). Intuitively the larger the range is, the more likely there 
will be a number "falling into" it. Therefore we need to choose index i which will maximize the range (nums[i], nums[j]). Since the upper 
bound nums[j] is fixed, this is equivalent to minimizing the lower bound nums[i]. 

public boolean find132pattern(int[] nums) {
    for (int j = 0, min = Integer.MAX_VALUE; j < nums.length; j++) {
         min = Math.min(nums[j], min);
         if (min == nums[j]) continue;
         
         for (int k = nums.length - 1; k > j; k--) {
             if (min < nums[k] && nums[k] < nums[j]) return true;
         }
     }
     
     return false;
}

III. Optimized O(n) solution
Assume we're currently scanning (from the end) the element with index j, our task is to find two elements nums[i] and nums[k] to determine 
if there exists a 132 pattern, with i < j < k. The left element nums[i], as it has been shown in part II, will be chosen as arr[j], 
the minimum element of subarray nums[0, j). What about the right element nums[k]?
First note we are only interested in elements that are greater than arr[j], so it is sensible to maintain only those elements. Second, among 
all these qualified elements, which one will be the most probable to fall into the range (nums[i], nums[j])? I would say it is the smallest 
one (i.e., if the smallest one is out of the range, all others will also be out of range). So to sum up, the "useful" information for current 
index j will be a collection of scanned elements that are greater than arr[j], and nums[k] will be chosen as the smallest one if the collection is not empty.

public boolean find132pattern(int[] nums) {
    int[] arr = Arrays.copyOf(nums, nums.length);

    for (int i = 1; i < nums.length; i++) {
        arr[i] = Math.min(nums[i - 1], arr[i - 1]);
    }
    
    for (int j = nums.length - 1, top = nums.length; j >= 0; j--) {
        if (nums[j] <= arr[j]) continue;
        while (top < nums.length && arr[top] <= arr[j]) top++;
        if (top < nums.length && nums[j] > arr[top]) return true;
        arr[--top] = nums[j];
    }
        
    return false;
}
