Question:
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]    


Solution: Backtracking


Intuition:
https://leetcode.com/problems/palindrome-partitioning/solution/  

The idea is to generate all possible substrings of a given string and expand each possibility if is a potential candidate. 
The first thing that comes to our mind is Depth First Search. In Depth First Search, we recursively expand potential 
candidate until the defined goal is achieved. After that, we backtrack to explore the next potential candidate.
Backtracking incrementally build the candidates for the solution and discard the candidates (backtrack) 
if it doesn't satisfy the condition. The backtracking algorithms consists of the following steps:
-Choose: Choose the potential candidate. Here, our potential candidates are all substrings that could be 
generated from the given string.
-Constraint: Define a constraint that must be satisfied by the chosen candidate. In this case, 
the constraint is that the string must be a palindrome.
-Goal: We must define the goal that determines if have found the required solution and we must backtrack. 
Here, our goal is achieved if we have reached the end of the string.

python link from https://leetcode.com/problems/palindrome-partitioning/discuss/1667647/Well-Explained-JAVA-C%2B%2B-PYTHON-JavaScript-oror-Easy-for-mind-to-Accept-it

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # which will be our answer
        self.helper(res, [], s) # calling to recursion function 
        return res
    
    # Entire recursive function, that generates all the partition substring
    def helper(self, res, curr, s):
        if s == "":
            res.append(curr)
        
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]): # what we are checking over here is, if we partition the string from index to i Example-(0, 0) is palindrome or not
                self.helper(res, curr + [s[:i + 1]], s[i + 1:]) # take the substring and store it in our list & call the next substring from index + 1
    
    # A simple palindromic function start from 0 go till end. And basically keep on checking till they don't cross. 
    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True  
