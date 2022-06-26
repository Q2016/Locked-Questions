Question:
From any string, we can form a subsequence of that string by deleting some number of 
characters (possibly no deletions).
Given two strings source and target, return the minimum number of subsequences of 
source such that their concatenation equals target. If the task is impossible, return -1.

Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source 
    string due to the character "d" in target string.

Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".




    
    
    
    
    
    
    
I thought we can solve this using backtracking    
    
Solution: first solution is simple


https://medium.com/swlh/google-interview-question-leetcode-1055-7670fbaf5bd3

Firstly, we will try to solve the problem with brute force method in O(n²) running time; 
then we will improve our algorithm to O(n log n) running time; finally we will further improve 
the algorithm to O(n).

Brute Force — O(n²)
The most intuitive implementation of the problem is, we can define a starting index i for 
string source, with an initialized value of 0. Then we loop through each character in the target:
If the character exists in source after position i (e.g. exists at position j where j>i), 
we move on to the next character, and set i to the value of j;
If the character does not exists in source after position i, and i is 0, we return -1 as we 
cannot form target by using source.
If the character does not exists in source after position i, and i is not 0, we increment 
the output count by 1, and set i to 0, and then repeat from step 1.
With this algorithm, we will basically have a nested loop, first level of the loop is the 
looping over string target, and second level of the loop is looping over the string source 
to check the existence and position of the character. So the running time will be O(n²).

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = 0
        res = 1
        for c in target:
            i = source.find(c, i)
            if i == -1:
                i = source.find(c)
                if i == -1:
                    return -1
                res += 1
            i += 1
        return res
      

Binary Search — O(n log n)
We can improve the second loop from O(n) to O(log n) by memorizing the positions of each 
character in the source, and using binary search for step 1 in the Brute Force Algorithm.
For example, if the source is 'abcabba', we can build a map to save the character positions 
as: {'a': [0, 3, 6], 'b': [1, 4, 5], 'c': [2]}. By using this map, we can do binary search 
when we try to find a character after position i, and it will improve our running time to O(n log n).
  
  class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def search(arr, val):
            lo, hi = 0, len(arr) - 1
            res = -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] == val:
                    return mid
                elif arr[mid] > val:
                    res = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return res
    
        mapping = collections.defaultdict(list)
        for i, ch in enumerate(source):
            mapping[ch].append(i)
        
        idx = 0
        res = 1
        for ch in target:
            if ch not in mapping:
                return -1
            else:
                nums = mapping[ch]
                if nums[-1] < idx:
                    res += 1
                    idx = 0
                j = search(nums, idx)
                idx = nums[j]+1
        
        return res
      
      
      
      
Improved Method — O(n)
If we assume copy an object takes O(1), then we can further improve the algorithm in 
linear time O(n). For each position i in source, we can memorize the first appearance 
of the characters after position i.
For example, if the source is 'abcabba', we can build a map to save the character 
positions as: {0: {'b': 1, 'a': 0, 'c': 2}, 1: {'b': 1, 'a': 3, 'c': 2}, 
2: {'b': 4, 'a': 3, 'c': 2}, 3: {'b': 4, 'a': 3}, 4: {'b': 4, 'a': 6}, 5: {'b': 5, 'a': 6}, 6: {'a': 6}}.
With this map, assume we are currently at index 2 (e.g. i=2), and our character to 
search is 'a', so we can get map[2]['a'] is 3, which means the first 'a' after index 2 
is at position 3; and then for the next character, we need to start search at 4, which 
means we need to set i to 4.


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        mapping = {}
        for i in range(len(source)-1, -1, -1):
            ch = source[i]
            if i == len(source)-1:
                mapping[i] = {}
            else:
                mapping[i] = mapping[i+1].copy()
            mapping[i][ch] = i
            
        idx = 0
        res = 1
        for ch in target:
            if ch not in mapping[0]:
                return -1
            else:
                if idx == len(source) or ch not in mapping[idx]:
                    idx = 0
                    res += 1
                
                idx = mapping[idx][ch] + 1
       	
        return res

  
  
