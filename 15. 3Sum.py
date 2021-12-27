# https://www.youtube.com/watch?v=jzZsG8n2R9A



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums=sorted(nums)# or nums.sort()
        
        res=[]
        
        for i, a in enumerate(nums): 
            
            l,r=i+1,len(nums)-1

            while l<r:
                threeSum=a+nums[l]+nums[r]
                
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                    
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                        
        return res
                
