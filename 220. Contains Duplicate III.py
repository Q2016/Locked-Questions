https://leetcode.com/problems/contains-duplicate-iii/discuss/61731/O(n)-Python-using-buckets-with-explanation-10-lines.

O(n) Python using buckets with explanation

def containsNearbyAlmostDuplicate(self, nums, k, t):
    # Bucket sort. Each bucket has size of t. For each number, the possible
    # candidate can only be in the same bucket or the two buckets besides.
    # Keep as many as k buckets to ensure that the difference is at most k.
    buckets = {}
    for i, v in enumerate(nums):
        # t == 0 is a special case where we only have to check the bucket
        # that v is in.
        bucketNum, offset = (v / t, 1) if t else (v, 0)
        for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
            if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                return True

        buckets[bucketNum] = nums[i]
        if len(buckets) > k:
            # Remove the bucket which is too far away. Beware of zero t.
            del buckets[nums[i - k] / t if t else nums[i - k]]

    return False
    

    
O(nlog n)    
    
 https://leetcode.com/problems/contains-duplicate-iii/discuss/824603/Python-SortedList-O(n-log-k)-solution-explained.   
  
  
In my opinion it is more like hard problem, because brute-force solution will get you TLE 
and all other solutions uses some not easy trick: either heaps or BST or bucket sort. If you 
know some other solution without these ideas, please let me know!

In this problem we need to iterate over window of size k+1 and check if there is numbers with 
difference <=t in this window. What we need to do efficiently is to add and remove elements 
from our window, and my choice of data structure is BST, which is implemented in SortedList 
in python. So on each step we have sorted list of elements in this window. Imagine the case:

[1, 3, 7, 12] and new number we need to insert is 10, and t = 2. Then we need to consider range 
[8,12] and check if we have numbers in our SList in this range. We can do two binary searches 
here: bisect_left for left boundary and bisect_right for right boundary. Also we need to check 
if pos1 != len(SList), if this is the case, it means that new number is bigger than bigges 
number in list + t, so in this case we just put it directly to our list. If pos1 != pos2, 
this means, that we found some number i our [nums[i] - t, nums[i] + t] range, so we immediatly 
return True.

Complexity: time complexity is O(n log k), because we do n steps, each one with O(log k) 
complexity to do binary search, remove and add elements. Space complexity is O(k) to keep 
our SortedList updated.

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
        
        return False
        
PS because of time complexity O(n log k), this solution will not be on top, there is O(n) 
bucket sort solution, but in my opinion it is for certain hard level.    
