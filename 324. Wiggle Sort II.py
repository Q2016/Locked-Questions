Question:
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.

Example 1:
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.    

Solution:
    
    def wiggleSort(self, nums: List[int]) -> None:
        
        nums=sorted(nums,reverse=True)
        arr=[]
        m=n=0
        for i in range(len(nums)):
            if i%2==0:
                arr.append(nums[len(nums)//2+m])
                m+=1
            else:
                arr.append(nums[n])
                n+=1
        nums=arr
