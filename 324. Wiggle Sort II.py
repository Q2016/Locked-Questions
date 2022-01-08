


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums=sorted(nums,reverse=True)
        #print(nums)
        arr=[]
        m=n=0
        for i in range(len(nums)):
            if i%2==0:
                arr.append(nums[len(nums)//2+m])
                m+=1
            else:
                #print(n)
                #print(nums[n])
                arr.append(nums[n])
                n+=1
        print(arr)
        nums=arr
