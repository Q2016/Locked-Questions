Question:
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
and return the product. A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.    
    
    
Solution: Kadane-like algorithm   
    

    def maxProduct(self, nums: List[int]) -> int:

        max_num=1
        min_num=1
        
        for n in nums:
            temp=max_num
            max_num=max(max_num*n, min_num*n, n)
            min_num=min(temp*n, min_num*n, n)
            print(max_num)
        return max(max_num, max(nums))
