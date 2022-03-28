Question:
Given an integer array arr and an integer difference, return the length of the longest 
subsequence in arr which is an arithmetic sequence such that the difference between adjacent 
elements in the subsequence equals difference.
A subsequence is a sequence that can be derived from arr by deleting some or no elements without 
changing the order of the remaining elements.

Example 1:
Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].        

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].        
        
        
        
        
        
Solution:  HashMap/dict
        
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count = {}
        for a in arr:
            count[a] = 1 + count.get(a - difference, 0)
        return max(count.values())
