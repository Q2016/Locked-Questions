# dynamic programing
#from Unofficial solution intuitive explanations O(n) two different approaches


#https://www.youtube.com/watch?v=lXVy6YWFcRM

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """

        
        max_num=1
        min_num=1
        
        for n in nums:
            temp=max_num
            max_num=max(max_num*n, min_num*n, n)
            min_num=min(temp*n, min_num*n, n)
            print(max_num)
        return max(max_num, max(nums))
