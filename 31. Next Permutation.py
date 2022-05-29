Question:
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
For example, the next permutation of arr = [1,2,3] is [1,3,2]. Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.

Example 1:
[1,2,4,1] =>[1,4,1,2] : 1241<1412   
[1,2,4,3] =>[1,3,2,4] : 1243<1324
[4,3,2,1] =>[1,2,3,4] : 4321<1234 !
[1,2,3,4] =>[1,2,4,3] : 1234<1243
    
    
    
    
    
    
    
    
    
    
    
Solution: 
    https://www.youtube.com/watch?v=6qXO72FkqwM

        
sort  O(nlogn)        
swap n/2 elements O(n)
        
        
According to Wikipedia, a man named Narayana Pandita presented the following simple algorithm to solve this problem in the 14th century.
- Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
- Find the largest index l > k such that nums[k] < nums[l].
- Swap nums[k] and nums[l].
- Reverse the sub-array nums[k + 1:].

    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
        
The above algorithm can also handle duplicates and thus can be further used to solve Permutations and Permutations II.
