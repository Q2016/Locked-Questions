Question:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [30,11,23,4,20], h = 5
Output: 30


Solution: Binary Search

In the previous approach, we tried every smaller eating speed, before finding the first workable speed. We shall look for a more efficient way to 
locate the minimum workable eating speed.
Recall how we calculated the total time for Koko to finish eating all the piles in approach 1. We can observe two laws:
If Koko can eat all the piles with a speed of nn, she can also finish the task with the speed of n + 1n+1. With a larger eating speed, Koko will 
spend less or equal time on every pile. Thus, the overall time is guaranteed to be less than or equal to that of the speed nn.
If Koko can't finish with a speed of nn, then she can't finish with the speed of n - 1n−1 either. With a smaller eating speed, Koko will spend more 
or equal time on every pile, thus the overall time will be greater than or equal to that of the speed nn.
Given the previous laws, the distribution will be:
If the current speed is workable, the minimum workable speed should be on its left inclusively. If the current speed is not workable, that is, too 
slow to finish the eating task, then the minimum workable speed should be on its right exclusively.
Therefore, we can use binary search to locate the boundary that separates workable speeds and unworkable speeds, to get the minimum workable speed.
First, let's set a reasonable upper and lower bound for binary search (to ensure that we do not miss any workable speed). Let the lower bound be 1, 
the minimum possible eating speed since there is no speed slower than 1. The upper bound will be the maximum eating speed, that is the maximum number 
of bananas in a pile. For instance, if the piles are [3,5,7,9], then 99 is the maximum number of bananas in a single pile, we can set the upper 
boundary as 99. Because Koko can eat every pile within 1 hour with a speed of 99, or any other faster speed, 99 is thus guaranteed to be a workable value.
Once we set the boundaries, we can then apply the binary search to reduce the search space. In each iteration, we will reduce the remaining search space 
by half until we have narrowed down the search space to just one element, which is the minimum workable eating speed!
There are many other interesting problems that can be solved by performing a binary search to find the optimal value. You can practice using the binary 
search approach on the following problems! (click to show)
Initialize the two boundaries of the binary search as left = 1, right = max(piles).
Get the middle value from leftleft and rightright, that is, middle=(left+right)/2, this is Koko's eating speed during this iteration.
Iterate over the piles and check if Koko can eat all the piles within h hours given this eating speed of middle.
If Koko can finish all the piles within hh hours, set right equal to middle signifying that all speeds greater than middle
are workable but less desirable by Koko. Otherwise, set left equal to middle + 1 signifying that all speeds less than or equal to middle are not workable.
Repeat the steps 2, 3, and 4 until the two boundaries overlap, i.e., left = right, which means that we have found the minimum speed by which Koko 
could finish eating all the piles within hh hours. We can return either left or right as the answer.


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right
