class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if len([1 for i in nums if i<k])==0:
            return 0
        
        
        left=right=0
        product=1
        n=0
        while left<len(nums):
            #print(right)
            product*=nums[right]
            if product>=k or right==len(nums)-1:
                left+=1
                product=1
                right=left-1
            
            right+=1
            n+=1
                
        return n
