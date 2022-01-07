
https://leetcode.com/problems/search-in-rotated-sorted-array/



class Solution {
public:
    int search(vector<int>& nums, int target) {

        if(nums.size()==0) return -1;
        int lo = 0, hi = nums.size() - 1;
        while (lo < hi)
        {
            int mid = lo + (hi - lo)/2;
            //target and mid are on the same side
            if((nums[mid]-nums[nums.size()-1])*(target-nums[nums.size()-1])>0)
            {
                if(nums[mid] < target)
                    lo = mid + 1;
                else
                    hi = mid;
            }else if(target > nums[nums.size()-1])
                hi = mid; // target on the left side
            else
                lo = mid + 1; // target on the right side
        }
        // now hi == lo
        return nums[lo] == target ? lo : -1;      
    }
};

/*
Explanation

Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. And the adjustment is done by comparing both the target and the actual element against nums[0].

Code

If nums[mid] and target are "on the same side" of nums[0], we just take nums[mid]. Otherwise we use -infinity or +infinity as needed.
*/
