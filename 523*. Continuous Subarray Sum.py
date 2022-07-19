Question:
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two 
whose elements sum up to a multiple of k, or false otherwise. An integer x is a multiple of k if there exists an integer 
n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

   
    
    
    
    
    
    
    
    
    
Solution: similar to 2-sum problem

https://www.youtube.com/watch?v=OKcrLfR-8mE
    
class Solution:
    def checkSubarraySum(self, nums):
        reminder={0:-1}
        total=0
        
        for i, n in enumerate(nums):
            total+=n
            r=total%k
            if r not in remainder:
                remainder[r]=i
            elif i-remainder[r]>1:
                return True
        return False
    
    
    
    
    
    
    
    
    
    
This is one of those magics of remainder theorem: (a+(n*x))%x is same as (a%x)
Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. So we just need to use a 
dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. 
Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

    def checkSubarraySum(self, nums, k):

        dic = {0:-1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False
                         
Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
                         
