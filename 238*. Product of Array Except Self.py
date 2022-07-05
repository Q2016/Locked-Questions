Question:
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i]. You must write an algorithm that runs in O(n) time 
and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]    

    
    
    
    
   

    
It's more like a IQ test    
    
Solution: Prefix, Postfix
    
We can simply calculate product of the whole array and for each element in nums, divide the product by nums[i]. 
This effectively leaves us with product of whole array except self at each index. We need to take 
care of zeros that may occur in the array -

1. If there are more than one 0s in nums, the result is an array consisting of all 0.
2. If there is a single 0 in nums, then the result is an array consisting of all 0 except at 
the index where there was 0 in nums, which will contain product of rest of array.
3. If there's no 0 in nums, then the result is an array ans where ans[i] = prod / nums[i] 
(prod = product of all elements in nums).


    def productExceptSelf(self, nums):
        res=[1]*(len(nums))
        
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *=nums[i]
            
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            res[i] *=posfix
            postfix *=nums[i]
        return res

    
Time Complexity : O(N)
Space Complexity : O(1)
