Question:
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for 
every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:
Input: arr = [3,1,3,6]
Output: false

    
    
     
    
    
    
    
    
    
    
    
Solution: Greedy (sorting is key here)
    
Idea

We greedily process elements starting from the smallest value, WHY smallest value but not an arbitrary value?
    Because since it's the smallest values, let say x, there is only one choice to pair with x:
        If x is a positive number, then it pairs with y = x*2, for example: x = 4 pair with y = 8.
        If x is a non-positive number, then it pairs with y = x/2, for example: x = -8 pair with y = -4.
        If there is no corresponding y then it's IMPOSSIBLE, return FALSE.
    If it's an arbitrary value, let say x, there are two choices, either x/2 or x*2 is also a good pairing with x 
    (no matter if x is a possible or negative number), if we choose x/2 or x*2 to pair with x, it maybe WRONG, because some other elements may 
    need it to make pair.
    For example: arr = [2, 4, 1, 8]
        If we process x = 2 first, then there are 2 choices, either 4 or 1 can be paired with 2, if we choose 4 -> we got WRONG ANSWER.
        Because 8 needs 4, so 2 should be paired with 1.
So we need to sort our arr array first.
When a pair of (x and y) match, we need to decrease their count. So we need to use a HashTable data structure to count the frequency of 
elements in the arr array.

class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True

    
Complexity Analysis

Time Complexity: O(NlogN), where N is the length of A.
Space Complexity: O(N).    
