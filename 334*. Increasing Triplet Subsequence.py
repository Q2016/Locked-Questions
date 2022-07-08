Question:
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and 
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.














One can solve using the LIS (longest increasing subsequence) in O(nlogn)
https://www.youtube.com/watch?v=QBiEJul9bUk
    
def increasingTriplet(self, nums):
    dp=[]
    
    for num in nums:
        index=bisect_left(dp, num) # find index of num in dp
         if index<len(dp):
            dp[index]=num
         else:
            dp.append(num)
            
         if len(dp)>2:
            return True
    
    return False
        


Main Solution: (Havent I seen this before? repeatetive? maybe in the easy Leetcode question)

But how do we know that this solves the subarray and not subsequence?
    
    def increasingTriplet(self, nums):
        smallest_num=second_smallest_num=sys.maxsize
        
        for num in nums:
            if num<=smallest_num:
                smallest_num=num
            elif num<=second_smallest_num:
                second_smallest_num=num
            else:
                return True
            
        return False

Time is O(n)
