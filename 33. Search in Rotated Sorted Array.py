Question:
There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, 
nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at 
pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums. 
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4    

    
    
    
    
    
    

Solution: BST
Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Because it's not fully sorted, we can't do normal binary search. But here comes the trick:
If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
And then we can simply do ordinary binary search.    


    def search(nums, target) :

        if (len(nums)==0): 
            return -1;
        lo = 0, 
        hi = len(nums)-1;
        
        while (lo < hi):
            mid = lo + (hi - lo)/2;
            #target and mid are on the same side
            if (nums[mid]-nums[len(nums)-1])*(target-nums[len(nums)-1])>0:    
                if nums[mid] < target:
                    lo = mid + 1;
                else:
                    hi = mid;
            else if: target > nums[len(nums)-1]
                hi = mid; # target on the left side
            else:
                lo = mid + 1; # target on the right side
       return lo if nums[lo] == target else -1;      
